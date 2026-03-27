# ui/menu.py - Blue Trigger Menu System

import os
import sys
from ui.colors import Colors

def get_terminal_width():
    try:
        return os.get_terminal_size().columns
    except:
        return 100

def separator(char='═', color=None):
    color = color or Colors.BRIGHT_BLUE
    width = get_terminal_width()
    print(f"{color}{char * width}{Colors.RESET}")

def thin_separator(char='─', color=None):
    color = color or Colors.DARK_BLUE
    width = get_terminal_width()
    print(f"{color}{char * width}{Colors.RESET}")

def box_line(text, width=None, align='center', color=None):
    """Print text inside a boxed line"""
    color = color or Colors.LIGHT_BLUE
    w = width or get_terminal_width()
    if align == 'center':
        padded = text.center(w - 4)
    elif align == 'left':
        padded = f" {text} ".ljust(w - 2)
    else:
        padded = text
    print(f"{Colors.BRIGHT_BLUE}║{color}{padded}{Colors.BRIGHT_BLUE}║{Colors.RESET}")

def print_header(version="1.0", title="Main Menu"):
    """Print the top header bar"""
    width = get_terminal_width()
    
    separator('═')
    
    left  = f"  {Colors.CYAN_BLUE}Blue Trigger {Colors.BOLD}{version}{Colors.RESET}{Colors.BRIGHT_BLUE}  [{Colors.LIGHT_BLUE}{title}{Colors.BRIGHT_BLUE}]"
    right = f"{Colors.CYAN_BLUE}[E]{Colors.LIGHT_BLUE} Exit    {Colors.CYAN_BLUE}[F]{Colors.LIGHT_BLUE} Tokens File  "
    
    # Raw string lengths (no color codes) for spacing
    left_raw  = f"  Blue Trigger {version}  [{title}]"
    right_raw = f"[E] Exit    [F] Tokens File  "
    
    spaces = width - len(left_raw) - len(right_raw)
    spaces = max(spaces, 1)
    
    print(f"{left}{' ' * spaces}{right}{Colors.RESET}")
    
    separator('═')

def print_footer():
    """Print footer hint bar"""
    width = get_terminal_width()
    separator('─')
    hints = [
        f"{Colors.CYAN_BLUE}[?]{Colors.LIGHT_BLUE} Help",
        f"{Colors.CYAN_BLUE}[B]{Colors.LIGHT_BLUE} Back",
        f"{Colors.CYAN_BLUE}[E]{Colors.LIGHT_BLUE} Exit",
        f"{Colors.CYAN_BLUE}[C]{Colors.LIGHT_BLUE} Clear",
    ]
    line = "   ".join(hints)
    raw_len = sum(len(h.replace('\033[38;5;27m','').replace('\033[38;5;39m','').replace('\033[0m','')) for h in hints) + (3 * (len(hints)-1))
    pad = (width - raw_len) // 2
    print(" " * max(pad,0) + line + Colors.RESET)
    separator('─')

def print_menu_items(items, columns=3):
    """
    items: list of (number, label) tuples
    Prints in N columns with blue styling
    """
    width = get_terminal_width()
    col_width = (width - 4) // columns
    
    # Pad items to fill evenly
    while len(items) % columns != 0:
        items.append(('  ', ''))
    
    for row_start in range(0, len(items), columns):
        row = items[row_start:row_start + columns]
        line = ""
        raw_line = ""
        for num, label in row:
            if label:
                num_str = f"{Colors.CYAN_BLUE}{str(num).zfill(2)}{Colors.RESET}"
                lbl_str = f"{Colors.LIGHT_BLUE} {label}{Colors.RESET}"
                entry = f"  {num_str}{lbl_str}"
                raw_len = 2 + 2 + 1 + len(label)
            else:
                entry = ""
                raw_len = 0
            padding = col_width - raw_len
            line += entry + " " * max(padding, 1)
        print(line)

def centered_url(url):
    width = get_terminal_width()
    pad = (width - len(url)) // 2
    print(f"{' ' * pad}{Colors.BOLD}{Colors.ICE_BLUE}{url}{Colors.RESET}")

def prompt_input(text="Select"):
    """Styled input prompt"""
    return input(f"\n  {Colors.CYAN_BLUE}╔══{Colors.LIGHT_BLUE} {text} {Colors.CYAN_BLUE}══╗{Colors.RESET}\n  {Colors.CYAN_BLUE}╚══>{Colors.WHITE} ")

def loading_spinner(message="Loading", duration=1.5):
    """Display a spinner animation"""
    import time
    frames = ["⠋","⠙","⠸","⠴","⠦","⠇"]
    start = __import__('time').time()
    i = 0
    while __import__('time').time() - start < duration:
        sys.stdout.write(f"\r  {Colors.CYAN_BLUE}{frames[i % len(frames)]}{Colors.RESET} {Colors.LIGHT_BLUE}{message}...{Colors.RESET}")
        sys.stdout.flush()
        __import__('time').sleep(0.1)
        i += 1
    sys.stdout.write(f"\r  {Colors.LIGHT_BLUE}✓ {message} complete!{Colors.RESET}        \n")
    sys.stdout.flush()

def print_info_box(title, lines):
    """Print a bordered info box"""
    width = max(len(line) for line in lines + [title]) + 6
    print(f"  {Colors.BRIGHT_BLUE}╔{'═' * (width)}╗{Colors.RESET}")
    print(f"  {Colors.BRIGHT_BLUE}║{Colors.BOLD}{Colors.ICE_BLUE}  {title.center(width - 2)}  {Colors.RESET}{Colors.BRIGHT_BLUE}║{Colors.RESET}")
    print(f"  {Colors.BRIGHT_BLUE}╠{'═' * (width)}╣{Colors.RESET}")
    for line in lines:
        print(f"  {Colors.BRIGHT_BLUE}║{Colors.LIGHT_BLUE}  {line.ljust(width - 2)}  {Colors.RESET}{Colors.BRIGHT_BLUE}║{Colors.RESET}")
    print(f"  {Colors.BRIGHT_BLUE}╚{'═' * (width)}╝{Colors.RESET}")

def success(msg):
    print(f"  {Colors.ICE_BLUE}[✓]{Colors.RESET} {Colors.LIGHT_BLUE}{msg}{Colors.RESET}")

def error(msg):
    print(f"  {Colors.BRIGHT_BLUE}[✗]{Colors.RESET} {Colors.PALE_BLUE}{msg}{Colors.RESET}")

def info(msg):
    print(f"  {Colors.CYAN_BLUE}[i]{Colors.RESET} {Colors.LIGHT_BLUE}{msg}{Colors.RESET}")

def warn(msg):
    print(f"  {Colors.BRIGHT_BLUE}[!]{Colors.RESET} {Colors.ICE_BLUE}{msg}{Colors.RESET}")
