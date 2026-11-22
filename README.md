# exomars-rover-reference

An **unofficial** reference for the dimensions and geometry of the ESA ExoMars Rosalind Franklin rover, built from public sources. It is **not affiliated with, endorsed by or produced for ESA** or any of the companies that build the rover.

The goal is accuracy: every number carries where it comes from, how it was obtained and how far to trust it, and where nothing reliable is known the table says so.

## What is here
| Path | Contents |
|---|---|
| `data/rover-frame.json`, `docs/rover-frame.md` | The rover's reference points (wheels, bogie pivots, steering axes, mast, pan-tilt axes, cameras, drill positioner, WISDOM, solar-array hinges) in the rover frame, from ESA's public SPICE kernels. |
| `data/dimensions.json`, `data/dimensions.md` | About 50 dimensions with a 1:1 value, source, status and tier: envelope, locomotion, solar array, body, mast head, drill, deck items. |
| `docs/TIERS.md` | What the status words (stated, derived, inferred, unknown) and the tiers (A to D) mean. |
| `docs/METHODS.md` | How the derived values were obtained, in outline. |
| `docs/SOURCES.md` | The public sources used, with identifiers. |
| `scripts/emrsp_geometry.py` | Downloads the ESA kernels and regenerates the rover-frame tables. |
| `NOTICE.md` | Attributions and what this repository does not contain. |

## Status
Early. The skeleton (reference points) is solid. Outlines and sizes of the body, the drill box and the housings are not known to better than a few percent, and several are still unknown (tier D in the table).

## Licence
Not chosen yet. Until one is added, all rights in the original content of this repository are reserved by the author; the sources keep their own licences (see `NOTICE.md`).
