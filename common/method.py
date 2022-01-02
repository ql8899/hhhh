

import time

def login(driver,name,passw):
    driver.get("http://erp.lemfix.com/login.html")
    driver.find_element_by_id("username").send_keys(name)
    driver.find_element_by_id("password").send_keys(passw)
    driver.find_element_by_id("btnSubmit").click()
    uname = driver.find_element_by_xpath("//p").text
    return uname

# def search(driver,key,name,passw):
#     login(driver,name,passw)
#     driver.find_element_by_xpath('//span[text()="零售出库"]').click()
#     time.sleep(2)
#     id = driver.find_element_by_xpath("//div[text()="零售出库"]/..").get_attribute("id")
#     frameid = id + "-frame"
#     driver.switch_to.frame(driver.find_element_by_xpath(f"//iframe[@class='{frameid}']"))
#     driver.find_element_by_id("serachNumber").send_keys(key)
#     driver.find_element_by_id("searchBtn").click()
#     time.sleep(2)  # 隐式等待+强制等待
#     num = driver.find_element_by_xpath("//tr[@id="datagrid-ro-r1-2-0"]//td[@field="number"]/div").text
#     return num
