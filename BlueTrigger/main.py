#!/usr/bin/env python3
# main.py - Blue Trigger v1.0

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.colors import Colors
from ui.banner import animate_logo, print_banner, clear, typewrite
from ui.menu import (
    print_header, print_footer, print_menu_items,
    centered_url, prompt_input, loading_spinner,
    success, error, info, warn, separator, thin_separator,
    print_info_box
)
from tools.token_tools import TOKEN_TOOLS
from tools.server_tools import SERVER_TOOLS
from tools.misc_tools import MISC_TOOLS
from tools.new_tools import NEW_TOOLS
from working.session import session
from data.config import load_config, load_tokens

# Page 1: Discord Tools
DISCORD_TOOLS = [
    (1,  "Token Information"),
    (2,  "Token Login"),
    (3,  "Token OnLiner"),
    (4,  "Token Generator"),
    (5,  "Token Disabler"),
    (6,  "Token Bio Changer"),
    (7,  "Token Alias Changer"),
    (8,  "Token CStatus Changer"),
    (9,  "Token Pfp Changer"),
    (10, "Token Language Changer"),
    (11, "House Changer"),
    (12, "Theme Changer"),
    (13, "Token Joiner"),
    (14, "Token Leaver"),
    (15, "Server Information"),
    (16, "Token Nuker"),
    (17, "Token Delete Friends"),
    (18, "Token Block Friends"),
    (19, "Token Unblock Users"),
    (20, "Token Spammer"),
    (21, "Token Mass Dm"),
    (22, "Token Delete Dm"),
    (23, "Id To Token"),
    (24, "Snowflake Decoder"),
    (25, "Bot Id To Invite"),
    (26, "Webhook Information"),
    (27, "Webhook Generator"),
    (28, "Webhook Spammer"),
    (29, "Webhook Deleter"),
    (30, "Nitro Generator"),
]

# Page 2: OSINT Tools
OSINT_TOOLS = [
    (31, "Phone Lookup"),
    (32, "Email Lookup"),
    (33, "Email Spammer"),
    (34, "IP Lookup"),
    (35, "Username Checker"),
    (36, "Discord Lookup"),
    (37, "Instagram Lookup"),
    (38, "Twitter Lookup"),
    (39, "GitHub Lookup"),
    (40, "Reddit Lookup"),
    (41, "Facebook Lookup"),
    (42, "TikTok Lookup"),
    (43, "YouTube Lookup"),
    (44, "Snapchat Lookup"),
    (45, "Telegram Lookup"),
]

# Page 3: Network Tools
NETWORK_TOOLS = [
    (46, "Port Scanner"),
    (47, "Ping Tool"),
    (48, "DNS Lookup"),
    (49, "Whois Lookup"),
    (50, "Traceroute"),
    (51, "Subdomain Finder"),
    (52, "HTTP Headers"),
    (53, "SSL Checker"),
    (54, "Reverse IP Lookup"),
    (55, "Banner Grabber"),
]

# Page 4: Crypto Tools
CRYPTO_TOOLS = [
    (56, "Wallet Generator"),
    (57, "Blockchain Lookup"),
    (58, "Transaction Checker"),
    (59, "Gas Price Checker"),
    (60, "Token Price Checker"),
    (61, "Wallet Balance Checker"),
    (62, "Smart Contract Scanner"),
]

# Combine all tools for execution
ALL_DISCORD_TOOLS = {**TOKEN_TOOLS, **SERVER_TOOLS, **MISC_TOOLS}
ALL_OSINT_TOOLS = NEW_TOOLS
ALL_NETWORK_TOOLS = {}
ALL_CRYPTO_TOOLS = {}

ALL_TOOLS = {
    **ALL_DISCORD_TOOLS,
    **ALL_OSINT_TOOLS,
    **ALL_NETWORK_TOOLS,
    **ALL_CRYPTO_TOOLS,
}

# Page configuration
PAGES = {
    1: {"name": "DISCORD TOOLS", "tools": DISCORD_TOOLS, "color": Colors.CYAN_BLUE},
    2: {"name": "OSINT TOOLS", "tools": OSINT_TOOLS, "color": Colors.GREEN},
    3: {"name": "NETWORK TOOLS", "tools": NETWORK_TOOLS, "color": Colors.YELLOW},
    4: {"name": "CRYPTO TOOLS", "tools": CRYPTO_TOOLS, "color": Colors.PURPLE},
}

current_page = 1

