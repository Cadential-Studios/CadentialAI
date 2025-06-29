# Environment Variable Setup Script for CadentialAI
# This script helps you set up environment variables for the project

param(
    [switch]$Setup,
    [switch]$List,
    [switch]$Test,
    [string]$SetVar,
    [string]$Value
)

Write-Host "🔧 CadentialAI Environment Variable Manager" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

function Setup-EnvironmentFiles {
    Write-Host "📁 Setting up environment files..." -ForegroundColor Yellow
    
    # Copy .env template
    if (-not (Test-Path "UFO\.env")) {
        if (Test-Path "UFO\.env.template") {
            Copy-Item "UFO\.env.template" "UFO\.env"
            Write-Host "✅ Created UFO\.env from template" -ForegroundColor Green
        }
    } else {
        Write-Host "✅ UFO\.env already exists" -ForegroundColor Green
    }
    
    # Copy dataflow .env template if it exists
    if (Test-Path "UFO\dataflow\.env.template") {
        if (-not (Test-Path "UFO\dataflow\.env")) {
            Copy-Item "UFO\dataflow\.env.template" "UFO\dataflow\.env"
            Write-Host "✅ Created UFO\dataflow\.env from template" -ForegroundColor Green
        }
    }
    
    Write-Host ""
    Write-Host "📝 Next steps:" -ForegroundColor Cyan
    Write-Host "1. Edit UFO\.env and add your API keys" -ForegroundColor White
    Write-Host "2. Run: .\env-setup.ps1 -Test to verify your setup" -ForegroundColor White
    Write-Host ""
    Write-Host "🔐 Required API Keys:" -ForegroundColor Yellow
    Write-Host "- OPENAI_API_KEY (from https://platform.openai.com/api-keys)" -ForegroundColor Gray
    Write-Host "- AZURE_OPENAI_API_KEY (if using Azure OpenAI)" -ForegroundColor Gray
}

function List-EnvironmentVariables {
    Write-Host "📋 Current Environment Variables:" -ForegroundColor Yellow
    Write-Host ""
    
    $envVars = @(
        'OPENAI_API_KEY',
        'AZURE_OPENAI_API_KEY', 
        'AZURE_OPENAI_ENDPOINT',
        'USER_NAME',
        'PREFERRED_VOICE',
        'DEBUG_MODE',
        'LOG_LEVEL'
    )
    
    foreach ($var in $envVars) {
        $value = [Environment]::GetEnvironmentVariable($var)
        if ($value) {
            if ($var -like "*API_KEY*") {
                # Mask API keys for security
                $masked = $value.Substring(0, [Math]::Min(10, $value.Length)) + "..." + $value.Substring([Math]::Max(0, $value.Length - 4))
                Write-Host "✅ $var = $masked" -ForegroundColor Green
            } else {
                Write-Host "✅ $var = $value" -ForegroundColor Green
            }
        } else {
            Write-Host "❌ $var = (not set)" -ForegroundColor Red
        }
    }
}

function Test-Configuration {
    Write-Host "🧪 Testing Configuration..." -ForegroundColor Yellow
    Write-Host ""
    
    # Test Python import
    try {
        $pythonTest = 'from config_manager import config_manager; config = config_manager.load_config(); print("Config loaded successfully")'
        $result = python -c $pythonTest 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Config loaded successfully" -ForegroundColor Green
        } else {
            Write-Host "❌ Config loading failed: $result" -ForegroundColor Red
            return
        }
    } catch {
        Write-Host "❌ Python import failed: $($_.Exception.Message)" -ForegroundColor Red
        return
    }
    
    # Test API key presence
    $apiKey = [Environment]::GetEnvironmentVariable('OPENAI_API_KEY')
    if ($apiKey -and $apiKey -ne "your_openai_api_key_here") {
        Write-Host "✅ OPENAI_API_KEY is set" -ForegroundColor Green
    } else {
        Write-Host "❌ OPENAI_API_KEY is not properly configured" -ForegroundColor Red
    }
    
    # Test .env file
    if (Test-Path "UFO\.env") {
        Write-Host "✅ UFO\.env file exists" -ForegroundColor Green
    } else {
        Write-Host "❌ UFO\.env file missing - run .\env-setup.ps1 -Setup" -ForegroundColor Red
    }
}

function Set-EnvironmentVariable {
    param($VarName, $VarValue)
    
    Write-Host "Setting $VarName..." -ForegroundColor Yellow
    
    # Set for current session
    [Environment]::SetEnvironmentVariable($VarName, $VarValue, "Process")
    
    # Set for user (persistent)
    [Environment]::SetEnvironmentVariable($VarName, $VarValue, "User")
    
    Write-Host "✅ $VarName has been set" -ForegroundColor Green
    Write-Host "🔄 Restart your terminal to use the new variable in other sessions" -ForegroundColor Yellow
}

# Main script logic
if ($Setup) {
    Setup-EnvironmentFiles
} elseif ($List) {
    List-EnvironmentVariables
} elseif ($Test) {
    Test-Configuration
} elseif ($SetVar -and $Value) {
    Set-EnvironmentVariable -VarName $SetVar -VarValue $Value
} else {
    Write-Host "Usage:" -ForegroundColor Cyan
    Write-Host "  .\env-setup.ps1 -Setup          # Set up .env files from templates"
    Write-Host "  .\env-setup.ps1 -List           # List current environment variables"
    Write-Host "  .\env-setup.ps1 -Test           # Test configuration"
    Write-Host "  .\env-setup.ps1 -SetVar NAME -Value VALUE  # Set a specific variable"
    Write-Host ""
    Write-Host "Examples:" -ForegroundColor Yellow
    Write-Host '  .\env-setup.ps1 -SetVar "OPENAI_API_KEY" -Value "sk-your-key-here"'
    Write-Host '  .\env-setup.ps1 -SetVar "USER_NAME" -Value "Scott"'
}
