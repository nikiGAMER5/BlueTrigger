import time
import requests
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input
from data.config import load_tokens

def run_token_block_friends():
    """Block all friends"""
    print()
    print_info_box(
        "Token Block Friends Tool",
        [
            "Blocks all friends instead of deleting them",
            "Status: Working"
        ]
    )
    print()
    
    tokens = load_tokens()
    if not tokens:
        warn("No tokens found in data/tokens.txt")
        return False
    
    # Optional: Show current friends before blocking
    token = tokens[0]
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        # Fetch friends list to show count
        response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers, timeout=5)
        if response.status_code == 200:
            relationships = response.json()
            friends = [r for r in relationships if r.get('type') == 1]  # Type 1 = friends
            if friends:
                info(f"Found {len(friends)} friends:")
                for i, friend in enumerate(friends[:5]):  # Show first 5 friends
                    username = friend.get('user', {}).get('username', 'Unknown')
                    print(f"  {i+1}. {username}")
                if len(friends) > 5:
                    print(f"  ... and {len(friends) - 5} more")
            else:
                info("No friends found to block")
                return True
        else:
            warn("Could not fetch friends list")
    
    except Exception as e:
        error(f"Error fetching friends: {str(e)}")
        return False
    
    confirm = input(f"\n{Colors.WARNING}⚠️ Are you sure you want to block ALL {len(friends) if 'friends' in locals() else 'your'} friends? (y/N): {Colors.RESET}").lower()
    
    if confirm != 'y':
        warn("Operation cancelled")
        return False
    
    # Second confirmation for safety
    second_confirm = input(f"{Colors.RED}⚠️ LAST WARNING: This action cannot be undone easily! Type 'BLOCK ALL' to confirm: {Colors.RESET}")
    
    if second_confirm != "BLOCK ALL":
        warn("Operation cancelled")
        return False
    
    loading_spinner("Fetching friends list", 1.2)
    
    try:
        # Get friends list again
        response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers, timeout=5)
        
        if response.status_code == 200:
            relationships = response.json()
            friends = [r for r in relationships if r.get('type') == 1]  # Type 1 = friends
            
            info(f"Blocking {len(friends)} friends...")
            print()
            
            blocked = 0
            failed = 0
            
            for friend in friends:
                try:
                    # Block user (type 2 = blocked)
                    block_data = {"type": 2}
                    block_response = requests.put(
                        f"https://discord.com/api/v9/users/@me/relationships/{friend['id']}", 
                        headers={**headers, "Content-Type": "application/json"}, 
                        json=block_data, 
                        timeout=3
                    )
                    
                    if block_response.status_code in [200, 204]:
                        blocked += 1
                        username = friend.get('user', {}).get('username', 'Unknown')
                        print(f"  {Colors.GREEN}✓{Colors.RESET} Blocked: {username}")
                    else:
                        failed += 1
                        print(f"  {Colors.RED}✗{Colors.RESET} Failed to block: {friend.get('user', {}).get('username', 'Unknown')} (Status: {block_response.status_code})")
                    
                    time.sleep(0.3)  # Small delay to avoid rate limits
                    
                except Exception as e:
                    failed += 1
                    print(f"  {Colors.RED}✗{Colors.RESET} Error blocking: {str(e)[:50]}")
            
            print()
            success(f"Successfully blocked {blocked} friends!")
            if failed > 0:
                warn(f"Failed to block {failed} friends")
                
            # Show summary
            info("Summary:")
            print(f"  {Colors.BRIGHT_BLUE}Total friends:{Colors.RESET} {len(friends)}")
            print(f"  {Colors.GREEN}Blocked:{Colors.RESET} {blocked}")
            print(f"  {Colors.RED}Failed:{Colors.RESET} {failed}")
            
        elif response.status_code == 401:
            error("Invalid token")
            return False
        else:
            error(f"Failed to fetch friends. Status: {response.status_code}")
            return False
            
    except Exception as e:
        error(f"Error: {str(e)}")
        return False
    
    return True