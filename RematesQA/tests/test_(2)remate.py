from pylenium.driver import Pylenium
from selenium.webdriver.common.keys import Keys
from utilities import Sele
import time
import pytest
#variables imagenes
casa ='C:/Users/felep/OneDrive/Documentos/GitHub/RematesQA/Imagenes/ImagenCasa.jpeg'
#crear modificador de fechas 
fechainicio='04022024'
fechatermino='07022024'
fvisitaInicio='01022024'
fvisitaFinal='03022024'

@pytest.fixture
def page(py: Pylenium):
    return Sele(py).goto()      

def test_crear_remate(page:Sele ,py:Pylenium):
    page.login_administrador()
    page.Click('//*[@id="pageContainer"]/main/section/div/button[1]')
    assert page.VerifyText('//*[@id="pageContainer"]/main/section/div[2]/p',"No hay remates ingresados")
    #crear nuev remate
    page.Click('//*[@id="pageContainer"]/main/section/div[3]/div/button')
    #Rellenar nombre remate
    page.Send('//*[@id="crear-remate-form"]/div[1]/input','RemateDePrueba2')
    #Rellenar fecha de inicio
    #3 dias posterior al dia actual
    page.Send('//*[@id="crear-remate-form"]/div[2]/input',fechainicio)
    page.Send('//*[@id="crear-remate-form"]/div[2]/input',Keys.TAB)
    page.Send('//*[@id="crear-remate-form"]/div[2]/input','1400')
    #Rellenar fecha de termino
    #6 dias posterior al dia actual
    page.Send('//*[@id="crear-remate-form"]/div[3]/input',fechatermino)
    page.Send('//*[@id="crear-remate-form"]/div[3]/input',Keys.TAB)
    page.Send('//*[@id="crear-remate-form"]/div[3]/input','1400')
    #Telefono del remate
    page.Send('//*[@id="crear-remate-form"]/div[4]/input','+56969696969')
    #Celular del remate
    page.Send('//*[@id="crear-remate-form"]/div[5]/input','+56969696969')
    #Direccion del Remate
    page.Send('//*[@id="crear-remate-form"]/div[6]/input','Avenida Siempre Viva 742')
    #seleccionar martillero
    py.getx('//*[@id="crear-remate-form"]/div[7]/div/select').select_by_text('Homero Simpson')
    #Rellenar precio garantia
    page.Send('//*[@id="crear-remate-form"]/div[8]/input','1800000')
    #Rellenar inicio de visita
    #dia actual
    page.Send('//*[@id="crear-remate-form"]/div[9]/div[1]/input',fvisitaInicio)
    #Rellenar termino de visita
    #2 dias posterior al dia actual
    page.Send('//*[@id="crear-remate-form"]/div[9]/div[2]/input',fvisitaFinal)
    #Rellenar horario de visita
    page.Send('//*[@id="crear-remate-form"]/div[9]/div[3]/input','12:00 - 18:00')
    #Rellenar descripcion de remate
    page.Send('//*[@id="crear-remate-form"]/div[11]/textarea','Este es un remate de prueba organizado por Homero Simpson')
    #Rellenar nota del remate
    page.Send('//*[@id="crear-remate-form"]/div[12]/textarea','Se remata Casa de Avenida Simpre Viva 742')
    #Click Destacar remate
    page.Click('//*[@id="crear-remate-form"]/div[13]/div/label/span')
    #click mostrar fecha de remate
    page.Click('//*[@id="crear-remate-form"]/div[14]/div/label/span')
    #Subir Imagen
    page.Send('//*[@id="crear-remate-form"]/div[10]/div/div[1]/input',casa)
    #crear remate
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    time.sleep(5)

    
def test_modificar_remate(page:Sele):
    page.login_administrador()
    #click remtates
    page.Click('//*[@id="pageContainer"]/main/section/div/button[1]')
    #ver ficha
    page.Click('//*[@id="pageContainer"]/main/section/div[2]/div/div[2]/button[1]')
    #editar remates
    page.Click('//*[@id="pageContainer"]/main/section/div/section/div[1]/div[1]/button')
    #Rellenar nombre remate
    page.Clear('//*[@id="modificar-remate-form"]/div[1]/input')
    page.Send('//*[@id="modificar-remate-form"]/div[1]/input','RemateDePrueba2')
    #Rellenar precio garantia
    page.Clear('//*[@id="modificar-remate-form"]/div[8]/input')
    page.Send('//*[@id="modificar-remate-form"]/div[8]/input','2000000')
    #crear remate
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    time.sleep(5)


