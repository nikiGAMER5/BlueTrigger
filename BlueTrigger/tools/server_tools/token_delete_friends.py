import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from data.config import load_tokens

def run_token_delete_friends():
    """Delete all friends"""
    print()
    print_info_box(
        "Token Delete Friends Tool",
        [
            "Deletes all friends from the user's friend list",
            "Status: Working"
        ]
    )
    print()
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    confirm = input(f"{Colors.WARNING}Are you sure you want to delete ALL friends? (y/N): {Colors.RESET}").lower()
    
    if confirm != 'y':
        warn("Operation cancelled")
        return False
    
    token = tokens[0]
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    loading_spinner("Fetching friends list", 1.2)
    
    try:
        # Get friends list
        response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers, timeout=5)
        
        if response.status_code == 200:
            friends = response.json()
            info(f"Found {len(friends)} friends")
            
            deleted = 0
            for friend in friends:
                try:
                    delete_response = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friend['id']}", headers=headers, timeout=3)
                    if delete_response.status_code in [200, 204]:
                        deleted += 1
                        print(f"  {Colors.GREEN}✓{Colors.RESET} Deleted friend: {friend.get('user', {}).get('username', 'Unknown')}")
                    time.sleep(0.2)
                except:
                    pass
            
            success(f"Successfully deleted {deleted} friends!")
        elif response.status_code == 401:
            error("Invalid token")
        else:
            error(f"Failed to fetch friends. Status: {response.status_code}")
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True