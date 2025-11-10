# Alternative: Download Kaggle Dataset Instructions
# Since you have limited disk space, here are your best options:

## RECOMMENDED: Use Google Colab or Kaggle Notebooks

### Option 1: Google Colab (FREE GPU)
"""
1. Upload your notebook to Google Colab
2. Run this code to download the dataset:

!pip install kaggle
!mkdir ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle competitions download -c histopathologic-cancer-detection
!unzip histopathologic-cancer-detection.zip -d data/
"""

### Option 2: Kaggle Notebooks (Dataset Pre-loaded)
"""
1. Go to: https://www.kaggle.com/c/histopathologic-cancer-detection
2. Click "Code" -> "New Notebook"
3. Dataset is automatically available at: /kaggle/input/histopathologic-cancer-detection/
4. Copy your notebook code there
5. Enable GPU: Settings -> Accelerator -> GPU
"""

### Option 3: Download to C: Drive (if it has more space)
"""
# PowerShell:
kaggle competitions download -c histopathologic-cancer-detection -p "C:\\kaggle_data"
cd C:\\kaggle_data
Expand-Archive histopathologic-cancer-detection.zip -DestinationPath .

# Then update your notebook path:
DATA_DIR = Path('C:/kaggle_data')
"""

### Option 4: Download Sample for Testing
"""
# Download just the labels and sample files first:
kaggle competitions download histopathologic-cancer-detection -f train_labels.csv -p data
kaggle competitions download histopathologic-cancer-detection -f sample_submission.csv -p data

# Then download a small subset of images for testing your code
"""

### Option 5: Clean Up D: Drive
"""
# Find large files to delete:
Get-ChildItem D:\\ -Recurse -File | 
    Sort-Object Length -Descending | 
    Select-Object -First 20 FullName, @{Name="SizeGB";Expression={[math]::Round($_.Length/1GB,2)}} |
    Format-Table -AutoSize
"""

## IMMEDIATE ACTION NEEDED
print("="*70)
print("DISK SPACE ISSUE")
print("="*70)
print(f"Current free space on D: ~2 MB")
print(f"Required space: ~8 GB (6.31 GB download + extraction)")
print(f"Shortage: ~7.998 GB")
print()
print("RECOMMENDATIONS:")
print("1. Use Kaggle Notebooks (EASIEST - no download needed)")
print("   -> Go to kaggle.com and work in their environment")
print()
print("2. Use Google Colab (FREE GPU)")
print("   -> Upload notebook and download data there")
print()
print("3. Free up 8 GB on D: drive")
print("   -> Delete unnecessary files")
print()
print("4. Download to C: drive or external drive")
print("   -> If you have more space elsewhere")
print("="*70)
