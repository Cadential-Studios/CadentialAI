# CadentialAI Setup Script
# Quick setup for development environment

param(
    [switch]$InstallDeps,
    [switch]$SetupDev,
    [switch]$SetupConfig,
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
    
    # Install UFO dependencies if UFO folder exists
    if (Test-Path "UFO\requirements.txt") {
        Write-Host "📦 Installing UFO dependencies..." -ForegroundColor Yellow
        pip install -r UFO\requirements.txt
    }
    Write-Host "✅ Dependencies installed" -ForegroundColor Green
}

if ($SetupConfig) {
    Write-Host "🔧 Setting up configuration..." -ForegroundColor Yellow
    
    # Create main config.yaml from template
    if (-not (Test-Path "config.yaml")) {
        if (Test-Path "config.template.yaml") {
            Copy-Item "config.template.yaml" "config.yaml"
            Write-Host "📋 Created config.yaml from template" -ForegroundColor Green
        } else {
            Write-Host "❌ config.template.yaml not found" -ForegroundColor Red
        }
    } else {
        Write-Host "📋 config.yaml already exists" -ForegroundColor Yellow
    }
    
    # Setup UFO config
    if (Test-Path "UFO\config\config.yaml.template") {
        if (-not (Test-Path "UFO\config\config.yaml")) {
            Copy-Item "UFO\config\config.yaml.template" "UFO\config\config.yaml"
            Write-Host "📋 Created UFO config.yaml from template" -ForegroundColor Green
        } else {
            Write-Host "📋 UFO config.yaml already exists" -ForegroundColor Yellow
        }
    }
    
    Write-Host ""
    Write-Host "⚠️  IMPORTANT: Please edit the following files with your API keys:" -ForegroundColor Yellow
    Write-Host "   - config.yaml (main CadentialAI config)" -ForegroundColor White
    Write-Host "   - UFO\config\config.yaml (UFO framework config)" -ForegroundColor White
    Write-Host ""
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
    
    Write-Host "✅ Development environment setup complete" -ForegroundColor Green
}

if ($RunTests) {
    Write-Host "🧪 Running tests..." -ForegroundColor Yellow
    python -m pytest tests/ -v
    Write-Host "✅ Tests completed" -ForegroundColor Green
}

Write-Host ""
Write-Host "🚀 Setup completed! Next steps:" -ForegroundColor Cyan
Write-Host "1. Run: .\setup.ps1 -SetupConfig  # Create config files" -ForegroundColor White
Write-Host "2. Edit config.yaml with your API keys" -ForegroundColor White
Write-Host "3. Edit UFO\config\config.yaml with your UFO settings" -ForegroundColor White
Write-Host "4. Run: python -m cadential_ai  # Start the assistant" -ForegroundColor White
Write-Host ""
Write-Host "For help, run:" -ForegroundColor Gray
Write-Host "  .\setup.ps1 -InstallDeps   # Install dependencies" -ForegroundColor Gray
Write-Host "  .\setup.ps1 -SetupConfig   # Setup config files" -ForegroundColor Gray
Write-Host "  .\setup.ps1 -SetupDev      # Setup dev environment" -ForegroundColor Gray
Write-Host "  .\setup.ps1 -RunTests      # Run tests" -ForegroundColor Gray
