import time
import pywifi
from pywifi import const
from print_gui import print_to_gui

def connection(ssid, password):
    """
    Attempt to connect to a Wi-Fi network with the given SSID and password.

    Args:
        ssid (str): The SSID of the Wi-Fi network to connect to.
        password (str): The password for the Wi-Fi network.

    Returns:
        bool: True if the connection was successful, False otherwise.
    """
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()
    time.sleep(1)  # Ensure disconnection

    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    if password == "none":
        profile.akm.append(const.AKM_TYPE_NONE)
        profile.cipher = const.CIPHER_TYPE_NONE
    else:
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password

    tmp_profile = iface.add_network_profile(profile)

    iface.connect(tmp_profile)
    time.sleep(5)  # Wait for connection

    return iface.status() == const.IFACE_CONNECTED

def connect_to_wifi(network, text_output):
    """
    Connects to a Wi-Fi network with the given SSID and password.
    """
    ssid = network["ssid"]
    password = network["password"] 
    print_to_gui(f"Attempting to connect to {ssid}...", text_output)
    if connection(ssid, password):
        print_to_gui(f"Connected to {ssid}", text_output)
    else:
        print_to_gui(f"Failed to connect to {ssid}", text_output)