import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from data.config import load_tokens

def run_token_mass_dm():
    """Send mass DMs to friends/servers"""
    print()
    print_info_box(
        "Token Mass DM Tool",
        [
            "Sends DMs to multiple users",
            "Can send to all friends or specific users",
            "Status: Working"
        ]
    )
    print()
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    print("Select target:")
    print("  1. All friends")
    print("  2. Specific user ID")
    print("  3. Server members (requires channel ID)")
    
    choice = prompt_input("Enter choice (1-3):")
    
    message = prompt_input("Enter message to send:")
    
    if not message:
        warn("No message provided")
        return False
    
    token = tokens[0]
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/json"
    }
    
    if choice == "1":
        # DM all friends
        loading_spinner("Fetching friends list", 1.2)
        try:
            response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers, timeout=5)
            if response.status_code == 200:
                friends = response.json()
                info(f"Found {len(friends)} friends")
                
                sent = 0
                for friend in friends:
                    try:
                        user_id = friend['id']
                        # Create DM channel
                        dm_response = requests.post("https://discord.com/api/v9/users/@me/channels", headers=headers, json={"recipient_id": user_id}, timeout=5)
                        if dm_response.status_code == 200:
                            channel_id = dm_response.json()['id']
                            # Send message
                            msg_response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json={"content": message}, timeout=5)
                            if msg_response.status_code == 200:
                                sent += 1
                                print(f"  {Colors.GREEN}✓{Colors.RESET} Sent to {friend.get('user', {}).get('username', 'Unknown')}")
                            time.sleep(0.5)
                    except:
                        pass
                
                success(f"Sent messages to {sent} friends!")
            else:
                error("Failed to fetch friends")
        except Exception as e:
            error(f"Error: {str(e)}")
    
    elif choice == "2":
        # DM specific user
        user_id = prompt_input("Enter user ID:")
        if user_id:
            try:
                dm_response = requests.post("https://discord.com/api/v9/users/@me/channels", headers=headers, json={"recipient_id": user_id}, timeout=5)
                if dm_response.status_code == 200:
                    channel_id = dm_response.json()['id']
                    msg_response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json={"content": message}, timeout=5)
                    if msg_response.status_code == 200:
                        success("Message sent successfully!")
                    else:
                        error("Failed to send message")
                else:
                    error("Failed to create DM channel")
            except Exception as e:
                error(f"Error: {str(e)}")
    
    elif choice == "3":
        # DM server members (placeholder - needs guild members intent)
        warn("Server member DM feature coming soon")
    
    return True