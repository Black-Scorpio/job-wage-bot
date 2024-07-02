from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


def clean_wage(wage):
    """Convert wage with comma to a float with period and round to 2 decimal places."""
    try:
        return round(float(wage.replace(",", ".")), 2)
    except ValueError:
        return wage


# Ask the user for the city name
city_name = input("Which city in Canada would you like to compare wages on? ")

# Set up the WebDriver
driver = webdriver.Chrome()

try:
    # URL of the initial page
    start_url = "https://www.jobbank.gc.ca/trend-analysis/search-wages"
    driver.get(start_url)

    # Wait for the dropdown button to be clickable
    wait = WebDriverWait(driver, 10)
    dropdown_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wages-inputs"]/div[1]/div/button')))
    dropdown_button.click()

    # Select the specific option from the dropdown
    dropdown_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wages-inputs"]/div[1]/div/div/ul/li['
                                                                       '2]/a')))
    dropdown_option.click()

    # Click on a neutral part of the page to change focus
    neutral_element = driver.find_element(By.TAG_NAME, 'body')
    neutral_element.click()

    # Wait for the search box to be present
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ec-wages:regionSearchBox"]')))

    # Clear any pre-existing text in the search box
    search_box.clear()

    # Input the city name into the search box
    search_box.send_keys(city_name)

    # Click inside the input to activate the dropdown options
    search_box.click()

    # Wait for the first option in the dropdown to be clickable and click it
    first_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="wages-loc-input"]/div/span[1]/div/div/p[1]')))
    first_option.click()

    # Click the search button
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wages-loc-input"]/div/span[4]')))
    search_button.click()

    # Wait for the new page to load and the table to be present
    wait.until(EC.presence_of_element_located((By.ID, "wage-loc-report")))

    # Extract the table and data as before
    table = driver.find_element(By.ID, "wage-loc-report")

    # Extract the headers
    headers = []
    header_rows = table.find_element(By.TAG_NAME, "thead").find_elements(By.TAG_NAME, "tr")
    for row in header_rows:
        headers.extend([header.text.strip() for header in row.find_elements(By.TAG_NAME, "th")])

    # Filter relevant headers (Occupation, Low, Median, High)
    relevant_headers = ["Occupation", "Low", "Median", "High"]

    # Extract the data from the table body
    rows = table.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")
    data = []
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")
        if len(columns) >= 5:
            row_data = [
                columns[0].text.strip(),
                clean_wage(columns[1].text.strip()),
                clean_wage(columns[2].text.strip()),
                clean_wage(columns[3].text.strip())
            ]
            data.append(row_data)

    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=relevant_headers)

    # Save the DataFrame to a CSV file with the city name included
    csv_filename = f'wage_report_{city_name.replace(" ", "_").lower()}.csv'
    df.to_csv(csv_filename, index=False)
    print(f"Data has been saved to {csv_filename}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Wait for a while before closing the browser to help with debugging
    time.sleep(5)
    driver.quit()
