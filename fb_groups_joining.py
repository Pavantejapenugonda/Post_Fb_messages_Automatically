from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from common_operations import *


def adding_group(keyword):
    driver = login_fb("cookingworld96@gmail.com","Pavani@99")
    keyword_search_url = "https://www.facebook.com/search/groups/?q={}&epa=SERP_TAB".format(keyword)
    driver.get(keyword_search_url)
    time.sleep(3)
    elements = driver.find_elements_by_xpath("//a[text()='Join']")
    print(elements)
    for ele in elements:
        print(ele)
        ele.click()
        time.sleep(3)
        try:
            driver.find_elements_by_xpath("//div[text()='Join Group']")[0].click()
            time.sleep(2)
            print("Group added")
        except:
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(2)
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            # cancel_ele = driver.find_elements_by_xpath("//span[text()='Close']")
            # print(cancel_ele)
            # print(len(cancel_ele))
            # cancel_ele[len(cancel_ele)-1].click()
            # time.sleep(2)
            # cancel_ele[len(cancel_ele)-1].click()
            print("Group not added")
            time.sleep(2)
            

# if __name__ == "__main__": 
#     adding_group("Cooking") 

