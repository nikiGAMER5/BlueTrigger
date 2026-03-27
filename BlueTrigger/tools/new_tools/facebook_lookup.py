import time
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input

def run_facebook_lookup():
    """Look up Facebook profile"""
    print()
    print_info_box(
        "Facebook Lookup Tool",
        [
            "Look up Facebook profile information",
            "Status: Coming Soon"
        ]
    )
    print()
    
    username = prompt_input("Enter Facebook username or profile ID:")
    
    if not username:
        warn("No input provided")
        return False
    
    loading_spinner(f"Looking up {username}", 1.5)
    
    print()
    info("Facebook lookup tool coming in v1.1")
    info("Features planned:")
    print("  • Profile information")
    print("  • Profile picture")
    print("  • Friend count")
    print("  • Account age")
    print()
    warn("This tool is not yet implemented")
    
    return True