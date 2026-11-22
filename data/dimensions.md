# Dimensions with source, status and tier

Unofficial reference, not affiliated with ESA. See `../docs/TIERS.md` for the status and tier definitions. Values in mm.


## Overall envelope

| Dimension | 1:1 mm | 1:4 mm | Source | Status | Uncertainty | Tier |
|---|---|---|---|---|---|---|
| Mast top above ground | 2049 | 512 | Vago et al. 2017, Fig. 4 | stated | about 0 (label); ESA SPICE kernels (K1): the NavCam centres are 2051.5 above the nominal ground, so the label marks the camera level (WACs 2066, HRC 2045); nominal ground = wheel centre - 142.5 | A |
| Deployed span, panel tip to tip | 2632 | 658 | Vago et al. 2017, Fig. 4 | stated | about 0; photogrammetry gave 2650 (+0.7 %) | A |
| Stowed envelope | 1500 x 1410 x 660 | 375 x 353 x 165 | Whetsel and Salvo 2011 (NASA slide 13) | stated | about 0 | A |
| Mast head width | 500 | 125 | Vago et al. 2017, Fig. 4; equals the WAC stereo baseline in Coates et al. 2017 | stated (that the head is the camera spacing is our inference) | about 0 | A |
| Mass; payload | 310 kg; 26 kg | n/a | Vago 2017 | stated | about 0 | A |
| Mast height above the deck | about 1070 | 268 | Vago et al. 2017, Fig. 4 pixel reading | derived | about 40 | B |

## Locomotion

| Dimension | 1:1 mm | 1:4 mm | Source | Status | Uncertainty | Tier |
|---|---|---|---|---|---|---|
| Wheel diameter, without grousers | 285 | 71 | Vago 2017 text | stated | about 0 | A |
| Wheel width | 120 | 30 | Vago 2017 text; Vago et al. 2017, Fig. 4 | stated | about 0 | A |
| Wheel overall height with grousers | 310 | 78 | Vago et al. 2017, Fig. 4 label (what it spans is our reading) | stated (reading ours) | about 5 | B |
| Clear gap between wheel inner faces | 1320 | 330 | Vago et al. 2017, Fig. 4 | stated | about 0 | A |
| Track, wheel centre to centre | 1440.0 | 360 | ESA SPICE structure kernel (K1) (wheel y = +-720.0 front, middle and rear); Vago et al. 2017, Fig. 4 labels (1320 + 120) agree | stated (ESA/ROCC operational geometry from TAS-I documentation) | about 0; the photogrammetry gave 1462 (+1.5 %) | A |
| Track, outer faces | 1560 | 390 | Vago et al. 2017, Fig. 4 (1320 + 240) | derived from labels | about 0 | A |
| Wheelbase, rear to front wheel centres | 1454.6 | 364 | ESA SPICE kernels (K1) (wheel x 705.0, 55.0, -749.6); the photogrammetric circle fits gave 1455 | stated (ESA/ROCC operational geometry) | about 0 | A |
| Rear-to-middle / middle-to-front spacing | 804.6 / 650.0 | 201 / 162.5 | ESA SPICE kernels (K1); the photogrammetry gave 807 / 648 | stated (ESA/ROCC operational geometry) | about 0 | A |
| Body underside width | 845 | 211 | Vago et al. 2017, Fig. 4 (what the extension lines span is our reading) | derived | about 20 | B |
| Bogie, steering and axle shapes and sizes | unknown |  |  | unverified | unknown | D |

## Solar array

