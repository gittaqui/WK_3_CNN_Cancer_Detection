# Dataset Download Instructions

## Problem
- D: drive has only ~2 MB free space
- Dataset requires ~8 GB (6.31 GB download + extraction)
- **Solution**: Download to C: drive (116 GB available)

## Quick Start - Option 1: PowerShell Script (RECOMMENDED)

Run the automated script:
```powershell
.\download_to_c_drive.ps1
```

This script will:
1. Create C:\kaggle_data\cancer_detection directory
2. Download the dataset (~6.31 GB)
3. Extract the files
4. Create a symbolic link from your project to C: drive data
5. Your notebook will work seamlessly!

## Manual Download - Option 2

### Step 1: Download
```powershell
# Create directory
New-Item -ItemType Directory -Path "C:\kaggle_data\cancer_detection" -Force

# Download dataset
kaggle competitions download -c histopathologic-cancer-detection -p "C:\kaggle_data\cancer_detection"
```

### Step 2: Extract
```powershell
# Extract the zip file
Expand-Archive -Path "C:\kaggle_data\cancer_detection\histopathologic-cancer-detection.zip" -DestinationPath "C:\kaggle_data\cancer_detection" -Force
```

### Step 3: Update Notebook Path
In your notebook, update the DATA_DIR path:
```python
# Option A: Direct path
DATA_DIR = Path('C:/kaggle_data/cancer_detection')

# Option B: Create symbolic link (run in PowerShell as Admin)
New-Item -ItemType SymbolicLink -Path "D:\MS_in_AI\WK3_CNN_Detection\WK_3_CNN_Cancer_Detection\data" -Target "C:\kaggle_data\cancer_detection" -Force
```

## Alternative Options

### Option 3: Kaggle Notebooks (NO DOWNLOAD NEEDED)
1. Go to: https://www.kaggle.com/c/histopathologic-cancer-detection
2. Click "Code" → "New Notebook"
3. Dataset is pre-loaded at: `/kaggle/input/histopathologic-cancer-detection/`
4. Enable GPU: Settings → Accelerator → GPU
5. Upload your notebook code

**Benefits:**
- No disk space needed
- Free GPU access
- Dataset already available
- Easy submission to competition

### Option 4: Google Colab (FREE GPU)
1. Upload notebook to Google Colab
2. Run:
```python
!pip install kaggle
!mkdir ~/.kaggle
# Upload your kaggle.json
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle competitions download -c histopathologic-cancer-detection
!unzip histopathologic-cancer-detection.zip -d data/
```

## Troubleshooting

### "403 Forbidden" Error
- You need to accept the competition rules
- Visit: https://www.kaggle.com/c/histopathologic-cancer-detection
- Click "Join Competition" or "I Understand and Accept"

### "API credentials not found"
- Create Kaggle API token: https://www.kaggle.com/settings/account
- Download `kaggle.json`
- Place in: `C:\Users\<YourUsername>\.kaggle\kaggle.json`
- Set permissions: `chmod 600 ~/.kaggle/kaggle.json` (Linux/Mac)

### Dataset Structure After Download
```
C:\kaggle_data\cancer_detection\
├── train\                  # 220,025 training images (.tif)
├── test\                   # 57,468 test images (.tif)
├── train_labels.csv        # Training labels
└── sample_submission.csv   # Submission format
```

## Disk Space Requirements
- Download: 6.31 GB (compressed)
- Extracted: ~7 GB
- **Total needed: ~13-14 GB** (keep zip + extracted)
- **Minimum: ~8 GB** (if you delete zip after extraction)

## After Download

Your notebook is ready to run! The DATA_DIR will automatically detect the dataset location.

**Run your notebook:**
```powershell
jupyter notebook notebooks\Cancer_Detection_CNN.ipynb
```

## Need Help?

- Kaggle Competition: https://www.kaggle.com/c/histopathologic-cancer-detection
- Kaggle API Docs: https://github.com/Kaggle/kaggle-api
- GitHub Issues: https://github.com/gittaqui/WK_3_CNN_Cancer_Detection/issues
