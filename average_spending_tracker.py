from num2words import num2words
money = int(input('Summa :'))
money_copy = money
money_50=money // 50
money=money - money_50 * 50

money_10=money // 10
money=money - money_10 * 10

money_5=money // 5
money=money - money_5 * 5

money_1=money // 1
money=money - money_1 * 1


result = f'$50 kupyuradan :{money_50} ta \n$10 kupyuradan :{money_10}\n'
result1 = f'5$ kupyuradan {money_5}ta \n1$ kupyuradan {money_1} ta \n'
result3 = f'umumiy summa {money_copy} '

words_en = num2words(money_copy, lang='en', to='currency')
words_ru = num2words(money_copy, lang='ru', to='currency')

print(result, result1, result3,words_en,words_ru)
