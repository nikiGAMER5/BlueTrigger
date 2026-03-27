# working/session.py - Session & State Manager

import time

class Session:
    def __init__(self):
        self.start_time = time.time()
        self.current_menu = "main"
        self.history = []
        self.tokens = []
        self.last_result = None

    def navigate(self, menu_name):
        self.history.append(self.current_menu)
        self.current_menu = menu_name

    def go_back(self):
        if self.history:
            self.current_menu = self.history.pop()
        else:
            self.current_menu = "main"

    def add_token(self, token):
        if token not in self.tokens:
            self.tokens.append(token)

    def get_uptime(self):
        elapsed = int(time.time() - self.start_time)
        m, s = divmod(elapsed, 60)
        h, m = divmod(m, 60)
        return f"{h:02d}:{m:02d}:{s:02d}"

# Global session instance
session = Session()
