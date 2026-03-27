import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input

def run_webhook_deleter():
    """Delete a webhook"""
    print()
    print_info_box(
        "Webhook Deleter Tool",
        [
            "Deletes a Discord webhook",
            "Status: Working"
        ]
    )
    print()
    
    webhook_url = prompt_input("Enter webhook URL:")
    
    if not webhook_url:
        warn("No webhook URL provided")
        return False
    
    confirm = input(f"{Colors.WARNING}Are you sure you want to delete this webhook? (y/N): {Colors.RESET}").lower()
    
    if confirm != 'y':
        warn("Operation cancelled")
        return False
    
    loading_spinner("Deleting webhook", 1.2)
    
    try:
        response = requests.delete(webhook_url, timeout=5)
        
        if response.status_code in [200, 204]:
            success("Webhook successfully deleted!")
        elif response.status_code == 404:
            error("Webhook not found")
        else:
            error(f"Failed to delete webhook. Status: {response.status_code}")
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True