import tkinter as tk
from PIL import Image, ImageTk
import cv2

# === Main Window ===
root = tk.Tk()
root.title("VMail: Voice-Based Email System")
root.attributes("-fullscreen", True)  # Start in fullscreen
root.configure(bg="white")
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))  # Exit fullscreen with ESC

# === Canvas for background ===
canvas = tk.Canvas(root, highlightthickness=0, bg="white")
canvas.pack(fill="both", expand=True)

# === Load Background Video ===
video_path = "E:/BITMAP ID(pratiksha)/24C9447 - Voice Email System for blind people/100% code/New folder/voicewave.mp4"
cap = cv2.VideoCapture(video_path)

def update_video():
    ret, frame = cap.read()
    if ret:
        screen_width = root.winfo_width()
        screen_height = root.winfo_height()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (screen_width, screen_height))
        img = Image.fromarray(frame)
        img_tk = ImageTk.PhotoImage(image=img)
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        canvas.image = img_tk
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    root.after(25, update_video)

# === Navigation Actions ===
def Login():
    from subprocess import call
    call(["python", "face_login.py"])

def Register():
    from subprocess import call
    call(["python", "registration_new.py"])

# === Hover Effects ===
def on_enter(e):
    e.widget.config(bg="#0b57d0", fg="white")

def on_leave(e):
    if e.widget == register_btn:
        e.widget.config(bg="#1a73e8", fg="white")
    else:
        e.widget.config(bg="white", fg="#1a73e8")

# === Header ===
header = tk.Frame(root, bg="white")
header_id = canvas.create_window(0, 0, anchor="n", window=header)

title = tk.Label(header, text="VMail", font=("Segoe UI", 28, "bold"), bg="white", fg="#1a73e8")
title.pack(side="left", padx=(40, 10), pady=20)

subtitle = tk.Label(header, text="Voice-Based Email System", font=("Segoe UI", 12), bg="white", fg="#5f6368")
subtitle.pack(side="left", pady=20)

# === Card Container ===
card = tk.Frame(root, bg="white", highlightbackground="#dadce0", highlightthickness=1)
card_id = canvas.create_window(0, 0, window=card, width=460, height=400)

# === Inner Layout ===
inner = tk.Frame(card, bg="white")
inner.pack(padx=30, pady=30, fill="both", expand=True)

tk.Label(inner, text="Welcome to VMail", font=("Segoe UI", 24, "bold"), bg="white", fg="#202124").pack(pady=(0, 10))
tk.Label(inner, text="Please sign in or create an account to continue.", font=("Segoe UI", 11), bg="white", fg="#5f6368").pack(pady=(0, 25))

# === Buttons ===
register_btn = tk.Button(inner, text="Create Account", font=("Segoe UI", 12, "bold"),
                         bg="#1a73e8", fg="white", activebackground="#0b57d0", activeforeground="white",
                         width=30, pady=12, bd=0, cursor="hand2", relief="flat", command=Register)
register_btn.pack(pady=(0, 20))
register_btn.bind("<Enter>", on_enter)
register_btn.bind("<Leave>", on_leave)

login_btn = tk.Button(inner, text="Sign In", font=("Segoe UI", 12, "bold"),
                      bg="white", fg="#1a73e8", activebackground="#e8f0fe", activeforeground="#174ea6",
                      width=30, pady=12, bd=1, relief="solid", cursor="hand2", command=Login)
login_btn.pack()
login_btn.bind("<Enter>", on_enter)
login_btn.bind("<Leave>", on_leave)

# === Footer ===
footer = tk.Label(root, text="© 2025 VMail — Voice-Based Email System", font=("Segoe UI", 9), bg="white", fg="#9aa0a6")
footer_id = canvas.create_window(0, 0, anchor="s", window=footer)

# === Reposition UI on Resize ===
def reposition_ui(event=None):
    w, h = root.winfo_width(), root.winfo_height()
    canvas.coords(card_id, w / 2, h / 2)
    canvas.coords(header_id, w / 2, 0)
    canvas.coords(footer_id, w / 2, h - 20)

root.bind("<Configure>", reposition_ui)

# === Start Everything ===
update_video()
root.mainloop()
