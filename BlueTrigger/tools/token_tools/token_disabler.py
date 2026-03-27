import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box
from data.config import load_tokens

def run_token_disabler():
    """Disable/Deauthorize a token"""
    print()
    print_info_box(
        "Token Disabler Tool",
        [
            "Disables a Discord token (logs it out)",
            "Warning: This will invalidate the token!"
        ]
    )
    print()
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    info(f"Found {len(tokens)} tokens")
    confirm = input(f"{Colors.WARNING}Are you sure you want to disable the first token? (y/N): {Colors.RESET}").lower()
    
    if confirm != 'y':
        warn("Operation cancelled")
        return False
    
    token = tokens[0]
    loading_spinner("Disabling token", 1.5)
    
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        # Revoke the token
        response = requests.post("https://discord.com/api/v9/auth/logout", headers=headers, json={"provider": None}, timeout=5)
        
        if response.status_code in [200, 204]:
            success("Token successfully disabled/invalidated")
            info("The token has been logged out from Discord")
        else:
            error(f"Failed to disable token. Status code: {response.status_code}")
            if response.status_code == 401:
                warn("Token might already be invalid")
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True