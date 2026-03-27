import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from data.config import load_tokens

def run_server_info():
    """Get server information"""
    print()
    print_info_box(
        "Server Information Tool",
        [
            "Gets detailed information about a Discord server",
            "Status: Working"
        ]
    )
    print()
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    server_id = prompt_input("Enter server ID:")
    
    if not server_id:
        warn("No server ID provided")
        return False
    
    token = tokens[0]
    loading_spinner("Fetching server information", 1.5)
    
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(f"https://discord.com/api/v9/guilds/{server_id}", headers=headers, timeout=5)
        
        if response.status_code == 200:
            guild = response.json()
            print()
            success("Server information retrieved:")
            print(f"  {Colors.BRIGHT_BLUE}Name:{Colors.RESET} {guild.get('name', 'Unknown')}")
            print(f"  {Colors.BRIGHT_BLUE}ID:{Colors.RESET} {guild.get('id', 'Unknown')}")
            print(f"  {Colors.BRIGHT_BLUE}Owner:{Colors.RESET} {guild.get('owner_id', 'Unknown')}")
            print(f"  {Colors.BRIGHT_BLUE}Members:{Colors.RESET} {guild.get('approximate_member_count', 'Unknown')}")
            print(f"  {Colors.BRIGHT_BLUE}Channels:{Colors.RESET} {guild.get('approximate_presence_count', 'Unknown')}")
            print(f"  {Colors.BRIGHT_BLUE}Created:{Colors.RESET} {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(guild.get('id', 0) >> 22 + 1420070400000 / 1000))}")
            print(f"  {Colors.BRIGHT_BLUE}Boost Level:{Colors.RESET} {guild.get('premium_tier', 0)}")
            print(f"  {Colors.BRIGHT_BLUE}Verification Level:{Colors.RESET} {guild.get('verification_level', 0)}")
        elif response.status_code == 401:
            error("Invalid token")
        elif response.status_code == 403:
            error("No access to this server")
        else:
            error(f"Failed to get server info. Status: {response.status_code}")
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True