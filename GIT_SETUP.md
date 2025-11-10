# Git & GitHub Setup Instructions

## Initial Setup (First Time Only)

### 1. Install Git

**Windows:**
Download from [git-scm.com](https://git-scm.com/download/win)

**Mac:**
```bash
brew install git
```

**Linux:**
```bash
sudo apt-get install git  # Ubuntu/Debian
sudo yum install git      # CentOS/RHEL
```

### 2. Configure Git

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3. Create GitHub Account

1. Go to [github.com](https://github.com)
2. Sign up for free account
3. Verify your email

## Push Project to GitHub

### Option A: Create New Repository on GitHub First (Recommended)

#### Step 1: Create Repository on GitHub
1. Go to [github.com/new](https://github.com/new)
2. Repository name: `WK_3_CNN_Cancer_Detection`
3. Description: "CNN-based cancer detection from histopathologic images"
4. **Keep it PUBLIC** (or private if preferred)
5. **DO NOT** initialize with README (we already have one)
6. Click "Create repository"

#### Step 2: Link Local Project to GitHub

```bash
# Navigate to your project directory
cd D:\MS_in_AI\WK3_CNN_Detection\WK_3_CNN_Cancer_Detection

# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Commit files
git commit -m "Initial commit: CNN Cancer Detection project"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/WK_3_CNN_Cancer_Detection.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Option B: Use GitHub Desktop (Easier for Beginners)

#### Step 1: Install GitHub Desktop
Download from [desktop.github.com](https://desktop.github.com/)

#### Step 2: Publish Repository
1. Open GitHub Desktop
2. File → Add Local Repository
3. Choose your project folder
4. Click "Publish repository"
5. Name: `WK_3_CNN_Cancer_Detection`
6. Click "Publish repository"

## Update Repository (After Changes)

### Using Command Line

```bash
# Check status
git status

# Add changed files
git add .

# Commit changes
git commit -m "Description of your changes"

# Push to GitHub
git push
```

### Using GitHub Desktop

1. Review changes in left panel
2. Write commit message
3. Click "Commit to main"
4. Click "Push origin"

## Common Git Commands

```bash
# Check status of files
git status

# Add specific file
git add filename.py

# Add all files
git add .

# Commit with message
git commit -m "Your message here"

# Push to remote
git push

# Pull latest changes
git pull

# View commit history
git log

# Create new branch
git checkout -b feature-name

# Switch branches
git checkout main

# View remote URL
git remote -v
```

## Updating README with Your GitHub URL

After creating your repository, update the README:

1. Replace `YOUR_USERNAME` with your actual GitHub username
2. Replace `YOUR_SCORE` with your actual Kaggle scores
3. Add your leaderboard screenshot to `results/`

```bash
# Update README
git add README.md
git commit -m "Update README with GitHub link and scores"
git push
```

## .gitignore Best Practices

The `.gitignore` file already excludes:
- ✅ Large data files (`*.tif`, `data/train/`, `data/test/`)
- ✅ Model files (`*.h5`, `*.keras`)
- ✅ Python cache (`__pycache__/`, `*.pyc`)
- ✅ Jupyter checkpoints (`.ipynb_checkpoints/`)
- ✅ Virtual environments (`venv/`, `env/`)

**Only commit to GitHub:**
- ✅ Code files (`.py`, `.ipynb`)
- ✅ Documentation (`.md`)
- ✅ Configuration (`requirements.txt`)
- ✅ Small sample files
- ✅ Results visualizations (`.png` < 1MB)

## Troubleshooting

### Issue: "fatal: remote origin already exists"

```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/WK_3_CNN_Cancer_Detection.git
```

### Issue: "Updates were rejected"

```bash
# Pull latest changes first
git pull origin main --rebase

# Then push
git push origin main
```

### Issue: Large Files Warning

If you accidentally committed large files:

```bash
# Remove from git but keep locally
git rm --cached data/train/*.tif
git rm --cached models/*.h5

# Commit the removal
git commit -m "Remove large files from git"

# Push
git push
```

### Issue: Authentication Required

**Using HTTPS:**
GitHub no longer accepts password authentication. Use Personal Access Token:

1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select scopes: `repo`
4. Use token as password when prompted

**Using SSH (Recommended):**

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Copy public key
cat ~/.ssh/id_ed25519.pub  # Linux/Mac
type %USERPROFILE%\.ssh\id_ed25519.pub  # Windows

# Add to GitHub:
# Settings → SSH and GPG keys → New SSH key

# Update remote URL
git remote set-url origin git@github.com:YOUR_USERNAME/WK_3_CNN_Cancer_Detection.git
```

## GitHub Repository Checklist

After pushing to GitHub, verify:

- ✅ README.md displays properly
- ✅ All notebook files are visible
- ✅ requirements.txt is present
- ✅ .gitignore is working (no large files)
- ✅ License file is present
- ✅ Repository description is set
- ✅ Topics/tags are added (machine-learning, deep-learning, cnn, kaggle)

## Making Repository Professional

### Add Topics/Tags
1. Go to your repository page
2. Click "⚙️ Settings" (or "About" → Edit)
3. Add topics: `machine-learning`, `deep-learning`, `cnn`, `kaggle`, `tensorflow`, `computer-vision`, `medical-imaging`

### Add Description
Repository description: "CNN-based cancer detection from histopathologic images - Kaggle competition project"

### Create GitHub Pages (Optional)
1. Settings → Pages
2. Source: Deploy from branch → main → /docs or /root
3. Your documentation will be at: `https://YOUR_USERNAME.github.io/WK_3_CNN_Cancer_Detection/`

### Pin Repository
1. Go to your GitHub profile
2. Click "Customize your pins"
3. Select this repository
4. It will appear prominently on your profile

## Sharing Your Project

### README Badges
Already included in README:
- Python version
- TensorFlow version  
- License
- Kaggle link

### Social Sharing
- LinkedIn: Share repository link with project description
- Twitter: Tweet your Kaggle score with repo link
- Kaggle: Add GitHub link to your Kaggle profile

### For Coursera Submission
When submitting for Coursera:
1. Submit GitHub repository URL
2. Ensure all requirements are met
3. Add Kaggle leaderboard screenshot
4. Verify repository is public

## Best Practices

### Commit Messages
- ✅ Use present tense: "Add feature" not "Added feature"
- ✅ Be descriptive: "Add data augmentation" not "Update code"
- ✅ Keep it short but meaningful

### Regular Updates
```bash
# After each working session
git add .
git commit -m "Descriptive message of what changed"
git push
```

### Branch Strategy
For larger features:
```bash
git checkout -b feature/new-model
# Make changes
git commit -m "Add new CNN architecture"
git checkout main
git merge feature/new-model
git push
```

## Need Help?

- Git Documentation: [git-scm.com/doc](https://git-scm.com/doc)
- GitHub Guides: [guides.github.com](https://guides.github.com/)
- GitHub CLI: [cli.github.com](https://cli.github.com/)

---

## Quick Reference Card

```bash
# Setup (once)
git init
git remote add origin <url>

# Daily workflow
git status                      # Check what changed
git add .                       # Stage all changes
git commit -m "message"         # Commit changes
git push                        # Upload to GitHub

# Get updates
git pull                        # Download from GitHub

# Undo changes (careful!)
git checkout -- filename        # Discard local changes
git reset HEAD~1                # Undo last commit (keep changes)
git reset --hard HEAD~1         # Undo last commit (lose changes)
```

---

**Ready to push?** Follow the steps in "Option A" or "Option B" above! 🚀
