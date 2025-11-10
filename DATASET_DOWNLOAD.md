# Dataset Download Instructions

## Quick Start

The dataset for this project comes from the [Kaggle Histopathologic Cancer Detection Competition](https://www.kaggle.com/c/histopathologic-cancer-detection).

## Method 1: Kaggle API (Recommended)

### Step 1: Install Kaggle API
```bash
pip install kaggle
```

### Step 2: Setup Kaggle Credentials
1. Go to [Kaggle Account Settings](https://www.kaggle.com/account)
2. Scroll to "API" section
3. Click "Create New API Token"
4. Save the downloaded `kaggle.json` file to:
   - **Windows**: `C:\Users\<YourUsername>\.kaggle\`
   - **Linux/Mac**: `~/.kaggle/`

### Step 3: Download Dataset
```bash
# Download competition files
kaggle competitions download -c histopathologic-cancer-detection

# Extract to data directory
# Windows PowerShell
Expand-Archive histopathologic-cancer-detection.zip -DestinationPath data/

# Linux/Mac
unzip histopathologic-cancer-detection.zip -d data/
```

### Step 4: Verify Files
```bash
# Check data directory
ls data/
```

You should see:
- `train/` (directory with ~220,025 .tif images)
- `test/` (directory with ~57,468 .tif images)
- `train_labels.csv` (~220,025 rows)
- `sample_submission.csv`

## Method 2: Manual Download

### Step 1: Download from Kaggle
1. Visit: https://www.kaggle.com/c/histopathologic-cancer-detection/data
2. Click "Download All" button (requires Kaggle account)
3. Wait for download to complete (~8 GB)

### Step 2: Extract Files
1. Extract the ZIP file
2. Move contents to `data/` directory in project root
3. Verify structure matches above

## Method 3: Use Alternative Location (C: Drive)

If you have limited space on your project drive:

### Option A: Download to C: Drive
```powershell
# Create directory on C: drive
New-Item -ItemType Directory -Path "C:\kaggle_data\cancer_detection"

# Download dataset there
cd C:\kaggle_data\cancer_detection
kaggle competitions download -c histopathologic-cancer-detection
Expand-Archive histopathologic-cancer-detection.zip -DestinationPath .
```

The notebooks will automatically detect data at `C:\kaggle_data\cancer_detection/`.

### Option B: Create Symbolic Link
```bash
# Windows (run as Administrator)
mklink /D "D:\MS_in_AI\WK3_CNN_Detection\WK_3_CNN_Cancer_Detection\data" "C:\kaggle_data\cancer_detection"

# Linux/Mac
ln -s /path/to/c/drive/data /path/to/project/data
```

## Troubleshooting

### Issue: "403 Forbidden" Error
**Solution**: Accept competition rules on Kaggle website first
1. Go to: https://www.kaggle.com/c/histopathologic-cancer-detection
2. Click "Join Competition" and accept rules
3. Try download again

### Issue: Not Enough Disk Space
**Solution**: Use alternative location (Method 3) or free up space
- Dataset size: ~8 GB compressed, ~6.3 GB extracted
- Recommended free space: 15+ GB (for models and results)

### Issue: Kaggle API Not Working
**Solution**: 
1. Verify `kaggle.json` is in correct location
2. Check file permissions (should be readable)
3. Try manual download (Method 2)

### Issue: Files Not Found in Notebook
**Solution**: Check path in notebook configuration cell
```python
# Update this path if needed
DATA_DIR = Path('C:/kaggle_data/cancer_detection')  # or your path
TRAIN_DIR = DATA_DIR / 'train'
TEST_DIR = DATA_DIR / 'test'
```

## Dataset Information

**Total Size**: ~6.3 GB (extracted)

**File Structure**:
```
data/
├── train/                    # 220,025 training images
│   ├── 0a7c9c5e2a2e9e8c.tif
│   ├── 0b2f2b9c5e3f9e8c.tif
│   └── ...
├── test/                     # 57,468 test images
│   ├── 0a2f2b9c5e3f9e8c.tif
│   ├── 0b7c9c5e2a2e9e8c.tif
│   └── ...
├── train_labels.csv          # Training labels (id, label)
└── sample_submission.csv     # Submission format template
```

**File Formats**:
- Images: `.tif` (TIFF format, 96×96 pixels, RGB)
- Labels: `.csv` (comma-separated values)

## Verification Script

Run this Python script to verify your dataset:

```python
import pandas as pd
from pathlib import Path

# Set your data path
DATA_DIR = Path('data')  # or 'C:/kaggle_data/cancer_detection'

# Check structure
print("Checking dataset structure...")
print(f"✓ Data directory exists: {DATA_DIR.exists()}")
print(f"✓ Train directory exists: {(DATA_DIR / 'train').exists()}")
print(f"✓ Test directory exists: {(DATA_DIR / 'test').exists()}")
print(f"✓ Labels file exists: {(DATA_DIR / 'train_labels.csv').exists()}")

# Count files
train_images = list((DATA_DIR / 'train').glob('*.tif'))
test_images = list((DATA_DIR / 'test').glob('*.tif'))
print(f"\nDataset statistics:")
print(f"  Training images: {len(train_images):,}")
print(f"  Test images: {len(test_images):,}")

# Load labels
df = pd.read_csv(DATA_DIR / 'train_labels.csv')
print(f"  Label rows: {len(df):,}")
print(f"  Class distribution:")
print(df['label'].value_counts())

print("\n✓ Dataset verification complete!")
```

## Next Steps

After downloading the dataset:

1. ✅ Verify file structure
2. ✅ Run verification script
3. ✅ Open main notebook: `notebooks/Cancer_Detection_CNN.ipynb`
4. ✅ Run cells sequentially to start training

## Support

If you encounter issues:
1. Check [Kaggle Competition FAQ](https://www.kaggle.com/c/histopathologic-cancer-detection/discussion)
2. Open an issue on GitHub
3. Check notebook comments for path configuration

---

**Ready to train?** → Open `notebooks/Cancer_Detection_CNN.ipynb` and start!
