# Kaggle SS4GG Hackathon: MIR Soil Spectroscopy Modeling

## Table of Contents

1. [Overview](#overview)
2. [Dataset Description](#dataset-description)
3. [Training and Test Sets](#training-and-test-sets)
4. [Instruments Involved](#instruments-involved)
5. [File Structure](#file-structure)
6. [Sample Submission](#sample-submission)
7. [Data Explorer](#data-explorer)
8. [Download and Metadata](#download-and-metadata)

---

## Overview

- **Challenge**: Machine learning competition focusing on consistently predicting clay content across multiple and diverse MIR instruments.
- **Teams**: 5
- **Last Updated**: 2 days ago
- **Sections**: Overview, Data, Code, Models, Discussion, Leaderboard, Rules, Team, Submissions

---

## Dataset Description

- **MIR Spectra Representation**: Pseudo absorption \( A \) in logarithm units (base 10). Calculated as \( A = \log_{10}(1/R) \), where \( R \) is the portion of light diffusely reflected by the soil surface.
- **Spectral Range**: Effective MIR range is 4000-650 \( \text{cm}^{-1} \), equivalent to 2,500 to 15,384 \( \text{nm} \).
- **Soil Properties**: Soil spectra have absorption features related to mineral and organic constituents, enabling the prediction of soil properties.

---

## Training and Test Sets

- **Training Set**: Derived from the Open Soil Spectral Library. Includes variables like `dataset`, `id`, `clay_perc`, `sand_perc`, `silt_perc`, and spectral range from 4000-650 \( \text{cm}^{-1} \).
- **Test Set**: Contains MIR spectra from 50 soil samples across 5 different instruments (total \( n = 250 \)). Columns include `unique_id`, `instrument`, `sample_id`, and spectral range from 4000-650 \( \text{cm}^{-1} \).

---

## Instruments Involved

- INST1: Bruker Alpha
- INST2: Perkin Elmer Spectrum 100
- INST3: Bruker Invenio
- INST4: Thermo Fisher Nicolet
- INST5: Agilent 4300

---

## File Structure

- **train.csv**: Training set with 57,268 rows and 1682 columns
- **test.csv**: Test set with 250 rows and 1679 columns
- **sample_submission.csv**: Sample submission file with 250 rows and 2 columns

---

## Sample Submission

- **Unique Values**: 250
- **Label Count**:
  - 0.00 - 10.00: 6
  - 10.00 - 20.00: 6
  - ...
  - 90.00 - 100.00: 6

---

## Data Explorer

- **File Size**: 760.77 MB
- **File Type**: csv
- **Column Count**: 2 of 2 columns

---

## Download and Metadata

- **Command**: `kaggle competitions download -c ss4gg-hackathon-mir-soil-spectroscopy`
- **License**: Subject to Competition Rules