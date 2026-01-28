# User Interface as an External Layer

In SelfLauncher, the user interface is treated as an optional and external layer.

The core system does not assume the presence of any interface. Interaction may occur through a graphical interface, a command line, or any other mechanism implemented externally.

The interface does not contain execution logic. Its sole responsibility is to present available commands and trigger them based on user input.

All aspects of the interface — layout, appearance, behavior, and available actions — are defined outside the core. This allows multiple interfaces to coexist or be replaced without affecting the system's functionality.

By decoupling the interface from execution logic, SelfLauncher ensures that presentation and behavior remain independent and flexible.
