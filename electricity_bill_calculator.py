from num2words import num2words

oy_boshi = float(input('Oy boshidagi korsatkich :'))
oy_oxiri = float(input('Oy oxiridagi korsatkich :'))

result = (oy_oxiri - oy_boshi) * 0.45

words_en = num2words(result,lang = 'en', to = 'currency')
words_ru = num2words(result,lang = 'ru', to = 'currency')

print(f'tolov {result}$, {words_en}, {words_ru}')