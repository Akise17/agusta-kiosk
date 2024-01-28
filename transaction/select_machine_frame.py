import tkinter as tk
import os
from config import ASSETS_DIR
from PIL import Image,ImageTk

class SelectMachineFrame(tk.Frame):
  def __init__(self, parent, is_member):
    super().__init__(parent)
    self.parent = parent
    self.is_member = is_member
    self.configure(bg="white")  # Set background color
    
    screen_width = parent.winfo_screenwidth()
    screen_height = parent.winfo_screenheight()
    self.config(width=screen_width, height=screen_height)

    # Make the frame fullscreen
    # self.pack(fill=tk.BOTH, expand=True)

    # Create a frame for the buttons
    self.button_frame = tk.Frame(self, bg="white")
    self.button_frame.pack(side=tk.RIGHT, fill=tk.Y, expand=True)
    self.button_frame.place(relx=1, rely=0.5, x=-50, y=-self.parent.winfo_screenheight() // 3, anchor="ne")

    # Calculate button size based on screen width
    button_width = int(parent.winfo_width() * 0.5)
    button_height = int(button_width * 0.3)
    button_font = ("Arial", int(parent.winfo_width() * 0.04))

    # Create Washer button
    washer_img = Image.open(os.path.join(ASSETS_DIR, "ic_washer.png"))
    washer_img = washer_img.resize((button_height, button_height))
    washer_icon= ImageTk.PhotoImage(washer_img)
    self.washer_button = tk.Button(self.button_frame, text="Washer", compound="left", width=button_width, height=button_height, image=washer_icon, font=button_font)
    self.washer_button.image = washer_icon
    self.washer_button.pack(pady=20)

    # Create Dryer button
    dryer_img = Image.open(os.path.join(ASSETS_DIR, "ic_dryer.png"))
    dryer_img = dryer_img.resize((button_height, button_height))
    dryer_icon= ImageTk.PhotoImage(dryer_img)
    self.dryer_button = tk.Button(self.button_frame, text="Dryer", compound="left", width=button_width, height=button_height, image=dryer_icon, font=button_font)
    self.dryer_button.image = dryer_icon
    self.dryer_button.pack(pady=20)

    # Create Back button
    back_img = Image.open(os.path.join(ASSETS_DIR, "back.png"))
    back_img = back_img.resize((button_height // 5, button_height // 5))
    back_icon= ImageTk.PhotoImage(back_img)
    self.back_button = tk.Button(self.button_frame, text="", width=button_width // 10, height=button_width // 10, image=back_icon, font=button_font, command=self.back_button_clicked, border=0)
    self.back_button.image = back_icon
    self.back_button.pack(side=tk.LEFT, pady=20)

  def back_button_clicked(self):
    # Destroy the current frame when the back button is clicked
    self.destroy()
