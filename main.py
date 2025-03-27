from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, json

cService = webdriver.ChromeService()

driver = webdriver.Chrome(service=cService)

driver.get('https://app.revpanda.com/')

email_input = driver.find_element(By.NAME, "email")

email_input.send_keys("rus@lo-k.com")

pass_input = driver.find_element(By.NAME, "password")

pass_input.send_keys("@Kv8PjnSgKCehs")

submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

submit_button.click()

time.sleep(10)

driver.get("https://app.revpanda.com/links")

time.sleep(5)
while True:
    rows = driver.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        datum = []
        tds = row.find_elements(By.TAG_NAME, 'td')

        for index, td in enumerate(tds):
            if index == 1:
                try:
                    element = td.find_element(By.TAG_NAME, 'div').find_element(By.TAG_NAME, 'div').find_element(By.TAG_NAME, 'div').find_element(By.TAG_NAME, 'button').find_element(By.TAG_NAME, 'div')

                    datum.append(element.get_attribute('innerHTML'))
                except:
                    break

            if index == 2:
                element = td.find_element(By.TAG_NAME, 'span')
                datum.append(element.get_attribute('innerHTML'))
            
            if index == 6 or index == 7 or index == 11 or index == 13:
                datum.append(td.get_attribute('innerHTML'))
            
            if index == 8:
                new_svgs = []
                svgs = td.find_element(By.TAG_NAME, 'div').find_element(By.TAG_NAME, 'div').find_elements(By.TAG_NAME, 'svg')
                for svg in svgs:
                    new_svgs.append(f"'''{svg}'''")
                datum.append(new_svgs)
            
            if index == 5:
                try:
                    datum.append(f"'''{td.find_element(By.TAG_NAME, 'svg')}'''")
                except:
                    break
            
        if len(datum) != 0:
            with open("data.json", 'r') as json_file:
                existing_data = json.load(json_file)

            existing_data.append(datum)

            with open("data.json", 'w') as json_file:
                json.dump(existing_data, json_file, indent=4)

        span_element = driver.find_element(By.CSS_SELECTOR, "span.relative.z-0.inline-flex.rounded-md.shadow-sm")
        last_span = span_element.find_elements(By.TAG_NAME, 'span')[-1]
        next_but = last_span.find_element(By.TAG_NAME, 'button')
        next_but.click()

        time.sleep(2)