def test_eliminar_remate(page:Sele):
    page.login_administrador()
    #click remtates
    page.Click('//*[@id="pageContainer"]/main/section/div/button[1]')
    #ver ficha
    page.Click('//*[@id="pageContainer"]/main/section/div[2]/div/div[2]/button[1]')
    #eliminar remate
    page.Click('//*[@id="pageContainer"]/main/section/div/div/button')
    #confirmar eliminacion
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    time.sleep(5)


    
    
def test_crear_remate2(page:Sele ,py:Pylenium):
    page.login_administrador()
    page.Click('//*[@id="pageContainer"]/main/section/div/button[1]')
    assert page.VerifyText('//*[@id="pageContainer"]/main/section/div[2]/p',"No hay remates ingresados")
    #crear nuev remate
    page.Click('//*[@id="pageContainer"]/main/section/div[3]/div/button')
    #Rellenar nombre remate
    page.Send('//*[@id="crear-remate-form"]/div[1]/input','RemateDePrueba2')
    #Rellenar fecha de inicio
    #3 dias posterior al dia actual
    page.Send('//*[@id="crear-remate-form"]/div[2]/input',fechainicio)
    page.Send('//*[@id="crear-remate-form"]/div[2]/input',Keys.TAB)
    page.Send('//*[@id="crear-remate-form"]/div[2]/input','1400')
    #Rellenar fecha de termino
    #6 dias posterior al dia actual
    page.Send('//*[@id="crear-remate-form"]/div[3]/input',fechatermino)
    page.Send('//*[@id="crear-remate-form"]/div[3]/input',Keys.TAB)
    page.Send('//*[@id="crear-remate-form"]/div[3]/input','1400')
    #Telefono del remate
    page.Send('//*[@id="crear-remate-form"]/div[4]/input','+56969696969')
    #Celular del remate
    page.Send('//*[@id="crear-remate-form"]/div[5]/input','+56969696969')
    #Direccion del Remate
    page.Send('//*[@id="crear-remate-form"]/div[6]/input','Avenida Siempre Viva 742')
    #seleccionar martillero
    py.getx('//*[@id="crear-remate-form"]/div[7]/div/select').select_by_text('Homero Simpson')
    #Rellenar precio garantia
    page.Send('//*[@id="crear-remate-form"]/div[8]/input','1800000')
    #Rellenar inicio de visita
    #dia actual
    page.Send('//*[@id="crear-remate-form"]/div[9]/div[1]/input',fvisitaInicio)
    #Rellenar termino de visita
    #2 dias posterior al dia actual
    page.Send('//*[@id="crear-remate-form"]/div[9]/div[2]/input',fvisitaFinal)
    #Rellenar horario de visita
    page.Send('//*[@id="crear-remate-form"]/div[9]/div[3]/input','12:00 - 18:00')
    #Rellenar descripcion de remate
    page.Send('//*[@id="crear-remate-form"]/div[11]/textarea','Este es un remate de prueba organizado por Homero Simpson')
    #Rellenar nota del remate
    page.Send('//*[@id="crear-remate-form"]/div[12]/textarea','Se remata Casa de Avenida Simpre Viva 742')
    #Click Destacar remate
    page.Click('//*[@id="crear-remate-form"]/div[13]/div/label/span')
    #click mostrar fecha de remate
    page.Click('//*[@id="crear-remate-form"]/div[14]/div/label/span')
    #Subir Imagen
    page.Send('//*[@id="crear-remate-form"]/div[10]/div/div[1]/input',casa)
    #crear remate
    page.Click('//*[@id="modalPortal"]/div/div/div[3]/button')
    time.sleep(5)     