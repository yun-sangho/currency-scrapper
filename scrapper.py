from selenium import webdriver
import re

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

    options = webdriver.ChromeOptions()

    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-infobars")
    options.add_argument("--no-sandbox")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--enable-logging")
    options.add_argument("--log-level=0")
    options.add_argument("--single-process")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--homedir=/tmp")
    options.binary_location = "./bin/headless-chromium"

    driver = webdriver.Chrome(
        "./bin/chromedriver",
        chrome_options=options)
    driver.get('http://www.smbs.biz/ExRate/TodayExRate.jsp')
    driver.implicitly_wait(100)

    try:
        driver.switch_to.alert
    # if there is not an alret window, parse currency data
    except Exception as e:
        print(e)
        data = parse_currency_data(driver)        
    # if there is, do not parse data
    else:
        data = None

    driver.quit()
    print('스크래핑이 완료되었습니다.')

    return data