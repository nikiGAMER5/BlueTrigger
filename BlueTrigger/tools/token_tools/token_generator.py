import time
import random
import string
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box

def run_token_generator():
    """Generate Discord tokens (fake/unchecked)"""
    print()
    print_info_box(
        "Token Generator Tool",
        [
            "Generates Discord tokens (placeholder)",
            "Warning: Generated tokens are not valid!",
            "This is for educational purposes only"
        ]
    )
    print()
    
    num_tokens = 5
    
    loading_spinner(f"Generating {num_tokens} tokens", 1.2)
    
    print()
    success(f"Generated {num_tokens} placeholder tokens:")
    print()
    
    for i in range(num_tokens):
        fake_token = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
        print(f"  {Colors.BRIGHT_BLUE}{i+1}.{Colors.RESET} {fake_token}")
    
    print()
    warn("These tokens are NOT valid Discord tokens!")
    print()
    
    return True