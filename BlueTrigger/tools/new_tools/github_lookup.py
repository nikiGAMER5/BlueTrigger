import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input

def run_github_lookup():
    """Look up GitHub profile"""
    print()
    print_info_box(
        "GitHub Lookup Tool",
        [
            "Look up GitHub profile information",
            "Status: Working"
        ]
    )
    print()
    
    username = prompt_input("Enter GitHub username:")
    
    if not username:
        warn("No username provided")
        return False
    
    loading_spinner(f"Looking up {username}", 1.5)
    
    try:
        response = requests.get(f"https://api.github.com/users/{username}", timeout=5)
        
        if response.status_code == 200:
            user = response.json()
            print()
            success("GitHub profile information:")
            print(f"  {Colors.BRIGHT_BLUE}Username:{Colors.RESET} {user.get('login', 'Unknown')}")
            print(f"  {Colors.BRIGHT_BLUE}Name:{Colors.RESET} {user.get('name', 'Not set')}")
            print(f"  {Colors.BRIGHT_BLUE}Bio:{Colors.RESET} {user.get('bio', 'Not set')}")
            print(f"  {Colors.BRIGHT_BLUE}Location:{Colors.RESET} {user.get('location', 'Not set')}")
            print(f"  {Colors.BRIGHT_BLUE}Company:{Colors.RESET} {user.get('company', 'Not set')}")
            print(f"  {Colors.BRIGHT_BLUE}Public Repos:{Colors.RESET} {user.get('public_repos', 0)}")
            print(f"  {Colors.BRIGHT_BLUE}Followers:{Colors.RESET} {user.get('followers', 0)}")
            print(f"  {Colors.BRIGHT_BLUE}Following:{Colors.RESET} {user.get('following', 0)}")
            print(f"  {Colors.BRIGHT_BLUE}Created:{Colors.RESET} {user.get('created_at', 'Unknown')[:10]}")
            print(f"  {Colors.BRIGHT_BLUE}Profile URL:{Colors.RESET} {user.get('html_url', 'Unknown')}")
        elif response.status_code == 404:
            error(f"User '{username}' not found")
        else:
            error(f"Failed to lookup. Status: {response.status_code}")
            
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True