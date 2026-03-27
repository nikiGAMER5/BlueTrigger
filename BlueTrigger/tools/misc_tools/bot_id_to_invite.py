import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input

def run_bot_id_to_invite():
    """Generate bot invite link from bot ID"""
    print()
    print_info_box(
        "Bot ID to Invite Tool",
        [
            "Generates a bot invite link from a bot ID",
            "Useful for inviting bots to servers",
            "Status: Working"
        ]
    )
    print()
    
    bot_id = prompt_input("Enter bot ID:")
    
    if not bot_id or not bot_id.isdigit():
        warn("Invalid bot ID")
        return False
    
    print()
    info("Bot invite links:")
    
    # Basic invite link
    basic_link = f"https://discord.com/oauth2/authorize?client_id={bot_id}&scope=bot"
    print(f"  {Colors.BRIGHT_BLUE}Basic:{Colors.RESET} {basic_link}")
    
    # With admin permissions
    admin_link = f"https://discord.com/oauth2/authorize?client_id={bot_id}&scope=bot&permissions=8"
    print(f"  {Colors.BRIGHT_BLUE}Admin:{Colors.RESET} {admin_link}")
    
    # With specific permissions (example: send messages, read messages)
    perms_link = f"https://discord.com/oauth2/authorize?client_id={bot_id}&scope=bot&permissions=2048"
    print(f"  {Colors.BRIGHT_BLUE}Basic Permissions:{Colors.RESET} {perms_link}")
    
    # Try to fetch bot info
    loading_spinner("Fetching bot information", 1.2)
    try:
        response = requests.get(f"https://discord.com/api/v9/users/{bot_id}", timeout=5)
        if response.status_code == 200:
            bot_data = response.json()
            print()
            info("Bot Information:")
            print(f"  {Colors.BRIGHT_BLUE}Name:{Colors.RESET} {bot_data.get('username', 'Unknown')}")
            print(f"  {Colors.BRIGHT_BLUE}Bot:{Colors.RESET} {bot_data.get('bot', False)}")
        else:
            warn("Could not fetch bot information")
    except:
        pass
    
    return True