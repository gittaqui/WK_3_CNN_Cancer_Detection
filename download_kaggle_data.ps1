# Kaggle Dataset Download Script for Histopathologic Cancer Detection
# This script helps download the dataset with space management options

Write-Host "=" * 70 -ForegroundColor Cyan
Write-Host "Kaggle Dataset Download - Histopathologic Cancer Detection" -ForegroundColor Cyan
Write-Host "=" * 70 -ForegroundColor Cyan

# Check Kaggle CLI
Write-Host "`nChecking Kaggle CLI installation..." -ForegroundColor Yellow
try {
    $kaggleVersion = kaggle --version 2>&1
    Write-Host "Kaggle CLI installed: $kaggleVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Kaggle CLI not installed!" -ForegroundColor Red
    Write-Host "Install with: pip install kaggle" -ForegroundColor Yellow
    exit 1
}

# Check disk space
Write-Host "`nChecking disk space..." -ForegroundColor Yellow
$drive = Get-PSDrive D
$freeSpaceGB = [math]::Round($drive.Free / 1GB, 2)
$requiredSpaceGB = 8

Write-Host "Free space on D: drive: $freeSpaceGB GB" -ForegroundColor Cyan
Write-Host "Required space: $requiredSpaceGB GB (6.31 GB download + extraction)" -ForegroundColor Cyan

if ($freeSpaceGB -lt $requiredSpaceGB) {
    Write-Host "`nWARNING: Insufficient disk space!" -ForegroundColor Red
    Write-Host "You need at least $requiredSpaceGB GB free space." -ForegroundColor Red
    Write-Host "`nOptions:" -ForegroundColor Yellow
    Write-Host "1. Free up space on D: drive"
    Write-Host "2. Download to different drive (see option below)"
    Write-Host "3. Use Kaggle Notebooks (online, no download needed)"
    Write-Host "`nTo download to C: drive instead:" -ForegroundColor Cyan
    Write-Host "  kaggle competitions download -c histopathologic-cancer-detection -p C:\temp\kaggle_data" -ForegroundColor White
    
    $continue = Read-Host "`nDo you want to continue anyway? (yes/no)"
    if ($continue -ne "yes") {
        Write-Host "Download cancelled." -ForegroundColor Yellow
        exit 0
    }
}

# Set download path
$downloadPath = "data"
Write-Host "`nDownload location: $downloadPath" -ForegroundColor Cyan

# Create data directory if it doesn't exist
if (-not (Test-Path $downloadPath)) {
    New-Item -ItemType Directory -Path $downloadPath -Force | Out-Null
    Write-Host "Created directory: $downloadPath" -ForegroundColor Green
}

# Download the dataset
Write-Host "`nDownloading dataset..." -ForegroundColor Yellow
Write-Host "Competition: histopathologic-cancer-detection" -ForegroundColor Cyan
Write-Host "This may take 10-30 minutes depending on your internet speed..." -ForegroundColor Yellow

try {
    kaggle competitions download -c histopathologic-cancer-detection -p $downloadPath
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`nDownload completed successfully!" -ForegroundColor Green
        
        # Check if zip file exists
        $zipFile = Join-Path $downloadPath "histopathologic-cancer-detection.zip"
        if (Test-Path $zipFile) {
            $zipSizeGB = [math]::Round((Get-Item $zipFile).Length / 1GB, 2)
            Write-Host "Downloaded file size: $zipSizeGB GB" -ForegroundColor Cyan
            
            Write-Host "`nExtracting files..." -ForegroundColor Yellow
            Expand-Archive -Path $zipFile -DestinationPath $downloadPath -Force
            Write-Host "Extraction completed!" -ForegroundColor Green
            
            # Optional: Remove zip file to save space
            $removeZip = Read-Host "`nRemove zip file to save space? (yes/no)"
            if ($removeZip -eq "yes") {
                Remove-Item $zipFile -Force
                Write-Host "Zip file removed." -ForegroundColor Green
            }
        }
        
        # List downloaded files
        Write-Host "`nDataset contents:" -ForegroundColor Cyan
        Get-ChildItem $downloadPath | Format-Table Name, Length, LastWriteTime -AutoSize
        
        Write-Host "`n" + "=" * 70 -ForegroundColor Green
        Write-Host "DATASET READY!" -ForegroundColor Green
        Write-Host "=" * 70 -ForegroundColor Green
        Write-Host "`nYou can now run the notebook: notebooks/Cancer_Detection_CNN.ipynb" -ForegroundColor Cyan
        
    } else {
        Write-Host "`nDownload failed!" -ForegroundColor Red
        Write-Host "Check your Kaggle API credentials in: $env:USERPROFILE\.kaggle\kaggle.json" -ForegroundColor Yellow
    }
    
} catch {
    Write-Host "`nERROR during download: $_" -ForegroundColor Red
    Write-Host "`nTroubleshooting:" -ForegroundColor Yellow
    Write-Host "1. Ensure you have accepted the competition rules on Kaggle website"
    Write-Host "2. Verify your API credentials: $env:USERPROFILE\.kaggle\kaggle.json"
    Write-Host "3. Check internet connection"
    Write-Host "4. Try downloading manually from: https://www.kaggle.com/c/histopathologic-cancer-detection/data"
}