| Dimension | 1:1 mm | 1:4 mm | Source | Status | Uncertainty | Tier |
|---|---|---|---|---|---|---|
| Panel plane height above ground | about 910 (photogrammetry 850 to 950; Vago et al. 2017, Fig. 4 pixels 870 to 935) | 228 | photogrammetry histogram; Vago et al. 2017, Fig. 4 | derived | about 40 | B |
| Solar-array hinge positions (primary front hinge, secondary hinge) | primary x -420, y +-800; secondary x -700, y +-800; both 840 above ground |  | ESA SPICE kernels (K1) (RM_SA*_PRI/SEC); primary hinge y + 515 panel width = 1315 half-span, consistent with the stated 2632 span | stated (ESA/ROCC) | about 0 | A |
| Deployable panel width (across the rover) | about 515 (518 right wing, 513 left; the earlier photogrammetry figure of 620 most likely included the gap to the central panel) | 129 | studio plan-view render (solar-cell lattice as the ruler), full 2D rectification on the cell lattice | derived | about 10 | B |
| Deployable panel lengths (fore-aft) | about 882 (all four panels) | 221 | studio plan-view render (solar-cell lattice as the ruler) ; photogrammetry had 880 to 920 | derived | about 12 | B |
| Hinge gap between a side's two panels (board to board) | about 198 (both wings) | 50 | studio plan-view render (solar-cell lattice as the ruler) | derived | about 15 | B |
| Wing zone fore-aft, each side | about 1964 | 491 | studio plan-view render (solar-cell lattice as the ruler); photogrammetry had 1940 to 1980 | derived | about 20 | B |
| Fixed (central) panel, bounding box across x fore-aft | about 1355 x 1058 (stepped outline; main block alone 1138 across) | 339 x 265 | studio plan-view render (solar-cell lattice as the ruler) ; photogrammetry had 1300 x 1090 | derived | about 20 | B |
| Cell outline | 40 x 80 (chamfered corners) | 10 x 20 | AZUR 3G30C datasheet (probably the rover's cell, not confirmed) | stated for the datasheet cell | about 0.1 | B |
| Cell pitch along a string | 40.6 to 40.8 | 10.2 | measured on the central panel | derived | about 0.2 | A |
| Cell counts | 18 per string; 720 total (288 central, 108 per deployable panel) | n/a | Ferrando et al. 2017, Astrium SAMM summary report 2005 | stated | 0 | A |
| Cell area | 2.17 m2 (0.87 central, 0.33 per deployable panel) | n/a | derived from the counts and the datasheet cell | derived | small | B |

## Body and rear

| Dimension | 1:1 mm | 1:4 mm | Source | Status | Uncertainty | Tier |
|---|---|---|---|---|---|---|
| Body (warm box) height | about 580 | 145 | Vago et al. 2017, Fig. 4 pixel reading | derived | about 40 | C |
| Body plan size (across x fore-aft) | not measured by ESA SPICE kernels (K1) (it gives reference points, not outlines); the stowed envelope (1500 x 1410) is the nearest bound |  | unresolved; TAS ground-test-model photos (tier C, ): the white front panels span about 894 across, the gold side box is about 1065 fore-aft (+- 60), after correcting the side plane for the box's lateral protrusion of about 120 mm read in GTM1; it matches the 1058 fixed panel | unknown | large | D |
| WISDOM antenna | 410 x 200 x 180 | 102 x 50 x 45 | Herve et al. 2020, Benedix et al. 2013, Benedix et al. 2024 (as built 410 x 199 x 178) | stated | about 0; the photogrammetry agrees to a few percent | A |
| WISDOM antenna height above ground (lower edge) | 380 | 95 | Herve et al. 2020, Benedix et al. 2024 | stated | about 10 | A |
| WISDOM tilt back | 8 degrees (antenna boresight against the base frame) |  | ESA SPICE kernels (K1) frames kernel (the 2011 design paper Ciarletti et al. 2011 said 7) | stated (ESA/ROCC) | about 0 | A |
| Which end is the front | the drill end |  | Ciarletti et al. 2011, Plettemeier et al. 2013 (EGU), ESA rear-view render caption, Vago et al. 2017, Fig. 4 (four sources) | stated | none | A |

## Mast head and PanCam

| Dimension | 1:1 mm | 1:4 mm | Source | Status | Uncertainty | Tier |
|---|---|---|---|---|---|---|
| Head envelope, camera heights | unknown |  | Coates et al. 2017 gives no envelope; the photogrammetry cannot see the head | unknown |  | D |
| WAC stereo baseline | 495.2 (calibrated; 500 is the nominal in Coates et al. 2017 and Vago et al. 2017, Fig. 4) | 124 | ESA SPICE kernels (K1) (WAC offsets +-247.6 from the PanCam frame, from calibration data) and Coates et al. 2017 | stated | about 0 | A |
| NavCam baseline / LocCam baseline / camera heights above ground | 154 / 154 / NavCam 2051.5, WAC 2066, HRC 2045, ISEM 1967, LocCam 942.4 |  | ESA SPICE kernels (K1) | stated (ESA/ROCC) | about 0 | A |
| Mast pole diameter | about 115 (photogrammetry core, low confidence) | 29 | photogrammetry | derived | about 30 | D |

## Drill

| Dimension | 1:1 mm | 1:4 mm | Source | Status | Uncertainty | Tier |
|---|---|---|---|---|---|---|
| Drill tool length | about 700 | 175 | Vago 2017 | stated (approximate) | about 50 | B |
| Extension rod length | 500 (three rods) | 125 | Vago 2017 | stated | about 0 | A |
| Drill tool diameter | 20 | 5 | Altieri 2023 | stated | about 0 | A |
| Drill box size and pose | unknown |  | the box lies across the front when travelling, vertical when drilling | unverified | large | D |
| Drill positioner pivot | x +340.0, y +100.0 (100 mm left of the centreline), 693.8 above ground |  | ESA SPICE kernels (K1) (RM_DRILL_POS_FIX) | stated (ESA/ROCC) | about 0 | A |

## Deck items

| Dimension | 1:1 mm | 1:4 mm | Source | Status | Uncertainty | Tier |
|---|---|---|---|---|---|---|
| PCT plate | 67 x 76, patches 18 and 30 diameter | 17 x 19 | ESA drawing via PCOT (MIT), Coates 2017; Fig. 11 CAD agrees to 0.3 mm | stated | about 0.5 | A |
| PCT plate thickness | 2 (photo) or about 5 (Fig. 11 edge) | 0.5 to 1.3 | photo; CAD render | estimated, conflicting | 3 | C |
| PCT position on the deck | teal patch centre u 588, v -538, H 938 (u right, v rear, H up) |  | triangulated from 18 video frames | derived | about 10 to 20 relative to our photogrammetry frame; the frame itself is good to about 2.5 % | B |
| PCT orientation | drawing +x = rover right, +y = rear (large patches face the rear); 0 degrees, within about 10 |  | 360 video, checked in the 2409 overhead | derived | about 10 degrees | B |
| PCT shadow posts | stems 4.5, balls 9, 15 high | 1.1, 2.3, 3.8 | one photo | measured | about 2 | C |
| FidM (fiducial marker) shape | 32 x 16 x 6.5, waisted, 9 to 10 mm bare disc | 8 x 4 x 1.6 | stated envelope (Coates et al. 2017); shape from the Fig. 11 inset | stated + derived | about 10 percent on the shape | C |
| FidM positions | unknown |  | arrows in Fig. 11 only (left-rear corner area, front tongue beside the PCT, right-rear bracket) | unknown | about 100 or worse | D |
| Two T-shaped deck posts | identified 2026-11-21: the two UHF monopole antennas (ESA's current-design render labels a T-post 'Communication antennas'; the ESA caption of the rear-view render, ESA rear-view render caption, says 'Two UHF monopole antennas are used to communicate with Mars orbiters'); size still unknown |  | ESA render label and caption (identity inferred from the label pointing at the post) | stated (identity), size unknown |  | C for identity, D for size |
| Small silver cones | unidentified (candidates: the dome caps of the suspension joints; not checked) |  | video, Fig. 11 | unknown |  | D |
| RIM (rover inspection mirror) | 50 mm sphere, on the left bogie bracket | 12.5 | Coates et al. 2017 | stated | 0 | A |
| Small separate multi-disc target on the lower body | about 15 across, unidentified |  | animation frames | unknown |  | D |
