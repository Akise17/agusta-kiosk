import tkinter as tk
from wifi.screen import open_wifi_screen
from transaction.select_machine_frame import SelectMachineFrame
from PIL import Image,ImageTk
import os
from config import ASSETS_DIR

def close_window(event=None):
  root.destroy()

def member_button_clicked():
  # Open select machine frame for members
  print("member_button_clicked")
  select_machine_frame = SelectMachineFrame(root, is_member=True)
  # select_machine_frame.grid(row=1, column=0, sticky="nsew")

def regular_button_clicked():
  # Open select machine frame for regular users
  print("regular_button_clicked")
  select_machine_frame = SelectMachineFrame(root, is_member=False)
  # select_machine_frame.grid(row=1, column=0, sticky="nsew")

root = tk.Tk()
root.configure(bg="white")
root.attributes("-fullscreen", True)  # Make the window fullscreen

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.config(width=screen_width, height=screen_height)

button_frame = tk.Frame(root, bg="white")
button_frame.grid(row=0, column=0, sticky="nsew")
button_frame.pack(side=tk.TOP)

button_width = int(root.winfo_screenwidth() * 0.3)
button_height = button_width
button_font = ("Arial", int(root.winfo_screenwidth() * 0.04))
image_size = int(button_height * 0.75)
padding = int(root.winfo_screenwidth() * 0.05)
padding_y = int((root.winfo_screenheight() - button_height) * 0.5)

# Create Member button
member_img = Image.open(os.path.join(ASSETS_DIR, "member.png"))
member_img = member_img.resize((image_size, image_size))
member_icon= ImageTk.PhotoImage(member_img)
member_button = tk.Button(button_frame, text="Member", compound="top", width=button_width, height=button_width, command=member_button_clicked, image=member_icon, font=button_font)
member_button.image = member_icon
member_button.pack(side=tk.LEFT, padx=padding, pady=padding_y)

# Create Regular button
regular_img = Image.open(os.path.join(ASSETS_DIR, "regular.png"))
regular_img = regular_img.resize((image_size, image_size))
regular_icon= ImageTk.PhotoImage(regular_img)
regular_button = tk.Button(button_frame, text="Regular", compound="top", width=button_width, height=button_width, command=regular_button_clicked, image=regular_icon, font=button_font)
regular_button.image = regular_icon
regular_button.pack(side=tk.RIGHT ,padx=padding, pady=padding_y)

# Create button to open Setting screen
button_setting_size = int(button_width // 3)
setting_image_size = button_setting_size
setting_img = Image.open(os.path.join(ASSETS_DIR, "setting.png"))
setting_img = setting_img.resize((setting_image_size, setting_image_size))
setting_icon= ImageTk.PhotoImage(setting_img)
wifi_font = ("Arial", int(button_width * 0.04))
connect_wifi_screen_button = tk.Button(root, text="", width=button_setting_size, height=button_setting_size, command=lambda: open_wifi_screen(root), image=setting_icon, border=0)
connect_wifi_screen_button.image = setting_icon
connect_wifi_screen_button.place(relx=1, x=-10, y=10, anchor="ne")

# Bind the Escape key to close the window
root.bind("<Escape>", close_window)

try:
  root.mainloop()
except KeyboardInterrupt:
  close_window()
