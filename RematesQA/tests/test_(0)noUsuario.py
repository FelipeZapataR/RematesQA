from pylenium.driver import Pylenium
from utilities import Sele
import time
import pytest

@pytest.fixture
def page(py: Pylenium):
    return Sele(py).goto()  


def test_preguntasFrecuentes(page:Sele):
    page.Click('//*[@id="pageContainer"]/main/section[1]/div/div[1]/div/div/button')
    assert page.VerifyText('//*[@id="pageContainer"]/main/section/div[1]/h1','Términos y Privacidad')
    assert page.VerifyText('//*[@id="pageContainer"]/main/section/div[2]/h3[1]','¿Por qué se solicita determinada información para la creación de la cuenta?')
    page.Click('//*[@id="pageContainer"]/main/section/div[1]/div/button[1]')
    assert page.VerifyText('//*[@id="pageContainer"]/main/section/div[2]/h3[1]','¿Cómo puedo participar en remates y hacer pujas?')
    page.Click('//*[@id="navWrapper"]/ul/li[1]/button')
    assert page.VerifyText('//*[@id="pageContainer"]/main/section[1]/div/div[1]/h1','GyC Remates')
    page.Click('//*[@id="navWrapper"]/ul/li[3]/button')
    assert page.VerifyText('//*[@id="pageContainer"]/main/section/div[2]/h3[1]','¿Por qué se solicita determinada información para la creación de la cuenta?')


def registrarseRemateSinUsuario(page:Sele):
   page.Click('//*[@id="navWrapper"]/ul/li[2]/button')
   page.Click('//*[@id="pageContainer"]/main/section/div/div/div[1]/div/div[2]/button[2]')
   assert page.VerifyText('//*[@id="loginSection"]/div[1]/div[1]/h3','Inicio de sesión')





