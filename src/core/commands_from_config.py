def load_config_commands(config, registry):
    for name, info in config.get("commands", {}).items():
        cmd_type = info.get("type")

        if cmd_type == "print":
            text = info.get("value", "")
            registry.register(name, lambda t=text: print(t))

        elif cmd_type == "exit":
            registry.register(name, lambda: exit(0))
