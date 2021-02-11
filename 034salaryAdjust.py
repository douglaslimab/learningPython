salary = int(input('Enter the Salary.\n'))
if salary <= 1250:
    salary = salary*1.15
    print('New salary is U$ {:.2f}'.format(salary))
else:
    salary = salary*1.10
    print('New salary is U$ {:.2f}'.format(salary))