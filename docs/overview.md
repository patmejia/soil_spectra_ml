## ss4gg hackathon: mir soil spectroscopy modeling dataset summary

![clay loam silt sand](/docs/img/clay_loam_silt_sand.png)

### overview
- **objective**: to develop ml models for predicting soil clay content using mir spectra.
- **evaluation metric**: root mean squared error (rmse) between the predicted and actual clay content.
- **spectral representation**: pseudo absorbance \( $A = \log_{10}(1/R)$ \), where \( $R$ \) is the portion of light diffusely reflected by soil.
- **effective mir range**: \( $4000-650 \, \text{cm}^{-1}$ \), equivalent to \( $2500-15384 \, \text{nm}$ \).
- **spectral interval**: 2 \( $\text{cm}^{-1}$ \).

### train dataset (`train.csv`)
- **dimensions**: 57,268 rows and 1682 columns.
- **target variable**: `clay_perc` (clay content in %).
- **additional soil variables**: 
  - `sand_perc`: sand content in %.
  - `silt_perc`: silt content in %.
  - `texture_sum`: summation of clay, sand, and silt percentages (always equals 100%).
- **spectral data**: 
  - range: \( $650 \, \text{cm}^{-1}$ \) to \( $4000 \, \text{cm}^{-1}$ \).
  - interval: \( $2 \, \text{cm}^{-1}$ \).

### test dataset (`test.csv`)
- **dimensions**: 250 rows and 1679 columns.
- **unique identifiers**: 
  - `unique_id`: composite of sample and instrument.
  - `instrument`: mir instrument used.
  - `sample_id`: soil sample identifier.
- **spectral data**: 
  - same range and interval as the train dataset.
- **instrument types**: 
  - inst1: bruker alpha
  - inst2: perkin elmer spectrum 100
  - inst3: bruker invenio
  - inst4: thermo fisher nicolet
  - inst5: agilent 4300

### sample submission (`sample_submission.csv`)
- **dimensions**: 250 rows and 2 columns.
- **columns**: 
  - `unique_id`: unique identifier for test set samples.
  - `clay_perc`: placeholder for predicted clay content.

### special considerations
- **high-dimensionality**: computational cost is a factor due to the large number of spectral features.
- **instrument variability**: different mir instruments in the test set could introduce variance in predictions.
- **data sensitivity**: soil texture is sensitive to instrument dissimilarity.
- **data source**: train set is from the open soil spectral library.

### file metadata
- **file size**: 760.77 mb
- **file type**: csv
- **license**: subject to competition rules

  