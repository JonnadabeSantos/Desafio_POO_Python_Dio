x = 12
y = 90

def valid( x,y ):
    if x > y:
        print('ok')
        return True

    else:
        print('fall')

    return False

print( valid( x, y ) )