def show_main_menu():
    """Render the main menu screen with pagination"""
    global current_page
    clear()
    print_banner()
    print()
    
    page_data = PAGES[current_page]
    title = f"{page_data['color']}{page_data['name']}{Colors.RESET}"
    print_header(version="1.0", title=title)
    print()
    
    centered_url("https://github.com/BlueTrigger/blue-trigger-tool")
    print()
    
    # Show current page tools
    print_menu_items(page_data["tools"], columns=3)
    
    print()
    thin_separator()
    
    # Navigation bar - using simple symbols
    uptime = session.get_uptime()
    tokens_loaded = len(load_tokens())
    
    # Simple navigation with [<] and [>]
    nav_left = f"{Colors.CYAN_BLUE}[<]{Colors.LIGHT_BLUE} Prev"
    nav_right = f"{Colors.CYAN_BLUE}[>]{Colors.LIGHT_BLUE} Next"
    nav_page = f"{Colors.CYAN_BLUE}[{current_page}/{len(PAGES)}]{Colors.LIGHT_BLUE} Page"
    
    left = f"  {Colors.CYAN_BLUE}[?]{Colors.LIGHT_BLUE} Help  {Colors.CYAN_BLUE}[I]{Colors.LIGHT_BLUE} Info  {Colors.CYAN_BLUE}[C]{Colors.LIGHT_BLUE} Changelog"
    right = f"{Colors.CYAN_BLUE}Uptime:{Colors.LIGHT_BLUE} {uptime}   {Colors.CYAN_BLUE}Tokens:{Colors.LIGHT_BLUE} {tokens_loaded}  "
    
    try:
        terminal_w = os.get_terminal_size().columns
    except:
        terminal_w = 100
    
    left_raw = "  [?] Help  [I] Info  [C] Changelog"
    nav_raw = f"  [<] Prev  [>] Next  [{current_page}/{len(PAGES)}] Page"
    right_raw = f"Uptime: {uptime}   Tokens: {tokens_loaded}  "
    
    # Calculate spacing
    total_len = len(left_raw) + len(nav_raw) + len(right_raw)
    spaces = terminal_w - total_len
    if spaces < 1:
        spaces = 1
    
    print(f"{left}{' ' * max(spaces, 1)}{nav_left}  {nav_page}  {nav_right}{' ' * max(spaces, 1)}{right}{Colors.RESET}")
    
    thin_separator()
    print()

def show_tool_screen(tool_num, tool_name):
    """Run a tool"""
    clear()
    print_banner()
    print()
    print_header(version="1.0", title=f"Tool {str(tool_num).zfill(2)}: {tool_name}")
    print()
    
    # Run the actual tool
    if tool_num in ALL_TOOLS:
        try:
            ALL_TOOLS[tool_num]()
        except Exception as e:
            error(f"Error running tool: {e}")
    else:
        from tools.placeholder import run_placeholder, placeholder_result
        run_placeholder(tool_name, tool_num)
        placeholder_result()
    
    print()
    info("Press [ENTER] to return to the main menu...")
    input()

def show_info_screen():
    """Show tool info"""
    clear()
    print_banner()
    print()
    print_header(version="1.0", title="Tool Information")
    print()
    print_info_box("Blue Trigger v1.0 — Tool Information", [
        "Name    : Blue Trigger",
        "Version : 1.0.0",
        "Author  : Blue Trigger Team",
        "Theme   : Blue",
        "Tools   : 62 Total",
        "",
        "Pages:",
        "  Page 1: Discord Tools (30 tools)",
        "  Page 2: OSINT Tools (15 tools)",
        "  Page 3: Network Tools (10 tools)",
        "  Page 4: Crypto Tools (7 tools)",
        "",
        "Navigation:",
        "  [<] or 1  : Previous page",
        "  [>] or 2  : Next page",
        "  [1-4]     : Jump to page",
    ])
    print()
    info("Press [ENTER] to go back...")
    input()

def show_changelog():
    """Show changelog"""
    clear()
    print_banner()
    print()
    print_header(version="1.0", title="Changelog")
    print()
    
    changelog = [
        ("v1.0.0", [
            "Initial release",
            "30 Discord tools implemented",
            "Multi-page menu system",
        ]),
        ("v1.1.0 - Coming Soon", [
            "OSINT Tools (15 tools)",
            "Network Tools (10 tools)",
            "Crypto Tools (7 tools)",
            "Phone/Email/IP Lookup",
            "Username checker across platforms",
        ]),
    ]
    
    for version, changes in changelog:
        print(f"  {Colors.BOLD}{Colors.ICE_BLUE}[{version}]{Colors.RESET}")
        for c in changes:
            print(f"    {Colors.BRIGHT_BLUE}•{Colors.RESET} {Colors.LIGHT_BLUE}{c}{Colors.RESET}")
        print()
    
    info("Press [ENTER] to go back...")
    input()

