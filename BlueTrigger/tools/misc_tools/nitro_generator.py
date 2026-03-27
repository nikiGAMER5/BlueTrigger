import time
import random
import string
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box

def run_nitro_generator():
    """Generate fake Nitro codes"""
    print()
    print_info_box(
        "Nitro Generator Tool",
        [
            "Generates Discord Nitro gift codes",
            "Warning: These codes are NOT valid!",
            "This is for educational purposes only"
        ]
    )
    print()
    
    num_codes = 5
    
    loading_spinner(f"Generating {num_codes} Nitro codes", 1.5)
    
    print()
    success(f"Generated {num_codes} placeholder Nitro codes:")
    print()
    
    for i in range(num_codes):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        print(f"  {Colors.BRIGHT_BLUE}{i+1}.{Colors.RESET} https://discord.gift/{code}")
    
    print()
    warn("These codes are NOT valid Discord Nitro gifts!")
    print()
    
    return True