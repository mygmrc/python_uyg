import turtle # kamlubaga modulu eklendi
import time
import random

hiz = 0.15

#pencere olusturma
pencere = turtle.Screen() # ekran olusturuldu
pencere.title('Yılan Oyunu') # baslık
pencere.bgcolor("lightgreen") # ekranin rengi
pencere.setup(600,600) # pencerenin boyutları w,h
pencere.tracer(0) # pencerenin guncellenmesini engelliyor

#kafa olusturma
kafa = turtle.Turtle() # nesne olustu
kafa.speed(0) # basta hızı sıfır,sonradan biz hareket vericez
kafa.shape('square') # kafanın sekli
kafa.color('black') # kafanin rengi
kafa.penup() # kafa hareket ederken yazi yazilmicak
kafa.goto(0,100) # noktaya gitti
kafa.direction = 'stop' # en basta duryor halde

#yemek olusturma
yemek = turtle.Turtle() # yemek nesnesi olustu
yemek.speed(0)
yemek.shape('circle')
yemek.color('red')
yemek.penup()
yemek.goto(0,0)
yemek.shapesize(0.80,0.80)

#kuyruk olusturma
kuyruklar = []
puan = 0

yaz = turtle.Turtle() # yemek nesnesi olustu
yaz.speed(0)
yaz.shape('square')
yaz.color('white')
yaz.penup()
yaz.goto(0,260)
yaz.hideturtle() # sekli yok sekil kapatma
yaz.write('Puan : {}'.format(puan),align='center',font=('Courier',24,'normal'))

#hareket sistemi
def move():
    if kafa.direction == 'up':
        y = kafa.ycor() # yukarı dogru hareket icin y koordinatı bilinmeli
        kafa.sety(y + 20) # y belirlendi ve artırıldı
    if kafa.direction == 'down':
        y = kafa.ycor()
        kafa.sety(y - 20)
    if kafa.direction == 'right':
        x = kafa.xcor()
        kafa.setx(x + 20)
    if kafa.direction == 'left':
        x = kafa.xcor()
        kafa.setx(x - 20) 

#klavye kontrolu
def goUp():
    if kafa.direction != 'down':
        kafa.direction = 'up'
def goDown():
    if kafa.direction != 'up':
        kafa.direction = 'down'
def goRight():
    if kafa.direction != 'left':
        kafa.direction = 'right'
def goLeft():
    if kafa.direction != 'right':
        kafa.direction = 'left'

pencere.listen()
pencere.onkey(goUp, 'Up')
pencere.onkey(goDown, 'Down')
pencere.onkey(goRight, 'Right')
pencere.onkey(goLeft, 'Left')


while True:
    pencere.update()

    # kenarlara carptıgında sonlanması
    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300 :
        time.sleep(1)
        kafa.goto(0,0)
        kafa.direction = 'stop'

        # kuyrukların alanın dısına tasınması
        for kuyruk in kuyruklar:
            kuyruk.goto(1000,1000)

        # liste sifirlandi 
        kuyruklar = []
        puan = 0
        yaz.clear()
        yaz.write('Puan : {}'.format(puan),align='center',font=('Courier',24,'normal'))

        hiz = 0.15
    # yemek
    if kafa.distance(yemek) < 20: #kafa ve yemek arasındaki mesafe 20 pikselden az carpısmıs
        x = random.randint(-250, 250) # yeni konum
        y = random.randint(-250, 250)
        yemek.goto(x,y)

        puan = puan + 10
        yaz.clear()
        yaz.write('Puan : {}'.format(puan),align='center',font=('Courier',24,'normal'))

        hiz = hiz - 0.001

        yeniKuyruk = turtle.Turtle() # kuyrukların kafayı takip etmesi
        yeniKuyruk.speed(0)
        yeniKuyruk.shape('square')
        yeniKuyruk.color('white')
        yeniKuyruk.penup()
        kuyruklar.append(yeniKuyruk)

    for i in range(len(kuyruklar)-1,0,-1): # kac kuyruk var
        x = kuyruklar[i -1].xcor() # bir oncekinin yerine gecmesi
        y = kuyruklar[i -1].ycor()
        kuyruklar[i].goto(x,y) 

    # en bastaki kuyruk kafanın yerine gecmesi
    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x,y)

    move() # surekli hareket etmesi gerek
    time.sleep(hiz)