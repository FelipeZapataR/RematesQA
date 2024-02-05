import time
from pylenium.driver import Pylenium
from utilities import Sele
import pytest
     
@pytest.fixture
def page(py: Pylenium):
    return Sele(py).goto()   

    
def solicitar_registrarse(page:Sele,py:Pylenium):
    page.login_usuario()
    page.Click('/html/body/div[1]/div/div/nav/div[2]/ul/li[2]/button')
    page.Click('//*[@id="pageContainer"]/main/section/div/div/div[1]/div/div[2]/button[2]')
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    page.Send('//*[@id="garantia-form"]/div[1]/input','Felipe Zapata')
    page.Send('//*[@id="garantia-form"]/div[2]/input','18.300.115-9')
    page.Send('//*[@id="garantia-form"]/div[3]/input','Banco Santander')
    py.getx('//*[@id="garantia-form"]/div[4]/div/select').select_by_text('Cuenta corriente')
    page.Send('//*[@id="garantia-form"]/div[5]/input','00769696969')
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    time.sleep(2)
    
def aceptar_garantia(page:Sele):
    page.login_administrador()
    page.Click('//*[@id="pageContainer"]/main/section/div/button[3]')
    page.Click('//*[@id="pageContainer"]/main/section/div/div/div[3]/button[1]')
    assert page.VerifyText('//*[@id="modalPortal"]/div/div/div[2]/section/div/p',"¿Estás seguro/a que deseas autorizar la solicitud de garantía del usuario felipezapatarodriguez@gmail.com?")
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button[2]')
    time.sleep(2)
    #mensaje de exito errado

def solicitar_registrarse2(page:Sele,py:Pylenium):
    page.login_usuario2()
    page.Click('/html/body/div[1]/div/div/nav/div[2]/ul/li[2]/button')
    page.Click('//*[@id="pageContainer"]/main/section/div/div/div[1]/div/div[2]/button[2]')
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    page.Send('//*[@id="garantia-form"]/div[1]/input','Felipe Zapata')
    page.Send('//*[@id="garantia-form"]/div[2]/input','18.300.115-9')
    page.Send('//*[@id="garantia-form"]/div[3]/input','Banco Santander')
    py.getx('//*[@id="garantia-form"]/div[4]/div/select').select_by_text('Cuenta corriente')
    page.Send('//*[@id="garantia-form"]/div[5]/input','00769696969')
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    time.sleep(2)

def aceptar_garantia2(page:Sele):
    page.login_administrador()
    page.Click('//*[@id="pageContainer"]/main/section/div/button[3]')
    page.Click('//*[@id="pageContainer"]/main/section/div/div/div[3]/button[1]')
    assert page.VerifyText('//*[@id="modalPortal"]/div/div/div[2]/section/div/p',"¿Estás seguro/a que deseas autorizar la solicitud de garantía del usuario felepex@outlook.es?")
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button[2]')
    time.sleep(2)
    #mensaje de exito errado
    
def test_ver_articulos(page:Sele):
    page.login_usuario()
    page.Click('//*[@id="navWrapper"]/ul/li[2]/button')
    page.Click('//*[@id="pageContainer"]/main/section/div/div/div[1]/div/div[2]/button[1]')
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    page.Click('//*[@id="pageContainer"]/main/section[2]/div/div/div/div/div[1]/div/div[2]/div/div/button')
    time.sleep(4)
    
def test_pujar_articulos(page:Sele):
    page.login_usuario()
    #presionar en remates navbar
    page.Click('//*[@id="navWrapper"]/ul/li[2]/button')
    #presionar en conectar al remate
    page.Click('//*[@id="pageContainer"]/main/section/div/div/div[1]/div/div[2]/button[2]')
    #cerrar card 1
    page.Click('//*[@id="pageContainer"]/main/section/div/div[1]/button')
    time.sleep(1)
    #cerrar card 2
    page.Click('//*[@id="pageContainer"]/main/section/div/div[2]/button')
    time.sleep(1)
    #abrir card 1
    page.Click('//*[@id="pageContainer"]/main/section/div/div[1]/button')
    time.sleep(1)
    #abrir card 2
    page.Click('//*[@id="pageContainer"]/main/section/div/div[2]/button')
    time.sleep(1)
    #pujar el primer articulo por el presion normal
    page.Click('//*[@id="pageContainer"]/main/section/div/div[1]/div/div[1]/div[3]/div[1]/button[1]')
    time.sleep(2)
    #presionar en editar valor del segundio articulo
    page.Click('//*[@id="pageContainer"]/main/section/div/div[2]/div/div[1]/div[3]/div[1]/button[2]')
    #limpiar celda de nuevo valoer
    page.Clear('//*[@id="monto-puja-form"]/div/input')
    #ingresar valor de nuevo monto a poujar
    page.Send('//*[@id="monto-puja-form"]/div/input','9000')
    #presionar aceptar valor
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    #pujar por segundo articulo por nuevo valor
    page.Click('//*[@id="pageContainer"]/main/section/div/div[2]/div/div[1]/div[3]/div[1]/button[1]')
    time.sleep(2)

def test_pujar_articulos2(page:Sele):
    page.login_usuario2()
    page.Click('//*[@id="navWrapper"]/ul/li[2]/button')
    #presionar en conectar al remate
    page.Click('//*[@id="pageContainer"]/main/section/div/div/div[1]/div/div[2]/button[2]')
    #pujar el primer articulo por el presion normal
    page.Click('//*[@id="pageContainer"]/main/section/div/div[1]/div/div[1]/div[3]/div[1]/button[1]')
    time.sleep(2)
    #presionar en editar valor del segundio articulo
    page.Click('//*[@id="pageContainer"]/main/section/div/div[2]/div/div[1]/div[3]/div[1]/button[2]')
    #limpiar celda de nuevo valoer
    page.Clear('//*[@id="monto-puja-form"]/div/input')
    #ingresar valor de nuevo monto a poujar
    page.Send('//*[@id="monto-puja-form"]/div/input','9000')
    #presionar aceptar valor
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    #pujar por segundo articulo por nuevo valor
    page.Click('//*[@id="pageContainer"]/main/section/div/div[2]/div/div[1]/div[3]/div[1]/button[1]')
    time.sleep(2)

          
    
    
    
        
    