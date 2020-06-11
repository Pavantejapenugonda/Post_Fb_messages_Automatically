from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def scroll_bar():
    SCROLL_PAUSE_TIME = 0.5

    while True:

        # Get scroll height
        ### This is the difference. Moving this *inside* the loop
        ### means that it checks if scrollTo is still scrolling 
        last_height = driver.execute_script("return document.body.scrollHeight")

        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:

            # try again (can be removed)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")

            # check if the page height has remained the same
            if new_height == last_height:
                # if so, you are done
                break
            # if not, move on to the next loop
            else:
                last_height = new_height
                continue

def login_fb(user_name,password):
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
    time.sleep(10)
    return driver