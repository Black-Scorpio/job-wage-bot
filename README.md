# Job Wage Bot

Job Wage Bot is a Python-based web scraping bot that extracts wage data for various occupations in different cities across Canada from the Job Bank website. The data is then saved into CSV files for further analysis.

## Features

- Web scraping using Selenium to gather wage data.
- Clean and convert wage data to numeric values.
- Save the cleaned data into CSV files.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Black-Scorpio/job-wage-bot.git
    cd job-wage-bot
    ```

2. Install the required libraries:
    ```bash
    pip install selenium pandas
    ```

3. Download and set up the appropriate WebDriver for your browser (e.g., ChromeDriver for Google Chrome).

## Usage

1. Run the `main.py` script:
    ```bash
    python main.py
    ```

2. Follow the prompts to enter the city name you wish to compare wages for.

3. The script will save the wage data into a CSV file named `wage_report_<city_name>.csv`.

## Example

```bash
$ python main.py
Which city in Canada would you like to compare wages on? Ottawa
Data has been saved to wage_report_ottawa.csv

Use explore_data.py to manipulate and explore data within your csv.