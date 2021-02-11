from datetime import datetime
def vote(year):
    year = datetime.now().year - year
    if year < 16:
        return 'DENIED'
    elif 16 <= year < 18 or year > 65:
        return 'OPTIONAL'
    elif year >= 18:
        return 'MANDATORY'
birth_year = int(input('Enter the year. '))
result = vote(birth_year)
print(result)
