import smtplib
import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200
EMAIL = "chowdhurya290@gmail.com"
PASSWORD = "Arpshchy-1099"

title = soup.find(id="productTitle").get_text().strip()
if price_as_float < 200:
    mail = smtplib.SMTP("smtp.gmail.com")
    mail.starttls()
    mail.login(user=EMAIL, password=PASSWORD)
    mail.sendmail(
        from_addr=EMAIL,
        to_addrs=EMAIL,
        msg=f"subject: AMAZON PRICE TRACKER\n\n{title} is now {price} you can get it now via\n{url}"
    )
