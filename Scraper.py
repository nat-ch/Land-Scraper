from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Initialize the web driver
driver = webdriver.Chrome()

# Create a list to store the scraped data
data = []

# Iterate through the first 3 pages
for i in range(1, 4):
    if i == 1:
        driver.get("https://www.land.com/Louisiana/all-land/")
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
#df.to_csv('land_listings.csv', index=False)
#new
#new2
#new 3