# apphandler

App installation utilities for Windows Python apps.

## Installation

```bash
pip install apphandler
```

## Usage

```python
from apphandler import first_launch, create_shortcut, create_start_menu

# First launch — returns True if first launch, False otherwise
if first_launch():
    create_shortcut("MyApp")
    create_start_menu("MyApp")

# Create desktop shortcut manually
create_shortcut("MyApp")

# Create Start Menu shortcut manually
create_start_menu("MyApp")
```

## Functions

### `first_launch(exe_path=None, flag=None)`
Validates if the app is launched for the first time by checking for a flag file.
- `exe_path` — defaults to `sys.argv[0]` (current running file)
- `flag` — defaults to `installed.flag` next to the exe
- Returns `True` on first launch, `False` on subsequent launches

### `create_shortcut(app_name, exe_path=None)`
Creates a desktop shortcut for the app.
- `app_name` — name of the shortcut file
- `exe_path` — defaults to `sys.argv[0]` (current running file)

### `create_start_menu(app_name, exe_path=None)`
Creates a Start Menu shortcut for the app.
- `app_name` — name of the shortcut file
- `exe_path` — defaults to `sys.argv[0]` (current running file)

## Requirements

- Windows only
- Python 3.x

## Author

**Manish Maharana**
- GitHub: [@Manish-Maharana-0g](https://github.com/Manish-Maharana-0g)