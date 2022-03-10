def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        print('number=', number)
        count += number
    for key in keywords:
        print('key=',key)
        print('keywords[key]=', keywords[key])
        count += keywords[key]
    return count

print (total(10, 1, 2, 3, vegetables=50, fruits=100))