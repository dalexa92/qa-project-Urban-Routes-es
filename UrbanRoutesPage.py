import data
import helpers
from selenium import webdriver
from selenium.webdriver import Keys  #Permite dar TAB o Enter
from selenium.webdriver.common.by import By #Permite seleccionar los elementos por diferentes metodos (ID, CSS)
from selenium.webdriver.support import expected_conditions as EC #Se agrega el alias para validar un nombre mas corto
from selenium.webdriver.support.wait import WebDriverWait #El q nos realiza las esperas para el cargue de elementos en la pantalla
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to') #estos son los dos primeros elementos
    request_taxi_button = (By.CSS_SELECTOR, ".button.round") #elemento del boton pedir un taxi
    comfort_rate_icon = (By.XPATH, "//div[@class='tcard-title' and text()= 'Comfort']") #Icono de confort
    phone_number_button = (By.CSS_SELECTOR, '.np-button') #Caja o casilla del numero de telefono
    phone_number_field = (By.ID, 'phone') # Numero de telefono
    next_button = (By.CSS_SELECTOR, ".button.full")
    sms_code_field = (By.ID, "code")
    sms_confirmation_button = (By.XPATH, "//div[@class='buttons']/button[text()='Confirmar']") #confirmar envio y cierre de casilla phone
    payment_method_button = (By.CSS_SELECTOR, ".pp-button") #botón metodo de pago
    add_card_button = (By.CSS_SELECTOR, ".pp-plus-container") #Botón + Agregar tarjeta
    card_number_field = (By.ID, "number")
    code_field = (By.NAME, "code") #cvv
    add_button = (By.XPATH, "//div[@class='pp-buttons']/button[text()='Agregar']") #boton de agregar
    card = (By.XPATH, "//div[@class='pp-title' and text()='Tarjeta']")
    close_popup_button = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]') #Cerrar ventana emergente
    message_for_driver_field = (By.ID, "comment") #mensaje para el conductor
    order_requirements = (By.CSS_SELECTOR, ".reqs-arrow") #Requisitos del pedido
    blanket_and_scarves_slider = (By.CLASS_NAME, "switch") #Slider manta y
    blanket_and_scarves_slider_input = (By.CLASS_NAME, "switch-input")
    ice_creams_counter_plus = (By.CLASS_NAME, "counter-plus") #numero de helados
    reserve_taxi_button = (By.CSS_SELECTOR, ".smart-button-main")
    countdown_modal = (By.XPATH, "//div[contains(@class, 'order-header-time')]")

    def __init__(self, driver):  # Este es el constructor - Siempre tiene que ir.
        self.driver = driver

    def set_from(self, from_address):  # recibo una direccion
        # self.driver.find_element(*self.from_field).send_keys(from_address) #envia una direccion
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.from_field)
                                            ).send_keys(from_address)  # solo dar una espera para que este el elemento

    def set_to(self, to_address):
        # self.driver.find_element(*self.to_field).send_keys(to_address)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.to_field)
                                            ).send_keys(to_address)

    def get_from(self):  # obtiene y Nos retorna el elemento
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_request_taxi_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.request_taxi_button)
                                                   )  # Metodo para buscar o traer el elemento

    def click_on_request_taxi_button(self):
        self.get_request_taxi_button().click()  # Darle clic, enviar un elemento

    def get_comfort_rate_icon(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.comfort_rate_icon))

    def click_on_comfort_rate_icon(self):
        self.get_comfort_rate_icon().click()

    def get_phone_number_button(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable(self.phone_number_button))

    def click_on_phone_number_button(self):
        self.get_phone_number_button().click()  # Botón del telefono

    def get_phone_number_field(self):  # obtinee el numero de telefono
        return WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(self.phone_number_field))

    def set_phone_number_field(self, phone_number):  # envia el numero?
        self.get_phone_number_field().send_keys(phone_number)

    def get_next_button(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable(self.next_button))

    def click_on_next_button(self):
        self.get_next_button().click()

    def get_sms_code(self):
        return WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(self.sms_code_field))

    def set_sms_code(self):
        self.get_sms_code().send_keys(helpers.retrieve_phone_code(self.driver))

    def get_sms_next_button(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable(self.sms_confirmation_button))

    def click_on_sms_next_button(self):
        self.get_sms_next_button().click()

    def get_payment_method_button(self):  # Boton de metodo de pago
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable(self.payment_method_button))

    def click_payment_method_button(self):
        self.get_payment_method_button().click()

    def get_add_card_button(self):  # Boton de metodo de pago
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable(self.add_card_button))

    def click_add_card_button(self):
        self.get_add_card_button().click()

    def get_card_number_field(self):  # obtinee el numero de telefono
        return WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located(self.card_number_field))

    def set_card_number_field(self):  # envia el numero?
        self.get_card_number_field().send_keys(data.card_number)

    def get_code_field(self):  # obtinee el numero de telefono
        return WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located(self.code_field))

    def set_code_field(self):  # envia el numero?
        self.get_code_field().send_keys(data.card_code)

    def get_add_button(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable(self.add_button))

    def click_on_add_button(self):
        self.get_add_button().click()

    def get_card_label(self):
        return WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(self.card))

    def get_close_popup_button(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable(self.close_popup_button))

    def click_on_close_popup_button(self):
        self.get_close_popup_button().click()

    def get_message_for_driver_field(self):  # obtinee el numero de telefono
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable(self.message_for_driver_field)
                                                   )

    def set_message_for_driver_field(self):  # envia el numero?
        self.get_message_for_driver_field().send_keys(data.message_for_driver)

    def get_order_requirements(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable(self.order_requirements))

    def get_blanket_and_scarves_slider(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable(self.blanket_and_scarves_slider))

    def set_blanket_and_scarves_slider(self):
        self.get_blanket_and_scarves_slider().click()

    def get_blanket_and_scarves_slider_input(self):
        return WebDriverWait(self.driver, 6).until(
            EC.presence_of_element_located(self.blanket_and_scarves_slider_input))

    def click_on_blanket_and_scarves_slider_input(self):
        self.get_blanket_and_scarves_slider_input().click()

    def get_ice_creams_counter_plus(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable(self.ice_creams_counter_plus))

    def click_ice_creams_counter_plus(self):
        self.get_ice_creams_counter_plus().click()

    def get_counter_value(self):
        counter_element = self.driver.find_element(By.CLASS_NAME, "counter-value")
        return int(counter_element.text)

    def get_reserve_taxi_button(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable(self.reserve_taxi_button))

    def click_on_reserve_taxi_button(self):
        self.get_reserve_taxi_button().click()

    def get_countdown_modal(self):
        return WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(self.countdown_modal))
