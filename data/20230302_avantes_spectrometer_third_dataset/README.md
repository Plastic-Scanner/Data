# Avantes_third_dataset

**Data collection with a Avantes industrial spectroscope.**

Machine used: AVASPEC-NIR256-2.0TEC\
Light source: Avalight-HAL Data: 03 March 2023

**Workflow:**

1.  Samples used from reference box C

2.  Executed in a darkened environment

3.  Sample is placed on under fiber optic end

4.  Spectrum settles

5.  Step 3 and 4 are repeated five times

6.  Export as .xlsx file

**Datastructure:**

Each file starts with:

Integration time \[ms\]: 105,000\
Averaging Nr. \[scans\]: 2\
Smoothing Nr. \[pixels\]: 0\
Data measured with spectrometer \[name\]: 1204091U1\
**Wavelength ;measurement 1 ;measurement 2 ;measurement 3 ; measurement
4 ;measurement 5**\
\[nm\] ;\[counts\] ;\[counts\] ;\[counts\] ;\[counts\] ;\[counts\]

After this the data starts

**Filenaming:**

Each file of the measured plastic has the same setup: (sample
code)\_(type of plastic)\_(fibre code).csv

The file "RefSpectrum_PlSc_FDP.csv" are the measurements taken from one
reference tile (tile provide by Plastic Scanner) with which the plastic
samples were measured. The setup is as follows: RefSpectrum\_(reference
tile)\_(fibre code).csv

**Data processing**

This Google Colab notebook uses the data from this repository to show
some example spectra [link to google
colab]([https://colab.research.google.com/drive/1LpmTrDJjxso9Lv-zOegcbH_Ezs8RKmB0](https://colab.research.google.com/drive/1lV_nJwXtI-wuD3B83oKq2dguGHzxLimc#scrollTo=5V-2m8YQry0D ))
