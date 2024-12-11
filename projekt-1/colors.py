class Color:
    # ANSI escape codes for text colors
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DEFAULT = '\033[0m'
    
    # ANSI escape codes for background colors
    BG_PURPLE = '\033[45m'
    BG_BLUE = '\033[44m'
    BG_CYAN = '\033[46m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_RED = '\033[41m'
    BG_DEFAULT = '\033[49m'
    
    # Text styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'