# Dollar and Petrol Price Alert System
## Project Overview
This project is a Python-based alert system that monitors the dollar to PKR exchange rate and petrol prices. If the current rate drops below the previous recorded rate, the system sends an email notification. The project uses web scraping to get the current rates and sends emails using the SMTP protocol.

## Features
- Monitor Dollar to PKR Exchange Rate: Scrapes the current exchange rate from Google search results.
- Monitor Petrol Prices: Scrapes the current petrol price from the PSO website.
- Email Notifications: Sends an email notification if the current rate is lower than the previously recorded rate.
- Persistence: Stores the previous rates in text files for comparison.
## Technology Stack
- Programming Language: Python
- Libraries:
  - os for environment variable management
  - smtplib for sending emails
  - email.message for creating email messages
  - dotenv for loading environment variables from a .env file
  - BeautifulSoup for web scraping
  - requests for making HTTP requests
## Setup Instructions
### Prerequisites
- Python 3.8+
- Required Python libraries (smtplib, email, dotenv, bs4, requests)
## Installation
1. Clone the repository:
   ```bash
    git clone https://github.com/Ahmad1015/Dollar-and-Petrol-Price-Alert-System.git
    cd dollar-petrol-price-alert
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
    ```
3. Set up environment variables:
Create a .env file in the root directory and add your email credentials:
```bash
send_email_from=your_email@gmail.com
EMAIL_PASSWORD=your_email_password
send_email_to=recipient_email@gmail.com
```
4. Create initial rate files:
Create dollar_rate.txt and petrol_rate.txt in the root directory and initialize them with the current rates.
## Usage
1. Run the main script:
```bash
python main.py
```
2. Functionality:
- The script will scrape the current dollar and petrol rates.
- It will compare the current rates with the previously recorded rates.
- If the current rate is lower than the previous rate, an email notification will be sent.

## Project Structure
- main.py: The main script that runs the program.
- requirements.txt: Contains the list of required Python packages.
- .env: Environment variables for email credentials (not included in the repo).
- dollar_rate.txt: Stores the previously recorded dollar rate.
- petrol_rate.txt: Stores the previously recorded petrol price.
## License
This project is licensed under the MIT License.

