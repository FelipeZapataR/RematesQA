from pylenium.driver import Pylenium
import time

 
class Sele:
    def __init__(self,py:Pylenium):
        self.py = py
    
    def goto(self) -> 'Sele':
        self.py.visit('https://gycremates-qa.solucionesok.cl/')
        return self   
    
    
    def Click(self,xpath):
        return self.py.getx(xpath).click()
    
    def Send(self,xpath,key):
        return self.py.getx(xpath).type(key)
    
    def VerifyExist(self,xpath):
        return self.py.getx(xpath).should().be_visible()
    
    def VerifyText(self,xpath,text):
        return self.py.getx(xpath).text() == text
    
    def Clear(self,xpath):
        return self.py.getx(xpath).clear()
    
    def SleepS():
        return time.sleep(0.5)
    
    def SleepM():
        return time.sleep(1)
    
    def SleepL():
        return time.sleep(2)
    
    def SleepXL():
        return time.sleep(5)
            
    def login_administrador(self):
        self.py.getx('//*[@id="userProfileNavButton"]/div/button').click()
        time.sleep(1)
        self.py.getx('//*[@id="userProfileNavButton"]/div/div/button[1]').click()
        self.py.getx('//*[@id="login-user-form"]/div[1]/input').type('alejandro.munoz@solucionesok.cl')
        self.py.getx('//*[@id="login-user-form"]/div[2]/button').submit()
        self.py.getx('//*[@id="login-password-form"]/div[1]/input').type('asd123')
        self.py.getx('//*[@id="login-password-form"]/div[2]/button').submit()
        time.sleep(1)
        self.hard_refresh()
        self.py.getx('//*[@id="RoleSelection"]/div/div/button[1]').click()
        self.hard_refresh()
            
    def login_usuario(self):
        self.py.getx('//*[@id="userProfileNavButton"]/div/button').click()
        time.sleep(1)
        self.py.getx('//*[@id="userProfileNavButton"]/div/div/button[1]').click()
        self.py.getx('//*[@id="login-user-form"]/div[1]/input').type('felipezapatarodriguez@gmail.com')
        self.py.getx('//*[@id="login-user-form"]/div[2]/button').submit()
        self.py.getx('//*[@id="login-password-form"]/div[1]/input').type('Asd1234asd')
        self.py.getx('//*[@id="login-password-form"]/div[2]/button').submit()
        self.hard_refresh()

    def login_usuario2(self):
        self.py.getx('//*[@id="userProfileNavButton"]/div/button').click()
        time.sleep(1)
        self.py.getx('//*[@id="userProfileNavButton"]/div/div/button[1]').click()
        self.py.getx('//*[@id="login-user-form"]/div[1]/input').type('felepex@outlook.es')
        self.py.getx('//*[@id="login-user-form"]/div[2]/button').submit()
        self.py.getx('//*[@id="login-password-form"]/div[1]/input').type('Asd1234asd')
        self.py.getx('//*[@id="login-password-form"]/div[2]/button').submit()
        self.hard_refresh()
    
    
    def hard_refresh(self):
        time.sleep(1)
        self.py.reload()
        time.sleep(1)    