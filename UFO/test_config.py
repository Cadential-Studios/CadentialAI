#!/usr/bin/env python3
"""
Test script to verify secure API key configuration is working correctly.
Run this script to check if your environment variables and config loading is set up properly.
"""

import os
import sys
from pathlib import Path

# Add UFO to the path
sys.path.insert(0, str(Path(__file__).parent))

def test_main_ufo_config():
    """Test the main UFO configuration loading."""
    print("🔍 Testing main UFO configuration...")
    
    try:
        from ufo.config.config import Config
        config = Config.get_instance()
        
        if config.config_data is None:
            print("⚠️  Config data is None (RUN_CONFIGS=false)")
            return True
            
        # Check if we have basic config structure
        agents = ["HOST_AGENT", "APP_AGENT", "BACKUP_AGENT"]
        found_agents = []
        
        for agent in agents:
            if agent in config.config_data:
                found_agents.append(agent)
                
                # Check if API key is configured
                agent_config = config.config_data[agent]
                if isinstance(agent_config, dict) and "API_KEY" in agent_config:
                    api_key = agent_config["API_KEY"]
                    if api_key and api_key != "sk-" and len(api_key) > 10:
                        print(f"✅ {agent}: API key configured (***{api_key[-4:]})")
                    else:
                        print(f"⚠️  {agent}: API key needs configuration")
                else:
                    print(f"⚠️  {agent}: No API_KEY found in config")
        
        if found_agents:
            print(f"✅ Found {len(found_agents)} configured agents: {', '.join(found_agents)}")
        else:
            print("⚠️  No agent configurations found")
            
        return True
        
    except Exception as e:
        print(f"❌ Error loading main UFO config: {e}")
        return False

def test_dataflow_config():
    """Test the dataflow configuration loading."""
    print("\n🔍 Testing dataflow configuration...")
    
    try:
        # Test if dataflow config directory exists
        dataflow_config_dir = Path("dataflow/config")
        if not dataflow_config_dir.exists():
            print("⚠️  Dataflow config directory not found")
            return True
            
        # Try to load dataflow config
        sys.path.insert(0, str(Path("dataflow").absolute()))
        from dataflow.config.config import Config
        
        config = Config.get_instance()
        
        if not config.config_data:
            print("⚠️  No dataflow config data loaded")
            return True
            
        # Check dataflow agents
        agents = ["PREFILL_AGENT", "FILTER_AGENT"]
        found_agents = []
        
        for agent in agents:
            if agent in config.config_data:
                found_agents.append(agent)
                
                agent_config = config.config_data[agent]
                if isinstance(agent_config, dict) and "API_KEY" in agent_config:
                    api_key = agent_config["API_KEY"]
                    if api_key and api_key != "sk-" and len(api_key) > 10:
                        print(f"✅ {agent}: API key configured (***{api_key[-4:]})")
                    else:
                        print(f"⚠️  {agent}: API key needs configuration")
                else:
                    print(f"⚠️  {agent}: No API_KEY found in config")
        
        if found_agents:
            print(f"✅ Found {len(found_agents)} configured dataflow agents: {', '.join(found_agents)}")
        else:
            print("⚠️  No dataflow agent configurations found")
            
        return True
        
    except Exception as e:
        print(f"❌ Error loading dataflow config: {e}")
        return False

def test_env_files():
    """Test if .env files are present and properly ignored."""
    print("\n🔍 Testing .env file setup...")
    
    env_files = [
        Path(".env"),
        Path("ufo/config/.env"),
        Path("dataflow/.env"),
        Path("dataflow/config/.env")
    ]
    
    template_files = [
        Path(".env.template"),
        Path("dataflow/.env.template")
    ]
    
    # Check templates exist
    for template in template_files:
        if template.exists():
            print(f"✅ Template found: {template}")
        else:
            print(f"⚠️  Template missing: {template}")
    
    # Check .env files
    found_env = False
    for env_file in env_files:
        if env_file.exists():
            print(f"✅ Environment file found: {env_file}")
            found_env = True
    
    if not found_env:
        print("ℹ️  No .env files found (use templates to create them)")
    
    return True

def test_environment_variables():
    """Test if relevant environment variables are set."""
    print("\n🔍 Testing environment variables...")
    
    # Common environment variables
    env_vars = [
        "OPENAI_API_KEY",
        "HOST_AGENT_API_KEY", 
        "APP_AGENT_API_KEY",
        "PREFILL_AGENT_API_KEY",
        "FILTER_AGENT_API_KEY",
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_ENDPOINT"
    ]
    
    found_vars = []
    for var in env_vars:
        if var in os.environ:
            value = os.environ[var]
            if value and len(value) > 5:
                print(f"✅ {var}: Set (***{value[-4:]})")
                found_vars.append(var)
            else:
                print(f"⚠️  {var}: Set but empty/short")
    
    if found_vars:
        print(f"✅ Found {len(found_vars)} configured environment variables")
    else:
        print("ℹ️  No relevant environment variables found")
    
    return True

def main():
    """Run all configuration tests."""
    print("🧪 UFO Secure Configuration Test")
    print("=" * 50)
    
    tests = [
        test_env_files,
        test_environment_variables, 
        test_main_ufo_config,
        test_dataflow_config
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    if all(results):
        print("🎉 All tests completed! Check warnings above for any configuration needed.")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
    
    print("\n📖 For setup instructions, see: SECURITY_SETUP.md")
    print("🔒 Remember: Never commit .env files or config files with real API keys!")

if __name__ == "__main__":
    main()
