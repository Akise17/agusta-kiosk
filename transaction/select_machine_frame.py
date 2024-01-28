import tkinter as tk
import os
from config import ASSETS_DIR
from PIL import Image,ImageTk

class SelectMachineFrame(tk.Frame):
  def __init__(self, parent, controller, is_member=False):
    tk.Frame.__init__(self, parent)
    
    # Calculate button size based on screen width
    button_width = int(parent.winfo_width() * 0.5)
    button_height = int(button_width * 0.3)
    button_font = ("Arial", int(parent.winfo_width() * 0.04))

    # Create Washer button
    washer_img = Image.open(os.path.join(ASSETS_DIR, "ic_washer.png"))
    washer_img = washer_img.resize((200, 200))
    washer_icon= ImageTk.PhotoImage(washer_img)
    self.washer_button = tk.Button(self, text="Washer", compound="left", width=button_width, height=button_height, image=washer_icon, font=button_font)
    self.washer_button.image = washer_icon
    self.washer_button.pack(pady=20)

    # Create Dryer button
    dryer_img = Image.open(os.path.join(ASSETS_DIR, "ic_dryer.png"))
    dryer_img = dryer_img.resize((200, 200))
    dryer_icon= ImageTk.PhotoImage(dryer_img)
    self.dryer_button = tk.Button(self, text="Dryer", compound="left", width=button_width, height=button_height, image=dryer_icon, font=button_font)
    self.dryer_button.image = dryer_icon
    self.dryer_button.pack(pady=20)

    # Create Back button
    back_img = Image.open(os.path.join(ASSETS_DIR, "back.png"))
    back_img = back_img.resize((200 // 5, 200 // 5))
    back_icon= ImageTk.PhotoImage(back_img)
    self.back_button = tk.Button(self, text="", width=button_width // 10, height=button_width // 10, image=back_icon, font=button_font, command=lambda : controller.show_frame(StartPage), border=0)
    self.back_button.image = back_icon
    self.back_button.pack(side=tk.LEFT, pady=20)

  def back_button_clicked(self):
    # Destroy the current frame when the back button is clicked
    
    self.parent.show_frame(StartPage)
