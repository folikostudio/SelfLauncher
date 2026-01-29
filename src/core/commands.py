# core/commands.py
class CommandRegistry:
    def __init__(self):
        self.commands = {}

    def register(self, name, func):
        self.commands[name] = func

    def execute(self, name, args=None):
        func = self.commands.get(name)
        if not func:
            print(f"[core] Unknown command or arguments")
            return
        try:
            # args
            func(args)
        except Exception as e:
            print(f"[core ERROR] {e}")
