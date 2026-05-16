from datetime import datetime
import getpass
import os
import tkinter as tk
from tkinter import messagebox

def detect_username():
	try:
		name = getpass.getuser()
	except Exception:
		name = None

	if not name:
		name = os.environ.get('USER') or os.environ.get('USERNAME')

	if not name:
		return "User"

	name = name.split('@')[0]
	return name.replace('_', ' ').title()

now = datetime.now()
username = detect_username()
message = f"Hello {username}, it is currently {now.strftime('%Y-%m-%d %H:%M:%S')} 🔥 👍 😄"

root = tk.Tk()
root.withdraw()

messagebox.showinfo("Date Time App", message)

root.destroy()
