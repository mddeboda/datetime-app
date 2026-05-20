# datetime-app
A simple Flask web app that greets the current user, shows today's date, and displays the weather.

## Python Flask App

The app shows a web page with this message:

> Hello User. Today is Wednesday, May 20, 2026 and the weather in New York is Clear, +20C.

The exact username, date, location, and weather will change based on your computer and request.
The app tries to detect your primary location automatically from your public IPv4 address.

## Setup

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the web server:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Weather Location

By default, the app looks up your public IPv4 address, uses that to estimate your city or region, and shows weather for that location.

If the IP lookup fails, the app falls back to `New York`.

To choose a different city in the browser, add a `location` query parameter:

```text
http://127.0.0.1:5000?location=Boston
```

You can also set a default location with an environment variable:

```powershell
$env:WEATHER_LOCATION = "Boston"
python app.py
```

The priority order is:

1. `location` query parameter
2. `WEATHER_LOCATION` environment variable
3. public IPv4 location lookup
4. `New York` fallback

## Code Behavior

`app.py` does the following:

1. creates a Flask web server
2. detects the username from the system or environment
3. formats today's local date
4. detects the public IPv4 address with `api.ipify.org`
5. estimates the primary location with `ipapi.co`
6. requests a simple weather summary from `wttr.in`
7. renders a web page with the greeting, date, location, and weather

## Requirements

- Python 3
- Flask
- requests

## Changelog

_Use this section to note changes to the app or documentation._
