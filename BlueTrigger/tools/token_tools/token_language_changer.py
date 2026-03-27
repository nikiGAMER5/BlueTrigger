import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from data.config import load_tokens

def run_token_language_changer():
    """Change Discord language"""
    print()
    print_info_box(
        "Token Language Changer",
        [
            "Changes the Discord interface language",
            "Status: Working"
        ]
    )
    print()
    
    languages = {
        "1": "en-US",  # English (US)
        "2": "en-GB",  # English (UK)
        "3": "es-ES",  # Spanish
        "4": "fr-FR",  # French
        "5": "de-DE",  # German
        "6": "it-IT",  # Italian
        "7": "pt-BR",  # Portuguese (Brazil)
        "8": "ru-RU",  # Russian
        "9": "ja-JP",  # Japanese
        "10": "ko-KR",  # Korean
        "11": "zh-CN",  # Chinese (Simplified)
        "12": "zh-TW",  # Chinese (Traditional)
        "13": "tr-TR",  # Turkish
        "14": "nl-NL",  # Dutch
        "15": "pl-PL",  # Polish
        "16": "sv-SE",  # Swedish
        "17": "fi-FI",  # Finnish
        "18": "da-DK",  # Danish
        "19": "no-NO",  # Norwegian
        "20": "cs-CZ",  # Czech
        "21": "hu-HU",  # Hungarian
    }
    
    print("Available languages:")
    for key, lang in languages.items():
        print(f"  {key}. {lang}")
    print()
    
    choice = prompt_input("Select language number:")
    
    if choice not in languages:
        warn("Invalid language selection")
        return False
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    token = tokens[0]
    loading_spinner("Changing language", 1.2)
    
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/json"
    }
    
    data = {"locale": languages[choice]}
    
    try:
        response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=data, timeout=5)
        
        if response.status_code in [200, 204]:
            success(f"Language successfully changed to {languages[choice]}!")
        elif response.status_code == 401:
            error("Invalid token")
        else:
            error(f"Failed to change language. Status: {response.status_code}")
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True