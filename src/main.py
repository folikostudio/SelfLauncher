from core.config import Config
from core.commands import CommandRegistry
from core.plugin_loader import PluginLoader
from core.commands_from_config import load_config_commands

# For plugins
import tkinter
import PyQt5

def main():
    # Config load
    config = Config()
    config.load()

    print(f"=== {config.data.get('launcher_name', 'SelfLauncher')} ===")

    # Create command registry
    registry = CommandRegistry()

    # Load commands from config
    load_config_commands(config.data, registry)

    # Plugin load
    PluginLoader().load(registry, config.data)

    # REPL
    while True:
        try:
            cmd = input("=>").strip()
            if not cmd:
                continue
            registry.execute(cmd)
        except KeyboardInterrupt:
            print("\n^C")
        except SystemExit:
            break

if __name__ == "__main__":
    main()
