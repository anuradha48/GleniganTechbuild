from behave import given, when, then
from selenium import webdriver


@given('Launch chrome browser')
def launchBrowser(context):
    context.driver= webdriver.Chrome(executable_path="C:\\driver\\chromedriver_win32 (6)\\chromedriver.exe")


@when('Open orange HRM')
def openOrange(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('Verify that logo present on page')
def verifyLogo(context):
    context.driver.find_element_by_xpath('//*[@id="divLogo"]/img').is_displayed()



@then('close browser')
def closeBrowser(context):
    context.driver.close()
