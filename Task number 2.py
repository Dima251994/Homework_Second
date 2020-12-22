
ordinaryNumbers = [
    "нуль", 
    ("один","одна"),
    ("дві","два"), 
    "три" ,
    "чотири" ,
    "п'ять",
    "шість",
    "сім",
    "вісім", 
    "дев'ять", 
    "десять", 
    "одинадцять", 
    "дванадцять", 
    "тринадцять", 
    "чотирнадцять", 
    "п'ятнадцять", 
    "шістнядцять", 
    "сімнадцять", 
    "вісімнадцять", 
    "дев'ятнадцять",
]

def getGrades(number):
    return (
        number / 1000000000,
        number % 1000000000 / 1000000,
        number % 1000000 / 1000,
        number % 1000 
    )

number = 0
while True:
    try:
        number = input("Please, enter the number from 0 to 2 147 483 647: " )
        number = int(number)
        assert number >= 0 and number < 2147483647, "Please, enter the number from 0 to 2000000000"
        break
    except ValueError:
        print("Enter number value!")
    except Exception as ex:
        print(ex)

output = getGrades(number)
print(output)