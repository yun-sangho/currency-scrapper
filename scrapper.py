from selenium import webdriver
from dotenv import load_dotenv
import re
import os

"""
환율 날짜 정보를 날짜 선택 창에서 가지고옵니다.
"""
def parse_date(driver):
    date_input = driver.find_element_by_id("searchDate")
    date = date_input.get_attribute("value")
    date = date.replace('.', '-')

    return date

"""
환율 정보를 환율 테이블에서 가지고옵니다.
"""
def parse_currency_data(driver):
    currency_data = []
    date = parse_date(driver)

    # parse currency talbes
    tables = driver.find_elements_by_class_name("table_type7")

    for table in tables:
        # parse table body form the table
        body = table.find_element_by_tag_name("tbody")

        # parse rows from the table body
        rows = body.find_elements_by_tag_name("tr")

        for row in rows:
            columns = row.find_elements_by_tag_name("td")

            # create an array that has date, acronym and rate
            # [date, acronym, rate]
            data = [
                date,
                # parse an acronym from the string
                re.findall(r"(?<=\()([A-Z]*)(?=\))", columns[0].text)[0],
                columns[1].text,
            ]

            currency_data.append(data)

    return currency_data

def run_scrapper():
    print("스크래핑을 시작합니다.")

    SCRAP_URL = os.getenv('SCRAP_URL')
    CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')

    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver.get(SCRAP_URL)
    driver.implicitly_wait(100)

    try:
        alret = driver.switch_to.alert
    # if there is not an alret window, parse currency data
    except Exception as e:
        print(e)
        
        alret.accept()
        driver.implicitly_wait(500)

        data = parse_currency_data(driver)        
    # if there is, do not parse data
    else:
        data = None

    driver.quit()
    print('스크래핑이 완료되었습니다.')

    return data