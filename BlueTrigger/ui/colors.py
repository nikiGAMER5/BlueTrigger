# ui/colors.py - Blue Trigger Color System

class Colors:
    # Blue Theme
    DEEP_BLUE    = '\033[38;5;17m'
    DARK_BLUE    = '\033[38;5;19m'
    BLUE         = '\033[38;5;21m'
    BRIGHT_BLUE  = '\033[38;5;27m'
    CYAN_BLUE    = '\033[38;5;33m'
    LIGHT_BLUE   = '\033[38;5;39m'
    ICE_BLUE     = '\033[38;5;45m'
    PALE_BLUE    = '\033[38;5;51m'

    # Additional Colors for different pages
    GREEN        = '\033[38;5;46m'
    YELLOW       = '\033[38;5;226m'
    PURPLE       = '\033[38;5;129m'
    RED          = '\033[38;5;196m'
    ORANGE       = '\033[38;5;208m'
    PINK         = '\033[38;5;205m'
    TEAL         = '\033[38;5;30m'
    LIME         = '\033[38;5;118m'
    MAGENTA      = '\033[38;5;201m'
    CYAN         = '\033[38;5;51m'
    
    # Status Colors
    SUCCESS      = '\033[38;5;46m'   # Green
    ERROR        = '\033[38;5;196m'  # Red
    WARNING      = '\033[38;5;226m'  # Yellow
    INFO         = '\033[38;5;39m'   # Light Blue
    
    # Backgrounds
    BG_DARK_BLUE = '\033[48;5;17m'
    BG_BLUE      = '\033[48;5;19m'
    BG_GREEN     = '\033[48;5;22m'
    BG_RED       = '\033[48;5;52m'
    BG_YELLOW    = '\033[48;5;58m'

    # Accents
    WHITE        = '\033[97m'
    GRAY         = '\033[38;5;240m'
    DARK_GRAY    = '\033[38;5;235m'
    SILVER       = '\033[38;5;250m'
    GOLD         = '\033[38;5;220m'

    # Effects
    BOLD         = '\033[1m'
    DIM          = '\033[2m'
    BLINK        = '\033[5m'
    UNDERLINE    = '\033[4m'
    RESET        = '\033[0m'

    # Separators
    SEP_COLOR    = BRIGHT_BLUE
    TITLE_COLOR  = ICE_BLUE
    MENU_COLOR   = LIGHT_BLUE
    ITEM_COLOR   = PALE_BLUE
    NUMBER_COLOR = CYAN_BLUE
    HIGHLIGHT    = BRIGHT_BLUE

    @staticmethod
    def colorize(text, color):
        return f"{color}{text}{Colors.RESET}"

    @staticmethod
    def success(text):
        return f"{Colors.SUCCESS}{text}{Colors.RESET}"
    
    @staticmethod
    def error(text):
        return f"{Colors.ERROR}{text}{Colors.RESET}"
    
    @staticmethod
    def warning(text):
        return f"{Colors.WARNING}{text}{Colors.RESET}"
    
    @staticmethod
    def info(text):
        return f"{Colors.INFO}{text}{Colors.RESET}"

    @staticmethod
    def gradient_text(text):
        """Apply a blue gradient to text character by character"""
        colors = [
            '\033[38;5;17m', '\033[38;5;19m', '\033[38;5;21m',
            '\033[38;5;27m', '\033[38;5;33m', '\033[38;5;39m',
            '\033[38;5;45m', '\033[38;5;51m',
        ]
        result = ""
        for i, char in enumerate(text):
            if char != ' ':
                result += colors[i % len(colors)] + char
            else:
                result += char
        return result + Colors.RESET

    @staticmethod
    def gradient_text_custom(text, color_list):
        """Apply a custom gradient to text"""
        result = ""
        for i, char in enumerate(text):
            if char != ' ':
                result += color_list[i % len(color_list)] + char
            else:
                result += char
        return result + Colors.RESET

    @staticmethod
    def box(text, color=None):
        """Create a colored box around text"""
        if color is None:
            color = Colors.BRIGHT_BLUE
        width = len(text) + 4
        top = f"{color}╔{'═' * (width - 2)}╗{Colors.RESET}"
        middle = f"{color}║ {text} ║{Colors.RESET}"
        bottom = f"{color}╚{'═' * (width - 2)}╝{Colors.RESET}"
        return f"\n{top}\n{middle}\n{bottom}\n"