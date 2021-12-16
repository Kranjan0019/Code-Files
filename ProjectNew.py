from selenium import webdriver
import time
driver=webdriver.Chrome("C://Users//rajee//OneDrive//Desktop//chromedriver.exe")
driver.get("http://www.durgasoft.com/registration.asp")
driver.maximize_window()
assert "DURGA" in driver.title
driver.find_element_by_id("name").send_keys("Rajeev")
'''
time.sleep(2)
driver.find_element_by_id("ph_no").send_keys("7584736571")
a=driver.find_element_by_xpath("//*[@value='Student']") 
print (a.is_selected())
a.click()
print (a.is_selected())
driver.find_element_by_xpath("//*[@value='Employed']").click()
print (a.is_selected())
'''

'''
time.sleep(2)
driver.find_element_by_xpath("//input[@value='Student']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='CORE_JAVA']").click()
driver.find_element_by_xpath("//*[@id='SPRING']").click()
time.sleep(2)
driver.find_element_by_id("date").send_keys("15 July")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='time']").send_keys("10:00am")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='desc']").send_keys("This class is important for me.")
driver.find_element_by_xpath("//a[text()='HOME']").click()
time.sleep(5)
driver.back()

'''