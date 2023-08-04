from selenium import webdriver
import time

chrome_driver = "C:\\Users\\KloverCloud\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver_win32\\chromedriver.exe"
# Replace 'path_to_webdriver' with the path to your WebDriver executable
driver = webdriver.Chrome(executable_path=chrome_driver)


def login(username, password):
    driver.get('https://app.gohighlevel.com/')
    driver.maximize_window()
    driver.implicitly_wait(20)
    time.sleep(5)

    # Assuming you have a login form with fields 'username' and 'password'
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login-button').click()
    time.sleep(10)

    # Wait for the login process to complete (you may need to adjust the time based on website behavior)
    driver.implicitly_wait(10)  # 10 seconds (you can increase or decrease this value)


def check_for_new_message():
    try:
        # Check if a new message has arrived (you need to replace the locator with the actual element representing a new message)
        new_message_element = driver.find_element_by_xpath('//div[@class="new-message"]')
        return new_message_element
    except:
        return None


def send_welcome_message():
    # Your welcome message to send
    welcome_message = "Welcome! Thank you for your message. How can I assist you today?"

    # Locate the input field to send the message and submit it
    input_field = driver.find_element_by_xpath('//input[@id="message-input"]')
    input_field.send_keys(welcome_message)
    input_field.submit()


if __name__ == "__main__":
    username = "odulanahammed@gmail.com"
    password = "oMcb6YKLb8#4m&9L"

    login(username, password)

    while True:
        new_message_element = check_for_new_message()
        if new_message_element:
            send_welcome_message()

        # Wait for a while before checking for new messages again (you can adjust the time as needed)
        time.sleep(5)  # 5 seconds
