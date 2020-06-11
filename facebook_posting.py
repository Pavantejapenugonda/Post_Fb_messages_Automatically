from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

# text_to_post = " Learners World A new way of learning platform 📓 \n ### H Lookup in Excel ### \n Video link : https://youtu.be/xDkwrOT7nzI \n If you want be a expert in Excel Course  \n Follow us on youtube channel link : \n https://www.youtube.com/channel/UCHOEbBY8s2aBKiOSQ_NGvtQ \n Watch previous videos of Vlookup click on below links : \n ## VLookup Rules ### \n Video link : https://youtu.be/xuYvz48zeTo \n ## Vlookup Exact match ## \n Video link : https://youtu.be/tNrwzP_H-9E \n Watch more videos on below links : \n ##15+ Important Shortcuts in Excel## \n https://www.youtube.com/watch?v=jfckGiYV6_c"
text_to_post = "https://youtu.be/VTpumW-QlzM "
user_name = "cookingworld96@gmail.com"
password = "Pavani@99"
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
driver.get("https://www.facebook.com/")
driver.maximize_window()
element = driver.find_element_by_id("email")
element.send_keys(user_name)
time.sleep(2)
element = driver.find_element_by_id("pass")
element.send_keys(password)
time.sleep(2)
submit = driver.find_element_by_id("u_0_b")
time.sleep(2)
submit.click()
time.sleep(5)
group_urls = ['https://www.facebook.com/groups/1997061680535584/?ref=group_browse','https://www.facebook.com/groups/775076752529150/?ref=group_browse','https://www.facebook.com/groups/238645432925244/?ref=group_browse']
# elements  = driver.find_elements_by_xpath("//a[starts-with(@href,'/groups/')]")
for url in group_urls:
    # url = elem.get_attribute("href")
    # if '/?ref=bookmarks' in url and url != 'https://www.facebook.com/groups/?ref=bookmarks':
    #     print(url)
    driver.get(url)
    time.sleep(20)
    ActionChains(driver).send_keys("p").perform()
    time.sleep(5)
    ActionChains(driver).send_keys(text_to_post).perform()
    time.sleep(20)
    driver.find_element_by_xpath("//button[@class='_1mf7 _4jy0 _4jy3 _4jy1 _51sy selected _42ft']").click()
    time.sleep(20)
    driver.find_element_by_link_text()
    # home_button_url = driver.find_element_by_xpath("//a[@class= '_2s25']").get_attribute("href")
    # print(home_button_url)  
    # driver.get(home_button_url)
    # time.sleep(20)
