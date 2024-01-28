import subprocess
import re
import platform

def get_current_wifi():
  # Get the current operating system
  current_os = platform.system()

  try:
    if current_os == "Linux":
      # Run the shell command to get the current Wi-Fi network on Linux
      output = subprocess.check_output(["/sbin/iwgetid", "-r"]).decode().strip()
      return output if output else "No Wi-Fi connected"
    elif current_os == "Darwin":  # macOS
      # Run the shell command to get the current Wi-Fi network on macOS
      output = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"]).decode().split("\n")
      for line in output:
        if " SSID:" in line:
          return line.split(":")[1].strip()
      return "No Wi-Fi connected"
    else:
      return "Unsupported operating system"
  except FileNotFoundError:
    return "Command not found"
  except subprocess.CalledProcessError:
    return "Failed to retrieve current Wi-Fi network"

def get_wifi_networks():
  current_os = platform.system()
  try:
    # Run the airport command to scan for Wi-Fi networks
    if current_os == "Darwin":
      output = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-s"])
      output = output.decode("utf-8").splitlines()
    elif current_os == "Linux":
      output = subprocess.check_output(["nmcli", "--fields", "SSID", "device", "wifi"])
      output = output.decode("utf-8").splitlines()
      output.pop(0)

    # Extract Wi-Fi network names
    wifi_networks = []
    for line in output:
      if re.match("^\s*SSID\s+BSSID\s+RSSI\s+CHANNEL\s+", line):
          continue
      ssid = line.split()[0]
      wifi_networks.append(ssid)

    return wifi_networks

  except subprocess.CalledProcessError:
    return None
