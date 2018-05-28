import labirint as lab


if(1 == 0):    
    labir = lab.Labirint()
    pos = labir.getCurPos()
    labir.printme()
    print(pos)
    """look = lab.look_around()"""

    move = labir.move('w')
    print('w ', move)

if(1 == 1):
    labir = lab.Labirint()
    move = labir.move('s')
    labir.printme()
    print('s ', move)

if(1 == 0):
    labir = lab.Labirint()
    move = labir.move('e')
    labir.printme()
    print('e ', move)

    labir = lab.Labirint()
    move = labir.move('n')
    labir.printme()
    print('n ', move)
