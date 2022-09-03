
task = input('Сколько будет 5+5:')

task.isdigit()
while task.isdigit()!= True:
    print('Вы ввели букву')
    print()
    task = input('Введите число:')
else:
	task=int(task)
	if task ==10:
		print('Правильно')
	else:
		print('Неправильно, будет 10')
