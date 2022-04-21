from selenium.webdriver.common.by import By


class LoginForm:
    EMAIL_ADDRESS = (By.CSS_SELECTOR, '#email_create')
    FIRST_NAME = (By.CSS_SELECTOR, '#customer_firstname')
    LAST_NAME = (By.CSS_SELECTOR, '#customer_lastname')
    PASSWORD = (By.CSS_SELECTOR, '#passwd')
    COMPANY = (By.CSS_SELECTOR, '#company')
    ADDRESS_LINE1 = (By.CSS_SELECTOR, '#address1')
    ADDRESS_LINE2 = (By.CSS_SELECTOR, '#address2')
    CITY = (By.CSS_SELECTOR, '#city')
    STATE = (By.CSS_SELECTOR, '#id_state')
    ZIP_POSTAL_CODE = (By.CSS_SELECTOR, '#postcode')
    COUNTRY = (By.CSS_SELECTOR, '#id_country')
    ADD_INFO = (By.CSS_SELECTOR, '#other')
    HOME_PHONE = (By.CSS_SELECTOR, '#phone')
    MABILE_PHONE = (By.CSS_SELECTOR, '#phone_mobile')
    ASSING_AN_ADDRESS_ALIAS_FOR_FUTURE_REFERENCE = (By.CSS_SELECTOR, '#phone_mobile')
    FEGISTER_BUTTON = (By.CSS_SELECTOR, '#alias')
