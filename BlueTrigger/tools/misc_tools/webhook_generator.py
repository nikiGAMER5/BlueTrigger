import time
import requests
import random
import string
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from data.config import load_tokens

def run_webhook_generator():
    """Create a webhook in a server"""
    print()
    print_info_box(
        "Webhook Generator Tool",
        [
            "Creates a webhook in a Discord server",
            "Requires: Token with manage webhook permission",
            "Status: Working"
        ]
    )
    print()
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    channel_id = prompt_input("Enter channel ID:")
    webhook_name = prompt_input("Enter webhook name:", "Blue Trigger Webhook")
    
    if not channel_id:
        warn("No channel ID provided")
        return False
    
    token = tokens[0]
    loading_spinner("Creating webhook", 1.5)
    
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/json"
    }
    
    data = {
        "name": webhook_name
    }
    
    try:
        response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/webhooks", headers=headers, json=data, timeout=5)
        
        if response.status_code == 200:
            webhook_data = response.json()
            success("Webhook created successfully!")
            print(f"  {Colors.BRIGHT_BLUE}Webhook URL:{Colors.RESET} https://discord.com/api/webhooks/{webhook_data['id']}/{webhook_data['token']}")
            print(f"  {Colors.BRIGHT_BLUE}Webhook ID:{Colors.RESET} {webhook_data['id']}")
        elif response.status_code == 403:
            error("Missing permission: manage webhooks")
        elif response.status_code == 401:
            error("Invalid token")
        else:
            error(f"Failed to create webhook. Status: {response.status_code}")
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True