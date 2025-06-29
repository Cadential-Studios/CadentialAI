# Environment Variable Setup Script for CadentialAI
# This script helps you set up environment variables for the project

param(
    [switch]$Setup,
    [switch]$List,
    [switch]$Test,
    [string]$SetVar,
    [string]$Value
)

Write-Host "Environment Variable Manager for CadentialAI" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan

function Setup-EnvironmentFiles {
    Write-Host "Setting up environment files..." -ForegroundColor Yellow
    
    # Copy .env template
    if (-not (Test-Path "UFO\.env")) {
        if (Test-Path "UFO\.env.template") {
            Copy-Item "UFO\.env.template" "UFO\.env"
            Write-Host "Created UFO\.env from template" -ForegroundColor Green
        }
    } else {
        Write-Host "UFO\.env already exists" -ForegroundColor Green
    }
    
    # Copy dataflow .env template if it exists
    if (Test-Path "UFO\dataflow\.env.template") {
        if (-not (Test-Path "UFO\dataflow\.env")) {
            Copy-Item "UFO\dataflow\.env.template" "UFO\dataflow\.env"
            Write-Host "Created UFO\dataflow\.env from template" -ForegroundColor Green
        }
    }
    
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Cyan
    Write-Host "1. Edit UFO\.env and add your API keys" -ForegroundColor White
    Write-Host "2. Run: .\env-setup-new.ps1 -Test to verify your setup" -ForegroundColor White
    Write-Host ""
    Write-Host "Required API Keys:" -ForegroundColor Yellow
    Write-Host "- OPENAI_API_KEY (from https://platform.openai.com/api-keys)" -ForegroundColor Gray
    Write-Host "- AZURE_OPENAI_API_KEY (if using Azure OpenAI)" -ForegroundColor Gray
}

function List-EnvironmentVariables {
    Write-Host "Current Environment Variables:" -ForegroundColor Yellow
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
                Write-Host "$var = $masked" -ForegroundColor Green
            } else {
                Write-Host "$var = $value" -ForegroundColor Green
            }
        } else {
            Write-Host "$var = (not set)" -ForegroundColor Red
        }
    }
}

function Test-Configuration {
    Write-Host "Testing Configuration..." -ForegroundColor Yellow
    Write-Host ""
    
    # Test .env file content
    if (Test-Path "UFO\.env") {
        Write-Host "UFO\.env file exists" -ForegroundColor Green
        
        # Check if API key is set in .env file
        $envContent = Get-Content "UFO\.env" -Raw
        if ($envContent -match "OPENAI_API_KEY=sk-[A-Za-z0-9\-_]+") {
            Write-Host "✅ OPENAI_API_KEY is properly configured in .env file" -ForegroundColor Green
        } elseif ($envContent -match "OPENAI_API_KEY=your_openai_api_key_here") {
            Write-Host "⚠️ OPENAI_API_KEY needs to be updated in .env file" -ForegroundColor Yellow
        } else {
            Write-Host "❌ OPENAI_API_KEY not found in .env file" -ForegroundColor Red
        }
    } else {
        Write-Host "UFO\.env file missing - run .\env-setup-new.ps1 -Setup" -ForegroundColor Red
    }
    
    # Test system environment variables
    $apiKey = [Environment]::GetEnvironmentVariable('OPENAI_API_KEY')
    if ($apiKey -and $apiKey -ne "your_openai_api_key_here") {
        Write-Host "OPENAI_API_KEY is also set as system environment variable" -ForegroundColor Green
    } else {
        Write-Host "OPENAI_API_KEY not set as system environment variable (this is OK if using .env)" -ForegroundColor Gray
    }
    
    # Test config.yaml
    if (Test-Path "config.yaml") {
        Write-Host "config.yaml file exists" -ForegroundColor Green
    } else {
        Write-Host "config.yaml file missing" -ForegroundColor Yellow
    }
    
    Write-Host ""
    Write-Host "Summary:" -ForegroundColor Cyan
    Write-Host "- Use .env files for project-specific settings (recommended)" -ForegroundColor White
    Write-Host "- System environment variables work across all projects" -ForegroundColor White
    Write-Host "- The application will load from .env files automatically" -ForegroundColor White
}

function Set-EnvironmentVariable {
    param($VarName, $VarValue)
    
    Write-Host "Setting $VarName..." -ForegroundColor Yellow
    
    # Set for current session
    [Environment]::SetEnvironmentVariable($VarName, $VarValue, "Process")
    
    # Set for user (persistent)
    [Environment]::SetEnvironmentVariable($VarName, $VarValue, "User")
    
    Write-Host "$VarName has been set" -ForegroundColor Green
    Write-Host "Restart your terminal to use the new variable in other sessions" -ForegroundColor Yellow
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
    Write-Host "  .\env-setup-new.ps1 -Setup          # Set up .env files from templates"
    Write-Host "  .\env-setup-new.ps1 -List           # List current environment variables"
    Write-Host "  .\env-setup-new.ps1 -Test           # Test configuration"
    Write-Host "  .\env-setup-new.ps1 -SetVar NAME -Value VALUE  # Set a specific variable"
    Write-Host ""
    Write-Host "Examples:" -ForegroundColor Yellow
    Write-Host '  .\env-setup-new.ps1 -SetVar "OPENAI_API_KEY" -Value "sk-your-key-here"'
    Write-Host '  .\env-setup-new.ps1 -SetVar "USER_NAME" -Value "Scott"'
}
