# 🔐 Secure API Key Setup for UFO

This guide explains how to securely configure your API keys for the UFO project without exposing them in version control.

## 🎯 Quick Setup

### 1. Copy Environment Template
```bash
# For main UFO configuration
cp UFO/.env.template UFO/.env

# For dataflow configuration  
cp UFO/dataflow/.env.template UFO/dataflow/.env
```

### 2. Configure Your API Keys

Edit the `.env` files with your actual API keys:

**UFO/.env** (for main UFO functionality):
```bash
# OpenAI Configuration
OPENAI_API_KEY=sk-your-actual-openai-key-here
OPENAI_API_BASE=https://api.openai.com/v1/chat/completions
OPENAI_MODEL=gpt-4-vision-preview

# Or for Azure OpenAI:
# AZURE_OPENAI_API_KEY=your-azure-key
# AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
# AZURE_OPENAI_DEPLOYMENT_ID=gpt-4-visual-preview
```

**UFO/dataflow/.env** (for dataflow agents):
```bash
# Both agents use the same key by default
PREFILL_AGENT_API_KEY=sk-your-actual-openai-key-here
FILTER_AGENT_API_KEY=sk-your-actual-openai-key-here

# Or configure differently for each agent
PREFILL_AGENT_API_TYPE=openai
FILTER_AGENT_API_TYPE=openai
```

## 🔒 Security Features

### ✅ What's Protected
- ✅ `.env` files are automatically ignored by git
- ✅ `config.yaml` files with secrets are gitignored  
- ✅ Only template files are tracked in version control
- ✅ Environment variables take highest priority

### ⚠️ What to Never Commit
- ❌ `.env` files
- ❌ `config.yaml` files with real API keys
- ❌ Any file containing `sk-` keys or similar secrets

## 🔄 Configuration Priority

The system loads configuration in this order (highest to lowest priority):

1. **Environment Variables** - Set directly in your shell
2. **`.env` files** - Local environment files  
3. **YAML config files** - Traditional config files

## 🛠️ Advanced Configuration

### Environment Variables
You can also set configuration directly as environment variables:

```bash
# Windows PowerShell
$env:OPENAI_API_KEY="sk-your-key-here"
$env:PREFILL_AGENT_API_KEY="sk-your-key-here"

# Windows Command Prompt  
set OPENAI_API_KEY=sk-your-key-here
set PREFILL_AGENT_API_KEY=sk-your-key-here

# Linux/Mac
export OPENAI_API_KEY="sk-your-key-here"
export PREFILL_AGENT_API_KEY="sk-your-key-here"
```

### Agent-Specific Configuration
Configure different settings for each agent:

```bash
# Different models for different agents
PREFILL_AGENT_API_MODEL=gpt-4-vision-preview
FILTER_AGENT_API_MODEL=gpt-4-turbo-preview

# Different API endpoints
PREFILL_AGENT_API_TYPE=openai
FILTER_AGENT_API_TYPE=aoai
FILTER_AGENT_API_BASE=https://your-azure-resource.openai.azure.com
```

### Global Parameters
Override default model parameters:

```bash
MAX_TOKENS=4000
TEMPERATURE=0.1  
TOP_P=0.9
TIMEOUT=120
```

## 🐛 Troubleshooting

### "API Key not found" Error
1. Check that your `.env` file exists and has the correct variable names
2. Verify the `.env` file is in the right directory (`UFO/.env` or `UFO/dataflow/.env`)
3. Ensure there are no spaces around the `=` in your `.env` file
4. Restart your application after changing `.env` files

### Variable Names
Make sure you're using the correct environment variable names:

**Main UFO agents:**
- `OPENAI_API_KEY` or `HOST_AGENT_API_KEY`
- `APP_AGENT_API_KEY` 
- `BACKUP_AGENT_API_KEY`

**Dataflow agents:**
- `PREFILL_AGENT_API_KEY`
- `FILTER_AGENT_API_KEY`

### Checking Configuration
The system will warn you if configuration files are missing, but will continue using environment variables.

## 📚 Additional Resources

- [OpenAI API Keys](https://platform.openai.com/api-keys)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service)
- [UFO Documentation](./README.md)

---

**🔒 Remember:** Never commit real API keys to version control. When in doubt, check `git status` before committing!
