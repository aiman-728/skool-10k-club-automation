import os

# Get credentials stored securely in GitHub Secrets
SKOOL_EMAIL = os.getenv("SKOOL_EMAIL")
SKOOL_PASSWORD = os.getenv("SKOOL_PASSWORD")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

def run_automation():
    print("Starting 10K Club Skool Automation...")
    # Your automation code goes here

if __name__ == "__main__":
    run_automation()
