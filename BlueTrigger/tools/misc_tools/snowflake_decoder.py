import time
from ui.colors import Colors
from ui.menu import loading_spinner, success, error, info, warn, print_info_box, prompt_input

def run_snowflake_decoder():
    """Decode Discord snowflake IDs"""
    print()
    print_info_box(
        "Snowflake Decoder Tool",
        [
            "Decodes Discord snowflake IDs",
            "Shows creation time and other metadata",
            "Status: Working"
        ]
    )
    print()
    
    snowflake_id = prompt_input("Enter Discord snowflake ID:")
    
    if not snowflake_id or not snowflake_id.isdigit():
        warn("Invalid snowflake ID")
        return False
    
    try:
        snowflake = int(snowflake_id)
        timestamp_ms = (snowflake >> 22) + 1420070400000
        created_at = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp_ms / 1000))
        
        print()
        success("Snowflake decoded successfully:")
        print(f"  {Colors.BRIGHT_BLUE}ID:{Colors.RESET} {snowflake_id}")
        print(f"  {Colors.BRIGHT_BLUE}Created (UTC):{Colors.RESET} {created_at}")
        print(f"  {Colors.BRIGHT_BLUE}Unix Timestamp:{Colors.RESET} {timestamp_ms / 1000}")
        print(f"  {Colors.BRIGHT_BLUE}Worker ID:{Colors.RESET} {(snowflake >> 17) & 0x1F}")
        print(f"  {Colors.BRIGHT_BLUE}Process ID:{Colors.RESET} {(snowflake >> 12) & 0x1F}")
        print(f"  {Colors.BRIGHT_BLUE}Increment:{Colors.RESET} {snowflake & 0xFFF}")
        
    except Exception as e:
        error(f"Error: {str(e)}")
    
    return True