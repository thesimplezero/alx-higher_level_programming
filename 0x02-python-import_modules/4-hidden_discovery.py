#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = sorted(name for name in dir(hidden_4) if not name.startswith('__'))
    print("\n".join(names))
