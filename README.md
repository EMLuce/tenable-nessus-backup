# Project Title

Tenable Nessus Configuration Backup Script.

## Description

A straightforward script designed to automate the process of backing up your Tenable Nessus configuration. The goal is to employ task scheduling to run the script as needed according to the specific requirements of your organization.

## Getting Started

### Dependencies

Operating System: The script is primarily intended for Windows operating systems. It has been tested and verified to work on Windows 10.

Python: Ensure you have Python 3.x installed on your system. You can download the latest version of Python from the official website: https://www.python.org/downloads/

Python Packages: The script requires the requests library to retrieve data from an external API. You can install this library using the following command: pip install requests

Elevated Privileges: To perform the Nessus backup and to execute some system commands, the script requires elevated (administrative) privileges. Make sure you run the script with administrative privileges.

Nessus Installation: The script assumes you have Nessus installed on your system. You should update the path variable in the script to point to the correct installation path of Nessus on your machine.

### Installing

You're welcome to install and use my repository in any way that suits your needs. To clone the repository, simply execute the command: git clone https://github.com/emluce/tenable-nessus-backup.git

### Executing program

Once you have the script installed on your device you can simply execute the

## Help

Python Version Mismatch:

    Issue: The script requires a specific Python version, and you may encounter errors if your version is incompatible.
    Solution: Make sure you have Python 3.x installed and that the script is executed using the correct version. Use the python --version command to verify your Python version.

Missing Dependencies:

    Issue: The script uses external libraries, and you might face errors if these dependencies are missing.
    Solution: Install the required dependencies using the pip install -r requirements.txt command within your virtual environment.

Nessus Path Incorrect:

    Issue: The script assumes a specific path for the Nessus installation directory.
    Solution: Modify the path variable in the script (inside the backup() function) to match the actual installation path of Nessus on your system.

Insufficient Privileges:

    Issue: Certain operations, such as the Nessus backup, require administrative privileges.
    Solution: Run the script as an administrator. Right-click on the terminal/command prompt and select "Run as administrator."

Network Connection Issues:

    Issue: The script fetches data from an external API, and network issues could prevent successful execution.
    Solution: Ensure you have a stable internet connection. If you encounter network-related errors, try running the script again after the network connection is restored.

API Changes or Unavailability:

    Issue: The script relies on an external API for Python version validation, which could change or become temporarily unavailable.
    Solution: If you encounter errors related to the API, check its status or update the script to use an alternative source for Python version information.

If you need help, have questions, or encounter any issues beyond the common problems listed here, feel free to contact me personally at eric@lucedev.com.

## Authors

Eric Luce
Email: eric@lucedev.com
GitHub: emluce
Website: www.lucedev.com

Feel free to reach out if you have any questions, feedback, or need assistance with the script. Your inquiries are always welcome!

## Version History

v1.0 (Initial Release) - [August 2023]

Initial version of the Python script for Nessus Backup and Python Version Check.
Validates Python version and enforces the use of the latest version.
Performs backup configuration for Nessus environment.
Provides informative logging for tracking and troubleshooting.
Supports running the script within a virtual environment.
Contact author at eric@lucedev.com for questions and assistance.
