# Notebook Visualization Plots

This directory contains screenshots and plots from the Jupyter notebook results.

## Required Images

Add the following images from your notebook execution:

1. **class_distribution.png** - Class distribution bar and pie charts
2. **sample_images.png** - Grid of sample histopathology images
3. **training_loss.png** - Training/validation loss curves
4. **training_accuracy.png** - Training/validation accuracy curves  
5. **training_auc.png** - AUC score progression
6. **confusion_matrices.png** - Confusion matrices for both models
7. **roc_curves.png** - ROC curves comparison
8. **image_properties.png** - Pixel value distributions (optional)

## How to Add Images

### Method 1: Screenshot (Quick)
1. Run the notebook
2. Take screenshots of plots
3. Save them here with the filenames above

### Method 2: Programmatic (Best Quality)
Add this after each plot in your notebook:

```python
from pathlib import Path
plots_dir = Path('../results/plots')
plots_dir.mkdir(parents=True, exist_ok=True)
plt.savefig(plots_dir / 'figure_name.png', dpi=300, bbox_inches='tight')
plt.show()
```

## Current Status

- [ ] class_distribution.png
- [ ] sample_images.png
- [ ] training_loss.png
- [ ] training_accuracy.png
- [ ] training_auc.png
- [ ] confusion_matrices.png
- [ ] roc_curves.png

Once you add the images:
1. Check them in: `git add results/plots/`
2. Commit: `git commit -m "Add notebook visualization plots"`
3. Push: `git push origin main`

The images will then display in the main README.md file!
