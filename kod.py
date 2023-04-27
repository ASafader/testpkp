class wyszukiwanie_polaczenia(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) #podmiana  self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://rozklad-pkp.pl/")
        zgoda = self.driver.find_element(By.CLASS_NAME,'css-47sehv')
        zgoda.click()

    def testnazwystacji(self):
        nazwa_stacji = self.driver.find_element(By.ID,'from-station')
        nazwa_stacji.send_keys('Warszawa Centralna')
        nazwa_stacji2 = self.driver.find_element(By.ID,'to-station')
        nazwa_stacji2.send_keys('Gdańsk Wrzeszcz')
        self.driver.execute_script("window.scrollTo(0, 500)") #polecenie do scrollowania
        sleep(2)
        numerdnia = self.driver.find_element(By.CLASS_NAME, 'day-number')
        numerdnia.click()
        kalendarz_strzalka = self.driver.find_element(By.CLASS_NAME, 'ui-datepicker-next')
        kalendarz_strzalka.click()
        dzien_1 = self.driver.find_element(By.PARTIAL_LINK_TEXT, '1')
        dzien_1.click()
        button_wybierz_date = self.driver.find_element(By.CLASS_NAME, 'pick-date')
        button_wybierz_date.click()
        #polaczenie_bezposrednie = self.driver.find_element(By.ID, 'directCheckbox')
        polaczenie_bezposrednie = self.driver.find_element(By.CLASS_NAME, 'icheckbox_minimal-blue') #mozemy zlapac element wyzej, w ktorym zawiera sie ten element
        polaczenie_bezposrednie.click()
        button_wyszukaj_polaczenie = self.driver.find_element(By. ID, 'singlebutton')
        button_wyszukaj_polaczenie.click()
        sleep(5)
       # kup_bilet = self.driver.find_element(By.CLASS_NAME, 'buy-ticket')
       # self.assertEqual('kup bilet',kup_bilet.text)
        zmien_kryteria_wyszukiwania = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'ZMIEŃ KRYTERIA WYSZUKIWANIA')
        self.assertEqual('ZMIEŃ KRYTERIA WYSZUKIWANIA', zmien_kryteria_wyszukiwania.text)
        sleep(5)
if __name__ == '__main__':
    unittest.main()

