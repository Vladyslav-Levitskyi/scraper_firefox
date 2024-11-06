# Automated Anonymity Parser

This project is designed to automate the process of saving and parsing web pages using Selenium and BeautifulSoup. It allows you to save web pages locally and scrape data from them automatically with authorization capabilities and a wide range of user-interaction simulations.

## Getting Started

To start working with the Automated Anonymity Parser, follow these steps:

1. **Run the `searcher_se.py` script** to save the HTML skeleton of target web pages. This script uses Selenium to automate actions on a website, including authentication and interaction with page elements.
   
   Output: A `source_file` containing the saved web page skeletons.

2. **Run the `scraper_bs.py` script** to parse the saved HTML and extract text data.

   Output: A JSON file (`product_file.json`) containing the structured data in text format.

## Code Overview

### `searcher_se.py`
- **Purpose**: Automates the process of loading and saving HTML content from web pages.
- **Functions**: Uses Selenium to interact with web pages, providing features like login automation, element input, drag and drop, clicks, and more to act like a real user.
  
### `scraper_bs.py`
- **Purpose**: Parses the saved HTML files, extracts specific data using BeautifulSoup, and stores it in a structured JSON format.

### Selenium Interaction Capabilities
With Selenium, this script can:
- Automate logins and other forms of user authentication
- Fill in input fields, drag and drop elements, perform clicks, double-clicks, long-press actions, and other user interactions
- Create automated action chains to perform complex sequences of actions

## Libraries Used

- **Selenium**: To interact with and automate actions on web pages.
- **BeautifulSoup**: For parsing HTML and extracting text data from saved pages.
- **JSON**: To store and organize parsed data.

## Usage Notes

- Ensure that you have set up the necessary web driver (e.g., ChromeDriver) for Selenium.
- Make sure to configure any required credentials or environment variables for secure access to web pages.
  
## Requirements

- Python 3.x
- Install dependencies:
  ```bash
  pip install -r requirements.txt

## License

MIT

## Copyright

(c) 11-2024 Vladyslav Levytskyi