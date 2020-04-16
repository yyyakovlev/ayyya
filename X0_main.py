import random

#Игровое поле на списках
Ls1 = [ '-' , '-' , '-' ]
Ls2 = [ '-' , '-' , '-' ]
Ls3 = [ '-' , '-' , '-' ]
Lsall = ['a0','a1','a2','b0','b1','b2','c0','c1','c2']

#Выигрышные комбинации
LsWin = [
        ['a0','a1','a2'],
        ['b0','b1','b2'],
        ['c0','c1','c2'],
        ['c0','b1','a2'],
        ['a0','b1','c2'],
        ['a0','b0','c0'],
        ['a1','b1','c1'],
        ['a2','b2','c2'],
        ]


#Вывод поля
print(' ', '  0', '   1', '   2')
print('A',Ls1)
print('B',Ls2)
print('C',Ls3)
print('Указывать ячейки в формате: a1, b2, c3 и т.д.')

#Глоб. переменные
Answ = input('Нолик - ходи первый: ' )
Genn = ''

#Цикл проверяет допустимые значения
while Answ not in Lsall:
    print('Ошибка! Правильный формат: a1, b2, c3 и т.д.')
    Answ = input('Нолик - ходи: ')
else:
    pass

def lsprin():
    print (' ', '  0', '   1', '   2')
    print('A', Ls1)
    print('B', Ls2)
    print('C', Ls3)

def winprint():
    print(LsWin)

#Класс с функциями нолика и крестика
class InsIndex():

    def nolik(Answ):
        if Answ in Lsall:
            if Answ == 'a0' or Answ == 'a1' or Answ == 'a2':
                ind = int(Answ[1])
                Ls1.insert(ind, '0')
                Ls1.pop(ind + 1)
                Lsall.remove(str(Answ))
                LsWin.remove(str(Answ))
            elif Answ == 'b0' or Answ == 'b1' or Answ == 'b2':
                ind = int(Answ[1])
                Ls2.insert(ind, '0')
                Ls2.pop(ind + 1)
                Lsall.remove (str (Answ))

            elif Answ == 'c0' or Answ == 'c1' or Answ == 'c2':
                ind = int(Answ[1])
                Ls3.insert(ind, '0')
                Ls3.pop(ind + 1)
                Lsall.remove (str (Answ))

            else:
                print('Формат ответа недопустим.')
                Answ = input ('Нолик: ')
                InsIndex.nolik(Answ)
        else:
            print ('Такой ход уже был. ')
            Answ = input ('Попробуй еще раз: ')
            InsIndex.nolik (Answ)
        lsprin ()
        winprint ()

    def ddx(Genn):
        if len(Lsall) > 0:
            Genn = str (random.choice (Lsall))
            print('Теперь крестик :')
            if Genn == 'a0' or Genn == 'a1' or Genn == 'a2':
                ind = int(Genn[1])
                Ls1.insert(ind, 'X')
                Ls1.pop(ind + 1)
                Lsall.remove (str (Genn))

            elif Genn == 'b0' or Genn == 'b1' or Genn == 'b2':
                ind = int(Genn[1])
                Ls2.insert(ind, 'X')
                Ls2.pop(ind + 1)
                Lsall.remove (str (Genn))

            elif Genn == 'c0' or Genn == 'c1' or Genn == 'c2':
                ind = int(Genn[1])
                Ls3.insert(ind, 'X')
                Ls3.pop(ind + 1)
                Lsall.remove (str (Genn))

            else:
                print ('СТОП!! Что-то пошло не так!')
            lsprin ()
            winprint ()
        else:
            print ('Ходов больше нет!!!')

    # def restart_game(Answ):
    #     Answ = input ('Нажми Y для повтора: ')
    #     if Answ == 'Y' or 'y':
    #         Answ = input ('Нолик - начинай: ')
    #         InsIndex.nolik (Answ)
    #     else:
    #         print ('Ок, ПОКА!!!')
#Запуск функций
InsIndex.nolik(Answ)
InsIndex.ddx(Genn)

#Цикл пока не случится победа или не останется свободных полей
while len(Lsall) > 0:
    Answ = input('Нолик: ')
    InsIndex.nolik(Answ)
    if (Ls1[0]==Ls2[0]==Ls3[0]=='0') or (Ls1[0]==Ls2[1]==Ls3[2]=='0') or (Ls1[1]==Ls2[1]==Ls3[1]=='0') or (Ls1[2]==Ls2[2]==Ls3[2]=='0') or (Ls1[0]==Ls1[1]==Ls1[2]=='0') or (Ls2[0]==Ls2[1]==Ls2[2]=='0') or (Ls3[0]==Ls3[1]==Ls3[2]=='0') or (Ls1[2]==Ls2[1]==Ls3[0]=='0'):
        print ('Победа НОЛИКА!!!')
        break
    InsIndex.ddx(Genn)
    if (Ls1[0]==Ls2[0]==Ls3[0]=='X') or (Ls1[0]==Ls2[1]==Ls3[2]=='X') or (Ls1[1]==Ls2[1]==Ls3[1]=='X') or (Ls1[2]==Ls2[2]==Ls3[2]=='X') or (Ls1[0]==Ls1[1]==Ls1[2]=='X') or (Ls2[0]==Ls2[1]==Ls2[2]=='X') or (Ls3[0]==Ls3[1]==Ls3[2]=='X') or (Ls1[2]==Ls2[1]==Ls3[0]=='X'):
        print('Победа КРЕСТИКА!!!')
        break
else:
    print ('Победила ДРУЖБА!!!')



