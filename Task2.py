number = '098454435d3'
if number.isdigit() == False:
	print('Неправильно набран номер')
elif len(number)>10:
	print('Неправильно набран номер(Больше 10 символов)')
else:
	print('Все норм')
