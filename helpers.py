from selenium import webdriver
def init_page(baseUrl): 
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)


    driver = webdriver.Chrome(options = options)
    driver.get(baseUrl)
    return driver