import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input

def run_webhook_info():
    """Get webhook information"""
    print()
    print_info_box(
        "Webhook Information Tool",
        [
            "Gets information about a Discord webhook",
            "Status: Working"
        ]
    )
    print()
    
    webhook_url = prompt_input("Enter webhook URL:")
    
    if not webhook_url:
        warn("No webhook URL provided")
        return False
    
    loading_spinner("Fetching webhook info", 1.2)
    
    try:
        response = requests.get(webhook_url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            print()
            success("Webhook information retrieved:")
            print(f"  {Colors.BRIGHT_BLUE}Name:{Colors.RESET} {data.get('name', 'Unknown')}")
            print(f"  {Colors.BRIGHT_BLUE}Channel:{Colors.RESET} {data.get('channel_id', 'Unknown')}")
            print(f"  {Colors.BRIGHT_BLUE}Guild:{Colors.RESET} {data.get('guild_id', 'Unknown')}")
            print(f"  {Colors.BRIGHT_BLUE}Avatar:{Colors.RESET} {data.get('avatar', 'None')}")
            print(f"  {Colors.BRIGHT_BLUE}Token:{Colors.RESET} {data.get('token', 'None')[:20]}...")
        elif response.status_code == 404:
            error("Webhook not found")
        else:
            error(f"Failed to get webhook info. Status: {response.status_code}")
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True