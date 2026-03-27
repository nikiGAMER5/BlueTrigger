import time
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input

def run_snapchat_lookup():
    """Look up Snapchat profile"""
    print()
    print_info_box(
        "Snapchat Lookup Tool",
        [
            "Look up Snapchat profile information",
            "Status: Coming Soon"
        ]
    )
    print()
    
    username = prompt_input("Enter Snapchat username:")
    
    if not username:
        warn("No username provided")
        return False
    
    loading_spinner(f"Looking up {username}", 1.5)
    
    print()
    info("Snapchat lookup tool coming in v1.1")
    info("Features planned:")
    print("  • Profile information")
    print("  • Snap score")
    print("  • Bitmoji")
    print("  • Account age")
    print()
    warn("This tool is not yet implemented")
    
    return True