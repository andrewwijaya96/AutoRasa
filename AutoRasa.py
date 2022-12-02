from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

PATH = "C:\Webdrivers\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(PATH, options=options)
kode = input("Masukkan kode misa ke kolom ini: ")

if(kode.lower() == "quit"):
    driver.quit()
    exit()

# Login petugas
driver.get("https://belarasa.id/petugas")

kodeMisa = driver.find_element(By.ID, value="kodeMisa")
loginButt = driver.find_element(By.ID, value="btnSubmitSignIn")

kodeMisa.send_keys(kode)
loginButt.click()
jumlahOrang = 0

while True:

    print(f"Jumlah Orang = {jumlahOrang}\n")
    url = input("Masukkan URL ke kolom ini: ")
    
    if(url == "quit"): #keluar program
        driver.quit()
        exit()
    else:
        #Buka website qr code
        driver.get(url)

        try:
            WebDriverWait(driver, 0.25).until (EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
            print("Pastikan QR Code Sudah Tepat untuk Kode Misa\n")
        except TimeoutException:
            try:
                masukButt = driver.find_element(By.CLASS_NAME, value="btn")
                verifTombol = masukButt.text
            except NoSuchElementException:
                print("Kesalahan teknis, mohon di periksa kembali")
            else:
                if(driver.find_element_by_class_name("btn")):
                    print("Lancar Jaya Tanpa Masalah")
                    # klik masuk kalau belum klik masuk
                    if(verifTombol == "Masuk"):                            
                        masukButt.click()
                        print("Berhasil Memasukkan")
                        jumlahOrang += 1
                    elif(verifTombol == "Sukses"):                            
                        print("Sudah Pernah Masuk")
                        
