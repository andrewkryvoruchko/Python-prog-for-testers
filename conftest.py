# в pytest файл с таким названием делает фикстуру общей для всех тестов
# и помещать его лучше в корень проэкта в самую верхнюю дирректорию

from fixure.application import Application
import pytest
import json
import os.path

fixture = None
target = None
# вынесение метода login из тестов в фикстуру делает его общим для всей сессии
# проверка с условным операторм if говорит если фикстура есть то используй ее
# но плюс к этому добавляет стабильность, если она ошибочно упала создай новую
@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")  # принимается значение переданное из консоли
    if target is None:
        path_to_config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(path_to_config_file) as config_file:  # читаем открываем файл
            target = json.load(config_file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture  # возвращает объект Application в тест

# для сохранения оптимизации разделяем инициализацию и финализацию
# благодаря scope="session" финализирующая фикстура сработет один раз в самом конце для всей сессии
# запущеных тестов, без этого выражения финализатор будет разрушать всю фиктруру в конце каждого теста
# благодаря autouse=True неуказанная в параметрах тестов финализирующая фиктсура все равно сработает (для pytest)
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.distroy()
    request.addfinalizer(fin)
    return fixture  # возвращает объект Application в тест

# добавляем опции pytest принимающие значения параметров в командной строке
def pytest_addoption(parser):  # (хук - зацепка специальная функция)
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")

