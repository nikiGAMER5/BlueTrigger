import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input

def run_webhook_spammer():
    """Spam messages via webhook"""
    print()
    print_info_box(
        "Webhook Spammer Tool",
        [
            "Spams messages using a webhook",
            "Can send multiple messages quickly",
            "Status: Working"
        ]
    )
    print()
    
    webhook_url = prompt_input("Enter webhook URL:")
    
    if not webhook_url:
        warn("No webhook URL provided")
        return False
    
    message = prompt_input("Enter message to spam:")
    count = prompt_input("Number of messages to send (default: 10)", "10")
    delay = prompt_input("Delay between messages in seconds (default: 0.5)", "0.5")
    
    try:
        count = int(count)
        delay = float(delay)
    except:
        count = 10
        delay = 0.5
    
    if not message:
        warn("No message provided")
        return False
    
    info(f"Spamming {count} messages...")
    warning_msg = f"{Colors.WARNING}Press Ctrl+C to stop{Colors.RESET}"
    print(warning_msg)
    
    sent = 0
    
    try:
        for i in range(count):
            data = {"content": message}
            
            try:
                response = requests.post(webhook_url, json=data, timeout=5)
                if response.status_code in [200, 204]:
                    sent += 1
                    print(f"  {Colors.GREEN}✓{Colors.RESET} Message {sent}/{count} sent")
                elif response.status_code == 429:
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