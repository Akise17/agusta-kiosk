
import tkinter as tk
from tkinter import ttk
from wifi.screen import open_wifi_screen
import os
from config import ASSETS_DIR
from PIL import Image,ImageTk
import requests
from check_serial_number import getMachine_addr
import configparser

LARGEFONT =("Verdana", 35)
WIDTH = 480
HEIGHT = 320
  
class tkinterApp(tk.Tk):
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
        # self.serial_number = self.load_or_create_config('app_config')['General']['serial_number']
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.attributes("-fullscreen", True)
        self.geometry(f"{WIDTH}x{HEIGHT}")

        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {}  
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, SelectMachineFrame, SelectTimeFrame, SettingsFrame):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
        self.bind("<Escape>", self.close_window)
        self.protocol("WM_DELETE_WINDOW", self.close_window)
  
    # to display the current frame passed as
    def show_frame(self, cont, **kwargs):
        frame = self.frames[cont]
        if kwargs:
            frame.load_arguments(**kwargs)
        frame.tkraise()

    def close_window(self, event=None):
        self.destroy()

    def load_or_create_config(self, file_path):
        config = configparser.ConfigParser()

        # Check if the configuration file exists
        if os.path.exists(file_path):
            # Load the configuration from the file
            config.read(file_path)
            print("Configuration file loaded successfully.")
        else:
            # Create a new configuration
            print("Configuration file not found. Creating a new one.")
            config['General'] = {'serial_number': getMachine_addr()}

            # Write the configuration to the file
            with open(file_path, 'w') as config_file:
                config.write(config_file)
            config.read(file_path)
            print("New configuration file created.")

        return config
  
