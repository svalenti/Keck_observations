# Observation Log:

# Notes:

* Conditions: 
* Seeing: 0.6
* SA: Percy
* OA: Tony
* Data Directory: /sdata1002/deimos8/2019aug28_B
* Data Directory on Dark: /dark/hal/data/20190827_Keck
* Starlist: starlist_20190827.txt
* Setup saved to:

Notes:
When we tried to switch back to spectroscopic observations after imaging 19osy and the direct slit image of 19krl we were unable to 
get the FCS to track. We restarted the FCS, ran the troubleshooting tool, and ultimately took new calibration images. 
At this same time we realized that the grating was no longer tilting to put the zeroth order on the detector.
To avoid further issues we stopped taking direct images of the slit and trusted that we were aligning the slit

## Setup:
Focus: -7309
Grating: 600ZD  
Filter: GG455  
Central Wavelength: 6925 
SlitMask: LVMslitC 
Width: 1.0"

| Obs #     | Target      | Exptime (s) |Filter  | Start Time (UT) | Airmass | Comments                                                   |
|-----------|-------------|-------------|--------|-----------------|---------|------------------------------------------------------------|
|   1       |    Qtz      |             |OGG455  |                 |    -    | LVMslitC slitmask check  
|   2       |    Qtz      |             |OGG455  |                 |    -    | Longslit1.5 slitmask check  
|   3       |NeArKrXe     | 1           |OGG455  |                 |    -    |
|   4       |NeArKrXe     | 1           |OGG455  |                 |    -    |
|   5       |InternalFlat | 6           |OGG455  |                 |    -    | 1.5" slit is saturated
|   6       |InternalFlat | 6           |OGG455  |                 |    -    | 1.5" slit is saturated
|   7       |InternalFlat | 6           |OGG455  |                 |    -    | 1.5" slit is saturated
|   8       |CdZnHg       | 3           |OGG455  |                 |    -    |
|   9       |CdZn         | 12          |OGG455  |                 |    -    |
|10         |DomeFlat     |7            |I       |                 |    -    | Suggested exposure times
|11         |DomeFlat     |7            |I       |                 |    -    | Suggested exposure times 
|12         |DomeFlat     |7            |I       |                 |    -    | Suggested exposure times 
|13         |DomeFlat     |10           |R       |                 |    -    | Suggested exposure times 
|14         |DomeFlat     |10           |R       |                 |    -    | Suggested exposure times 
|15         |DomeFlat     |15           |R       |                 |    -    | increased exposure time to get count rate similar to that on website
|16         |DomeFlat     |10           |I       |                 |    -    | increased exposure time to get count rate similar to that on website
|17         |Bias         |0            |        |                 |    -    | Hatch wasn't closed - may not make a difference
|18         |Bias         |0            |        |                 |    -    | 
|19         |BD174708     |10           |OGG455  |10:27:59         | 1        |
|20         |2018eog_S1   |10           |OGG455  |10:42:09         | 1        | MIRA (focus) before this exposure; direct image of offset to check slit slignment
|21         |2018eog      |1200         |OGG455  |10:47:02         |  1.31     |  Target was reaching telescope pointing limit, so split evenly the last 2 exposures 
|22         |2018eog      |900          |OGG455  | 11:08:11        |  1.33     |     
|23         |2018eog      |900          |OGG455  | 11:24:20        |  1.43     |     
|24         |2019osy      |  10         |OGG455  | 11:43:45        |  1.54     |     direct image of slit on offset star
|25         |2018osy      | 900s        |OGG455  | 11:47:03        |  1.54     |     spec exposure
|26         |2018osy      | 900s        |OGG455  | 12:03:12        |  1.5      |     spec exposure
|27         |2018osy      | 60s         |I       | 12:22:20        |  1.47     |      I band image
|28         |2018osy      | 60s         |I       | 12:23:56        |  1.47     |      I band image
|29         |LTT9239      | 1s          |I       | 12:28:03        |  1.46     |      I band standard - saturated
|30         |LTT9239      | 1s          |I       | 12:32:00        |  1.47     |      I band standard defocused - not saturated
|31         |2019krl      | 10          | OGG455 | 12:45:30        |  1.02     |     direct image of slit. However we were unable to get the FCS to track when we moved to our target, had to restart and recalibrate, grating wheel was not able to go to zero position. So we reacquired the offset star and then offset to the science target
|32         |2019krl      | 400         | OGG455 | 13:18:07        |  1        |     
|33         |2019krl      | 400         |OGG455  | 13:25:55        |  1        |     
|34         |2019krl      | 400         |OGG455  | 13:33:43        |  1        |     
|35         |2018ivc      | 1200        |OGG455  | 13:44:29        |  1.09     |     
|36         |2018ivc      | 1200        |OGG455  | 14:05:41        |  1.07     |  
|37         |2018ivc      | 1200        |OGG455  | 14:26:47        |  1.06     |
|38         |2018zd       | 420         |OGG455  | 14:51:20        |  2.21     |
|39         |2018zd       | 420         |OGG455  | 14:59:28        |  2.18     |  This exposure ends after 15 deg twilight
|40         |Hiltner600   | 20          |OGG455  | 15:10:41        |  1.72     | high airmass standard
|41         |HD19445      | 10          |OGG455  | 15:16:16        |  1.01     |  Nothing to guide on but probably ok  
|42         |InternalFlat | 4           |OGG455  | 15:22:33        |    -      |
|43         |InternalFlat | 4           |OGG455  | 15:23:46        |    -      |
|44         |InternalFlat | 4           |OGG455  | 15:24:59        |    -      |
|45         |InternalFlat | 2           |OGG455  | 15:30:31        |    -      | Too faint in the blue
|46         |InternalFlat | 2           |OGG455  | 15:31:42        |    -      |
|47         |InternalFlat | 2           |OGG455  | 15:32:53        |    -      |

