import time
import pytesseract as tess
from PIL import Image, ImageGrab
import pyautogui
from googletrans import Translator

im1 = pyautogui.screenshot()
im2 = pyautogui.screenshot('my_screenst.png')

img = Image.open('my_screenst.png')
texto = tess.image_to_string(img)

with open('traduzido.txt', 'w' ) as arquivo:
	for valor1 in texto:
		arquivo.write(str(valor1))


a = texto
b = 'en'

trans = Translator()
t = trans.translate(a, src ='en', dest='pt')
print(f'Source: {t.src}')
print(f'Destination: {t.dest}')
print(f"{t.origin} == {t.text}")


trans = Translator()
t = trans.translate(
	a, src = 'en', dest='de'
	)
print(f'Source: {t.src}')
print(f'Destination: {t.dest}')

print(f"{t.origin} == {t.text}")
trans = Translator()
t = trans.translate(
	a, src = 'en', dest='zh-cn'
	)
print(f'Source: {t.src}')
print(f'Destination: {t.dest}')

print(f"{t.origin} == {t.text}")

trans = Translator()
t = trans.translate(a, src = 'en', dest='ru')
print(f'Source: {t.src}')
print(f'Destination: {t.dest}')

print(f"{t.origin} == {t.text}")


from googletrans import LANGUAGES
for lang in LANGUAGES:
	print(f'{lang} - {LANGUAGES[lang]}')