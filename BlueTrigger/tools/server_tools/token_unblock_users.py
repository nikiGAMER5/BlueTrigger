import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from data.config import load_tokens

def run_token_unblock_users():
    """Unblock all blocked users"""
    print()
    print_info_box(
        "Token Unblock Users Tool",
        [
            "Unblocks all blocked users",
            "Status: Working"
        ]
    )
    print()
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    confirm = input(f"{Colors.WARNING}Are you sure you want to unblock ALL users? (y/N): {Colors.RESET}").lower()
    
    if confirm != 'y':
        warn("Operation cancelled")
        return False
    
    token = tokens[0]
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    loading_spinner("Fetching relationships", 1.2)
    
    try:
        response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers, timeout=5)
        
        if response.status_code == 200:
            relationships = response.json()
            blocked = [r for r in relationships if r.get('type') == 2]  # Type 2 = blocked
            
            info(f"Found {len(blocked)} blocked users")
            
            unblocked = 0
            for user in blocked:
                try:
                    delete_response = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{user['id']}", headers=headers, timeout=3)
                    if delete_response.status_code in [200, 204]:
                        unblocked += 1
                        print(f"  {Colors.GREEN}✓{Colors.RESET} Unblocked: {user.get('user', {}).get('username', 'Unknown')}")
                    time.sleep(0.2)
                except:
                    pass
            
            success(f"Successfully unblocked {unblocked} users!")
        elif response.status_code == 401:
            error("Invalid token")
        else:
            error(f"Failed to fetch relationships. Status: {response.status_code}")
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True