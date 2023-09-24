# Shodan Command-Line Automation Tool
The Shodan Command-Line Automation Tool is a Python script that allows you to easily perform Shodan searches from your Linux terminal, providing a user-friendly interface. The results of your searches are saved in a text file for further analysis. This tool simplifies the process of leveraging Shodan's powerful search capabilities for security research, bug hunting, and more.

## Prerequisites
Before using the Shodan Command-Line Automation Tool, ensure you have the following prerequisites:

- Python 3: Make sure you have Python 3 installed on your Linux system.

- Shodan API Key: Obtain a Shodan API key by signing up on the Shodan website. Replace 'YOUR_API_KEY' in the script with your actual API key.

- Dependencies: Install the required Python libraries using the following command:
```bash
pip install shodan click
```
## Usage
- Download the Script: Download the shodan_automation.py script to your Linux system.

- Run the Script: Open a terminal and navigate to the directory where the script is located. Run the script using the following command:


```bash
python3 main.py
```
- Enter Your API Key: When prompted, enter your Shodan API key. If you don't have one, you can sign up on the Shodan website to obtain it.

- Enter Your Shodan Search Query: After entering your API key, you'll be prompted to enter your Shodan search query. You can use various query parameters to narrow down your search (e.g., country:"IN" to search for results in India).

- View Results: The script will perform the Shodan search and display the total number of results found.

- Save Results: The results of your search will be saved in a text file named shodan_results.txt in the same directory where the script is located.

## Example
Here's an example of running the script:

```bash
python3 main.py
```
You will be prompted to enter your Shodan API key and your search query. The script will then execute the search, display the total results found, and save the results to shodan_results.txt.

# Responsible Use
Always use the Shodan Command-Line Automation Tool responsibly and in compliance with Shodan's terms of service and legal guidelines. Obtain proper authorization before conducting any form of information gathering, and never use the obtained information for malicious purposes.

# Disclaimer
This tool is intended for legitimate security research, network monitoring, and ethical hacking purposes. Any misuse or illegal activity conducted with this tool is the sole responsibility of the user. Use it responsibly and within the bounds of the law.





