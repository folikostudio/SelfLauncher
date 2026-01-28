import os
import importlib.util
from core.utils import get_base_dir

PLUGIN_PREFIX = "slf"

class PluginLoader:
    def load(self, registry, config=None):
        base = get_base_dir()
        for file in os.listdir(base):
            if not (file.startswith("slf") and file.endswith(".py")):
                continue
            path = os.path.join(base, file)
            name = file[:-3]

            spec = importlib.util.spec_from_file_location(name, path)
            module = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(module)
                if hasattr(module, "register"):
                    module.register(registry, config)
            except Exception as e:
                print(f"[PLUGIN ERROR] {file}: {e}")

                
