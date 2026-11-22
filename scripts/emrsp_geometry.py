"""Rover structure positions from ESA's public ExoMars RSP SPICE kernels (ROCC / ESA SPICE Service), in the rover frame, in mm, and above the nominal ground.
usage (repo root): python scripts/emrsp_geometry.py [--json data/rover-frame.json]
needs spiceypy (venv).  Downloads (once, to the git-ignored data/lit/emrsp/) fk/emrsp_rm_v014.tf and spk/emrsp_rm_struct_v007.bsp from
https://spiftp.esac.esa.int/data/SPICE/ExoMarsRSP/kernels/  (dataset citation: ESA SPICE Service, ExoMarsRSP Operational SPICE Kernel Dataset, https://doi.org/10.5270/esa-uvyv4w5).
Frame: RM_ROVER, +x forward, +y LEFT, +z up; origin on the body mid-plane, 252.5 mm aft of the plane through the front body HDRM bolt axes and 30 mm below the plane of the rover body base (FK section 'RM Rover Frames').
What is computed: each structure's SPK segment gives a position relative to its centre in the centre's frame; chained here assuming every intermediate frame is aligned with RM_ROVER (bogie, steering, mast, pan and tilt angles all zero, solar arrays deployed, rover on flat ground),
which is the nominal deployed configuration (except the PanCam cameras, whose offsets are rotated by the bench misalignment, and LocCam, taken as stored in the rover frame). The positions are the ROCC's operational structure values (SPK versions 0.0.6/0.0.7: 'components positions from TAS-I documentation EXM-RM-TNO-AI-0448, 13 December 2021', PanCam from calibration data), not a CAD export.
Ground: the six wheel centres are all 157.5 mm below the origin and the wheel radius is 142.5 mm (285 mm diameter without grousers), so the nominal ground plane is z = -300 mm (no tyre deflection, no grousers)."""
import os, sys, json, urllib.request
import numpy as np, spiceypy as sp
arg = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
D = 'data/lit/emrsp'; BASE = 'https://spiftp.esac.esa.int/data/SPICE/ExoMarsRSP/kernels/'
FK, SPK = 'fk/emrsp_rm_v014.tf', 'spk/emrsp_rm_struct_v007.bsp'
for f in (FK, SPK):
    p = os.path.join(D, f)
    if not os.path.exists(p):
        os.makedirs(os.path.dirname(p), exist_ok=True); urllib.request.urlretrieve(BASE + f, p)
sp.furnsh(os.path.join(D, FK))
h = sp.dafopr(os.path.join(D, SPK)); sp.dafbfs(h); seg = {}
sp.furnsh(os.path.join(D, SPK))
while sp.daffna():
    dc, ic = sp.dafus(sp.dafgs(), 2, 6); body, center, frame = ic[:3]
    st, _ = sp.spkez(int(body), dc[0] + 1.0, sp.frmnam(int(frame)), 'NONE', int(center))
    seg[sp.bodc2n(int(body))] = (sp.bodc2n(int(center)), np.array(st[:3]) * 1e6)      # km -> mm
sp.dafcls(h)
def pos(n):                                                                         # rover-frame position, all intermediate frames aligned
    c, o = seg[n]
    return o if c in ('RM_ROVER', 'EXOMARS ROVER') else pos(c) + o
P = {n: pos(n) for n in seg}
# LocCam left/right are stored with centre RM_MAST but carry rover-frame numbers (the same x and z as RM_LOCCAM, which is centred on RM_ROVER): take them as rover-frame positions
for n in ('RM_LOCCAM_L', 'RM_LOCCAM_R'): P[n] = seg[n][1].copy()
# PanCam cameras: offsets are in RM_PANCAM_BASE, which is rotated against the pan-tilt frame by the bench misalignment (about 5.3 degrees yaw, 6.7 degrees pitch): rotate them
Rb = sp.pxform('RM_PANCAM_BASE', 'RM_PTR', 0.0)
for n in ('RM_PANCAM_WAC_L', 'RM_PANCAM_WAC_R', 'RM_PANCAM_HRC'): P[n] = P['RM_PANCAM'] + Rb @ seg[n][1]
GZ = P['RM_WHEEL_LF'][2] - 142.5                                                    # nominal ground plane z
rows = []
def add(group, name, key, note=''):
    v = P[key]; rows.append(dict(group=group, name=name, key=key, x=round(v[0], 1), y=round(v[1], 1), z=round(v[2], 1), above_ground=round(v[2] - GZ, 1), note=note))
