# в pytest файл с таким названием делает фикстуру общей для всех тестов
# и помещать его лучше в корень проэкта в самую верхнюю дирректорию

from fixure.application import Application
import pytest

fixture = None
# вынесение метода login из тестов в фикстуру делает его общим для всей сессии
# проверка с условным операторм if говорит если фикстура есть то используй ее
# но плюс к этому добавляет стабильность, если она ошибочно упала создай новую
@pytest.fixture
def app():
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid(): # если возвращается False создай фикстуру заново (запусти браузер)
            fixture = Application()
    fixture.session.ensure_login(username="andrew1973@gmail.com", password="giovanni")
    return fixture  # возвращает объект Application в тест

# для сохранения оптимизации разделяем инициализацию и финализацию
# благодаря scope="session" финализирующая фикстура сработет один раз в самом конце для всей сессии
# запущеных тестов, без этого выражения финализатор будет разрушать всю фиктруру в конце каждого теста
# благодаря autouse=True неуказанная в параметрах тестов фиктсура все равно сработает (для pytest)
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.distroy()
    request.addfinalizer(fin)
    return fixture  # возвращает объект Application в тест

