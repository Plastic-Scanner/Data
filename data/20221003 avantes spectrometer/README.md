# Data collection with a Avantes industrial spectroscope.  
Machine used:  AVASPEC-NIR256-2.0TEC  
Light source: Avalight-HAL
Data: 03 October 2022

## Workflow:
- Sample is chosen at random from bag of clean samples
- Sample is placed on under fiber optic end
- Spectrum settles
- Export as .txt file

## Datastructure:  
Each file starts with: 

> Integration time [ms]:  15,000  
Averaging Nr. [scans]: 10  
Smoothing Nr. [pixels]: 0  
Data measured with spectrometer [name]: 1204091U1  
**Wave   ;Sample   ;Dark     ;Reference;Reflectance**  
[nm]   ;[counts] ;[counts] ;[counts] ;[%]  

After this the data starts

## Filenaming:  
0-99 series is PP.  
100-199 series is PET.  
200-299 series is HDPE.  
300-399 series is PS
900-999 series is unknowns, can be anthing like ABS, PLA, POM or plastics that are missing marking.other items that do not have this naming have the plastic type in the name itself.


## Data processing  
This Google Colab notebook uses the data from this repository to show some example spectra
[link to google colab](https://colab.research.google.com/drive/1LpmTrDJjxso9Lv-zOegcbH_Ezs8RKmB0)
