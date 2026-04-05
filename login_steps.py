from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@given('I open the login page')
def step_open_login_page(context):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://www.saucedemo.com/")

@when('I enter username "{username}"')
def step_enter_username(context, username):
    context.driver.find_element(By.ID, "user-name").send_keys(username)

@when('I enter password "{password}"')
def step_enter_password(context, password):
    context.driver.find_element(By.ID, "password").send_keys(password)

@when('I click the "{button}" button')
def step_click_button(context, button):
    if button == "Login":
        context.driver.find_element(By.ID, "login-button").click()

@then('I am redirected to the inventory page')
def step_check_inventory(context):
    assert "inventory.html" in context.driver.current_url
    context.driver.quit()

@then('I see an error message')
def step_check_error(context):
    error = context.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert error.is_displayed()
    context.driver.quit()