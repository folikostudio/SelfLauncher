# Extensions and Modules

SelfLauncher is designed to be extended through external modules.

Modules are loaded automatically at startup and can introduce new commands, modify existing behavior, or implement additional functionality. The core does not depend on any specific module and remains functional even without extensions.

Modules interact with the system through a shared interface that provides access to configuration data and the command registry. This enables loose coupling and independent development.

There are no imposed limits on what a module can do. Modules may implement execution logic, user interaction, automation, or integration with external systems.

The extension system allows SelfLauncher to evolve without changing its core, making it suitable for long-term use and experimentation.
