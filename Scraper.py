from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
# Create a list to store the scraped data
data = []

# Get user input for state and number of pages
s = input("Enter the state (e.g., Louisiana): ")
p = int(input("Enter the number of pages to scrape: "))

# Initialize the web driver
driver = webdriver.Chrome()

# Iterate through the first 3 pages
for i in range(1,p):
    if i == 1:
        driver.get(f"https://www.land.com/{s}/all-land/")
    else:
        driver.get(f"https://www.land.com/Louisiana/all-land/page-{i}/")
    
    time.sleep(3)  # Allow some time for the page to load

    # Get the list of land listings
    lands = driver.find_elements(By.XPATH, '//*[@id="placard-info"]')

    # Iterate through each land listing
    for land in lands:
        try:
            price = land.find_element(By.XPATH, './/div[1]/div[1]/div[1]/a/span[1]').text
            acres = land.find_element(By.XPATH, './/div[1]/div[1]/div[1]/a/span[3]').text
            address = land.find_element(By.CLASS_NAME,'af8d6').text
            seller = land.find_element(By.XPATH,'//*[@id="placard-broker"]/div[2]/a/div[1]').text
            data.append({'Price': price, 'Acres': acres,'Address': address, 'Seller': seller})
        except Exception as e:
            print(f"An error occurred: {e}")

# Close the web driver
driver.quit()

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame as a table
print(df)

# Save the DataFrame to a CSV file
df.to_csv(f'{s} land_listings.csv', index=False)
