import datetime
import platform
import subprocess
import sys
import requests
import logging
import os

logging.basicConfig(filename='nessus_backup.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

# Function to validate the current Python version.
# Ensuring up-to-date software is a critical aspect of cybersecurity.
# This function enforces the use of the latest Python version; it halts program execution otherwise.
def check_python_version():
    current_version = platform.python_version()
    print(f"Your current Python version is {current_version}")
    url = "https://endoflife.date/api/python.json"
    try:
        response = requests.get(url)
        data = response.json()
        latest_version = data[0]["latest"]
        print(f"The latest version of Python is {latest_version}")
        if current_version != latest_version:
            print("Your version of Python is out of date. Please update before running any scripts.")
            logging.error(f'FAILED: Python version {current_version} needs to be updated to {latest_version}.')
            # If your computer doesn't have the latest Python version, raise sys.exit() to terminate the script.
            sys.exit(1)
        else:
            logging.info('Your version of Python is up to date')
    except requests.exceptions.RequestException as e:
        logging.error('Python version validation failed.')
        # If the function doesn't execute properly, raise sys.exit() to terminate the script.
        sys.exit(1)

# Function to create a backup configuration file for your Nessus environment.
def backup():
    # Update this path if Nessus is installed in a different location on your machine.
    path = r"C:\Program Files\Tenable\Nessus"
    
    #This try/except is used to catch where or not the path provided above exists on your machine.
    try:
        os.chdir(path)
    except OSError:
        logging.error(f'FAILED TO FIND: {path}.')
        return
    
    # Customize the backup name. The current name includes a formatted date for tracking.
    backup_name = "Tenable_Nessus_Backup" + datetime.datetime.now().strftime("%m-%d-%y")
    
    # Do not modify the backup command; it's from the documentation at docs.tenable.com.
    backup_command = f"nessuscli backup --create \"{backup_name}\""
    
    # Use subprocess to run the backup command via the command-line interface. Run this script with elevated privileges.
    backup_process = subprocess.run(backup_command, shell=True)
    
    try:
        backup_process = subprocess.run(backup_command, shell=True, stderr=subprocess.PIPE, text=True)
        
        if backup_process.returncode != 0:
            logging.error(f'FAILED: {backup_command}. Error: {backup_process.stderr}')
        else:
            logging.info(f'SUCCESS: {backup_command}')
    except subprocess.CalledProcessError as e:
        logging.error(f'FAILED: {backup_command}. Error: {e.stderr}')

def main():
    check_python_version()  # Check the Python version
    backup()  # Perform the backup of Tenable Nessus.

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
