# Git Initialization Script for CadentialAI
# Run this script to initialize your GitHub repository

Write-Host "🚀 Initializing CadentialAI GitHub Repository..." -ForegroundColor Green

# Check if git is installed
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Git is not installed. Please install Git first." -ForegroundColor Red
    exit 1
}

# Initialize git repository if not already initialized
if (-not (Test-Path ".git")) {
    Write-Host "📦 Initializing Git repository..." -ForegroundColor Yellow
    git init
} else {
    Write-Host "✅ Git repository already exists." -ForegroundColor Green
}

# Add all files to git
Write-Host "📁 Adding files to Git..." -ForegroundColor Yellow
git add .

# Create initial commit
Write-Host "💾 Creating initial commit..." -ForegroundColor Yellow
git commit -m "feat: initial commit - CadentialAI Personal Windows AI Assistant

- Add project structure and documentation
- Integrate Microsoft UFO² framework
- Set up CI/CD pipeline and GitHub workflows
- Add comprehensive README and contributing guidelines
- Implement security policy and issue templates
- Create testing framework and basic tests"

# Set up main branch
Write-Host "🌟 Setting up main branch..." -ForegroundColor Yellow
git branch -M main

# Instructions for adding remote origin
Write-Host ""
Write-Host "🔗 Next Steps:" -ForegroundColor Cyan
Write-Host "1. Create a new repository on GitHub named 'CadentialAI'"
Write-Host "2. Copy the repository URL (e.g., https://github.com/yourusername/CadentialAI.git)"
Write-Host "3. Run the following commands:"
Write-Host ""
Write-Host "   git remote add origin https://github.com/yourusername/CadentialAI.git" -ForegroundColor Yellow
Write-Host "   git push -u origin main" -ForegroundColor Yellow
Write-Host ""
Write-Host "📝 Don't forget to:"
Write-Host "- Update the repository URL in setup.py and README.md"
Write-Host "- Add your email address in setup.py"
Write-Host "- Replace placeholder email in SECURITY.md"
Write-Host "- Configure your API keys in the UFO config files"
Write-Host ""
Write-Host "✨ Repository initialized successfully!" -ForegroundColor Green
