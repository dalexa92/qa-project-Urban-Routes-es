import time

import data
from selenium import webdriver
from selenium.webdriver import Keys  #Permite dar TAB o Enter
from selenium.webdriver.common.by import By #Permite seleccionar los elementos por diferentes metodos (ID, CSS)
from selenium.webdriver.support import expected_conditions as EC #Se agrega el alias para validar un nombre mas corto
from selenium.webdriver.support.wait import WebDriverWait #El q nos realiza las esperas para el cargue de elementos en la pantalla
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from main import UrbanRoutesPage


class TestUrbanRoutes: #esta es la prueba

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url) #abre la pagina del servidor
        routes_page = UrbanRoutesPage(self.driver) #Se esta creando un objeto de la clase urban routes page
        address_from = data.address_from #crean variable q toda la direccion de data
        address_to = data.address_to
        routes_page.set_route(address_from, address_to) #el set es un metodo lo que realiza es digitar la direccion en la pagina
        assert routes_page.get_from() == address_from  #los assert compara y confirma que si sea lo que correspode
        assert routes_page.get_to() == address_to

    def test_select_comfort_rate(self):
        self.test_set_route() #esto corre la prueba dejando en un estado el explorador
        routes_page = UrbanRoutesPage(self.driver) #se crea un objeto de esta clase
        routes_page.click_on_request_taxi_button() #lo que se quiere es clickear
        routes_page.click_on_comfort_rate_icon() #icono de comfort

        comfort_rate = routes_page.get_comfort_rate_icon().text
        comfort_text = "Comfort"
        assert  comfort_rate in comfort_text
        assert routes_page.get_comfort_rate_icon().text in "Comfort" #que texto tiene el icono

    def test_phone_number(self):
        self.test_select_comfort_rate() #Utilizamos el test anterior
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_phone_number_button()
        phone_number = data.phone_number
        routes_page.set_phone_number_field(phone_number)
        routes_page.click_on_next_button()
        routes_page.set_sms_code()
        routes_page.click_on_sms_next_button()

        assert routes_page.get_phone_number_field().get_attribute('value') == data.phone_number

    def test_payment_method_button(self):
        self.test_phone_number() #Inicio con el test anteior
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_payment_method_button()
        routes_page.click_add_card_button()
        routes_page.set_card_number_field()
        routes_page.get_card_number_field().send_keys(Keys.TAB)
        routes_page.set_code_field()
        routes_page.get_code_field().send_keys(Keys.TAB)
        routes_page.click_on_add_button()
        assert routes_page.get_card_label().text ==  'Tarjeta'
        routes_page.click_on_close_popup_button()

    def test_message_for_driver_field(self):
        self.test_payment_method_button()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_message_for_driver_field()
        routes_page.set_message_for_driver_field()
        assert routes_page.get_message_for_driver_field().text in 'Traeme un snack'

    def test_blanket_and_scarves_slider(self):
        self.test_message_for_driver_field()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_blanket_and_scarves_slider()
        assert routes_page.get_blanket_and_scarves_slider_input().get_property('checked')

    def test_add_ice_cream(self):
        self.test_blanket_and_scarves_slider()
        routes_page = UrbanRoutesPage(self.driver)
        initial_value = routes_page.get_counter_value()
        routes_page.click_ice_creams_counter_plus()
        new_value = routes_page.get_counter_value()
        assert new_value == initial_value + 1, f"Error: Se esperaba {initial_value + 1}, resultado {new_value}"

    def test_reserve_taxi_button(self):
        self.test_add_ice_cream()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_reserve_taxi_button()
        routes_page.click_on_reserve_taxi_button()
        assert routes_page.get_reserve_taxi_button().text in "Pedir un taxi"












    @classmethod
    def teardown_class(cls):
        cls.driver.quit()