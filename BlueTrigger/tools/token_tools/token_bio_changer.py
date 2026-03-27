import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from data.config import load_tokens

def run_token_bio_changer():
    """Change user bio/about me"""
    print()
    print_info_box(
        "Token Bio Changer",
        [
            "Changes the 'About Me' section of the user",
            "Status: Working"
        ]
    )
    print()
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    new_bio = prompt_input("Enter new bio text (max 190 chars):")
    
    if not new_bio:
        warn("No bio text provided")
        return False
    
    if len(new_bio) > 190:
        warn("Bio too long! Max 190 characters.")
        return False
    
    token = tokens[0]
    loading_spinner("Updating bio", 1.2)
    
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/json"
    }
    
    data = {"bio": new_bio}
    
    try:
        response = requests.patch("https://discord.com/api/v9/users/@me", headers=headers, json=data, timeout=5)
        
        if response.status_code == 200:
            success("Bio successfully updated!")
            info(f"New bio: {new_bio}")
        elif response.status_code == 401:
            error("Invalid token")
        else:
            error(f"Failed to update bio. Status: {response.status_code}")
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True