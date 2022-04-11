from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome('C:\\Users\\bearu\\PycharmProjects\\teste_web_petz\\drivers\\chromedriver100.exe')
    context.driver.maximize_window()

def after_all(context):
    context.driver.quit()

def after_step(context, step):
    print()