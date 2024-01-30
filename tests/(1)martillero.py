from pylenium.driver import Pylenium
from utilities import Sele
import time
import pytest

@pytest.fixture
def page(py: Pylenium):
    return Sele(py).goto()      
    
def crear_martillero(page:Sele):
    page.login_administrador()
    page.Click('//*[@id="pageContainer"]/main/section/div/button[2]')
    assert page.VerifyExist('//*[@id="pageContainer"]/main/section/div[1]/h1')
    page.Click('//*[@id="pageContainer"]/main/section/div[3]/div/button')
    page.Send('//*[@id="crear-martillero-form"]/div[1]/input','Homero Simpson')
    page.Send('//*[@id="crear-martillero-form"]/div[2]/input','123123123')
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    assert page.VerifyExist('//*[@id="pageContainer"]/main/section/div[2]/div/div[1]/h2')
    

def modificar_martillero(page:Sele):
    page.login_administrador()
    page.Click('//*[@id="pageContainer"]/main/section/div/button[2]')
    assert page.VerifyExist('//*[@id="pageContainer"]/main/section/div[1]/h1')
    page.Click('//*[@id="pageContainer"]/main/section/div[2]/div/div[2]/button[1]')
    page.Clear('//*[@id="modificar-martillero-form"]/div[1]/input')
    page.Send('//*[@id="modificar-martillero-form"]/div[1]/input','Marge Simpson')
    page.Clear('//*[@id="modificar-martillero-form"]/div[2]/input')
    page.Send('//*[@id="modificar-martillero-form"]/div[2]/input','123412341234')
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    page.SleepS()
    assert page.VerifyText('//*[@id="pageContainer"]/main/section/div[2]/div/div[1]/h2','Marge Simpson')

    
    
def test_eliminar_martillero(page:Sele):
    page.login_administrador()
    page.Click('//*[@id="pageContainer"]/main/section/div/button[2]')
    assert page.VerifyExist('//*[@id="pageContainer"]/main/section/div[1]/h1')
    page.Click('//*[@id="pageContainer"]/main/section/div[2]/div/div[2]/button[2]')
    page.SleepS()
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button[2]')
    page.SleepS()

def test_crear_martillero2( page:Sele):
    page.login_administrador()
    page.Click('//*[@id="pageContainer"]/main/section/div/button[2]')
    assert page.VerifyExist('//*[@id="pageContainer"]/main/section/div[1]/h1')
    page.Click('//*[@id="pageContainer"]/main/section/div[3]/div/button')
    page.Send('//*[@id="crear-martillero-form"]/div[1]/input','Homero Simpson')
    page.Send('//*[@id="crear-martillero-form"]/div[2]/input','123123123')
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    assert page.VerifyExist('//*[@id="pageContainer"]/main/section/div[2]/div/div[1]/h2')
    page.SleepS()
      
# def test_errosCrearMartillero(page:Sele):
#     page.login_administrador()
#     page.Click('//*[@id="pageContainer"]/main/section/div/button[2]')
#     assert page.VerifyExist('//*[@id="pageContainer"]/main/section/div[1]/h1')
#     page.Click('//*[@id="pageContainer"]/main/section/div[3]/div/button')
    

    
    
    
    
    