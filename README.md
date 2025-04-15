# Track Target Location on Ome TV

This script is used to detect and retrieve geographical location information from an IP address, including continent, country, region, city, ISP, and geographical coordinates. The data is fetched from an external API and displayed in a human-readable format.

Features:
- Detects IP addresses from input strings.
- Retrieves geolocation information from the IP address using an API.
- Displays geographical and ISP information for the given IP address.

Prerequisites:
Before running the script, make sure you have installed the following dependencies:

- Python 3.x
- requests module
- re module
- json module
- os module
- http.client module
- urllib module

To install the required dependencies, run the following command:
pip install requests

How to Use:
- Run the script using Python:
  python located.py
- Enter an input containing the IP address or a string that includes an IP address found via inspect.
- The script will search for the IP address in the input and display the related location information.

Output:
The displayed information includes:
- IP Address
- Continent
- Country
- Region
- City
- ISP
- Latitude and Longitude
- Response time (ms)
