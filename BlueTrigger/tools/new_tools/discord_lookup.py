import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from data.config import load_tokens

def run_discord_lookup():
    """Look up Discord user information"""
    print()
    print_info_box(
        "Discord Lookup Tool",
        [
            "Look up Discord user information",
            "Shows user ID, creation date, avatar, etc.",
            "Status: Working"
        ]
    )
    print()
    
    user_input = prompt_input("Enter Discord User ID or Username#0000:")
    
    if not user_input:
        warn("No input provided")
        return False
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        warn("Some features may be limited")
    
    token = tokens[0] if tokens else None
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    if token:
        headers["Authorization"] = token
    
    loading_spinner(f"Looking up {user_input}", 1.5)
    
    try:
        # Try to get user by ID or username
        user_id = None
        if user_input.isdigit():
            user_id = user_input
        else:
            # Try to resolve username#discriminator
            if "#" in user_input:
                name, discrim = user_input.split("#")
                response = requests.get(f"https://discord.com/api/v9/users/{name}", headers=headers, timeout=5)
                if response.status_code == 200:
                    users = response.json()
                    for user in users:
                        if user.get('discriminator') == discrim:
                            user_id = user.get('id')
                            break
        
        if user_id:
            response = requests.get(f"https://discord.com/api/v9/users/{user_id}", headers=headers, timeout=5)
            if response.status_code == 200:
                user = response.json()
                print()
                success("User information retrieved:")
                print(f"  {Colors.BRIGHT_BLUE}Username:{Colors.RESET} {user.get('username', 'Unknown')}")
                print(f"  {Colors.BRIGHT_BLUE}Discriminator:{Colors.RESET} {user.get('discriminator', '0000')}")
                print(f"  {Colors.BRIGHT_BLUE}User ID:{Colors.RESET} {user.get('id', 'Unknown')}")
                print(f"  {Colors.BRIGHT_BLUE}Bot:{Colors.RESET} {user.get('bot', False)}")
                print(f"  {Colors.BRIGHT_BLUE}System:{Colors.RESET} {user.get('system', False)}")
                
                # Decode creation date from ID
                if user.get('id'):
                    timestamp_ms = (int(user['id']) >> 22) + 1420070400000
                    created_at = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp_ms / 1000))
                    print(f"  {Colors.BRIGHT_BLUE}Account Created:{Colors.RESET} {created_at}")
                
                if user.get('avatar'):
                    avatar_hash = user['avatar']
                    if avatar_hash.startswith('a_'):
                        avatar_url = f"https://cdn.discordapp.com/avatars/{user['id']}/{avatar_hash}.gif"
                    else:
                        avatar_url = f"https://cdn.discordapp.com/avatars/{user['id']}/{avatar_hash}.png"
                    print(f"  {Colors.BRIGHT_BLUE}Avatar URL:{Colors.RESET} {avatar_url}")
            else:
                error(f"User not found. Status: {response.status_code}")
        else:
            error("Could not resolve user")
            
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True