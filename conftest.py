# в pytest файл с таким названием делает фикстуру общей для всех тестов
# и помещать его лучше в корень проэкта в самую верхнюю дирректорию

from fixure.application import Application
import pytest

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(username="andrew1973@gmail.com", password="giovanni")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="andrew1973@gmail.com", password="giovanni")
    return fixture  # возвращает объект Application в тест

# благодаря scope="session" фикстура сработет один раз для всей сессии запущеных тестов
# благодаря autouse=True неуказанная в тестах фиктсура сработает (для pytest)
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.distroy()
    request.addfinalizer(fin)
    return fixture  # возвращает объект Application в тест

