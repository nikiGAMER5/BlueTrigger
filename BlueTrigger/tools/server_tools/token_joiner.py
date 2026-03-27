import time
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from working.session import session
from data.config import load_tokens

def run_token_joiner():
    """Join a Discord server using a token"""
    print()
    print_info_box(
        "Token Joiner Tool",
        [
            "Joins a Discord server using token(s)",
            "Requires server invite code",
            "Status: Placeholder - Coming soon"
        ]
    )
    print()
    
    invite = prompt_input("Enter invite code (e.g., discord, abc123)").strip()
    
    if not invite:
        warn("No invite code provided")
        return False
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    info(f"Joining server with {len(tokens)} tokens...")
    loading_spinner(f"Joining discord.gg/{invite}", 1.8)
    
    print()
    success(f"Successfully joined discord.gg/{invite} (placeholder)")
    print()
    
    return True