import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from data.config import load_tokens

def run_theme_changer():
    """Change Discord theme"""
    print()
    print_info_box(
        "Theme Changer Tool",
        [
            "Changes Discord theme (Dark/Light)",
            "Status: Working"
        ]
    )
    print()
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    print("Select Theme:")
    print("  1. Dark")
    print("  2. Light")
    
    choice = prompt_input("Enter choice (1-2)")
    
    theme_map = {
        "1": "dark",
        "2": "light"
    }
    
    if choice not in theme_map:
        warn("Invalid choice")
        return False
    
    theme = theme_map[choice]
    token = tokens[0]
    
    loading_spinner(f"Changing theme to {theme}", 1.2)
    
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/json"
    }
    
    data = {"theme": theme}
    
    try:
        response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=data, timeout=5)
        
        if response.status_code in [200, 204]:
            success(f"Theme successfully changed to {theme}!")
        elif response.status_code == 401:
            error("Invalid token")
        else:
            error(f"Failed to change theme. Status: {response.status_code}")
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True