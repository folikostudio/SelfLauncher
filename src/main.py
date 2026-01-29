# main.py
from core.config import Config
from core.commands import CommandRegistry
from core.plugin_loader import PluginLoader
from core.commands_from_config import load_config_commands

# For plugins
import tkinter
import PyQt5
from mistralai import Mistral

def main():
    # --------------------------------------------------
    # Load config
    # --------------------------------------------------
    config = Config()
    config.load()

    launcher_name = config.data.get('launcher_name', 'SelfLauncher')
    print(f"=== {launcher_name} ===")

    # --------------------------------------------------
    # Create command registry
    # --------------------------------------------------
    registry = CommandRegistry()

    # --------------------------------------------------
    # Load commands from config
    # --------------------------------------------------
    load_config_commands(config.data, registry)

    # --------------------------------------------------
    # Load plugins
    # --------------------------------------------------
    PluginLoader().load(registry, config.data)

    # --------------------------------------------------
    # REPL (read-eval-print loop)
    # --------------------------------------------------
    while True:
        try:
            cmd_line = input("=>").strip()
            if not cmd_line:
                continue

            # Split command and arguments
            parts = cmd_line.split()
            cmd_name = parts[0]
            args = parts[1:] if len(parts) > 1 else []

            # Execute command with args
            registry.execute(cmd_name, args)

        except KeyboardInterrupt:
            print("\n^C")
        except SystemExit:
            break
        except Exception as e:
            print(f"[core ERROR] {e}")

if __name__ == "__main__":
    main()
