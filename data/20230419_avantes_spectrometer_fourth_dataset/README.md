# Avantes_third_dataset

**Data collection with a Avantes industrial spectroscope.**

Machine used: AVASPEC-NIR256-2.0TEC\
Light source: Avalight-HAL  
Date: 19 April 2023

**Workflow:**

1.  Samples used from reference box C

2.  Executed in a Lab environment

3.  Sample is placed on under fiber optic end

4.  Spectrum settles

5.  Spectrum exported as txt  

6.  Step 3, 4 and 5 are repeated three times


**Datastructure:**

Each file starts with:

Integration time \[ms\]: 100,000\
Averaging Nr. \[scans\]: 1\
Smoothing Nr. \[pixels\]: 0\
Data measured with spectrometer [name]: 1204091U1  
**Wave   ;Sample   ;Dark     ;Reference;Reflectance**  
[nm]   ;[counts] ;[counts] ;[counts] ;[%]  
After this the data starts

**Filenaming:**

Each file of the measured plastic has the same setup: (sample
code)\_(type of plastic)\_(fibre code)\_(scan itteration).csv

The file "RefSpectrum.csv" are the measurements taken from one
reference tile (tile provide by Plastic Scanner) with which the plastic
samples were measured. The setup is as follows: RefSpectrum\_(reference
tile)\_(fibre code).csv

**Data processing**