for k, nm in [('RM_WHEEL_LF', 'wheel centre left front'), ('RM_WHEEL_LM', 'left middle'), ('RM_WHEEL_LR', 'left rear'), ('RM_WHEEL_RF', 'right front'), ('RM_WHEEL_RM', 'right middle'), ('RM_WHEEL_RR', 'right rear')]: add('locomotion', nm, k)
for k, nm in [('RM_STEER_LF', 'steering axis left front'), ('RM_STEER_LM', 'left middle'), ('RM_STEER_LR', 'left rear')]: add('locomotion', nm, k, 'steering axis position; y equals the wheel y (the axis lies in the wheel mid-plane)')
for k, nm in [('RM_BOGIE_LF', 'left bogie pivot'), ('RM_BOGIE_RF', 'right bogie pivot'), ('RM_BOGIE_MR', 'rear bogie pivot')]: add('locomotion', nm, k)
for k, nm in [('RM_MAST', 'mast base (deployment hinge frame origin)'), ('RM_PTR', 'pan-tilt axes intersection (top of mast)'), ('RM_NAVCAM_L', 'NavCam left'), ('RM_NAVCAM_R', 'NavCam right'), ('RM_PANCAM', 'PanCam frame origin'), ('RM_PANCAM_WAC_L', 'WAC left'), ('RM_PANCAM_WAC_R', 'WAC right'), ('RM_PANCAM_HRC', 'HRC'), ('RM_ISEM', 'ISEM (Enfys replaces it)'), ('RM_LOCCAM_L', 'LocCam left'), ('RM_LOCCAM_R', 'LocCam right')]: add('mast and head', nm, k)
for k, nm in [('RM_DRILL_POS_FIX', 'drill positioner pivot'), ('RM_ALD_CSTM_FIX', 'ALD core sample transfer mechanism'), ('RM_ALD_PSDDS', 'ALD PSDDS'), ('RM_ALD_PSHS', 'ALD PSHS'), ('RM_WISDOM', 'WISDOM base (middle of the two antenna mounts)')]: add('body', nm, k)
for k, nm in [('RM_SA1_PRI', 'left primary panel, first hinge'), ('RM_SA1_SEC', 'left secondary panel, first hinge'), ('RM_SA2_PRI', 'right primary panel, first hinge'), ('RM_SA2_SEC', 'right secondary panel, first hinge')]: add('solar array', nm, k, 'hinge centre of the hinge nearest the front (primary) or nearest the body (secondary); array deployed (angle 0)')
w = {k: P[k] for k in P if k.startswith('RM_WHEEL_')}
der = dict(
    ground_plane_z=round(GZ, 1), wheel_centre_z=round(P['RM_WHEEL_LF'][2], 1),
    track_mm=round(P['RM_WHEEL_LF'][1] - P['RM_WHEEL_RF'][1], 1), track_rear_mm=round(P['RM_WHEEL_LR'][1] - P['RM_WHEEL_RR'][1], 1),
    wheelbase_front_rear_mm=round(P['RM_WHEEL_LF'][0] - P['RM_WHEEL_LR'][0], 1), spacing_front_middle_mm=round(P['RM_WHEEL_LF'][0] - P['RM_WHEEL_LM'][0], 1), spacing_middle_rear_mm=round(P['RM_WHEEL_LM'][0] - P['RM_WHEEL_LR'][0], 1),
    mast_ahead_of_middle_axle_mm=round(P['RM_MAST'][0] - P['RM_WHEEL_LM'][0], 1),
    navcam_baseline_mm=round(P['RM_NAVCAM_L'][1] - P['RM_NAVCAM_R'][1], 1), wac_baseline_mm=round(np.linalg.norm(P['RM_PANCAM_WAC_L'] - P['RM_PANCAM_WAC_R']), 1), loccam_baseline_mm=round(P['RM_LOCCAM_L'][1] - P['RM_LOCCAM_R'][1], 1),
    body_base_plane_z=30.0, body_base_above_ground_mm=round(30.0 - GZ, 1),
    sa_primary_hinge_half_width_mm=round(P['RM_SA1_PRI'][1], 1), half_span_check_mm=round(P['RM_SA1_PRI'][1] + 515, 1),
)
print('ground plane z = %.1f mm; wheel centre z = %.1f' % (GZ, P['RM_WHEEL_LF'][2]))
for r in rows: print('%-13s %-48s x %8.1f  y %8.1f  z %8.1f  above ground %8.1f' % (r['group'], r['name'], r['x'], r['y'], r['z'], r['above_ground']))
print(json.dumps(der, indent=1))
if '--json' in sys.argv: json.dump(dict(source='ESA SPICE Service, ExoMarsRSP Operational SPICE Kernel Dataset, https://doi.org/10.5270/esa-uvyv4w5; fk emrsp_rm_v014.tf, spk emrsp_rm_struct_v007.bsp', frame='RM_ROVER (+x fwd, +y left, +z up), mm', structures=rows, derived=der), open(arg('--json', ''), 'w'), indent=1)
