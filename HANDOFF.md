# Handoff (written 2026-11-22 by the session that scaffolded this repository)

Read `CLAUDE.md` first (rules). This file is the context CLAUDE.md does not carry.

## How this repository came to be
It is the public face of a private research project (`exomars-rover-private`, same author). The private project spent several sessions (2026-11-17 to 22) measuring the rover from public material, with strict provenance rules (every number: source, status, tier). This repository holds only what is safe and presentable. The dimension table (`data/dimensions.*`) was exported from the private repository's table by a script with a blocklist (`sfm/export_public.py` there); the rover-frame data (`data/rover-frame.json`, `docs/rover-frame.md`, `scripts/emrsp_geometry.py`) comes from ESA's public SPICE kernels. You cannot re-run the export from here: ask the author to refresh it, or hand-edit and say so in the commit message.

## The one thing that changed everything
ESA publishes the rover's structure geometry in its SPICE kernels (doi 10.5270/esa-uvyv4w5). Before that the project relied on photogrammetry of an ESA animation, renders and photographs. The kernel values (track 1440.0, wheelbase 1454.6, mast base 149 mm ahead of the middle axle, NavCam centres 2051.5 mm above ground, WAC baseline 495.2, solar-array hinges at y +-800) now anchor the table; the earlier measurements agreed with them to 2 to 10 mm, which is the best evidence the methods work. Everything below tier A in the table is measured by us and should be read with its stated uncertainty.

## Facts a newcomer tends to get wrong
- **Frame:** +x forward, **+y left**, +z up, mm. The origin is on the body mid-plane, 252.5 mm aft of the plane through the front body HDRM bolt axes and 30 mm below the plane of the rover body base. Nominal ground is z = -300 (wheel centres at -157.5, radius 142.5), so the body base is 330 mm above ground. These heights assume no tyre deflection and no grousers.
- **Kernel values are nominal.** They are the operations centre's design values (from the manufacturer's documentation, December 2021; PanCam from calibration), not a CAD export and not measurements of a built unit. Several are round numbers.
- **Where the kernel disagrees with itself:** the comment block inside the structure kernel carries an older table (solar-array hinges at x -490/-770, y 620/820; drill-tip y 320.4; PanCam at 60 mm) that differs from the data in the file (hinges x -420/-700, y 800/800; drill tip y 342.9; PanCam from calibration). We used the file's data. One entry (CLUPI mirror 1, z = 985) looks like a typo for 98.5 and is not used.
- **LocCam left and right** are stored with the wrong centre (the mast) but carry rover-frame numbers; `scripts/emrsp_geometry.py` handles this. **Cameras on the head** use offsets in a PanCam frame that is rotated against the pan-tilt frame (about 5.3 degrees yaw and 6.7 degrees pitch); the script rotates them.
- **Solar array hinge origins** are the centre of the first (front) hinge of each panel, not a panel centre. The panel surface is about 70 mm above the hinge axis (840 above ground vs a panel plane of about 910).
- **The 'mast top above ground' label (2049 mm)** in Vago et al. 2017 Fig. 4 marks the camera level of the head (NavCams at 2051.5), not the top of the housing.
- **WISDOM:** the antennas are tilted 8 degrees (ESA frames kernel), not 7 (an older paper). The kernel's WISDOM base is the top of the antenna assembly (560.4 above ground; the assembly is 180 mm high with its lower edge at 380).
- **Panel sizes** (primary and secondary panel about 882 x 515, hinge gap about 198, fixed panel main block about 1138 across, 1355 x 1058 with the end blocks) come from a rectified studio plan-view render using the solar-cell lattice as a ruler: tier B.
- **Front-face sizes of a ground test model** (white front panels about 458 + 198 gap + 238 wide, drill box about 825 long (a lower bound), front face about 183 high) are tier C, about +-5 percent; the ground test model is a replica used for operations training, with simulator cells, not flight hardware.

## Things deliberately not included, and why
Images, animations, point clouds and datasheets (licences or unclear terms); a popular third-party 3D model of the rover (its parts run from 0.8 to 2.0 times the real size, so it must not be used for sizes, and its meshes must not be copied); a third-party visualisation tool whose repository carries no licence (nothing from it is used or restated). The identity of the two T-shaped deck posts as the UHF antennas is stated by ESA (caption and label) and kept in the table.

## Known gaps (tier D) and leads
- **Outlines and sizes:** body, drill box, housings, wheel grousers (12 at 30 degrees per one thesis, unverified; their height is unknown), mast pole diameter, head housing.
- **Positions of deck items:** FidMs (shape known, positions unknown), the PCT position is tier B.
- **Unidentified:** the small silver cones, the small multi-patch colour chart on a bracket under the body near the drill.
- **Best lead for outlines:** the structure kernel cites 'ExoMars 2018 Rover Module Outline Drawings (ICD), EXM-D2-ICD-AI-0078, Thales Alenia Space, issue 03 (2019)' and EXM-RM-TNO-AI-0448. Neither is public as far as we found. The ESA SPICE Service (spice@sciops.esa.int) and the rover operations centre are the people to ask whether an outline drawing can be shared. That is the single most valuable email someone could send.
- **Also unread:** the surface platform structure kernel (`spk/emrsp_sp_struct_*`), later kernel versions, other ESA SPICE mission pages.

## Suggestions for this repository
Render the skeleton as our own diagrams (top, side and front views of the reference points, drawn from `data/rover-frame.json`); add a small JSON schema for `dimensions.json`; add a script that greps the repository for the blocklist terms so a leak is caught before pushing; keep the table's 'Uncertainty' column honest (some cleaned rows lost context, check any row before relying on it).

## Style
The author wants plain statements of what is known, 'I don't know' where it is not, source and tier on every number, and no silent assumptions.
