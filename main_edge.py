import tkinter as tk
from tkinter import scrolledtext, messagebox
from threading import Thread
# from wifi_connection import connect_to_wifi
from WebDriverEdge import set_up_edge_web_driver 
from print_gui import print_to_gui
from config import configure_checkpoint 

def configure_routers(text_output, checkpoint_wifi_name, headless_mode):
    """
    Configures the selected Checkpoint router using the Edge WebDriver.
    """
    print_to_gui("Starting the router configuration process...", text_output)

    try:
        # Connect to router with internet
        # connect_to_wifi(router_with_internet, text_output)
        
        # Call the dedicated Edge setup function
        driver = set_up_edge_web_driver(headless=headless_mode)
        print_to_gui("Edge WebDriver is running", text_output)

        # Start configuration for the Checkpoint router
        print_to_gui(f"Starting configuration for {checkpoint_wifi_name}", text_output)
        configure_checkpoint(driver, text_output, checkpoint_wifi_name)
            
        driver.quit()
        
    except Exception as e:
        print_to_gui(f"An error occurred: {e}", text_output)

def start_configuration(text_output, checkpoint_wifi_name, headless_mode):
    """
    Starts the configuration process in a separate thread.
    """
    # Start the configuration in a separate thread
    thread = Thread(target=configure_routers, args=(text_output, checkpoint_wifi_name, headless_mode))
    thread.start()


# GUI setup
root = tk.Tk()
root.title("Checkpoint Configuration - Edge Only")

# # Frame for router with Internet parameters (Row 0)
# router_params_frame = tk.Frame(root)
# router_params_frame.grid(row=0, column=0, padx=10, pady=5, sticky="w")

# router_label = tk.Label(router_params_frame, text="Parameters for router with Internet (SSID, Password):")
# router_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# ssid_entry = tk.Entry(router_params_frame, width=30)
# tk.Label(router_params_frame, text="SSID:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
# ssid_entry.grid(row=1, column=1, padx=5, pady=5)

# password_entry = tk.Entry(router_params_frame, show="*", width=30)
# tk.Label(router_params_frame, text="Password:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
# password_entry.grid(row=2, column=1, padx=5, pady=5)

# Frame for Checkpoint WiFi parameters (Row 1)
checkpoint_params_frame = tk.Frame(root)
checkpoint_params_frame.grid(row=1, column=0, padx=10, pady=5, sticky="w") 

tk.Label(checkpoint_params_frame, text="Checkpoint WiFi Name to set:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
checkpoint_entry = tk.Entry(checkpoint_params_frame, width=30)
checkpoint_entry.grid(row=0, column=1, padx=10, pady=5)

# Frame for headless mode (Row 2)
headless_frame = tk.Frame(root)
headless_frame.grid(row=2, column=0, padx=10, pady=5, sticky="w") 

tk.Label(headless_frame, text="Browser Mode (Edge):").grid(row=0, column=0, padx=10, pady=5, sticky="w")

headless_mode = tk.BooleanVar(value=True) 

tk.Radiobutton(headless_frame, text="Headless", variable=headless_mode, value=True).grid(row=0, column=1, padx=5, pady=5, sticky="w")
tk.Radiobutton(headless_frame, text="Visible", variable=headless_mode, value=False).grid(row=0, column=2, padx=5, pady=5, sticky="w")


# Run button (Row 3)
run_button = tk.Button(
    root, 
    text="Run", 
    command=lambda: start_configuration(
        text_output, 
        #ssid_entry.get().strip(), 
        #password_entry.get().strip(),
        checkpoint_entry.get().strip(),
        headless_mode.get() 
    )
)
run_button.grid(row=3, column=0, columnspan=2, pady=10) 

# Output area (Row 4)
text_output = scrolledtext.ScrolledText(root, width=60, height=15, wrap=tk.WORD)
text_output.grid(row=4, column=0, columnspan=2, padx=10, pady=5) 

root.mainloop()