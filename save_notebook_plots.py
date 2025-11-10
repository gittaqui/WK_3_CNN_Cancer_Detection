"""
Helper script to save plots from Jupyter notebook for README visualization.

This script helps you save key visualizations from the Cancer_Detection_CNN.ipynb
notebook to include in your GitHub README.

Usage:
    1. Run the Jupyter notebook first to generate all plots
    2. When a plot is displayed, run this in a code cell:
       
       from pathlib import Path
       plots_dir = Path('../results/plots')
       plots_dir.mkdir(parents=True, exist_ok=True)
       plt.savefig(plots_dir / 'figure_name.png', dpi=300, bbox_inches='tight')
       plt.show()

Recommended figure names:
    - class_distribution.png
    - sample_images.png
    - training_loss.png
    - training_accuracy.png
    - training_auc.png
    - confusion_matrices.png
    - roc_curves.png
"""

from pathlib import Path
import matplotlib.pyplot as plt

def setup_plots_directory():
    """Create results/plots directory if it doesn't exist"""
    plots_dir = Path('results/plots')
    plots_dir.mkdir(parents=True, exist_ok=True)
    print(f"✅ Created directory: {plots_dir.resolve()}")
    return plots_dir

def save_current_plot(filename, dpi=300):
    """
    Save the current matplotlib figure to results/plots/
    
    Parameters:
    - filename: Name of the file (e.g., 'class_distribution.png')
    - dpi: Resolution (default 300 for high quality)
    
    Usage:
        plt.figure()
        # ... your plotting code ...
        save_current_plot('my_plot.png')
    """
    plots_dir = Path('results/plots')
    plots_dir.mkdir(parents=True, exist_ok=True)
    
    filepath = plots_dir / filename
    plt.savefig(filepath, dpi=dpi, bbox_inches='tight', facecolor='white')
    print(f"✅ Saved: {filepath}")

def main():
    """Main function to set up directories"""
    plots_dir = setup_plots_directory()
    
    print("\n" + "="*70)
    print("PLOT SAVING HELPER - READY")
    print("="*70)
    print("\nTo save plots from your notebook, add this code after each plot:")
    print("\n  from pathlib import Path")
    print("  plots_dir = Path('../results/plots')")
    print("  plots_dir.mkdir(parents=True, exist_ok=True)")
    print("  plt.savefig(plots_dir / 'figure_name.png', dpi=300, bbox_inches='tight')")
    print("  plt.show()")
    print("\n" + "="*70)
    print("\nRecommended filenames:")
    
    recommended_plots = [
        ("class_distribution.png", "Bar and pie charts of class distribution"),
        ("sample_images.png", "Grid of sample histopathology images"),
        ("training_loss.png", "Training and validation loss curves"),
        ("training_accuracy.png", "Training and validation accuracy curves"),
        ("training_auc.png", "Training and validation AUC curves"),
        ("confusion_matrices.png", "Confusion matrices for both models"),
        ("roc_curves.png", "ROC curves comparison for both models"),
        ("image_properties.png", "Pixel value distribution histograms")
    ]
    
    for filename, description in recommended_plots:
        print(f"  • {filename:<30} - {description}")
    
    print("\n" + "="*70)
    print("After saving plots, commit to Git:")
    print("  git add results/plots/")
    print("  git commit -m 'Add visualization plots from notebook'")
    print("  git push origin main")
    print("="*70)

if __name__ == "__main__":
    main()
