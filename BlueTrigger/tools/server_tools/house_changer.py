import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from data.config import load_tokens

def run_house_changer():
    """Change HypeSquad house"""
    print()
    print_info_box(
        "House Changer Tool",
        [
            "Changes your HypeSquad house",
            "Options: Bravery (1), Brilliance (2), Balance (3)"
        ]
    )
    print()
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    print("Select HypeSquad House:")
    print("  1. Bravery (Red)")
    print("  2. Brilliance (Blue)")
    print("  3. Balance (Green)")
    
    choice = prompt_input("Enter choice (1-3)")
    
    house_map = {
        "1": 1,  # Bravery
        "2": 2,  # Brilliance
        "3": 3   # Balance
    }
    
    if choice not in house_map:
        warn("Invalid choice")
        return False
    
    house_id = house_map[choice]
    token = tokens[0]
    
    loading_spinner("Changing HypeSquad house", 1.2)
    
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/json"
    }
    
    try:
        # First leave current house if any
        requests.post("https://discord.com/api/v9/hypesquad/online", headers=headers, json={}, timeout=5)
        time.sleep(0.5)
        
        # Join new house
        response = requests.post(f"https://discord.com/api/v9/hypesquad/online", headers=headers, json={"house_id": house_id}, timeout=5)
        
        if response.status_code in [200, 204]:
            success("HypeSquad house successfully changed!")
        elif response.status_code == 401:
            error("Invalid token")
        else:
            error(f"Failed to change house. Status: {response.status_code}")
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True