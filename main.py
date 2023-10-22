#installing libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl

# Parsing through starting page
base_url = 'https://agmarknet.gov.in/PriceAndArrivals/CommodityWiseDailyReport.aspx'


# Initialize a webdriver (make sure you have the appropriate driver for your browser)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://agmarknet.gov.in/PriceAndArrivals/CommodityWiseDailyReport.aspx")

# Locate the dropdown menu by its HTML element ID (or other locator)
dropdown = Select(driver.find_element("id","cphBody_drpDwnYear"))

# Select an item by its visible text
item_to_select = "2020"  # Replace with the text of the item you want to select
dropdown.select_by_visible_text(item_to_select)

wait = WebDriverWait(driver,10)

# date = wait.until(EC.presence_of_element_located((By.LINK_TEXT,'4')))
# date.click()

time.sleep(15)
date = driver.find_element(By.LINK_TEXT,'4')
date.click()

submit = wait.until(EC.presence_of_element_located((By.ID, "cphBody_Submit_list")))
submit.click()
# submit = driver.find_element(By.ID, "cphBody_Submit_list")
# submit.click()
# time.sleep(15)

checkbox = wait.until(EC.presence_of_element_located((By.ID, "cphBody_GridView1_RowLevelCheckBox_3")))

# checkbox = driver.find_element(By.ID, "cphBody_GridView1_RowLevelCheckBox_3")
checkbox.click()

# submit_2 = driver.find_element(By.ID, "cphBody_btnSubmit")
submit_2 = wait.until(EC.presence_of_element_located((By.ID, "cphBody_btnSubmit")))
submit_2.click()

# time.sleep(15)

# Find the table element by its ID, class name, or other appropriate method
table = wait.until(EC.presence_of_element_located((By.ID, "cphBody_DivExport")))
# table = driver.find_element(By.ID, "cphBody_DivExport")

# Find all rows in the table
rows = table.find_elements(By.TAG_NAME, "tr")

data = []

# Loop through rows and extract data from cells
for row in rows[1:]:
    # Find cells in the current row
    cells = row.find_elements(By.TAG_NAME, "td")

    # Extract data from each cell and store it in a list
    row_data = [cell.text for cell in cells]
    data.append(row_data)

# Create a Pandas DataFrame from the extracted data
agMarketData = pd.DataFrame(data)

# Print the DataFrame
print(agMarketData)
filename = "agMark_Data.xlsx"
agMarketData.to_excel(filename, index=False)

# Remember to close the WebDriver when you're done
driver.quit()
