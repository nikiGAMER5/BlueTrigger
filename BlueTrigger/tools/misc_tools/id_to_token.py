import time
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input

def run_id_to_token():
    """Convert user ID to token (educational only)"""
    print()
    print_info_box(
        "ID to Token Tool",
        [
            "⚠️ This tool is for EDUCATIONAL purposes only!",
            "You cannot get a token from just an ID.",
            "Tokens are secure and cannot be derived from IDs.",
            "This tool shows the structure of Discord IDs."
        ]
    )
    print()
    
    user_id = prompt_input("Enter Discord user ID:")
    
    if not user_id or not user_id.isdigit():
        warn("Invalid user ID")
        return False
    
    try:
        # Discord ID contains timestamp in snowflake
        timestamp_ms = (int(user_id) >> 22) + 1420070400000
        created_at = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp_ms / 1000))
        
        print()
        info("Discord ID Information:")
        print(f"  {Colors.BRIGHT_BLUE}User ID:{Colors.RESET} {user_id}")
        print(f"  {Colors.BRIGHT_BLUE}Created at:{Colors.RESET} {created_at}")
        print(f"  {Colors.BRIGHT_BLUE}Worker ID:{Colors.RESET} {(int(user_id) >> 17) & 0x1F}")
        print(f"  {Colors.BRIGHT_BLUE}Process ID:{Colors.RESET} {(int(user_id) >> 12) & 0x1F}")
        print(f"  {Colors.BRIGHT_BLUE}Increment:{Colors.RESET} {int(user_id) & 0xFFF}")
        
        warn("\n⚠️ You CANNOT get a token from a user ID!")
        warn("Tokens are secure credentials that cannot be derived.")
        info("This tool only shows information about the ID structure.")
        
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True