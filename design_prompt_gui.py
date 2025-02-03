import random
import tkinter as tk
from tkinter import ttk

# Categories (same as the ones above)
# ...

def generate_prompt():
    theme = random.choice(themes)
    product = random.choice(products)
    color_scheme = random.choice(color_schemes)
    mood = random.choice(moods)
    typography = random.choice(typography_styles)
    audience = random.choice(target_audiences)
    challenge = random.choice(optional_challenges)

    prompt = (f"🎨 Design a {product} with a {theme} theme.\n"
              f"🎨 Color Scheme: {color_scheme}\n"
              f"🎨 Mood: {mood}\n"
              f"🎨 Typography: {typography}\n"
              f"🎨 Target Audience: {audience}\n"
              f"🔥 Optional Challenge: {challenge}")

    prompt_label.config(text=prompt)

# Create GUI Window
root = tk.Tk()
root.title("DesignSpark Lite")
root.geometry("500x400")
root.resizable(False, False)

# Title Label
title_label = ttk.Label(root, text="🎨 DesignSpark Lite 🎨", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Display the Logo
logo = tk.PhotoImage(file="logo.png")  # Make sure logo.png is in the same folder
logo_label = tk.Label(root, image=logo)
logo_label.pack(pady=10)

# Prompt Display Label
prompt_label = ttk.Label(root, text="Click 'Generate' to get a prompt!", wraplength=450, justify="center", font=("Arial", 12))
prompt_label.pack(pady=20)

# Generate Button
generate_button = ttk.Button(root, text="Generate New Prompt", command=generate_prompt)
generate_button.pack(pady=20)

# Run the GUI
root.mainloop()
