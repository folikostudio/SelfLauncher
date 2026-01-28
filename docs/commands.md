# Command Concept

Commands are the fundamental unit of behavior in SelfLauncher.

A command is a named action that can be executed by the system. Commands represent all possible operations, regardless of their complexity or purpose.

Commands can be triggered from:
- user interfaces
- configuration files
- other commands or modules

The core does not impose rules on what a command does. It only provides a mechanism to register and invoke commands by name.

This abstraction allows the same system to support a wide range of use cases. A command may start a process, modify internal state, open an interface, or perform arbitrary logic defined by extensions.

By reducing all actions to commands, SelfLauncher maintains a consistent and predictable execution model while remaining fully extensible.
