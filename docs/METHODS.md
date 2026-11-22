# Methods, in outline

- **Stated values** come straight from the cited source (a dimension on a drawing, a number in the text, an ESA data file). Where a label spans something ambiguous, the table says it is our reading.
- **ESA SPICE kernels.** The structure kernel gives positions of reference points in the rover frame. Chains of offsets are summed assuming every intermediate frame is aligned with the rover frame (bogie, steering, mast, pan and tilt angles zero, arrays deployed, flat ground). The nominal ground plane is the wheel centre height minus the stated wheel radius (142.5 mm). The kernel's own history says the positions come from the manufacturer's documentation (2021) and PanCam calibration data; they are nominal design values, not a CAD export and not measurements of a built unit. See `rover-frame.md`.
- **Photogrammetry.** A reconstruction of the rover from frames of an ESA animation, scaled by the mast-height label and checked against the solar-cell pitch; used for sizes the sources do not give, with an uncertainty of about 2.5 percent from the scale plus edge-picking error.
- **Plan-view measurement.** The solar cells are a regular lattice (cell 40 x 80 mm, pitch measured on the central panel), so a render of the rover seen from above can be rectified using the lattice as the ruler. This gave the solar panel sizes and positions (tier B).
- **Photographs.** Straight edges of the rover (it is rectilinear) give vanishing points, hence a camera calibration; the cell lattice or a stated-size feature supplies the scale; the result is tier C, with a stated uncertainty of about 5 percent. Photographs of a ground test model (a replica used for operations training) were used for the front face, with the same caveat.
- **Cross-checks.** Where two methods overlap, the table says how well they agree.

Every derived value should be treated at the tier shown in the table.
