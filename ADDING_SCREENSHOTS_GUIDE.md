# Adding Notebook Visualizations to README

This guide explains how to capture and add screenshots from your Jupyter notebook results to the GitHub README.

## Quick Start

### Option 1: Manual Screenshot Method (Easiest)

1. **Open the notebook** in Jupyter:
   ```bash
   jupyter notebook notebooks/Cancer_Detection_CNN.ipynb
   ```

2. **Run all cells** to generate visualizations

3. **Take screenshots**:
   - Windows: Use **Snipping Tool** (Win + Shift + S) or **Snip & Sketch**
   - Mac: Use **Command + Shift + 4**
   - Linux: Use **Screenshot** tool or **Flameshot**

4. **Save screenshots** to `results/plots/` folder with these names:
   - `class_distribution.png`
   - `sample_images.png`
   - `training_history.png`
   - `roc_curves.png`
   - `confusion_matrices.png`

5. **Commit to Git**:
   ```bash
   git add results/plots/
   git commit -m "Add visualization screenshots from notebook"
   git push origin main
   ```

### Option 2: Programmatic Method (Best Quality)

Add these code snippets to your notebook after each plot:

```python
from pathlib import Path

# Create directory
plots_dir = Path('../results/plots')
plots_dir.mkdir(parents=True, exist_ok=True)

# Save the current figure
plt.savefig(plots_dir / 'figure_name.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()
```

## Recommended Screenshots to Capture

### 1. Class Distribution (Section 4)
**Cell**: Class Distribution Analysis  
**Save as**: `class_distribution.png`  
**Shows**: Bar chart and pie chart of benign vs malignant distribution

**Code to add**:
```python
plots_dir = Path('../results/plots')
plots_dir.mkdir(parents=True, exist_ok=True)
plt.savefig(plots_dir / 'class_distribution.png', dpi=300, bbox_inches='tight')
plt.show()
```

### 2. Sample Images (Section 4)
**Cell**: Visualize Sample Images from Both Classes  
**Save as**: `sample_images.png`  
**Shows**: Grid of sample histopathology images (benign and malignant)

### 3. Training History - Loss (Section 8)
**Cell**: Plot Training History for Both Models (Loss)  
**Save as**: `training_loss.png`  
**Shows**: Training and validation loss curves for both models

### 4. Training History - Accuracy (Section 8)
**Cell**: Plot Training History for Both Models (Accuracy)  
**Save as**: `training_accuracy.png`  
**Shows**: Training and validation accuracy curves

### 5. Training History - AUC (Section 8)
**Cell**: Plot Training History for Both Models (AUC)  
**Save as**: `training_auc.png`  
**Shows**: AUC score progression during training

### 6. Confusion Matrices (Section 8)
**Cell**: Confusion Matrix and ROC Curve Visualization  
**Save as**: `confusion_matrices.png`  
**Shows**: Side-by-side confusion matrices for both models

### 7. ROC Curves (Section 8)
**Cell**: plot_roc_curves function output  
**Save as**: `roc_curves.png`  
**Shows**: ROC curves comparing both models with AUC scores

## Complete Example: Modified Notebook Cells

### For Class Distribution Cell

```python
# Class Distribution Analysis
if 'df' in locals():
    # ... existing code ...
    
    plt.tight_layout()
    
    # SAVE THE PLOT
    from pathlib import Path
    plots_dir = Path('../results/plots')
    plots_dir.mkdir(parents=True, exist_ok=True)
    plt.savefig(plots_dir / 'class_distribution.png', dpi=300, bbox_inches='tight')
    
    plt.show()
    
    # ... rest of code ...
```

### For ROC Curves Cell

```python
def plot_roc_curves(y_true_1, y_pred_probs_1, y_true_2, y_pred_probs_2):
    """Plot ROC curves for both models"""
    # ... existing code ...
    
    plt.tight_layout()
    
    # SAVE THE PLOT
    from pathlib import Path
    plots_dir = Path('../results/plots')
    plots_dir.mkdir(parents=True, exist_ok=True)
    plt.savefig(plots_dir / 'roc_curves.png', dpi=300, bbox_inches='tight')
    
    plt.show()
```

## Using the Helper Script

Run the helper script to set up directories:

```bash
python save_notebook_plots.py
```

This will:
- Create the `results/plots/` directory
- Display instructions for saving plots
- List all recommended plot filenames

## Image Specifications

**Recommended settings**:
- **Format**: PNG (best for web)
- **DPI**: 300 (high quality)
- **Background**: White (`facecolor='white'`)
- **Size**: Automatic (bbox_inches='tight')

**File sizes**:
- Typical size: 50-200 KB per image
- GitHub README handles images up to 10MB
- Keep total images folder under 5MB for fast loading

## Verify in README

After saving images, check that they display correctly:

1. **Push to GitHub**:
   ```bash
   git add results/plots/
   git commit -m "Add notebook visualizations"
   git push origin main
   ```

2. **View on GitHub**: Visit your repository and check the README

3. **Local preview**: Install grip to preview README locally:
   ```bash
   pip install grip
   grip README.md
   ```
   Then open http://localhost:6419

## Alternative: Use Kaggle Notebooks

If you're running on Kaggle:

1. Run your notebook on Kaggle
2. Right-click on each plot → "Save Image As..."
3. Download to your local computer
4. Upload to `results/plots/` in your repository

## Troubleshooting

### Images not displaying in README
- Check file paths are relative: `results/plots/image.png`
- Verify files are committed and pushed to GitHub
- Ensure filenames match exactly (case-sensitive)

### Images too large
- Reduce DPI: use `dpi=150` instead of `dpi=300`
- Compress images: Use online tools like TinyPNG
- Resize images: Use Pillow/PIL in Python

### Plots look blurry
- Increase DPI: use `dpi=300` or higher
- Use vector format: Save as SVG (not widely supported in GitHub README)
- Ensure `bbox_inches='tight'` is set

## Complete Workflow Example

```python
# 1. At the top of your notebook (setup cell)
from pathlib import Path
import matplotlib.pyplot as plt

PLOTS_DIR = Path('../results/plots')
PLOTS_DIR.mkdir(parents=True, exist_ok=True)

def save_plot(filename):
    """Helper function to save current plot"""
    plt.savefig(PLOTS_DIR / filename, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✅ Saved: {filename}")

# 2. After each plot
plt.figure(figsize=(12, 6))
# ... your plotting code ...
save_plot('class_distribution.png')
plt.show()

# 3. Commit all at once
# git add results/plots/
# git commit -m "Add all notebook visualizations"
# git push origin main
```

## Summary Checklist

- [ ] Create `results/plots/` directory
- [ ] Run notebook to generate all plots
- [ ] Save/screenshot each key visualization
- [ ] Name files according to convention
- [ ] Commit and push to GitHub
- [ ] Verify images display in README on GitHub
- [ ] Update README captions if needed

## Need Help?

See the main README for image placeholders and descriptions. The README already contains the structure - you just need to add the actual images!

**Key files**:
- `README.md` - Contains image placeholders
- `results/plots/` - Where to save your images
- `save_notebook_plots.py` - Helper script
- This guide - `ADDING_SCREENSHOTS_GUIDE.md`
