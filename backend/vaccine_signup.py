from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

data = pd.DataFrame(columns=['phone_number', 'contact', 'positive_test', 'symptoms', 
'signup_type', 'vaccine_site',
'age', 'teacher', 'vaccine_date', 'name', 'birth_date', 'gender', 'address', 'email', 'coverage'])
data = data.append({'phone_number': "1234561234", 'positive_test': "No", 'contact': "No",
                    'symptoms': "No", 'signup_type': 1, 'age': 20, 
                    'vaccine_site': "CVS", 'teacher': "No", 'vaccine_date': "today", 
                    'name': "John Doe", 'birth_date': "1/2/2001", 'gender': "Male",
                     'address': "456 Street Drive", 'email': "N/A", 'coverage': "none"}, ignore_index=True)

print(data)
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

driver.get("http://localhost:3000/")

input_elements = driver.find_elements_by_tag_name("input")
print(input_elements)
print(len(input_elements))
print(len(data.columns))
print(data.columns)
row = data.iloc[0].to_dict()
print(row)
for i in row:
    input_element = driver.find_element_by_id(i)
    input_element.send_keys(row[i])
submit_button = driver.find_element_by_id("submit")
submit_button.click()

information = []
for id in ["visit_type", "date", "location", "csn"]:
    information.append(driver.find_element_by_id(id).get_attribute("innerHTML").replace("</b>", "").replace("<b>", ""))

all_information = "\n".join(information)
print(all_information)