def show_coming_soon():
    """Simple coming soon screen"""
    clear()
    print_banner()
    print()
    print_header(version="1.0", title="Coming Soon")
    print()
    
    print_info_box("Coming Soon in v1.1", [
        "OSINT Tools:",
        "  • Phone Lookup",
        "  • Email Lookup", 
        "  • Email Spammer",
        "  • IP Lookup",
        "  • Username Checker",
        "  • Social Media Lookups",
        "",
        "Network Tools:",
        "  • Port Scanner",
        "  • DNS Lookup",
        "  • Whois Lookup",
        "",
        "Crypto Tools:",
        "  • Wallet Generator",
        "  • Blockchain Lookup",
    ])
    
    print()
    separator()
    print()
    
    info("These tools are currently in development")
    info("Use [<] and [>] to browse different tool categories")
    print()
    
    info("Press [ENTER] to return to main menu...")
    input()

def show_tokens_file():
    """Show tokens"""
    clear()
    print_banner()
    print()
    print_header(version="1.0", title="Tokens File")
    print()
    
    tokens = load_tokens()
    if tokens:
        for i, t in enumerate(tokens, 1):
            masked = t[:10] + "..." + t[-5:] if len(t) > 15 else t
            print(f"  {Colors.CYAN_BLUE}{str(i).zfill(2)}{Colors.RESET} {Colors.LIGHT_BLUE}{masked}{Colors.RESET}")
    else:
        warn("No tokens loaded. Add tokens to data/tokens.txt")
    
    print()
    info("Press [ENTER] to go back...")
    input()

def main():
    """Main program entry"""
    global current_page
    animate_logo()
    
    # Create tool map from all pages
    tool_map = {}
    for page_data in PAGES.values():
        for num, name in page_data["tools"]:
            tool_map[str(num)] = name
    
    while True:
        show_main_menu()
        
        choice = prompt_input("Enter Option Number or Command").strip().lower()
        
        if choice in ('e', 'exit', 'quit', 'q'):
            clear()
            print()
            typewrite("  Goodbye! Blue Trigger shutting down...", Colors.LIGHT_BLUE, 0.03)
            time.sleep(0.5)
            sys.exit(0)
        
        elif choice == 'f':
            show_tokens_file()
        
        elif choice in ('?', 'help', 'h'):
            clear()
            print_banner()
            print()
            print_header("1.0", "Help")
            print()
            print_info_box("Blue Trigger Help", [
                "Enter a tool number to run a tool.",
                "[<] or 'prev' : Previous page",
                "[>] or 'next' : Next page",
                "[1] - [4]     : Jump to page 1-4",
                "[E] or 'exit' : Quit the program",
                "[F]           : View tokens file",
                "[?] or 'help' : Show this help screen",
                "[I] or 'info' : Show tool information",
                "[C]           : View changelog",
                "[S]           : View coming soon features",
                "",
                "Use [<] and [>] to switch between tool categories",
            ])
            print()
            info("Press [ENTER] to go back...")
            input()
        
        elif choice in ('i', 'info'):
            show_info_screen()
        
        elif choice in ('c', 'changelog'):
            show_changelog()
        
        elif choice in ('s', 'coming', 'soon'):
            show_coming_soon()
        
        # Page navigation with simple symbols
        elif choice in ('prev', '<', '['):
            current_page -= 1
            if current_page < 1:
                current_page = len(PAGES)
        
        elif choice in ('next', '>', ']'):
            current_page += 1
            if current_page > len(PAGES):
                current_page = 1
        
        # Direct page jump with numbers 1-4
        elif choice in ('1', '2', '3', '4'):
            page_num = int(choice)
            if 1 <= page_num <= len(PAGES):
                current_page = page_num
            else:
                error(f"Page must be between 1 and {len(PAGES)}")
                time.sleep(1)
        
        elif choice.isdigit() and choice in tool_map:
            show_tool_screen(int(choice), tool_map[choice])
        
        elif choice.isdigit():
            num = str(int(choice))
            if num in tool_map:
                show_tool_screen(int(num), tool_map[num])
            else:
                error(f"Invalid option: {choice}")
                time.sleep(1)
        
        else:
            error(f"Unknown command: '{choice}'. Type '?' for help.")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n  {Colors.LIGHT_BLUE}[!] Interrupted. Exiting Blue Trigger...{Colors.RESET}\n")
        sys.exit(0)