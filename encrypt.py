from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import minify_html


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8000/encrypt.html')
    html = driver.find_element(By.ID, 'html')
    password_element = driver.find_element(By.ID, 'password')
    html_path = sys.argv[1]
    password = sys.argv[2]
    output_path = sys.argv[3]
    html_content = open(html_path, 'r').read()
    html_content = minify_html.minify(html_content, minify_css=True, minify_js=True)
    driver.execute_script('arguments[0].value = arguments[1]', html, html_content)
    password_element.send_keys(password)
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
    input('Press any key to continue...')
    encrypted = driver.find_element(By.ID, 'encrypted').get_attribute('value')
    text_to_replace = '{"salt":"lOaI7tegght/UDo2YDUpNg==","nonce":"5wK6ZTEIk5Gn8yit","ciphertext":"MWAINBeb00VxPn5yAKpb7GkzKc8g5g/oQ92h"}'
    wrapper_content = open('wrapper.html', 'r').read().replace(text_to_replace, encrypted)
    wrapper_content = minify_html.minify(wrapper_content, minify_css=True, minify_js=True)
    open(output_path, 'w').write(wrapper_content)
