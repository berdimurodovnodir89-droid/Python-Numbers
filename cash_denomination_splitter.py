from num2words import num2words

first_price = float(input('First_price :'))
second_price = float(input('Second_price :'))
third_price = float(input('Third_price :'))

result = first_price + second_price + third_price 

total_words = num2words(result, lang='en', to='currency')

print(f'umumiy summa {result}')
print(f'{total_words}')