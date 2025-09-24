import tkinter as tk
from tkinter import scrolledtext, messagebox
from threading import Thread
from wifi_connection import connect_to_wifi
from ChromeWebDriver import set_up_chrome_web_driver
from print_gui import print_to_gui
from config import configure_checkpoint

def configure_routers(text_output, router_with_internet, checkpoint_wifi_name, headless_mode):
    """
    Configures the selected Checkpoint router.

    Args:
        text_output: The object for displaying text in the GUI.
        router_with_internet (dict): The data for connecting to the router_with_internet router.
        checkpoint_wifi_name (str): The desired name for the Checkpoint WiFi network.
        headless_mode (bool): Determines if the browser runs in headless mode.
    """
    print_to_gui("Starting the router configuration process...", text_output)

    try:
        # Connect to router_with_internet to install ChromeDriver
        connect_to_wifi(router_with_internet, text_output)
        driver = set_up_chrome_web_driver(headless=headless_mode)
        print_to_gui("Chromedriver is running", text_output)

        # Start configuration for the Checkpoint router
        print_to_gui(f"Starting configuration for {checkpoint_wifi_name}", text_output)
        configure_checkpoint(driver, text_output, checkpoint_wifi_name)
            
        driver.quit()
        
    except Exception as e:
        print_to_gui(f"An error occurred: {e}", text_output)

def start_configuration(text_output, router_with_internet_ssid, router_with_internet_password, checkpoint_wifi_name, headless_mode):
    """
    Starts the configuration process in a separate thread.
    
    Args:
        text_output: The object for displaying text in the GUI.
        router_with_internet_ssid (str): The SSID of the router_with_internet Wi-Fi network.
        router_with_internet_password (str): The password of the router_with_internet Wi-Fi network.
        checkpoint_wifi_name (str): The name for the Checkpoint WiFi network.
        headless_mode (bool): The headless mode setting from the GUI.
    """
    if not router_with_internet_ssid or not checkpoint_wifi_name:
        messagebox.showerror("Error", "Please fill in all the required fields.")
        return

    router_with_internet = {"ssid": router_with_internet_ssid, "password": router_with_internet_password}

    # Start the configuration in a separate thread
    thread = Thread(target=configure_routers, args=(text_output, router_with_internet, checkpoint_wifi_name, headless_mode))
    thread.start()

# GUI setup
root = tk.Tk()
root.title("Checkpoint Configuration")

# Frame for router with Internet parameters
router_params_frame = tk.Frame(root)
router_params_frame.grid(row=0, column=0, padx=10, pady=5, sticky="w")

router_label = tk.Label(router_params_frame, text="Parameters for router with Internet (SSID, Password):")
router_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="w")

ssid_label = tk.Label(router_params_frame, text="SSID:")
ssid_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
ssid_entry = tk.Entry(router_params_frame, width=30)
ssid_entry.grid(row=1, column=1, padx=5, pady=5)

password_label = tk.Label(router_params_frame, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(router_params_frame, show="*", width=30)
password_entry.grid(row=2, column=1, padx=5, pady=5)

# Frame for Checkpoint WiFi parameters
checkpoint_params_frame = tk.Frame(root)
checkpoint_params_frame.grid(row=3, column=0, padx=10, pady=5, sticky="w")

checkpoint_label = tk.Label(checkpoint_params_frame, text="Checkpoint WiFi Name to set:")
checkpoint_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
checkpoint_entry = tk.Entry(checkpoint_params_frame, width=30)
checkpoint_entry.grid(row=0, column=1, padx=10, pady=5)

# Frame for headless mode
headless_frame = tk.Frame(root)
headless_frame.grid(row=4, column=0, padx=10, pady=5, sticky="w")

headless_label = tk.Label(headless_frame, text="Browser Mode:")
headless_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

headless_mode = tk.BooleanVar(value=True) # Sets headless to True by default

headless_radio = tk.Radiobutton(headless_frame, text="Headless", variable=headless_mode, value=True)
headless_radio.grid(row=0, column=1, padx=5, pady=5, sticky="w")

visible_radio = tk.Radiobutton(headless_frame, text="Visible", variable=headless_mode, value=False)
visible_radio.grid(row=0, column=2, padx=5, pady=5, sticky="w")


# Run button
run_button = tk.Button(
    root, 
    text="Run", 
    command=lambda: start_configuration(
        text_output, 
        ssid_entry.get().strip(), 
        password_entry.get().strip(),
        checkpoint_entry.get().strip(),
        headless_mode.get()
    )
)
run_button.grid(row=5, column=0, columnspan=2, pady=10)

# Output area
text_output = scrolledtext.ScrolledText(root, width=60, height=15, wrap=tk.WORD)
text_output.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

print(Thread.__version__)
print(tk.__version__)

# Start the GUI
root.mainloop()