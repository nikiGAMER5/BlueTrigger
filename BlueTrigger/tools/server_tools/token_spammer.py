import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from data.config import load_tokens
import threading
import queue

def run_token_spammer():
    """Spam messages in a channel"""
    print()
    print_info_box(
        "Token Spammer Tool",
        [
            "Sends multiple messages to a channel",
            "Can use multiple tokens",
            "Status: Working"
        ]
    )
    print()
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    channel_id = prompt_input("Enter channel ID:")
    message = prompt_input("Enter message to spam:")
    count = prompt_input("Number of messages to send (default: 10)", "10")
    delay = prompt_input("Delay between messages in seconds (default: 1)", "1")
    
    try:
        count = int(count)
        delay = float(delay)
    except:
        count = 10
        delay = 1
    
    if not channel_id or not message:
        warn("Missing channel ID or message")
        return False
    
    info(f"Spamming {count} messages with {len(tokens)} tokens...")
    warning_msg = f"{Colors.WARNING}Press Ctrl+C to stop{Colors.RESET}"
    print(warning_msg)
    
    sent = 0
    token_index = 0
    
    try:
        for i in range(count):
            token = tokens[token_index % len(tokens)]
            token_index += 1
            
            headers = {
                "Authorization": token,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Content-Type": "application/json"
            }
            
            data = {"content": message}
            
            try:
                response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=data, timeout=5)
                if response.status_code == 200:
                    sent += 1
                    print(f"  {Colors.GREEN}✓{Colors.RESET} Message {sent}/{count} sent")
                elif response.status_code == 429:
                    # Rate limited
                    retry_after = response.json().get('retry_after', 5)
                    warn(f"Rate limited! Waiting {retry_after}s")
                    time.sleep(retry_after)
                else:
                    warn(f"Failed: {response.status_code}")
            except Exception as e:
                error(f"Error: {str(e)}")
            
            time.sleep(delay)
            
    except KeyboardInterrupt:
        print()
        warn("Spamming stopped by user")
    
    success(f"Sent {sent} messages successfully!")
    return True