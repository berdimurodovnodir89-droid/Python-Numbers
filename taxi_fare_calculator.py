from num2words import num2words
masofa = float(input('masofa :'))
kelishi = 3.0
km = 1.20

result = (masofa * km) + kelishi
words_en = num2words(result, lang='en',to='currency')
words_ru = num2words(result, lang='ru',to='currency')

print(f'Taxi narxi :{result}')
print(words_en,words_ru)