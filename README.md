# datetime-app
A simple Python app that shows a Tkinter popup with the current username and local date/time.

## Python App

The Python app uses `tkinter` to display a message box containing:

- the detected username (using `getpass.getuser()` or environment values)
- the current local datetime

If no username can be detected, it falls back to `User`.

Run it with:

```bash
python app.py
```

Example message shown by the app:

> Hello Maria, it is currently 2026-05-16 14:50:30 🔥 👍 😄

## Code behavior

`app.py` does the following:

1. imports `datetime`, `getpass`, `os`, and `tkinter`
2. detects the username from the system or environment
3. formats the current local datetime as `YYYY-MM-DD HH:MM:SS`
4. builds a friendly greeting string with emoji
5. displays the string in a Tkinter information popup

## Requirements

- Python 3
- `tkinter` available in your Python installation

## Changelog

_Use this section to note changes to the app or documentation._
