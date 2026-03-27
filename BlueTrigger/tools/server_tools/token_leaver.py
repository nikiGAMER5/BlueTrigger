import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from data.config import load_tokens

def run_token_leaver():
    """Leave Discord servers"""
    print()
    print_info_box(
        "Token Leaver Tool",
        [
            "Leaves specified Discord servers",
            "Status: Working"
        ]
    )
    print()
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    server_id = prompt_input("Enter server ID to leave:")
    
    if not server_id:
        warn("No server ID provided")
        return False
    
    token = tokens[0]
    loading_spinner(f"Leaving server {server_id}", 1.2)
    
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{server_id}", headers=headers, timeout=5)
        
        if response.status_code == 204:
            success("Successfully left the server!")
        elif response.status_code == 401:
            error("Invalid token")
        elif response.status_code == 403:
            error("Cannot leave server (owner or no permission)")
        elif response.status_code == 404:
            error("Server not found or not a member")
        else:
            error(f"Failed to leave server. Status: {response.status_code}")
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True