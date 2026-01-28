class CommandRegistry:
    def __init__(self):
        self._commands = {}

    def register(self, name, func):
        self._commands[name] = func

    def execute(self, name):
        if name not in self._commands:
            print("[core] Unknown command or arguments")
            return
        self._commands[name]()

    def list(self):
        return list(self._commands.keys())
