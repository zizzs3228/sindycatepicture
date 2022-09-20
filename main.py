import requests
from bs4 import BeautifulSoup
import re
from PIL import Image, ImageFont, ImageDraw
import datetime

r = requests.get('https://coinmarketcap.com/').text
soup = BeautifulSoup(r, "lxml")
MCAP = soup.find(href="/charts/", class_="cmc-link").text
MCAPC = re.findall(r'\d+\.?\d+', MCAP)
MCAP = MCAPC[0]+MCAPC[1]+MCAPC[2]+MCAPC[3]

DOM = soup.find(href="/charts/#dominance-percentage", class_="cmc-link").text
DOMC = re.findall(r'\d+\.?\d+', DOM)

r = requests.get('https://coinmarketcap.com/currencies/bitcoin/').text
soup = BeautifulSoup(r, "lxml")
BTC = soup.find(class_="priceValue").text

r = requests.get('https://coinmarketcap.com/currencies/ethereum/').text
soup = BeautifulSoup(r, "lxml")
ETH = soup.find(class_="priceValue").text

r = requests.get('https://coinmarketcap.com/currencies/BNB/').text
soup = BeautifulSoup(r, "lxml")
BNB = soup.find(class_="priceValue").text

r = requests.get('https://www.investing.com/currencies/usd-rub').text
soup = BeautifulSoup(r, "lxml")
USD = soup.find_all(class_="text-2xl")[2].text

r = requests.get('https://www.investing.com/currencies/eur-rub').text
soup = BeautifulSoup(r, "lxml")
EUR = soup.find_all(class_="text-2xl")[2].text

r = requests.get('https://www.investing.com/commodities/metals').text
soup = BeautifulSoup(r, "lxml")
GOLD = soup.find(class_="pid-8830-last").text
COPPER = soup.find(class_="pid-8831-last").text
SILVER = soup.find(class_="pid-8836-last").text

r = requests.get('https://www.investing.com/indices/us-spx-500').text
soup = BeautifulSoup(r, "lxml")
SPX = soup.find_all(class_="text-2xl")[2].text

r = requests.get('https://www.investing.com/indices/nq-100').text
soup = BeautifulSoup(r, "lxml")
NAS = soup.find_all(class_="text-2xl")[2].text


r = requests.get('https://www.investing.com/commodities/brent-oil').text
soup = BeautifulSoup(r, "lxml")
BRENT = soup.find_all(class_="text-2xl")[2].text

r = requests.get('https://fapi.coinglass.com/api/futures/longShortRate?symbol=BTC&timeType=2').text
LONG = re.findall(r'\d+\.?\d+', r)

r = requests.get('https://fapi.coinglass.com/api/fundingRate/v2/home').text
soup = BeautifulSoup(r, "lxml")
FUNDING = re.findall(r'\d+\.?\d+', r)
#print(FUNDING[0])

r = requests.get('https://fapi.coinglass.com/api/futures/liquidation/info?symbol=BTC&timeType=1&size=12').text
soup = BeautifulSoup(r, "lxml")
BTCLIQS = re.findall(r'\d+\.?\d+', r)

r = requests.get('https://fapi.coinglass.com/api/futures/liquidation/info?symbol=ETH&timeType=1&size=12').text
soup = BeautifulSoup(r, "lxml")
ETHLIQS = re.findall(r'\d+\.?\d+', r)

r = requests.get('https://fapi.coinglass.com/api/futures/liquidation/info?symbol=ETC&timeType=1&size=12').text
soup = BeautifulSoup(r, "lxml")
ETCLIQS = re.findall(r'\d+\.?\d+', r)

r = requests.get('https://bitstat.top/fear_greed.php').text
soup = BeautifulSoup(r, "lxml")
INDEX = soup.find(class_="trx-index").text
#print(INDEX)
indexint = int(INDEX)

image = Image.open('SHABLON.png')
font = ImageFont.truetype('Montserrat-SemiBold.ttf', 50)
draw = ImageDraw.Draw(image)
MCAPF = round(float(MCAP)/1000000000, 2)
FUNDINGF = round(float(FUNDING[0]), 6)

if 0<=indexint<=25:
    draw.text((1688, 722), f"{indexint}", font=font, fill='#ff2d55')
if 26<=indexint<=46:
    draw.text((1688, 722), f"{indexint}", font=font, fill='#f46a1a')
if 47<=indexint<=53:
    draw.text((1688, 722), f"{indexint}", font=font, fill='#d19900')
if 54<=indexint<=74:
    draw.text((1688, 722), f"{indexint}", font=font, fill='#9ebd04')
if 75<=indexint<=100:
    draw.text((1688, 722), f"{indexint}", font=font, fill='#4cd964')
# USD = round(float(USD), 2)
# EUR = round(float(EUR), 2)
LONG[0] = round(float(LONG[0]), 1)
LONG[2] = round(float(LONG[2]), 1)
BTCLIQS[-3] = round(float(BTCLIQS[-3])/1000000, 2)
ETHLIQS[-3] = round(float(ETHLIQS[-3])/1000000, 2)
ETCLIQS[-3] = round(float(ETCLIQS[-3])/1000000, 2)
fontH = ImageFont.truetype('Montserrat-SemiBold.ttf', 40)
font = ImageFont.truetype('Montserrat-SemiBold.ttf', 42)
draw.text((1285, 732), f"{DOMC[0]}%", font=font, fill='white')
draw.text((825, 502), f"${MCAPF} МЛРД", font=font, fill='#7D7DC9')
draw.text((925, 602), FUNDING[0][0:8], font=font, fill='#7D7DC9')
draw.text((937, 702), f"{LONG[0]}/{LONG[2]}", font=font, fill='#7D7DC9')
draw.text((250, 192), BTC, font=fontH, fill='#7D7DC9')
draw.text((625, 192), ETH, font=fontH, fill='#7D7DC9')
draw.text((980, 193), BNB, font=fontH, fill='#7D7DC9')
draw.text((1350, 192), f"{USD[0:5]} ₽", font=font, fill='#7D7DC9')
draw.text((1660, 192), f"{EUR[0:5]} ₽", font=font, fill='#7D7DC9')
draw.text((210, 343), f"${GOLD}", font=font, fill='#7D7DC9')
draw.text((600, 343), f"${SILVER}", font=font, fill='#7D7DC9')
draw.text((970, 343), f"${COPPER}", font=font, fill='#7D7DC9')
draw.text((320, 501), f"${SPX}", font=font, fill='#7D7DC9')
draw.text((320, 595), f"${NAS}", font=font, fill='#7D7DC9')
draw.text((320, 685), f"${BRENT}", font=font, fill='#7D7DC9')
draw.text((590, 947), f"${BTCLIQS[-3]} M", font=font, fill='#7D7DC9')
draw.text((240, 947), f"${ETHLIQS[-3]} M", font=font, fill='#7D7DC9')
draw.text((940, 947), f"${ETCLIQS[-3]} M", font=font, fill='#7D7DC9')
today = datetime.datetime.now()
today = today.strftime("%d-%m-%Y")
draw.text((1565, 100), f"{today}", font=ImageFont.truetype('MontserratBOLD.ttf', 50), fill='white')
image.save(f"{(today)}.png")
#image.show()
