# find the age of the User from the given date of birth


def calculate_age(year, month, day):
    today = datetime=today()
    birth_date = date=(year, month, day)
    age = today.year - birth_date.year
    
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

print(calculate_age(1995, 9, 17))  
 