from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException
import os 

# Define the expected driver file path
DRIVER_FILE_NAME = "msedgedriver.exe"
# Construct the path relative to the script
DRIVER_DIR = "drivers"


def get_edge_driver_path():
    """
    Checks for the msedgedriver.exe executable in the required drivers folder.
    """
    driver_path = os.path.join(DRIVER_DIR, DRIVER_FILE_NAME)
    
    if os.path.exists(driver_path):
        print(f"msedgedriver.exe found at: {driver_path}")
        return driver_path
    
    # Critical error if the driver is not found
    error_msg = (
        "CRITICAL ERROR: Edge WebDriver not found. "
        f"Please ensure you have manually downloaded 'msedgedriver.exe' (compatible with your Edge version) "
        f"and placed it inside the required project folder: '{DRIVER_DIR}'"
    )
    raise WebDriverException(error_msg)


def set_up_edge_web_driver(headless=True):
    """
    Sets up and returns a Microsoft Edge WebDriver instance using Selenium 4+ syntax
    by using a pre-installed driver executable path.

    Args:
        headless (bool): If True, the browser runs in headless mode.

    Returns:
        webdriver: The initialized Edge WebDriver instance.
    """
    
    # 1. Get the path to the local driver file
    driver_executable_path = get_edge_driver_path()
    
    # Arguments to be applied to Options object
    common_args = ["--no-sandbox"]
    if headless:
        # Use 'new' for modern, reliable headless mode
        common_args.extend(["--headless=new", "--disable-gpu", "--window-size=1920,1080"]) 

    try:
        print("Attempting to set up Microsoft Edge WebDriver (Local File)...")
        
        options = EdgeOptions()
        for arg in common_args:
            options.add_argument(arg)
            
        # FIX: Create the EdgeService object using the local driver executable path
        service = EdgeService(driver_executable_path)
        
        # Initialize the Edge WebDriver using the modern 'service' keyword
        driver = webdriver.Edge(service=service, options=options) 

        return driver

    except SessionNotCreatedException as e:
        error_msg = (
            "Failed to start Edge driver. Ensure the 'msedgedriver.exe' file in the 'drivers' folder "
            "is the correct version compatible with your Microsoft Edge browser. "
            f"Original Error: {e}"
        )
        raise WebDriverException(error_msg) from e
        
    except Exception as e:
        error_msg = (
            "An unexpected error occurred during Edge setup. "
            f"Original Error: {e}"
        )
        raise WebDriverException(error_msg) from e