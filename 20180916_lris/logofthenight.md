# Observation Log:
LOTS OF CALIBRATION MIS-STEPS - MAKE SURE TO USE CORRECT EXPOSURES

* Conditions: Excellent
* Seeing: 0.6"
* SA: Josh W. 
* OA: John P. 
* Data Directory: /sd243/lris2/2018sep17
* Data Directory on Dark: /dark/hal/data/20180916_Keck
* Starlist: open: file --> load private starlist --> kroot/starlists/web

## Setup:
# Blue imaging focus: -3546
### Blue Side:
   - Grism: 600/4000
   - Filter: Clear
   - Focus: -3606
### Red Side:
    - Grating: 400/8500
    - Filter: Clear
    - Focus: -0.62


| Side | Obs #     | Target    | Exptime (s) | Start Time (UT) | Airmass | Comments                                                   |
|------|-----------|-----------|-------------|---------|---------|------------------------------------------------------------|
red    | 01        | Arc       |      3      | 01:56  |         | Note these were our test arcs to check the wavelength range; the object name says internal flat - it isn't|
blue   | bfoc01-09 | img focus |             | ~02:05  |         | The trap door didn't open, ignore these|
blue   | bfoc10-16 | img focus |             |  02:11  |         | imaging focus observations|
blue   | bfoc17-20 | spec focus|             | 02:24  |         | blue spec focus observations, trapdoor open, ignore these|
red    | rfoc2-3   | spec focus|             | 02:24  |         | red spec focus observations, trapdoor open, ignore these|
blue   | bfoc21-27 | spec focus|             | ~2:32  |         | blue spec focus observations|
red    | rfoc4-10  | spec focus|             | ~2:32  |         | red spec focus observations|
blue   | bfoc28-29 | arc       |      1      | 02:55  |         | 1.5" Slit ignore these - focus routine did not change windowing back |
red    | 11-12     | arc       |      1      | 02:56  |         | 1.5" Slit; this have the full frame red readout instead of the longslit window|
blue   | 30        | arc       |      1      | 03:00  |         | 1.5" Slit; ignore note the filename has the incorrect prefix bfoc|
blue   | 31-32     | arc       |      1      | 03:03  |         | 1.5" Slit|
blue   | 33 - 34   | arc       |      1      | 03:06  |         | 1.0" slit|
red    | 13-14     | arc       |      1      | 03:07  |         | 1.0" slit this have the full frame red readout instead of the longslit window|
blue   | 35-36     | arc       |      3      | 03:16  |         | 1.5" Slit|
red    | 15-16     | arc       |      3      | 03:16  |         | 1.5" Slit|
blue   | 37-38     | arc       |      3      | 03:21  |         | 1.0" slit|
red    | 17-18     | arc       |      3      | 03:21  |         | 1.0" slit|
blue   | 39-48     | Flat      |    150      | 03:26  |         | 1.5" Slit|
red    | 19-28     | Flat      |     35      | 03:26  |         | 1.5" Slit|
blue   | 49-55     | Flat      |    150      | 04:00  |         | 1.0" slit hung during 55; restarted|
red    | 29-38     | Flat      |     35      | 04:01  |         | 1.0" slit|
red    | 39-40     | arc       |      1      | 04:50  |         | 1.0" slit|
red    | 40-41     | arc       |      1      | 04:56  |         | 1.5" slit|
blue   | 56        | s15517+3254|     10     | 5:19   |    1.3  | telescope set up/imaging focusing?|
blue   | 57        | s15517+3254|     10     | 5:20   |    1.3  | telescope set up/imaging focusing?|
blue   | 58        | BD+33d2642|      30     | 05:29  |    1.34 | 1.0" standard|
red    | 43        | BD+33d2642|      30     | 05:29  |    1.34 | 1.0" standard|
blue   | 59        | BD+33d2642|      20     | 05:32  |    1.36 | 1.5" standard|
red    | 44        | BD+33d2642|      20     | 05:32  |    1.36 | 1.5" standard|
blue   | 60        | 18bek     |    1200     | 05:39  |    1.89 | 1.0" SN; we exposed for this to be ~21mag, its actually 22.5mag on SNEX, so will probably be low S/N |
red    | 45        | 18bek     |   1200      | 05:39  |   1.89 | 1.0" SN; we exposed for this to be ~21mag, its actually 22.5mag on SNEX, so will probably be low S/N |
blue   | 61        | 18bek     |    1200     | 05:39  |    1.99 | 1.0" SN; we exposed for this to be ~21mag, its actually 22.5mag on SNEX, so will probably be low S/N |
red    | 46        | 18bek     |   1200      | 05:39  |   2.0 | 1.0" SN; we exposed for this to be ~21mag, its actually 22.5mag on SNEX, so will probably be low S/N |
blue  | 62         | 18gj      |    600      | 06:26  |  2.18 | 1.0" SN |
red   | 47         | 18gj      |    600      | 06:26  |  2.18 | 1.0" SN |
blue  | 63         | 18gj      |    600      | 06:38  |  2.22 | 1.0" SN |
red   | 48         | 18gj      |    600      | 06:39  |  2.22 | 1.0" SN |
blue  | 64         | BD+33d2642|      30     | 06:54  |  1.98 | 1.0" standard high airmass|
red   | 49         | BD+33d2642|      30     | 06:54  |  1.98 | 1.0" standard high airmass|
blue  | 65         | 18gk      |   1200      | 07:00  |  1.63 | 1.5" blind offset from #3 |
red   | 50         | 18gk      |   1200      | 07:00  |  1.63 | 1.5" blind offset from #3 |
blue  | 66         | 18gk      |   1200      | 07:21  |  1.79 | 1.5" blind offset from #3 |
red   | 51         | 18gk      |   1200      | 07:22  |  1.8  | 1.5" blind offset from #3 |
blue  | 67         | 18gk      |   1200      | 07:42  |  2.0  | 1.5" blind offset from #3 |
red   | 52         | 18gk      |   1200      | 07:44  |  2.03 | 1.5" blind offset from #3 |
blue  | 68         | 17hxv     |    900      | 08:16  |  1.54 | 1.0" SN; fainter than expected, squeezing in an extra 5 min|
red   | 53         | 17hxv     |    900      | 08:16  |  1.54 | 1.0" SN; fainter than expected, squeezing in an extra 5 min |
blue  | 69         | 17hxv     |    900      | 08:32  |  1.54 | 1.0" SN | 
red   | 54         | 17hxv     |    900      | 08:33  |  1.54 | 1.0" SN | 
blue  | 70         | 17hxv     |    300      | 08:48  |  1.56 | 1.0" SN | 
red   | 55         | 17hxv     |    300      | 08:50  |  1.56 | 1.0" SN |
blue  | 71         | 17bwo     |   1200      | 08:59  |  1.57 | 1.0" blind offset from #1| 
red   | 56         | 17bwo     |   1200      | 09:00  |  1.57 | 1.0" blind offset from #1|
blue  | 72         | 17bwo     |   1200      | 09:20  |  1.5 | 1.0" blind offset from #1| 
red   | 57         | 17bwo     |   1200      | 09:22  |  1.5 | 1.0" blind offset from #1|
blue  | 73         | 17bwo     |   1200      | 09:41  |  1.44 | 1.0" blind offset from #1| 
red   | 58         | 17bwo     |   1200      | 09:44  |  1.44 | 1.0" blind offset from #1|
blue  | 74         | Feige 110 |     60      | 10:06  |  1.1 | 1.5"| 
red   | 59         | Feige 110 |     60      | 10:06  |  1.1 | 1.5"|
blue  | 74         | Feige 110 |     60      | 10:10  |  1.1 | 1.0"| 
red   | 59         | Feige 110 |     60      | 10:10  |  1.1 | 1.0"|

Greg will take internal flats and standards in the morning



