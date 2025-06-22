# CadentialAI Setup Script
# Quick setup for development environment

param(
    [switch]$InstallDeps,
    [switch]$SetupDev,
    [switch]$RunTests
)

Write-Host "🤖 CadentialAI Setup Script" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan

# Check Python version
$pythonVersion = python --version 2>&1
if ($pythonVersion -match "Python (\d+\.\d+)") {
    $version = [version]$matches[1]
    if ($version -ge [version]"3.10") {
        Write-Host "✅ Python $($matches[1]) found" -ForegroundColor Green
    } else {
        Write-Host "❌ Python 3.10+ required. Found: $($matches[1])" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "❌ Python not found. Please install Python 3.10+" -ForegroundColor Red
    exit 1
}

if ($InstallDeps) {
    Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    Write-Host "✅ Dependencies installed" -ForegroundColor Green
}

if ($SetupDev) {
    Write-Host "🔧 Setting up development environment..." -ForegroundColor Yellow
    
    # Install development dependencies
    pip install pytest pytest-cov black flake8
    
    # Create virtual environment if it doesn't exist
    if (-not (Test-Path "venv")) {
        Write-Host "🌐 Creating virtual environment..." -ForegroundColor Yellow
        python -m venv venv
    }
    
    # Copy config templates
    if (Test-Path "UFO\config\config.yaml.template") {
        if (-not (Test-Path "UFO\config\config.yaml")) {
            Copy-Item "UFO\config\config.yaml.template" "UFO\config\config.yaml"
            Write-Host "📋 Config template copied. Please edit UFO\config\config.yaml with your settings." -ForegroundColor Yellow
        }
    }
    
    Write-Host "✅ Development environment setup complete" -ForegroundColor Green
}

if ($RunTests) {
    Write-Host "🧪 Running tests..." -ForegroundColor Yellow
    python -m pytest tests/ -v
    Write-Host "✅ Tests completed" -ForegroundColor Green
}

Write-Host ""
Write-Host "🚀 Setup completed! Next steps:" -ForegroundColor Cyan
Write-Host "1. Edit UFO\config\config.yaml with your API keys" -ForegroundColor White
Write-Host "2. Run: python -m ufo to start the assistant" -ForegroundColor White
Write-Host "3. Check the documentation in the docs/ folder" -ForegroundColor White
Write-Host ""
Write-Host "For help, run:" -ForegroundColor Gray
Write-Host "  .\setup.ps1 -InstallDeps  # Install dependencies" -ForegroundColor Gray
Write-Host "  .\setup.ps1 -SetupDev     # Setup dev environment" -ForegroundColor Gray
Write-Host "  .\setup.ps1 -RunTests     # Run tests" -ForegroundColor Gray
