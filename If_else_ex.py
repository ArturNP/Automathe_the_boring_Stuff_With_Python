password = input('Password: ')
if password:
    if password == 'swordfish':
        print ('Acess granted')    
    else:
        print('Acces denied')
else:
    print('You need a password')