work_reg = list()
employee = dict()

employee['name'] = str(input('Name: ')).strip().capitalize()
birth_year = int(input('Birth year: '))
employee['age'] = 2021 - birth_year
employee['register'] =int(input('Register: '))
if employee['register'] != 0:
    employee['contract_year'] = int(input('Contract year: '))
    r_age = employee['contract_year'] - birth_year + 35
    employee['retirement_age'] = r_age
    employee['salary'] = float(input('Salary: '))
print(employee)
for k, v in employee.items():
    print(f'{k.capitalize()}: {v}')