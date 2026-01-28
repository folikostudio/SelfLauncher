# Architecture

SelfLauncher follows a modular architecture centered around a minimal core and externally defined behavior.

The core is responsible only for:
- loading configuration files
- discovering external modules
- registering commands
- executing commands by name

All higher-level functionality is implemented outside of the core. The core has no knowledge of specific features, interfaces, or workflows.

Extensions are loaded dynamically at startup and interact with the system through a shared command registry. This allows new behavior to be added or replaced without altering the executable.

The architecture enforces separation between:
- execution logic
- configuration
- user interface
- extensions

This separation ensures that changes in one area do not require changes in others and allows the system to scale in complexity without increasing core size.
