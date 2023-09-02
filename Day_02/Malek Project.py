total_money = 1000
print('Hello ' + input('Enter Your Name'))

withdraw = int(input('Choose the number you want to withdraw'))
if withdraw <= 1000:
    print('stay')
    print(total_money - withdraw)


else:
    a = str(total_money)
    print('no, withdraw less than ' + a)
print('Do You Want To Enter Money')