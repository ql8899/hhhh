
from selenium import webdriver
from common import method
from testdata import data   #从包里导入

driver = webdriver.Chrome()
driver.implicitly_wait(10)
name = data.test_data["name"]
passw = data.test_data["passw"]

uname = method.login(driver,name,passw)   # 调用导入包里的方法
if uname=="测试用户":
    print(f"登录用户是{uname}")
else:
    print("用例失败")