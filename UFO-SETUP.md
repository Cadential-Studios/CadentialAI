# UFO Framework Setup Instructions

This project depends on Microsoft's UFO² framework. Since UFO is a separate Git repository, it needs to be cloned separately.

## Quick Setup

1. **Clone the UFO repository** into your project directory:
   ```powershell
   git clone https://github.com/microsoft/UFO.git
   ```

2. **Install UFO dependencies**:
   ```powershell
   cd UFO
   pip install -r requirements.txt
   cd ..
   ```

3. **Configure UFO**:
   - Copy `UFO/config/config.yaml.template` to `UFO/config/config.yaml`
   - Add your API keys and configuration settings

## Alternative: Using Git Submodule

If you prefer to manage UFO as a Git submodule:

```powershell
git submodule add https://github.com/microsoft/UFO.git UFO
git submodule update --init --recursive
```

## Configuration

Make sure to configure the following in `UFO/config/config.yaml`:

- **API Keys**: OpenAI or Azure OpenAI credentials
- **Model Settings**: Choose your preferred AI model
- **Windows Settings**: Configure UI automation preferences

## Verification

Test your setup by running:
```powershell
cd UFO
python -m ufo --help
```

For more details, see the [UFO documentation](https://microsoft.github.io/UFO/).
