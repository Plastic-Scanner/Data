# Avantes_second_dataset

**Data collection with a Avantes industrial spectroscope.**

Machine used: AVASPEC-NIR256-2.0TEC\
Light source: Avalight-HAL Data: 23 February 2023

**Workflow:**

1.  Samples used from reference box C

2.  Executed in a lightened environment

3.  Sample is placed on under fiber optic end

4.  Spectrum settles

5.  Step 3 and 4 are repeated five times

6.  Export as .xlsx file

A more detailed workflow is written in 'Measurement_report1_referenceboxC.pdf' [link to pdf](https://github.com/Plastic-Scanner/data/blob/main/data/20230222_avantes_spectrometer_second_dataset/Measurement_report1_referenceboxC.pdf)

**Datastructure:**

Each file starts with:

Integration time \[ms\]: 140,000\
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

The reference tile measured are set up in the following order:
Ref\_(reference tile)\_(fibre code).csv

The files starting with "RefSpectrum" are the measurements taken from
one reference tile with which the plastic samples were measured.

**Data processing**

This Google Colab notebook uses the data from this repository to show
some example spectra [link to google
colab](https://colab.research.google.com/drive/1lV_nJwXtI-wuD3B83oKq2dguGHzxLimc#scrollTo=5V-2m8YQry0D)
