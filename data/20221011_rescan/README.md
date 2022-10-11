# Rescan of items
this is a rescan of the items that were both in the 20220531 DB2.1 test and the 20221003 Avantes scan.


# How the data was collected
All made in a single day, on the 31st of May 2022
Measurements taken with DB2.1 board #01
## Installed LED’s: 

|Wavelength (nm) |940 |1050 |1200 |1300 |1460 |1550 |1650 |1720 |
|---|---|---|---|---|---|---|---|---|
|Current limiting resistor (Ω) |200 |150 |240 |240 |150 |150 |40 |130 |

Firmware version: used the firmware in this state: https://github.com/Plastic-Scanner/DB2.x-Firmware/tree/d3c327b010a1d05257fe97519fa377fe8ecc6a79

Spectraplot version: used the software in this state:
https://github.com/Plastic-Scanner/PSplot/tree/bea524f7bcbdfb529c8c889efb674bfaf6252db4


Workflow:
- Sample is chosen at random from bag of clean samples
- Sample is placed on #01 board
- Lid is closed
- Spectraplot asks the board to scan 5 times with 1 second interval
- Lid is opened
- Sample is moved to #03 board
- Lid is closed
- Spectraplot asks the board to scan 5 times with 1 second interval
- Lid is opened
- Sample is placed in photobooth for picture 

## Filenaming  
0-99 series is PP.  
100-199 series is PET.  
200-299 series is HDPE.  
300-399 series is PS.  
900-999 series is unknowns, can be anthing like ABS, PLA, POM or plastics that are missing marking.other items that do not have this naming have the plastic type in the name itself.