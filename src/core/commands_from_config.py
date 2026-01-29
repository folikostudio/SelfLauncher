# core/commands_from_config.py

def load_config_commands(config, registry):
    commands = config.get("commands", {})

    for name, cmd in commands.items():
        ctype = cmd.get("type")

        # ---------------- PRINT ----------------
        if ctype == "print":
            value = cmd.get("value", "")

            def make_print(val):
                def _cmd(args=None):
                    print(val)
                return _cmd

            registry.register(name, make_print(value))

        # ---------------- EXIT ----------------
        elif ctype == "exit":
            def _exit(args=None):
                raise SystemExit
            registry.register(name, _exit)
