import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from data.config import load_tokens

def run_token_alias_changer():
    """Change user's display name (alias)"""
    print()
    print_info_box(
        "Token Alias Changer",
        [
            "Changes the user's display name (nickname)",
            "Status: Working"
        ]
    )
    print()
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    new_alias = prompt_input("Enter new alias/display name:")
    
    if not new_alias:
        warn("No alias provided")
        return False
    
    if len(new_alias) > 32:
        warn("Alias too long! Max 32 characters.")
        return False
    
    token = tokens[0]
    loading_spinner("Changing alias", 1.2)
    
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/json"
    }
    
    data = {"global_name": new_alias}
    
    try:
        response = requests.patch("https://discord.com/api/v9/users/@me", headers=headers, json=data, timeout=5)
        
        if response.status_code == 200:
            success(f"Alias successfully changed to: {new_alias}")
        elif response.status_code == 400:
            error("Invalid alias format")
        elif response.status_code == 401:
            error("Invalid token")
        else:
            error(f"Failed to change alias. Status: {response.status_code}")
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True