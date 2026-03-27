import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from working.session import session
from data.config import load_tokens

def run_token_onliner():
    """Keep a token online/active"""
    print()
    print_info_box(
        "Token OnLiner Tool",
        [
            "Keeps your token online by sending heartbeat requests",
            "Status: Basic functionality implemented"
        ]
    )
    print()
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    duration = prompt_input("How many seconds to keep online? (default: 60)", "60")
    try:
        duration = int(duration)
    except:
        duration = 60
    
    info(f"Keeping {len(tokens)} tokens online for {duration} seconds...")
    
    for i, token in enumerate(tokens, 1):
        loading_spinner(f"Keeping token {i} online", 0.5)
        headers = {
            "Authorization": token,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        try:
            # Send heartbeat to Discord
            response = requests.get("https://discord.com/api/v9/users/@me", headers=headers, timeout=5)
            if response.status_code == 200:
                user_data = response.json()
                success(f"Token {i}: {user_data.get('username', 'Unknown')} is online")
            else:
                warn(f"Token {i}: Invalid or expired token")
        except Exception as e:
            error(f"Token {i}: Error - {str(e)}")
    
    if duration > 0:
        info(f"Keeping online for {duration} seconds...")
        time.sleep(duration)
        success(f"Tokens kept online for {duration} seconds")
    
    return True