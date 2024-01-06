age = input("How old are you?")
try:
    if int(age) >= 18:
        print('Please come in...')
    else:
        print('Sorry, I cannot let you in...')
except:
    print('Cannot recognize the age')
