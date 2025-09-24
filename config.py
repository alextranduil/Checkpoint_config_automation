import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from ChromeWebDriver import set_up_chrome_web_driver
from print_gui import print_to_gui
import tkinter as tk
from tkinter import scrolledtext

def configure_checkpoint(driver, text_output, wifi_name='Checkpoint'):
    """
    Automatically configures a Checkpoint router.

    Args:
        driver: The Chrome WebDriver instance.
        text_output: The object for displaying text in the GUI.
        wifi_name (str): The name for the WiFi network.
    """
    
    ROUTER_IP = "192.168.10.1"
    ADMIN_PASSWORD = 'admin' # change
    WIFI_NAME = wifi_name
    WIFI_PASSWORD = '12345678' # change
    COUNTRY = 'Ukraine'
    CLI_COMMAND = "add fw rules service any action allow src wlan dest gw forward-to undefined ports 0 protocol any qosclass Default redirectport 0 index 1 log false disabled false description \"WLAN access gateway\" time always" 
    
    try:
        # Step 1: Access the login page
        driver.get(f"http://{ROUTER_IP}/")
        time.sleep(3)
        print_to_gui("Step 1: Opened the login page.", text_output)

        # Step 2: Enter password and log in
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "swpassword"))
        )
        password_field.send_keys(ADMIN_PASSWORD)
        print_to_gui("Password entered.", text_output)
        
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "swconfirmpassword"))
        )
        password_field.send_keys(ADMIN_PASSWORD)
        print_to_gui("Password confirmed.", text_output)
        
        ok_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "frstok"))
        )
        ok_button.click()
        print_to_gui("Step 2: Logged in successfully.", text_output)
        time.sleep(1)

        driver.get(f"http://{ROUTER_IP}/Network_Int.html")
        time.sleep(2)
        print_to_gui("Navigated to the Network page.", text_output)

        edit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@onclick='editNet(3);']"))
        )
        edit_button.click()
        print_to_gui("Clicked the Edit (editNet(3)) button.", text_output)
        time.sleep(1)
        
        # Get the original window handle
        main_window_handle = driver.current_window_handle
        
        ok_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "ntwkwiz"))
        )
        ok_button.click()
        print_to_gui("WiFi Wizard is opened.", text_output)
        time.sleep(2)

        # Switch focus to the new window
        for window_handle in driver.window_handles:
            if window_handle != main_window_handle:
                driver.switch_to.window(window_handle)
                break
        
        # Switch to the frame inside the new window
        print_to_gui("Switching to the 'popmain' frame...", text_output)
        driver.switch_to.frame("popmain")
        print_to_gui("Focus switched to frame. Filling out the form...", text_output)
        time.sleep(1)
        
        # Step 1: Check the checkbox
        print_to_gui("Step 1: Checking the 'Enable wireless networking' checkbox...", text_output)
        checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "tnetmode"))
        )
        if not checkbox.is_selected():
            checkbox.click()
        print_to_gui("Checkbox checked.", text_output)
        time.sleep(1)

        # Step 2: Set network name value
        print_to_gui("Step 2: Setting the network name...", text_output)
        network_name_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "tnetwname"))
        )
        network_name_field.clear()
        network_name_field.send_keys(WIFI_NAME)
        print_to_gui(f"Network name '{WIFI_NAME}' set.", text_output)
        time.sleep(1)
        
        # Step 3: Select the country from the dropdown
        print_to_gui(f"Step 3: Selecting '{COUNTRY}' from the country dropdown...", text_output)
        country_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "tnetwcountry"))
        )
        select = Select(country_dropdown)
        select.select_by_visible_text(COUNTRY)
        print_to_gui(f"Country '{COUNTRY}' selected.", text_output)
        time.sleep(1)

        # Step 4: Click the first Next button
        print_to_gui("Step 4: Clicking the 'Next' button...", text_output)
        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "wiznext"))
        )
        next_button.click()
        print_to_gui("Next button clicked.", text_output)
        time.sleep(2)

        # Step 5: Check the radio button for Bridge Mode
        print_to_gui("Step 5: Selecting 'Bridge Mode'...", text_output)
        bridge_mode_radio = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//td[text()='Bridge Mode']/preceding-sibling::td/input[@type='radio']"))
        )
        bridge_mode_radio.click()
        print_to_gui("'Bridge Mode' selected.", text_output)
        time.sleep(1)
        
        # Step 6: Click the second Next button
        print_to_gui("Step 6: Clicking the next 'Next' button...", text_output)
        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "wiznext"))
        )
        next_button.click()
        print_to_gui("Next button clicked.", text_output)
        time.sleep(2)
        
        # Step 7: Set the pre-shared key value
        print_to_gui("Step 7: Setting the pre-shared key...", text_output)
        psk_key_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "tnetwpskkey"))
        )
        psk_key_field.clear()
        psk_key_field.send_keys(WIFI_PASSWORD)
        print_to_gui(f"Key value '{WIFI_PASSWORD}' set.", text_output)
        time.sleep(1)
        
        # Step 8: Click the third Next button
        print_to_gui("Step 8: Clicking the next 'Next' button...", text_output)
        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "wiznext"))
        )
        next_button.click()
        print_to_gui("Next button clicked.", text_output)
        time.sleep(2)
        
        # Step 9: Click the fourth Next button
        print_to_gui("Step 9: Clicking the final 'Next' button...", text_output)
        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "wiznext"))
        )
        next_button.click()
        print_to_gui("Next button clicked.", text_output)
        time.sleep(2)

        # Step 10: Click the Finish button
        print_to_gui("Step 10: Clicking the 'Finish' button...", text_output)
        finish_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "wizcancel"))
        )
        finish_button.click()
        print_to_gui("Finish button clicked. Waiting for process to complete...", text_output)
        time.sleep(3)
        
        # Return to the main window
        driver.switch_to.window(main_window_handle)
        
        # Step 11: Go to the CLI page
        print_to_gui("Step 11: Navigating to the CLI page...", text_output)
        driver.get(f"http://{ROUTER_IP}/Tools_Cli.html")
        time.sleep(2)
        
        # Step 12: Set the CLI command and click 'Go'
        print_to_gui("Step 12: Entering the CLI command...", text_output)
        cli_command = CLI_COMMAND
        cli_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "cmd"))
        )
        cli_input.clear()
        cli_input.send_keys(cli_command)
        time.sleep(2)
        
        go_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "cli"))
        )
        go_button.click()
        print_to_gui("CLI command sent.", text_output)
        time.sleep(1)
        print_to_gui(f"Configuration process for {WIFI_NAME} is completed!", text_output)

    except Exception as e:
        print_to_gui(f"An error occurred: {e}", text_output)


if __name__ == "__main__":
    driver = set_up_chrome_web_driver(headless=True)
    root = tk.Tk()
    text_output = scrolledtext.ScrolledText(root, width=60, height=15, wrap=tk.WORD) # placeholder for text output - no messages
    WIFI_NAME = "Checkpoint8"
    configure_checkpoint(driver, text_output, WIFI_NAME)