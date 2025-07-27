# Flood Detection using Sentinel-1 SAR Imagery

This Python script detects flood-affected areas by analyzing backscatter differences between pre- and post-event Sentinel-1 SAR images. It generates a binary flood mask based on a threshold value and applies morphological filters to remove noise.

---

## Overview

Flooding significantly reduces backscatter values in SAR imagery due to smooth water surfaces. This script compares two SAR images (pre-flood and post-flood) and flags pixels with decreased backscatter beyond a set threshold as flooded.

---

## Features

- Reads Sentinel-1 GeoTIFF images
- Computes pixel-wise difference
- Detects flooded areas using a threshold
- Applies morphological operations (noise cleaning)
- Exports a binary GeoTIFF flood mask
- Displays flood-affected areas using `matplotlib`

---

## Setup Instructions

Follow the steps below to set up and run the script in an isolated Python environment:

### 1. Create Virtual Environment

```bash
python -m venv myenv
```

### 2. Activate Virtual Environment

- On **Windows**:

```bash
myenv\Scripts\activate
```

- On **macOS/Linux**:

```bash
source myenv/bin/activate
```

### 3. Install Dependencies

Make sure you're in the same directory where `requirements.txt` is located, then run:

```bash
pip install -r requirements.txt
```

### 4. Run the Script

Once all packages are installed, run the flood detection script:

```bash
python flood_detection.py
```

> **Note**: Make sure to edit the file paths in `flood-detection.py` before running the script.

---

## Requirements

Your `requirements.txt` should include the following:

```
numpy
rasterio
matplotlib
scipy
```

---

## File Paths (Edit in Script)

Modify the following lines in the script to point to your input and output files:

```python
preImagePath = "D:/DeepakAssig/Sentinal1/Pre_20220611.tif"
postImagePath = "D:/DeepakAssig/Sentinal1/Post_20220623.tif"
floodOutputPath = "D:/DeepakAssig/Threshhold/flood_mask_0.09.tif"
```

---

## How It Works

1. **Load raster files** using `rasterio`
2. **Replace no-data values (`0`)** with `NaN`
3. **Crop** the larger image to match the smaller one
4. **Compute difference**: `post - pre`
5. **Threshold**: Identify pixels with a drop greater than `0.09`
6. **Clean**: Apply `binary_opening` and `binary_closing`
7. **Save flood mask** as a GeoTIFF
8. **Display map** of flood-affected areas

---

## Output

- **GeoTIFF flood mask** (`1` = flood, `0` = no flood)
- **Matplotlib visualization** of the flood extent in blue

---

## Threshold Logic

The threshold `0.09` is used to detect significant drops in SAR backscatter:

```python
flood_pixel = diff < -0.09
```

This is a common SAR-based flood detection value, but can be tuned based on scene conditions.

---

## 🖊️ Notes

- This method is most effective with calibrated and co-registered Sentinel-1 SAR images (GRD products).
- Works even under cloud cover (thanks to SAR).
- Ensure both images are from the same polarization and orbit direction (e.g., VV, ascending).
