from num2words import num2words

monday = float(input('summa :'))
tuesday = float(input('summa :'))
wednesday = float(input('summa :'))
thursday = float(input('summa :'))
friday= float(input('summa :'))
saturday = float(input('summa :'))
sunday = float(input('summa :'))

total = ( monday + tuesday + wednesday + thursday + friday + saturday + sunday )/7
words_en = num2words(total,lang='en',to='currency')
words_ru = num2words(total,lang='ru',to='currency')
print(f'Ortacha xarajat :{total}')
print(words_en,words_ru)