import time
import requests
import base64
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from data.config import load_tokens
import os

def run_token_pfp_changer():
    """Change profile picture"""
    print()
    print_info_box(
        "Token Profile Picture Changer",
        [
            "Changes the user's avatar/profile picture",
            "Supports image files (PNG, JPG, GIF)",
            "Status: Working"
        ]
    )
    print()
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    image_path = prompt_input("Enter path to image file:")
    
    if not image_path or not os.path.exists(image_path):
        warn("Image file not found")
        return False
    
    try:
        with open(image_path, "rb") as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')
        
        # Determine image type
        ext = os.path.splitext(image_path)[1].lower()
        if ext in ['.png', '.jpg', '.jpeg', '.gif']:
            image_type = ext[1:]
            if image_type == 'jpg':
                image_type = 'jpeg'
        else:
            error("Unsupported image format. Use PNG, JPG, or GIF")
            return False
        
        token = tokens[0]
        loading_spinner("Uploading new avatar", 2.0)
        
        headers = {
            "Authorization": token,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Content-Type": "application/json"
        }
        
        data = {
            "avatar": f"data:image/{image_type};base64,{image_data}"
        }
        
        response = requests.patch("https://discord.com/api/v9/users/@me", headers=headers, json=data, timeout=10)
        
        if response.status_code == 200:
            success("Profile picture successfully changed!")
        elif response.status_code == 400:
            error("Invalid image format or file too large")
        elif response.status_code == 401:
            error("Invalid token")
        else:
            error(f"Failed to change profile picture. Status: {response.status_code}")
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True