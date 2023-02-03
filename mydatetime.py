import datetime

def ageCalculator(y, m, d):
    today = datetime.now().date()
    dob =  datetime.date(y,m,d)
    age = int((today - dob.days) / 365.25) 
    print(age) 
    print("hello")

    ageCalculator(1998,9,3)
    print("hello")   
