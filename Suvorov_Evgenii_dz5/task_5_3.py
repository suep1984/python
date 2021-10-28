tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий',
          'Борис', 'Елена', 'Alex', 'Leo', 'Max', 'Anna', 'Maria']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

result = (res for res in zip(tutors, klasses + [None for n in range(len(tutors) - len(klasses))]))

print(type(result))
