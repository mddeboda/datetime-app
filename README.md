# datetime-app
Date time app

## Python App

The Python app shows a popup with the current username and local time.

Run it with:

```bat
python app.py
```

## C++ Windows App

This beginner-friendly C++ program prints:

- the current Windows username
- the computer name
- the current local time

The source code is in [main.cpp](main.cpp).

### Build and Run

Using the Microsoft C++ compiler from a Developer Command Prompt:

```bat
cl /EHsc main.cpp Advapi32.lib
main.exe
```

Using MinGW g++:

```bat
g++ main.cpp -o datetime-app.exe -ladvapi32
datetime-app.exe
```

Example output:

```text
Username: Maria
Computer name: DESKTOP-12345
Current time: 2026-05-16 14:50:30
```

### Line-by-Line Explanation

```cpp
#include <windows.h>
```

Includes Windows API types and functions, such as `DWORD`, `GetUserNameA`, and `GetComputerNameA`.

```cpp
#include <Lmcons.h>
```

Includes Windows constants such as `UNLEN`, which tells us the maximum username length.

```cpp
#include <ctime>
```

Includes C++ time tools, such as `std::time_t`, `std::time`, and `std::tm`.

```cpp
#include <iomanip>
```

Includes `std::put_time`, which formats the time for printing.

```cpp
#include <iostream>
```

Includes `std::cout`, which prints text to the console.

```cpp
int main() {
```

Starts the program. Every C++ console program begins running inside `main`.

```cpp
    char username[UNLEN + 1];
```

Creates a character array to hold the Windows username. `UNLEN` is the maximum username length, and `+ 1` leaves room for the string-ending null character.

```cpp
    DWORD usernameSize = UNLEN + 1;
```

Stores the size of the username array. Windows API functions use `DWORD` for many size values.

```cpp
    char computerName[MAX_COMPUTERNAME_LENGTH + 1];
```

Creates a character array to hold the computer name.

```cpp
    DWORD computerNameSize = MAX_COMPUTERNAME_LENGTH + 1;
```

Stores the size of the computer-name array.

```cpp
    bool gotUsername = GetUserNameA(username, &usernameSize);
```

Calls the Windows API function `GetUserNameA`. If it works, the username is placed in `username`, and `gotUsername` becomes `true`.

```cpp
    bool gotComputerName = GetComputerNameA(computerName, &computerNameSize);
```

Calls `GetComputerNameA`. If it works, the computer name is placed in `computerName`, and `gotComputerName` becomes `true`.

```cpp
    std::time_t currentTime = std::time(nullptr);
```

Gets the current time from the system and stores it as a timestamp.

```cpp
    std::tm localTime{};
```

Creates an empty `std::tm` structure, which will hold readable local time parts like year, month, day, hour, minute, and second.

```cpp
    localtime_s(&localTime, &currentTime);
```

Converts the timestamp into local Windows time and stores the result in `localTime`.

```cpp
    std::cout << "Username: "
              << (gotUsername ? username : "Unknown user") << '\n';
```

Prints the username. If Windows could not read it, the program prints `Unknown user` instead.

```cpp
    std::cout << "Computer name: "
              << (gotComputerName ? computerName : "Unknown computer") << '\n';
```

Prints the computer name. If Windows could not read it, the program prints `Unknown computer` instead.

```cpp
    std::cout << "Current time: "
              << std::put_time(&localTime, "%Y-%m-%d %H:%M:%S") << '\n';
```

Prints the current local time in `year-month-day hour:minute:second` format.

```cpp
    return 0;
```

Ends the program successfully. Returning `0` means nothing went wrong.

```cpp
}
```

Closes the `main` function.

## Project README Updater Agent

This repository includes an agent configuration file at [.agent.md](.agent.md) that
helps keep this `README.md` up-to-date as the project progresses. The agent
can append concise changelog entries, update a short progress summary, and
adjust the Usage section when features or interfaces change.

- **Purpose:** Keep README content synchronized with development progress.
- **How to request updates:** Ask the assistant something like "Update README: added X" or
	"Append progress: implemented Y and updated usage".
- **Example prompts:**
	- "Update README: added timezone-aware parsing and tests"
	- "Append changelog: refactored date formatting to ISO8601"

## Changelog

_Entries added by the README Updater Agent will appear here with timestamps._

