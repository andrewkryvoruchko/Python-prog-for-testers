# в pytest файл с таким названием делает фикстуру общей для всех тестов
# и помещать его лучше в корень проэкта в самую верхнюю дирректорию

from fixure.application import Application
import pytest

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.distroy)
    return fixture

