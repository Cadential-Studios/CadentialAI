"""
CadentialAI Main Launcher
Entry point for the personal AI assistant
"""

import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "UFO"))

def main():
    """Main entry point for CadentialAI."""
    try:
        # Import configuration manager
        from config_manager import config_manager
        
        print("🤖 CadentialAI - Personal Windows AI Assistant")
        print("=" * 50)
        
        # Load configuration
        try:
            config = config_manager.load_config()
            user_settings = config_manager.get_user_settings()
            print(f"👋 Hello, {user_settings.get('USER_NAME', 'User')}!")
        except Exception as e:
            print(f"⚠️  Configuration error: {e}")
            print("Please run: .\\setup.ps1 -SetupConfig")
            return 1
        
        # Check if UFO is available
        ufo_path = project_root / "UFO"
        if not ufo_path.exists():
            print("❌ UFO framework not found!")
            print("Please ensure the UFO folder is present in your project directory.")
            return 1
        
        # Import and start UFO
        print("🚀 Starting UFO framework...")
        try:
            # Change to UFO directory and run
            os.chdir(str(ufo_path))
            
            # Import UFO main module
            from ufo import main as ufo_main
            
            # Start UFO with CadentialAI configuration
            print("✅ UFO framework loaded successfully!")
            print("🎯 CadentialAI is ready to assist you!")
            print("💡 Type your commands or say 'help' for available actions.")
            
            # Run UFO
            ufo_main()
            
        except ImportError as e:
            print(f"❌ Failed to import UFO: {e}")
            print("Please ensure UFO dependencies are installed:")
            print("  pip install -r UFO/requirements.txt")
            return 1
        except Exception as e:
            print(f"❌ Error starting UFO: {e}")
            return 1
            
    except KeyboardInterrupt:
        print("\n👋 CadentialAI shutting down. Goodbye!")
        return 0
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