class StartPage(tk.Frame):
    def load_arguments(self, **kwargs):
        self.kwargs = kwargs
    
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="white")

        button_width = int(self.winfo_screenwidth() * 0.3)
        button_height = button_width
        button_font = ("Arial", int(self.winfo_screenwidth() * 0.04))

        padding = int(self.winfo_screenwidth() * 0.05)
        padding_y = int((self.winfo_screenheight() - button_height) * 0.5)

        image_size = int(button_height * 0.75)
  
        # Create Member button
        member_img = Image.open(os.path.join(ASSETS_DIR, "member.png"))
        member_img = member_img.resize((image_size, image_size))
        member_icon= ImageTk.PhotoImage(member_img)
        member_button = tk.Button(self, text="Member", compound="top", width=button_width, height=button_width, image=member_icon,
                                  font=button_font, command = lambda : controller.show_frame(SelectMachineFrame, is_member=True))
        member_button.image = member_icon
        member_button.pack(side=tk.LEFT, padx=padding, pady=padding_y)
     
        # Create Regular button
        regular_img = Image.open(os.path.join(ASSETS_DIR, "regular.png"))
        regular_img = regular_img.resize((image_size, image_size))
        regular_icon= ImageTk.PhotoImage(regular_img)
        regular_button = tk.Button(self, text="Regular", compound="top", width=button_width, height=button_width,
                                   image=regular_icon, font=button_font, command = lambda : controller.show_frame(SelectMachineFrame, is_member=False))
        regular_button.image = regular_icon
        regular_button.pack(side=tk.RIGHT ,padx=padding, pady=padding_y)

        # Create button to open Setting screen
        button_setting_size = int(button_width // 3)
        setting_image_size = button_setting_size
        setting_img = Image.open(os.path.join(ASSETS_DIR, "setting.png"))
        setting_img = setting_img.resize((setting_image_size, setting_image_size))
        setting_icon= ImageTk.PhotoImage(setting_img)
        self.connect_wifi_screen_button = tk.Button(self, text="", width=button_setting_size, height=button_setting_size, image=setting_icon,
                                                    border=0, bg="white", highlightthickness=0, command = lambda : controller.show_frame(SettingsFrame))
        self.connect_wifi_screen_button.image = setting_icon
        self.connect_wifi_screen_button.place(relx=1, x=-10, y=10, anchor="ne")
        
class SelectMachineFrame(tk.Frame):
    def load_arguments(self, **kwargs):
        self.kwargs = kwargs
        try:
            if self.kwargs['is_member']:
                self.dryer_button.config(state=tk.DISABLED)
                print("Member Welcome")
            else:
                self.dryer_button.config(state=tk.NORMAL)
        except:
            pass

    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent, bg="white")

        self.kwargs = kwargs
        
        # Calculate button size based on screen width
        button_width = int(self.winfo_screenwidth() * 0.3)
        button_height = button_width
        button_font = ("Arial", int(self.winfo_screenwidth() * 0.04))

        padding = int(self.winfo_screenwidth() * 0.05)
        padding_y = int((self.winfo_screenheight() - button_height) * 0.5)

        image_size = int(button_height * 0.75)

        # Create Washer button
        washer_img = Image.open(os.path.join(ASSETS_DIR, "ic_washer.png"))
        washer_img = washer_img.resize((image_size, image_size))
        washer_icon= ImageTk.PhotoImage(washer_img)
        self.washer_button = tk.Button(self, text="Washer", compound="top", width=button_width, height=button_height, image=washer_icon,
                                       font=button_font, command = lambda : controller.show_frame(SelectTimeFrame, is_member=False))
        self.washer_button.image = washer_icon
        self.washer_button.pack(side=tk.LEFT ,padx=padding, pady=padding_y)

        # Create Dryer button
        dryer_img = Image.open(os.path.join(ASSETS_DIR, "ic_dryer.png"))
        dryer_img = dryer_img.resize((image_size, image_size))
        dryer_icon= ImageTk.PhotoImage(dryer_img)
        self.dryer_button = tk.Button(self, text="Dryer", compound="top", width=button_width, height=button_height, image=dryer_icon, font=button_font)
        self.dryer_button.image = dryer_icon
        self.dryer_button.pack(side=tk.RIGHT ,padx=padding, pady=padding_y)

        # Create Back button
        button_back_size = int(button_width // 3)
        back_image_size = button_back_size
        back_img = Image.open(os.path.join(ASSETS_DIR, "back.png"))
        back_img = back_img.resize((back_image_size, back_image_size))
        back_icon= ImageTk.PhotoImage(back_img)
        self.back_button = tk.Button(self, text="", width=button_back_size, height=button_back_size, image=back_icon, font=button_font, command=lambda : controller.show_frame(StartPage), border=0, bg="white", highlightthickness=0)
        self.back_button.image = back_icon
        self.back_button.place(relx=1, x=-10, y=10, anchor="ne")

class SelectTimeFrame(tk.Frame):
    def load_arguments(self, **kwargs):
        self.kwargs = kwargs
    
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent, bg="white")

        self.kwargs = kwargs
        self.product_list = []
        
        # Calculate button size based on screen width
        button_width = int(self.winfo_screenwidth() * 0.1) // 10
        button_height = button_width
        button_font = ("Arial", int(self.winfo_screenwidth() * 0.02))

        padding = int(self.winfo_screenwidth() * 0.06)
        padding_y = int((self.winfo_screenheight() - button_height) * 0.2)

        # Create Product List button
        for product in self.product_list:
            self.washer_button = tk.Button(self, text="Washer", compound="top", width=button_width, height=button_height, font=button_font)
            self.washer_button.pack(side=tk.LEFT ,padx=padding, pady=padding_y)

        # Create Back button
        back_button_width = int(self.winfo_screenwidth() * 0.3)
        
        button_back_size = int(back_button_width // 3)
        back_image_size = button_back_size
        back_img = Image.open(os.path.join(ASSETS_DIR, "back.png"))
        back_img = back_img.resize((back_image_size, back_image_size))
        back_icon= ImageTk.PhotoImage(back_img)
        self.back_button = tk.Button(self, text="", width=button_back_size, height=button_back_size, image=back_icon, font=button_font, command=lambda : controller.show_frame(SelectMachineFrame), border=0, bg="white", highlightthickness=0)
        self.back_button.image = back_icon
        self.back_button.place(relx=1, x=-10, y=10, anchor="ne")
    
    def call_api(self):
        # Example API endpoint
        api_url = "https://api.example.com/data"
        
        try:
            response = requests.get(api_url)
            data = response.json()
            # Process the API response data
            print(data)
        except requests.exceptions.RequestException as e:
            # Handle exceptions
            print("Error:", e)

class SettingsFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent, bg="white")

        # Display the serial number
        self.serial_label = tk.Label(self, text=f"Serial Number: {getMachine_addr()}", font=LARGEFONT, bg="white", fg="black")
        self.serial_label.pack(side=tk.TOP)

        # Create Back button
        button_font = ("Arial", int(self.winfo_screenwidth() * 0.02))
        back_button_width = int(self.winfo_screenwidth() * 0.3)
        
        button_back_size = int(back_button_width // 3)
        back_image_size = button_back_size
        back_img = Image.open(os.path.join(ASSETS_DIR, "back.png"))
        back_img = back_img.resize((back_image_size, back_image_size))
        back_icon= ImageTk.PhotoImage(back_img)
        self.back_button = tk.Button(self, text="", width=button_back_size, height=button_back_size, image=back_icon, font=button_font, command=lambda : controller.show_frame(StartPage), border=0, bg="white", highlightthickness=0)
        self.back_button.image = back_icon
        self.back_button.place(relx=1, x=-10, y=10, anchor="ne")

# Driver Code
app = tkinterApp()
app.mainloop()
