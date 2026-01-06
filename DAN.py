import customtkinter
from tkinter import messagebox
from google import genai
from google.genai.errors import APIError
import os

try:
    with open("API_key.txt", "r") as f:
        API_KEY = f.read().strip()
        if not API_KEY:
            messagebox.showerror("Error", "Paste Gemini API key in API_key.txt")
except FileNotFoundError:
    messagebox.showerror("Error", "API_key.txt not found!")
    exit()

try:
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    messagebox.showerror("Error", f"Error while loading AI: {e}")
    exit()

character = "Generate ONLY raw Python code. DO NOT use markdown formatting. DO NOT use ```python or ``` blocks. Your output must start and end with Python code only. Use double quotes for strings. If you need to interact, use tkinter.messagebox. If you using libraries, import it first. Request: "

def execute():
    prompt = entry.get()
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=character+prompt,
        config={'temperature': 0.7}
    )
    print(response.text.strip())
    exec(response.text.strip())

app = customtkinter.CTk()
app.title("DAN")
if os.path.exists("icon.ico"):
    app.iconbitmap("icon.ico")

title = customtkinter.CTkLabel(app, text="Do anything now", font=("Arial", 24, "bold"))
title.grid(row=0, column=0, padx=20, pady=20)

entry = customtkinter.CTkEntry(app, placeholder_text="Let AI execute anything", width=250)
entry.grid(row=1, column=0, padx=20, pady=20)

btn = customtkinter.CTkButton(app, text="Execute", command=execute)
btn.grid(row=2, column=0, padx=20, pady=20)

app.mainloop()