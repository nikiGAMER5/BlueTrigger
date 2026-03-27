import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from data.config import load_tokens

def run_token_cstatus_changer():
    """Change custom status"""
    print()
    print_info_box(
        "Token Custom Status Changer",
        [
            "Changes the user's custom status",
            "Status: Working"
        ]
    )
    print()
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    status_text = prompt_input("Enter custom status text:")
    emoji_name = prompt_input("Enter emoji name (optional, press Enter to skip):", "")
    expiry = prompt_input("Expiry in seconds (0 = never, default: 0)", "0")
    
    try:
        expiry = int(expiry)
    except:
        expiry = 0
    
    token = tokens[0]
    loading_spinner("Updating custom status", 1.2)
    
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/json"
    }
    
    status_data = {
        "custom_status": {
            "text": status_text
        }
    }
    
    if emoji_name:
        status_data["custom_status"]["emoji_name"] = emoji_name
    
    if expiry > 0:
        status_data["custom_status"]["expires_at"] = time.time() + expiry
    
    try:
        response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=status_data, timeout=5)
        
        if response.status_code in [200, 204]:
            success("Custom status updated successfully!")
            if status_text:
                info(f"Status: {status_text}")
            if emoji_name:
                info(f"Emoji: {emoji_name}")
        elif response.status_code == 401:
            error("Invalid token")
        else:
            error(f"Failed to update status. Status: {response.status_code}")
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True