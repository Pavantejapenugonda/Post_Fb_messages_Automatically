from common_operations import *
from bs4 import BeautifulSoup

driver = login_fb("learnerzworld@gmail.com","Pavani@99")
driver.get("https://www.facebook.com/groups/")
driver.find_element_by_xpath("//span[text()='See more']").click()
soup = BeautifulSoup(driver.page_source, 'html.parser')
for ele in soup.find_all('a',class_='_2yau'):
    print(ele.get('href'))