# Quick Download to C: Drive Script
# Run this PowerShell script to download the Kaggle dataset

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Kaggle Dataset Download to C: Drive" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Create directory
$downloadDir = "C:\kaggle_data\cancer_detection"
Write-Host "Creating directory: $downloadDir" -ForegroundColor Yellow
New-Item -ItemType Directory -Path $downloadDir -Force | Out-Null

# Download dataset
Write-Host "`nDownloading dataset (~6.31 GB)..." -ForegroundColor Yellow
Write-Host "This will take 10-30 minutes depending on your internet speed.`n" -ForegroundColor Cyan

kaggle competitions download -c histopathologic-cancer-detection -p $downloadDir

if ($LASTEXITCODE -eq 0) {
    Write-Host "`nDownload complete!" -ForegroundColor Green
    
    # Extract
    Write-Host "`nExtracting files..." -ForegroundColor Yellow
    $zipFile = Join-Path $downloadDir "histopathologic-cancer-detection.zip"
    Expand-Archive -Path $zipFile -DestinationPath $downloadDir -Force
    
    Write-Host "`nExtraction complete!" -ForegroundColor Green
    Write-Host "`nDataset location: $downloadDir" -ForegroundColor Cyan
    
    # Optional: Create symbolic link to D: drive project
    Write-Host "`nCreating symbolic link in your project..." -ForegroundColor Yellow
    $projectDataDir = "D:\MS_in_AI\WK3_CNN_Detection\WK_3_CNN_Cancer_Detection\data"
    
    if (Test-Path $projectDataDir) {
        Remove-Item $projectDataDir -Recurse -Force
    }
    
    New-Item -ItemType SymbolicLink -Path $projectDataDir -Target $downloadDir -Force
    Write-Host "Symbolic link created: $projectDataDir -> $downloadDir" -ForegroundColor Green
    
    Write-Host "`n========================================" -ForegroundColor Green
    Write-Host "SETUP COMPLETE!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "`nYou can now run your notebook!" -ForegroundColor Cyan
    
} else {
    Write-Host "`nDownload failed!" -ForegroundColor Red
    Write-Host "Please ensure you have:" -ForegroundColor Yellow
    Write-Host "1. Accepted competition rules at: https://www.kaggle.com/c/histopathologic-cancer-detection" -ForegroundColor White
    Write-Host "2. Valid Kaggle API credentials in: $env:USERPROFILE\.kaggle\kaggle.json" -ForegroundColor White
}
