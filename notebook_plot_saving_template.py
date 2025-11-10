# Notebook Cell Template for Saving Plots
# Copy and paste this cell at the TOP of your notebook (after imports)

"""
PLOT SAVING SETUP
Run this cell once at the beginning of your notebook to enable easy plot saving.
"""

from pathlib import Path
import matplotlib.pyplot as plt

# Create plots directory
PLOTS_DIR = Path('../results/plots')
PLOTS_DIR.mkdir(parents=True, exist_ok=True)

print("✅ Plots directory ready!")
print(f"📁 Location: {PLOTS_DIR.resolve()}")

# Helper function to save plots
def save_plot(filename, dpi=300):
    """
    Save the current matplotlib figure to results/plots/
    
    Usage:
        plt.figure()
        # ... your plotting code ...
        save_plot('my_plot.png')
        plt.show()
    
    Parameters:
    - filename: Name of the file (e.g., 'class_distribution.png')
    - dpi: Resolution (default 300 for high quality)
    """
    filepath = PLOTS_DIR / filename
    plt.savefig(filepath, dpi=dpi, bbox_inches='tight', facecolor='white')
    print(f"💾 Saved: {filename}")

print("\n📝 Usage:")
print("   After any plot, call: save_plot('filename.png')")
print("\n📋 Recommended filenames:")
print("   • class_distribution.png")
print("   • sample_images.png")
print("   • training_loss.png")
print("   • training_accuracy.png")
print("   • training_auc.png")
print("   • confusion_matrices.png")
print("   • roc_curves.png")

# =============================================================================
# EXAMPLE USAGE IN OTHER CELLS:
# =============================================================================

# After Class Distribution plot:
#   save_plot('class_distribution.png')
#   plt.show()

# After Sample Images plot:
#   save_plot('sample_images.png')
#   plt.show()

# After Training History plots:
#   save_plot('training_loss.png')
#   plt.show()

# After Confusion Matrix plot:
#   save_plot('confusion_matrices.png')
#   plt.show()

# After ROC Curves plot:
#   save_plot('roc_curves.png')
#   plt.show()

# =============================================================================
# ALTERNATIVE: Modify existing plot cells
# =============================================================================

# Find cells with plt.show() and replace with:
#   save_plot('appropriate_name.png')
#   plt.show()

# Example for Class Distribution cell:
"""
# Original code:
    plt.tight_layout()
    plt.show()

# Modified to save:
    plt.tight_layout()
    save_plot('class_distribution.png')
    plt.show()
"""

# =============================================================================
# AFTER SAVING ALL PLOTS
# =============================================================================

# Run this in a terminal or command prompt:
"""
cd D:\MS_in_AI\WK3_CNN_Detection\WK_3_CNN_Cancer_Detection
git add results/plots/
git commit -m "Add notebook visualization plots"
git push origin main
"""

# Then check your GitHub repository README - images should now display!
