<!-- GENERATED from the private repository (public/docs/rover-frame.md); do not edit by hand -->

# Rover structure geometry from ESA's SPICE kernels

**Licence and credit.** The SPICE kernels are produced by the ESA SPICE Service and ROCC and are licensed by ESA under the Creative Commons Attribution-NonCommercial 3.0 IGO licence (https://creativecommons.org/licenses/by-nc/3.0/igo/). The numbers below are read from those kernels (positions in the rover frame, converted from km to mm, ground plane and above-ground heights derived by us), so this page is an adaptation: credit ESA SPICE Service and the mission team, and do not use it commercially.

**What this is.** ESA's SPICE Service publishes the operational kernel set for the ExoMars RSP rover (public, ESA/ROCC/ALTEC), including a structure kernel with the positions of the wheels, steering axes, bogie pivots, mast, pan-tilt unit, every PanCam and NavCam camera, LocCam, drill positioner, WISDOM, solar-array hinges and more, all in the rover's own frame. Source: ESA SPICE Service, *ExoMarsRSP Operational SPICE Kernel Dataset*, https://doi.org/10.5270/esa-uvyv4w5, files `fk/emrsp_rm_v014.tf` (frames, Feb 2023) and `spk/emrsp_rm_struct_v007.bsp` (structure positions, Jul 2022), https://spiftp.esac.esa.int/data/SPICE/ExoMarsRSP/kernels/. The kernels are not copied into this repository; `scripts/emrsp_geometry.py` downloads them from ESA and regenerates the tables and `data/rover-frame.json`.

**How good it is.** The structure kernel's own history says the component positions come from Thales Alenia Space documentation (EXM-RM-TNO-AI-0448, 13 December 2021, 'Frames Homogeneous Transformation Matrices'; earlier from the Rover Module Outline Drawings ICD EXM-D2-ICD-AI-0078, issue 03, 2019) and the PanCam positions from calibration data. These are the numbers the rover operations centre uses to point cameras and plan drives, so they are nominal design values of the flight design, not measurements of a unit and not a CAD export. Several are round (0.38, 0.325, 0.65, 0.8, 0.54 m), so treat the round ones as nominal. The comment block inside the SPK carries an older table whose solar-array hinge entries (x -490/-770, y 620/820) differ from the data in the file (x -420/-700, y 800/800); I used the data in the file (the PINPOINT block and the segments agree).

**Frame.** RM_ROVER: +x forward, **+y left**, +z up. Origin on the body mid-plane, 252.5 mm aft of the plane through the front body HDRM bolt axes and 30 mm below the plane of the rover body base (FK, 'RM Rover Frames'). Values below are the nominal deployed configuration (bogie, steering, mast, pan and tilt angles all zero, arrays deployed, flat ground). **Ground** = wheel centre (z -157.5 for all six wheels) minus the wheel radius 142.5 mm = z -300 (no tyre deflection, no grousers).

## Locomotion (mm)
| Item | x | y | z | above ground |
|---|---|---|---|---|
| Wheel centres, front / middle / rear (left; right is -y) | 705.0 / 55.0 / -749.6 | +720.0 | -157.5 | 142.5 |
| Steering axes, front and middle / rear | 705.0 and 55.0 / -749.6 | +720.0 | 110.8 / 196.7 | 410.8 / 496.7 |
| Side bogie pivots (left, right) | 380.0 | +517.1, -517.1 | 60.0 | 360.0 |
| Rear bogie pivot | -517.4 | 0 | 130.0 | 430.0 |

Derived: **track 1440.0 mm** (front and middle 1440.05, rear 1440.0); **wheelbase front to rear 1454.6**; front-middle spacing 650.0, middle-rear 804.6; side bogie pivots exactly midway between the front and middle wheels; steering axis 268.3 (side) above the wheel centre and in the wheel mid-plane; **rover body base plane 330 mm above ground**.

## Mast and head (mm, pan = tilt = 0)
| Item | x | y | z | above ground |
|---|---|---|---|---|
| Mast base (deployment frame origin) | 204.0 | 0 | 642.9 | 942.9 |
| Pan-tilt axes intersection (top of mast) | 204.0 | 0 | 1540.4 | 1840.4 |
| NavCams left / right | 320.1 | +77.0 / -77.0 | 1751.5 | 2051.5 |
| WACs left / right (PanCam bench rotated about 5.3 deg yaw, 6.7 deg pitch against the PTU frame, included) | 185.0 / 230.4 | +251.7 / -241.5 | 1766.3 / 1765.8 | 2066 |
| HRC | 348.9 | -143.1 | 1745.2 | 2045.2 |
| ISEM (Enfys takes its place) | 314.0 | -154.0 | 1666.9 | 1966.9 |
| LocCams left / right | 358.6 | +77.0 / -77.0 | 642.4 | 942.4 |

Derived: **NavCam baseline 154 mm; WAC baseline 495.2 mm; LocCam baseline 154 mm**; the mast stands **149 mm ahead of the middle axle** on the centreline. The NavCam centres are 2051.5 mm above ground, which matches the 2049 mm 'mast top above ground' label of Vago et al. 2017 Fig. 4: that label evidently marks the camera level of the head, not the top of the housing (the WACs and HRC sit 15 to 20 mm higher). The pan-tilt axes are 897.5 mm above the mast base.

## Body, drill, WISDOM, solar array (mm)
| Item | x | y | z | above ground |
|---|---|---|---|---|
| Drill positioner pivot (fixed part) | 340.0 | +100.0 | 393.8 | 693.8 |
| ALD core sample transfer mechanism | 265.7 | -233.9 | 420.5 | 720.5 |
| WISDOM base (midway between the two antenna mounts) | -649.9 | 0 | 260.4 | 560.4 |
| Left / right primary panel, first (front) hinge | -420.0 | +800 / -800 | 540.0 | 840.0 |
| Left / right secondary panel, first hinge (nearest the body) | -700.0 | +800 / -800 | 540.0 | 840.0 |

Notes. The WISDOM antenna boresight axes are rotated **8 degrees** from the base frame (FK; the 2011 design paper said 7). The WISDOM base sits 560.4 mm above ground and the antenna assembly is 180 mm high with its lower edge 380 mm above ground (Herve et al. 2020; Benedix et al. 2024): the base origin is therefore the top of the assembly (560.4 - 180 = 380.4). The drill positioner pivot is 100 mm left of the centreline. The primary hinge at y = 800 plus the 515 mm panel width gives a half-span of 1315 mm, i.e. 2630 mm: the stated deployed span is 2632.

## Cross-checks
Independent estimates made elsewhere agree with these values: the track equals the sum of the two label dimensions in Vago et al. 2017 Fig. 4 (1320 clear gap + 120 wheel width); a photogrammetric reconstruction of the ESA animation gave the wheelbase and wheel spacings to within 3 mm and the mast position to 10 mm; the stated deployed span of 2632 mm equals twice the primary hinge offset (800) plus the measured panel width (515); the NavCam height equals the 2049 mm 'mast top' label of Vago et al. 2017 Fig. 4 to 2.5 mm; the WISDOM base sits 180 mm above the stated lower edge of the antennas (380 mm), the antenna height.

Not in the kernel: body outline and size, drill box size, panel sizes, wheel width and grousers, anything on the deck (PCT, FidMs, antennas), the shape of any part. The structure kernel positions reference points (hinges, pivots, optical centres), not outlines.

## Drill positioner kinematics and the stowed drill pose
- The positioner has a translation joint (TRA, along the rover's vertical) and a rotation joint (ROT, about the rover's x axis); their axes intersect at (340.0, 100.0, 393.8) mm in the rover frame (693.8 above ground), defined with the drill horizontal and highest.
- Named positions: stowed TRA 135 mm, ROT 0; lifting TRA 5, ROT 0; vertical alignment TRA 5, ROT 90; drilling TRA 375, ROT 90 (lowest); horizontal before sample discharge TRA 0, ROT 180; sample discharge TRA 5, ROT 150. ROT 0 means the drill is horizontal below the rotation axis. The drill string at full extension travels about 1.5 m. The core-sample transfer travels 300 mm.
- The retracted drill tip is (+140.9, +342.9, -160.6) mm from the positioner moving frame. Stowed (all frames aligned): **tip at x = 480.9, y = +442.9 (the rover's left end), z = 98.2 (398 above ground)**; the drill axis runs along y at x = 480.9, z = 98.2.
- The frames kernel's text gives the drill rod diameter as 25 mm where Altieri et al. 2023 give 20 mm for the tool; the difference is unresolved (probably tool versus rod).

## Instrument kernels (`ik/`)
Fields of view only (half-angles in the file): WAC 19.15 degrees (38.3 degrees full, square), HRC 2.44 (4.9 full), NavCam and LocCam 32.5 (65 full). No focal lengths or pixel sizes are given. The frame kernel also records the calibrated PanCam bench misalignment against the pan-tilt frame (rotation about 5.3 degrees yaw, 6.7 degrees pitch, 0.06 roll) and each camera's own boresight misalignment (all under 3 degrees).
