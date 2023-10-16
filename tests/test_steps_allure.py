import allure
from selene import browser, by, be




def test_steps_allure(settings_browser):
    with allure.step('Открываем главную страницу Гитхаба'):
        browser.open('https://github.com/')

    with allure.step('Поиск репозитория'):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').send_keys('Maxunris/quru8_9').press_enter()

    with allure.step('Заходим в репозиторий'):
        browser.element(by.link_text('Maxunris/quru8_9')).click()

    with allure.step('Нажимаем на Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверка наличия кнопки Issues'):
        browser.element(by.partial_text('test issue')).should(be.visible)
