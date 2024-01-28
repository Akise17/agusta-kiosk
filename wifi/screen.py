import tkinter as tk
from tkinter import messagebox
from wifi.connection import get_wifi_networks, get_current_wifi

def open_wifi_screen(root):
  new_window = tk.Toplevel(root)
  new_window.title("Wi-Fi Selection")

  # Add Wi-Fi selection components here
  label = tk.Label(new_window, text="Select Wi-Fi Network:")
  label.pack(pady=10)
  custom_font = ("Arial", 25)

  # Show current connected Wi-Fi network
  current_wifi_label = tk.Label(new_window, text="Connected to: " + get_current_wifi(), font=custom_font)
  current_wifi_label.pack(pady=5)

  # Example: Wi-Fi listbox
  wifi_networks = get_wifi_networks()
  if wifi_networks:
    # Define a custom font
    # Create a Listbox with custom font and increased spacing
    wifi_list = tk.Listbox(new_window, selectbackground="lightblue", selectforeground="black", bd=0, highlightthickness=0, relief=tk.FLAT, font=custom_font, justify=tk.CENTER)
    for network in wifi_networks:
      wifi_list.insert(tk.END, network)
    wifi_list.pack(padx=10, pady=5, ipadx=10, ipady=5)  # Increase internal padding
  else:
    # Display an error message if Wi-Fi networks retrieval fails
    error_label = tk.Label(new_window, text="Failed to retrieve Wi-Fi networks.")
    error_label.pack(padx=10, pady=5)

  # Example: Connect button
  connect_button = tk.Button(new_window, text="Connect", command=lambda: messagebox.showinfo("Connected", f"Connected to {wifi_list.get(tk.ACTIVE)}"))
  connect_button.pack(pady=10)

  # Example: Close button
  close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
  close_button.pack(pady=5)

