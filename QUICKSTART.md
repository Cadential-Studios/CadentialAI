# 🚀 CadentialAI Quick Start Guide

## Step 1: Installation
```powershell
git clone https://github.com/yourusername/CadentialAI.git
cd CadentialAI
pip install -r requirements.txt
pip install -r UFO\requirements.txt
```

## Step 2: Configuration
```powershell
# Create config files from templates
.\setup.ps1 -SetupConfig

# Edit your API keys (file is Git-ignored for security)
notepad config.yaml
```

### Required API Keys
Add these to your `config.yaml`:
- **OpenAI API Key**: Get from https://platform.openai.com/api-keys
- **Azure OpenAI** (alternative): Get from Azure portal

### Sample config.yaml:
```yaml
OPENAI:
  API_KEY: "sk-your-openai-key-here"
  API_MODEL: "gpt-4o"

CADENTIAL_AI:
  USER_NAME: "Your Name"
  VOICE_ENABLED: true
```

## Step 3: Launch
```powershell
# Start CadentialAI
python cadential_ai.py

# Or run UFO directly  
cd UFO
python -m ufo
```

## 🔒 Security Features

✅ **API keys are secure**: `config.yaml` is excluded from Git commits  
✅ **Template provided**: `config.template.yaml` shows the required structure  
✅ **Environment fallback**: Can use environment variables instead  
✅ **No accidental commits**: `.gitignore` protects sensitive files  

## 🆘 Troubleshooting

**Problem**: "Configuration error" when starting
**Solution**: Run `.\setup.ps1 -SetupConfig` and edit `config.yaml`

**Problem**: "UFO framework not found"  
**Solution**: Ensure UFO folder exists in project directory

**Problem**: Import errors
**Solution**: Install dependencies with `pip install -r requirements.txt`

## 📞 Need Help?

- Check the main [README.md](README.md) for detailed information
- Review [CONTRIBUTING.md](CONTRIBUTING.md) for development setup
- Create an issue for bugs or feature requests
