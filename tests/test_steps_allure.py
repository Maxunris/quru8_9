import allure
from selene import browser, by, be




def test_steps_allure(settings_browser):
    with allure.step('Открываем главную страницу Гитхаба'):
        browser.open('https://github.com/').element('.search-input').click()

    with allure.step('поиск репозитория'):
        browser.element('#query-builder-test').send_keys('Maxunris/quru8_9').press_enter()
        browser.element(by.link_text('Maxunris/quru8_9')).click()

    browser.element('#issues-tab').click()
    browser.element(by.partial_text('test issue')).should(be.visible)

    browser.quit()