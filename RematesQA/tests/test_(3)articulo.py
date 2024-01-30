from pylenium.driver import Pylenium
from utilities import Sele
import time
import pytest

#variables imagenes
ayudanteSanta1 ='C:/Users/felep/OneDrive/Documentos/GitHub/RematesQA/RematesQA/Imagenes/AyudanteSanta.jpeg'
ayudanteSanta2 ='C:/Users/felep/OneDrive/Documentos/GitHub/RematesQA/RematesQA/Imagenes/AyudanteSanta2.jpeg'
sillon1 ='C:/Users/felep/OneDrive/Documentos/GitHub/RematesQA/RematesQA/Imagenes/Sillon.jpeg'
sillon2 ='C:/Users/felep/OneDrive/Documentos/GitHub/RematesQA/RematesQA/Imagenes/Sillon2.jpeg'


@pytest.fixture
def page(py: Pylenium):
    return Sele(py).goto()      

def test_crear_articulo(page:Sele):
    page.login_administrador()
    page.Click('//*[@id="pageContainer"]/main/section/div/button[1]')
    page.Click('//*[@id="pageContainer"]/main/section/div[2]/div/div[2]/button[2]')
    page.Send('//*[@id="crear-articulo-form"]/div[1]/input','Aayudante de asanta')
    page.Send('//*[@id="crear-articulo-form"]/div[2]/input','100000')
    page.Send('//*[@id="crear-articulo-form"]/div[3]/input','10000')
    page.Send('//*[@id="crear-articulo-form"]/div[4]/input','600000')  
    page.Send('//*[@id="crear-articulo-form"]/div[5]/textarea','Perro familiar galgo')  
    page.Send('//*[@id="crear-articulo-form"]/div[6]/div/div[1]/input',ayudanteSanta1)  
    page.Send('//*[@id="crear-articulo-form"]/div[7]/div/div[1]/input',ayudanteSanta2) 
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    time.sleep(1)


def modificar_articulo(page:Sele):
    page.login_administrador()  
    #click en remates
    page.Click('//*[@id="pageContainer"]/main/section/div/button[1]')
    #Click en ver Ficha
    page.Click('//*[@id="pageContainer"]/main/section/div[2]/div[1]/div[2]/button[1]')
    #Click en datos de articulo
    page.Click('//*[@id="pageContainer"]/main/section/aside/div[1]/div[2]/div/button[2]')
    #Click en los 3 puntitos
    page.Click('//*[@id="pageContainer"]/main/section/div/section/div/div[1]/div[1]/div[2]/button')
    time.sleep(0.5)
    #Click en editar
    page.Click('//*[@id="pageContainer"]/main/section/div/section/div/div[1]/div[1]/div[2]/div/button[1]')
    #editar Descripcion
    page.Clear('//*[@id="modificar-articulo-form"]/div[5]/textarea')
    page.Send('//*[@id="modificar-articulo-form"]/div[5]/textarea','Perro familiar galgo Editado')
    #Click acpetar
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    time.sleep(1)

def elimiar_articulo(page:Sele):
    page.login_administrador()  
    #click en remates
    page.Click('//*[@id="pageContainer"]/main/section/div/button[1]')
    #Click en ver Ficha
    page.Click('//*[@id="pageContainer"]/main/section/div[2]/div[1]/div[2]/button[1]')
    #Click en datos de articulo
    page.Click('//*[@id="pageContainer"]/main/section/aside/div[1]/div[2]/div/button[2]')
    #Click en los 3 puntitos
    page.Click('//*[@id="pageContainer"]/main/section/div/section/div/div[1]/div[1]/div[2]/button')
    time.sleep(0.5)
    #Click en eliminar
    page.Click('//*[@id="pageContainer"]/main/section/div/section/div/div[1]/div[1]/div[2]/div/button[2]')
    #Click confirmar eliminacion
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    time.sleep(1)

def crear_articulo1(page:Sele):
    page.login_administrador()
    page.Click('//*[@id="pageContainer"]/main/section/div/button[1]')
    page.Click('//*[@id="pageContainer"]/main/section/div[2]/div/div[2]/button[2]')
    page.Send('//*[@id="crear-articulo-form"]/div[1]/input','0Ayudante de santa')
    page.Send('//*[@id="crear-articulo-form"]/div[2]/input','100000')
    page.Send('//*[@id="crear-articulo-form"]/div[3]/input','10000')
    page.Send('//*[@id="crear-articulo-form"]/div[4]/input','600000')  
    page.Send('//*[@id="crear-articulo-form"]/div[5]/textarea','Perro familiar galgo')  
    page.Send('//*[@id="crear-articulo-form"]/div[6]/div/div[1]/input',ayudanteSanta1)  
    page.Send('//*[@id="crear-articulo-form"]/div[7]/div/div[1]/input',ayudanteSanta2) 
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    time.sleep(2)
    
   
def crear_articulo2(page:Sele):
    page.login_administrador()
    page.Click('//*[@id="pageContainer"]/main/section/div/button[1]')
    page.Click('//*[@id="pageContainer"]/main/section/div[2]/div/div[2]/button[2]')
    page.Send('//*[@id="crear-articulo-form"]/div[1]/input','Sillon Familiar')
    page.Send('//*[@id="crear-articulo-form"]/div[2]/input','80000')
    page.Send('//*[@id="crear-articulo-form"]/div[3]/input','8000')
    page.Send('//*[@id="crear-articulo-form"]/div[4]/input','360000')  
    page.Send('//*[@id="crear-articulo-form"]/div[5]/textarea','Sillon familiar 3 cuerpos')  
    page.Send('//*[@id="crear-articulo-form"]/div[6]/div/div[1]/input',sillon1)  
    page.Send('//*[@id="crear-articulo-form"]/div[7]/div/div[1]/input',sillon2) 
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    time.sleep(2)
        