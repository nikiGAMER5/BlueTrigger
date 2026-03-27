import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input

def run_reddit_lookup():
    """Look up Reddit profile"""
    print()
    print_info_box(
        "Reddit Lookup Tool",
        [
            "Look up Reddit user profile information",
            "Status: Working"
        ]
    )
    print()
    
    username = prompt_input("Enter Reddit username:")
    
    if not username:
        warn("No username provided")
        return False
    
    loading_spinner(f"Looking up u/{username}", 1.5)
    
    try:
        response = requests.get(f"https://www.reddit.com/user/{username}/about.json", 
                               headers={"User-Agent": "BlueTrigger/1.0"}, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            user = data.get('data', {})
            print()
            success("Reddit profile information:")
            print(f"  {Colors.BRIGHT_BLUE}Username:{Colors.RESET} {user.get('name', 'Unknown')}")
            print(f"  {Colors.BRIGHT_BLUE}Karma:{Colors.RESET} {user.get('total_karma', 0)}")
            print(f"  {Colors.BRIGHT_BLUE}Post Karma:{Colors.RESET} {user.get('link_karma', 0)}")
            print(f"  {Colors.BRIGHT_BLUE}Comment Karma:{Colors.RESET} {user.get('comment_karma', 0)}")
            print(f"  {Colors.BRIGHT_BLUE}Account Created:{Colors.RESET} {time.strftime('%Y-%m-%d', time.localtime(user.get('created_utc', 0)))}")
            print(f"  {Colors.BRIGHT_BLUE}Verified Email:{Colors.RESET} {user.get('has_verified_email', False)}")
            print(f"  {Colors.BRIGHT_BLUE}Is Gold:{Colors.RESET} {user.get('is_gold', False)}")
            print(f"  {Colors.BRIGHT_BLUE}Profile URL:{Colors.RESET} https://reddit.com/user/{username}")
        elif response.status_code == 404:
            error(f"User '{username}' not found")
        else:
            error(f"Failed to lookup. Status: {response.status_code}")
            
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True