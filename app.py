from datetime import datetime
import getpass
import os

import requests
from flask import Flask, render_template_string, request


app = Flask(__name__)
DEFAULT_LOCATION = "New York"


def detect_username():
    try:
        name = getpass.getuser()
    except Exception:
        name = None

    if not name:
        name = os.environ.get("USER") or os.environ.get("USERNAME")

    if not name:
        return "User"

    name = name.split("@")[0]
    return name.replace("_", " ").title()


def get_weather(location):
    try:
        response = requests.get(
            f"https://wttr.in/{location}",
            params={"format": "%C, %t"},
            timeout=5,
        )
        response.raise_for_status()
    except requests.RequestException:
        return "unavailable right now"

    weather = response.text.strip()
    return weather or "unavailable right now"


def get_public_ipv4():
    try:
        response = requests.get("https://api.ipify.org", timeout=5)
        response.raise_for_status()
    except requests.RequestException:
        return None

    ipv4 = response.text.strip()
    return ipv4 or None


def get_location_from_ip(ipv4):
    if not ipv4:
        return None

    try:
        response = requests.get(f"https://ipapi.co/{ipv4}/json/", timeout=5)
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError):
        return None

    city = data.get("city")
    region = data.get("region")
    country = data.get("country_name")

    if city and region:
        return f"{city}, {region}"

    if city and country:
        return f"{city}, {country}"

    return city or region or country


def get_primary_location():
    if os.environ.get("WEATHER_LOCATION"):
        return os.environ["WEATHER_LOCATION"]

    ipv4 = get_public_ipv4()
    return get_location_from_ip(ipv4) or DEFAULT_LOCATION


@app.route("/")
def home():
    username = detect_username()
    detected_location = get_primary_location()
    location = request.args.get("location") or detected_location
    today = datetime.now().strftime("%A, %B %d, %Y")
    weather = get_weather(location)

    return render_template_string(
        """
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Date Time App</title>
            <style>
                body {
                    margin: 0;
                    min-height: 100vh;
                    display: grid;
                    place-items: center;
                    font-family: Arial, sans-serif;
                    background: #f4f7fb;
                    color: #20242a;
                }

                main {
                    width: min(680px, calc(100% - 32px));
                    padding: 32px;
                    border: 1px solid #d8dee8;
                    border-radius: 8px;
                    background: white;
                    box-shadow: 0 10px 30px rgba(32, 36, 42, 0.08);
                }

                h1 {
                    margin: 0 0 12px;
                    font-size: clamp(1.8rem, 4vw, 3rem);
                    line-height: 1.1;
                }

                p {
                    margin: 0;
                    font-size: 1.1rem;
                    line-height: 1.6;
                }

                .hint {
                    margin-top: 8px;
                    color: #586274;
                    font-size: 0.95rem;
                }

                form {
                    display: flex;
                    gap: 8px;
                    margin-top: 24px;
                }

                input,
                button {
                    font: inherit;
                    padding: 10px 12px;
                    border-radius: 6px;
                    border: 1px solid #b8c0cc;
                }

                input {
                    flex: 1;
                    min-width: 0;
                }

                button {
                    border-color: #2563eb;
                    background: #2563eb;
                    color: white;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <main>
                <h1>Hello {{ username }}</h1>
                <p>Today is {{ today }} and the weather in {{ location }} is {{ weather }}.</p>
                <p class="hint">Primary location: {{ detected_location }}</p>

                <form method="get">
                    <input name="location" value="{{ location }}" aria-label="Weather location">
                    <button type="submit">Update</button>
                </form>
            </main>
        </body>
        </html>
        """,
        username=username,
        today=today,
        location=location,
        detected_location=detected_location,
        weather=weather,
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
