import pandas
import time 
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec

excel_credenciales = r'credentials_COTPS.xlsx'

df = pandas.read_excel(excel_credenciales)
c = 0;
i = 0;

user = df['name'][c]
psw = df['contraseña'][c]
cod = df['codigo'][c]

url = 'https://www.cotps.com'

# Selectores
                 
boton_comercio = 'body > uni-app > uni-tabbar > div.uni-tabbar > div:nth-child(3)'
boton_codigo = 'body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view:nth-child(5) > uni-text'
selector_codigo = 'body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view.form-item > uni-view > uni-input > div > input'
boton_confirmarcod = 'body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view.form-item > uni-button'
selector_usuario = 'body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view:nth-child(5) > uni-input > div > input'
selector_contraseña = 'body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view:nth-child(7) > uni-input > div > input'
boton_login = 'body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-button'
modal_aceptar = 'body > uni-app > uni-modal > div.uni-modal > div.uni-modal__ft > div'
btn_pedirahora = 'body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view.grab-orders-wrap.grab-orders-wrap1 > uni-button'
btn_vender = 'body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view.fui-dialog__wrap.fui-wrap__show > uni-view > uni-view > uni-view.buttons > uni-button:nth-child(2)'
btn_confv = 'body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view.fui-dialog__wrap.fui-wrap__show > uni-view > uni-view > uni-button'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()
driver.get(url)
driver.fullscreen_window()
try:
    time.sleep(5)

    driver.find_element_by_css_selector(boton_comercio).click()

    time.sleep(7)

    driver.find_element_by_css_selector(boton_codigo).click()

    time.sleep(5)

    driver.find_element_by_css_selector(selector_codigo).send_keys(str(cod))

    time.sleep(5)

    driver.find_element_by_css_selector(boton_confirmarcod).click();

    time.sleep(5)

    driver.find_element_by_css_selector(selector_usuario).send_keys(str(user))

    time.sleep(5)

    driver.find_element_by_css_selector(selector_contraseña).send_keys(str(psw))


    time.sleep(5)

    driver.find_element_by_css_selector(boton_login).click()

    time.sleep(12)
    try:
        driver.find_element_by_css_selector(modal_aceptar).click()
    except:
        time.sleep(3)

    driver.find_element_by_css_selector(boton_comercio).click()
except:
    print('ERROR EN INICIO')
konkun = 0
vari = 0



while vari < 1:
    time.sleep(5)
    try: 
        time.sleep(10)
        
        driver.find_element_by_css_selector(btn_pedirahora).click()

        time.sleep(10)

        driver.find_element_by_css_selector(btn_vender).click()
    
        time.sleep(10)
        
        driver.find_element_by_css_selector(btn_confv).click()
        
        #profile
        konkun = konkun + 1
        print('el numero de Ventas realizadas = '+str(konkun))
    
    except:
        print('ERROR EN COMERCIO')
        time.sleep(10)
        num = driver.find_element_by_css_selector('body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view.division-wrap > uni-view.division-right > uni-view.division-num')
        numero = num.text
        if str(numero) <= '5.000':
            print('VALOR EN WALLET'+str(numero))
            try:
                time.sleep(10)
                driver.find_element_by_css_selector('body > uni-app > uni-tabbar > div.uni-tabbar > div:nth-child(5) > div > div.uni-tabbar__icon > img').click()
            
                time.sleep(10)
                #team
                driver.find_element_by_css_selector('body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view.box-wrap > uni-view.menu-wrap > uni-view:nth-child(6) > uni-view').click()
        
                time.sleep(10)
                #aceptar
                driver.find_element_by_css_selector('body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view.card-wrap > uni-view > uni-button').click()
                time.sleep(7)                           
                #lv2
                driver.find_element_by_css_selector('body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view.tabs > uni-view:nth-child(2)').click()
                driver.find_element_by_css_selector('body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view.card-wrap > uni-view > uni-button').click()
                time.sleep(7)
                #lv3
                driver.find_element_by_css_selector('body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view.tabs > uni-view:nth-child(3)').click()
                driver.find_element_by_css_selector('body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view.card-wrap > uni-view > uni-button').click()
                time.sleep(7)
                #back
                driver.find_element_by_css_selector('body > uni-app > uni-page > uni-page-head > div.uni-page-head > div.uni-page-head-hd > div.uni-page-head-btn').click()
                time.sleep(10)
                driver.find_element_by_css_selector(boton_comercio).click()
                time.sleep(300)
                driver.refresh()
                driver.maximize_window()
            except: 
                print('ERROR EN RECAUDOS')
                
        driver.refresh()
        driver.maximize_window()
        time.sleep(10)
        driver.fullscreen_window()
        
        
