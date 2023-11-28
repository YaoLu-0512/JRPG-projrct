from ast import Global, If
import pygame
import math
import PySimpleGUI as sg
import pickle
# meth is better
Ar=[]
users=[]
#parte de definir o sistema de coordenadas
class Bloc:
    #definir os blocos como objecto
    def __init__(self,axix,axiy,type):  #os blocos diferenciam-se por x,y e tipo de bloco(Land,Sea)
        self.axix = axix         
        self.axiy = axiy
        self.type = type
#LOCALIDADES
class Sea:
    #definir blocos de mar

     walk = False
     imag = pygame.image.load(r"C:\Users\luyao\OneDrive\Desktop\YAOI\Sea blob.png")
class Land:
     
    #defininr blocos de terra
    
     walk = True
     imag = pygame.image.load(r"C:\Users\luyao\OneDrive\Desktop\YAOI\land green.png") 
class Sand:
    walk = True
    
    imag=pygame.image.load(r"C:\Users\luyao\OneDrive\Desktop\YAOI\Sand2.png")
class Dirt:
    walk =True

    imag=pygame.image.load(r"C:\Users\luyao\OneDrive\Desktop\YAOI\Dirt2.png")
 


# OBJECTOS PARA INTERAGIR NA MAPA
class Chest:
    #caixas que contem objetos
    def __init__(self,axix,axiy,content):
        self.raxix = axix
        self.raxiy = axiy
        self.cnt = content
    keey = False
    imag = pygame.image.load(r"C:\Users\luyao\OneDrive\Desktop\YAOI\chest 1.png")
    
class Monsta:
    #monstros que vão ser encontrado na mapa
    def __init__(self,axix,axiy,typee,count): #vamos usar type para identificar que monstro
        self.axix = axix         
        self.axiy = axiy
        self.type = typee 
        self.count = count

class Mcountainer:
    # usamos isto dentro de sistema de combate
    def __init__(self, monster1,monster2,monster3):
        self.mons = [monster1,monster2,monster3]

#COMBATE
class Slime_W:
    #slime usado no combate
    alive = True
    element = 'water'
    helth = 30
    atk = 10
    imag = pygame.image.load(r"C:\Users\luyao\OneDrive\Desktop\YAOI\SLIMEW1.png")
    
    
    
#OBJECTOS QUE UM JOGADOR PODE OBTER
class Wand:
    #arma para protanonista
    def __init__(self,name,atk,cash):
        self.name = name
        self.atk = atk
        self.cash = cash
    img = None

#PERSNAGENS
class Dude:
    #o caracter que vamos mexer na mapa
     speed = 1
     imag = pygame.image.load(r"C:\Users\luyao\OneDrive\Desktop\YAOI\witch state 1.png")
     abaxix = 60
     abaxiy = 60 #se tu aumentares isto, muda a posição do blit da nova posição 
class Cdude:
    #usado durante o combate
    hp = 100
    atkm = 1
    icepwr = [True,False,False]
    firepwr = [True,False,False]
    arcpwr = [True,False,False,False]
    mana = 40

#FUNÇÕES MAMADAS \o/

def Inii(liss): #coordenadas
        #iniciar
        for yi in range(14):# 0-13
            for xi in range (26): #0-25
             liss.append(Bloc(xi,13-yi,Sea)) #mete o ecrã todo com Sea

def pint(liss): #print da lista na ordem que vamos apresentar no terminal(consola da tua mãe), e vai pintar toda a ercã com Sea
      
       count = 0 
       for yi in range(14):
            for xi in range (26):
             print(liss[count].axix,liss[count].axiy,liss[count].type)
             screen.blit(liss[Find(liss,xi,yi)].type.imag,(xi*50,yi*50))
             count += 1 
       print(count)
def Pintbloc(liss): #pint só que não vai apaecer blocos inúteis no cmd
    
        for yi in range(14):
            for xi in range (26):
             screen.blit(liss[Find(liss,xi,yi)].type.imag,(xi*50,yi*50))
def Iniim(liss,chestliss,monliss): #iniciar o MAPA TODA
     Pintbloc(liss)    
     for i in range(len(chestliss)):
        screen.blit(chestliss[i][2].imag,(chestliss[i][0],chestliss[i][1]))         
     for i in range(len(monliss)):
         screen.blit(monliss[i].type.imag,(monliss[i].axix,monliss[i].axiy))
        
        
#ESCOLHER AS COORDENADAS Q QUERES PINTAR (mudar o tipo)
def Find(liss,x,y):   # liss é a lista das coordenadas todas dos blocos
    #procurar o bloco com determindada coordenada
    lisx = []
    end = None
    for i in range(len(liss)):  #procura o x na lista, vai ter o x para todos os y
        if liss[i].axix == x:
            lisx.append(liss[i])
    for u in range(len(lisx)): #procura o y na lista do x(lisx)
        if lisx[u].axiy == y:
         end = lisx[u]  
    # da-nos a porra do index que bloco tem dentro da lista
    return liss.index(end)
def Square(liss,x,y,size): #pede o tamanho do quadrado que quer desenhar e o coordenada em que começa(Find), ver mais em doc
    
    select = []
    for p in range(size): #É preciso fazer p e l para garantir q n fica (1,1)(2,2)(3,3)...
        for l in range(size):
            select.append(Find(liss,x+l,y+p))# Find dá nos o index do objeto com a coordenada pretendida
    return select
def Sett(liss,select,typp):  # Depois de escolher as coordenadas que começa(Find) e o tamanho do quadrado(Square), muda os tipos dos blocos(Sett) no select
   
    for b in range(len(select)):    #select são as coordenadas do quadrado
     liss[select[b]].type = typp          

#Mexe Mexe
def Move_d(guy,events,screen,liss,chestliss,monliss):
       
 image = guy.imag
    #backg = Land.imag
 keys= pygame.key.get_pressed()
    
 
 if keys[pygame.K_w] or keys[pygame.K_UP] :
            #mexe para cima
             print('moved up')
             guy.abaxiy -=7
             #ver se podemos andar
             if Waka(liss,guy.abaxix,guy.abaxiy) == True:
             #para a personagem n aparecer 2 vezes:
              Iniim(liss,chestliss,monliss)
              screen.blit(image,(guy.abaxix,guy.abaxiy))
             else:
                 guy.abaxiy +=7
                 print('no lol')
             
 if keys[pygame.K_s] or keys[pygame.K_DOWN] :
                 #mexe para baixo
             print("moved down")
             guy.abaxiy +=7
             if Waka(liss,guy.abaxix,guy.abaxiy) == True:
              Iniim(liss,chestliss,monliss)
              screen.blit(image,(guy.abaxix,guy.abaxiy))
             else:
                 guy.abaxiy -=7
                 print('no lol')
     
 if keys[pygame.K_a] or keys[pygame.K_LEFT]:
          #mexe para esquerda
             print('moved left')
             guy.abaxix -=7
             if Waka(liss,guy.abaxix,guy.abaxiy) == True:
              Iniim(liss,chestliss,monliss)
              screen.blit(image,(guy.abaxix,guy.abaxiy))
             else:
                 guy.abaxix +=7
                 print('no lol')
     
     
 if keys[pygame.K_d] or keys[pygame.K_RIGHT] :
              #mexe para direita
             print('moved right,now in',guy.abaxix,guy.abaxiy)
             guy.abaxix +=7
             if Waka(liss,guy.abaxix,guy.abaxiy) == True:
              Iniim(liss,chestliss,monliss)
              screen.blit(image,(guy.abaxix,guy.abaxiy))
             else:
                 guy.abaxix -=7
                 print('no lol')

def Waka(liss,raxix,raxiy):  # dá-nos a coordenada do bloco que queremos ir, e verifica se podemos, de facto, andar nele
   #TÁ RESOLVIDO
    axix = raxix // 50
    axiy = raxiy // 50
    if raxix//50 != 0:
        axix +=1
    if raxiy//50 != 0:
        axiy +=1
    
    if 0 <= axix < 26 and 0 <= axiy < 14:
        bloc = Find(liss, axix, axiy)
        
        if axix <= 25 and axiy <= 13:
            if liss[bloc].type.walk == False:
                return False
            else:
                return True
        
    else:
        return False    

# SISTEMA DE INTERAGIR COM CAIXA
def Fetch(sack,box,guy,event,): #calcular a distancia a cada caixa, e abre o mais proximo 
    
    
   for event in events:
    if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_e:
             #calcular a distancia 
           distance = []
           closeboxindex = 0
           for i in range(len(box)):
             a = abs(box[i][0]-guy.abaxix)
             b = abs(box[i][1]-guy.abaxiy)
             distance.append(math.sqrt(a**2+b**2))
           Bsort(distance)  
           #dps de encontrar a distancia mais perto, procuramos qual caixa é que está mais perto
           for i in range(len(box)):
             a = abs(box[i][0]-guy.abaxix)
             b = abs(box[i][1]-guy.abaxiy)
             currentdis = math.sqrt(a**2+b**2)
             if currentdis == distance[0]:
                 closeboxindex = i
                 break
           if distance[0] <100:
               #abrir e adicionar ao inventorio , se a distancia for pequeno

              if box[closeboxindex][2].keey == False:
               print('fetch attempted')
               sack.append(box[closeboxindex][2].cnt)
              else:
                 print('key needed')
           else:
                  print('chest too far')

# SISTEMA DE ENCONTRATR OS MOSTROS NA MAPA
def Encount(monliss,guy):
      #calcular a distancia 
    # tenho de fazer esta bosta para fazer com que o python reconhece uma variavel global
    global  battle
    global  locked
    
    distance = []
    for i in range(len(monliss)):
     a = abs(monliss[i].axix-guy.abaxix)
     b = abs(monliss[i].axiy-guy.abaxiy)
     distance.append(math.sqrt(a**2+b**2))
    Bsort(distance)  
    
    if distance[0]< 30:
             if battle == False:
               
               battle= True
               locked= True
               print('ENCOUNTERED')
               
def Encountw(monliss,guy):
    # vou fazer isso para determinar qual monstro é que encontramos na mapa
    distance = []
    for i in range(len(monliss)):
     a = abs(monliss[i].axix-guy.abaxix)
     b = abs(monliss[i].axiy-guy.abaxiy)
     distance.append(math.sqrt(a**2+b**2))
    Bsort(distance)
    for i in range(len(monliss)):
        a = abs(monliss[i].axix-guy.abaxix)
        b = abs(monliss[i].axiy-guy.abaxiy)
        currentdis= (math.sqrt(a**2+b**2))
        if currentdis == distance[0]:
            return(monliss[i].count)
def Encountwi(monliss,guy):
    # vou fazer isso para determinar qual monstro é que encontramos na mapa,return dá-nos a INDEX do monstro no lista de monstros na mapa
    distance = []
    for i in range(len(monliss)):
     a = abs(monliss[i].axix-guy.abaxix)
     b = abs(monliss[i].axiy-guy.abaxiy)
     distance.append(math.sqrt(a**2+b**2))
    Bsort(distance)
    for i in range(len(monliss)):
        a = abs(monliss[i].axix-guy.abaxix)
        b = abs(monliss[i].axiy-guy.abaxiy)
        currentdis= (math.sqrt(a**2+b**2))
        if currentdis == distance[0]:
            return(i)  
             
def Cselectw():
   #aqui escolhes qual dos inimigos queres atacar 
   inin = input(int('qual queres atacar'))  
   return inin
             
# SISTEMA DE COMBATE             
def Battlem1(screen,container,equiped,events,mlissindex):
    #váriavéis que vão sei úteis
    global myturn,sack,cguy,locked,battle,scran,cheses,monmon,guy
    selects = False
    win = False
    sloc = [(200,224),(200,529),(100,376)]
    #iniciar a background
    bground= pygame.image.load(r"C:\Users\luyao\OneDrive\Desktop\YAOI\grassland_battlefield.png")
    prota = pygame.image.load(r"C:\Users\luyao\OneDrive\Desktop\YAOI\witch combat unarmed.png")
    screen.blit(bground,(0,0))
    screen.blit(prota,(900,271))
    #blit dos mosntros
    if len(container.mons) == 0:
        #mete o ui de ganhaste , espaço para aceitar e sair ao mapa 
        win = True
                
    for i in range(3):
        if container.mons[i].alive == True:
         # print quando tão vivos
         screen.blit(container.mons[i].imag,sloc[i])  
       
    if cguy.hp <= 0 :
       screen.fill((0, 0, 0))
       print('game over')
    
    #mete a bosta de ui aqui para ter um menu de click em vez de tecaldo 
    for event in events:
      if event.type == pygame.KEYDOWN : 
         if event.key == pygame.K_SPACE:
             #sair quando ganha
             if win == True:
                 locked,battle = False,False
                 monmon.pop(mlissindex)
                 Iniim(scran,cheses,monmon) 
         if event.key == pygame.K_ESCAPE:
             #fugir  , vai levar dano
             print('ran away ')
             cguy.hp -= 0.5*cguy.hp
             locked,battle = False,False
             #vamos ter de teletransportar para isso n entrar num loop de encounter e fugir
             guy.abaxix+= 31 
             #re inicia a mapa
             Iniim(scran,cheses,monmon)
             screen.blit(guy.imag,(guy.abaxix,guy.abaxiy))
         if event.key == pygame.K_q:  
             #abrir o inventorio , depois pode escolher cenas para usar ali  
             print (sack)
         if event.key == pygame.K_a:
             #escolher cenas para atacar
             selects = True
         if selects == True:
             # aqui mostra as magias diferentes que pode escolher, ou vai simplesmente dar uma pancada
             if event.key == pygame.K_0:
              try:
                container[Cselectw()].hp -= cguy.atkm*25
              except:
                 print('a tua mae')
                 # diz que n é válido
                  
# YUMMY PICKLE IN MY TUMMY (estou a enloucecer)   
def Saveg():
    #guadrar 
    global guy,sack,equi,cguy,battle,cheses,monmon,savv
    savv = [guy,sack,equi,cguy,battle,cheses,monmon]
    pick= open('Game.data','bw')
    pickle.dump(savv,pick)
    pick.close()
   
    print('saved')  
    
def Loadg():
    # ler do pickle o q foi guardado 
    global guy,sack,equi,cguy,battle,cheses,monmon,savv 
    loadingtime = [guy,sack,equi,cguy,battle,cheses,monmon]
    loadd = True
    loaded= [None,None,None,None,None,None,None]
    try:
    #ler e por os dados no list que vai ser usado no jogo
    # !!!IMPORATNTE++!! se o que obtivemos de DADOS.data n for uma lista , ignora o que estava dentro e criar uma lista vazio
      pick= open('GAME.data','br')
      loaded= pickle.load(pick)
      if type(loaded) != list:
        loaded = []
        loadd = False
      if len(loaded) != len(loadingtime):
        loaded = []
        loadd = False
     # ver se podemos usar a bosta guardada                       
    except:
     pick= open('GAME.data','bw')
     pick.close()

    if loadd == False:
        print('saved file unreadable')
    else:
        for i in range(len(loadingtime)):
            loaded[i]= loadingtime[i]
        


       
          



def Bsort(liss):
    #vamos fazer um bubble sort
    count = -1 
    iliss = liss
    temp1 = 0
    temp2 = 0
    while count != 0:
     count = 0
     for i in range(len(liss)-1):
        if iliss[i]>iliss[i+1]:
            temp1 = iliss[i]
            temp2 = iliss[i+1]
            iliss[i+1] = temp1
            iliss[i] = temp2
            count += 1
        
    return iliss
#Ainda n usados

def Wbloc(guy, liss):
    # dá-nos o bloco que se encontra no lugar do caracter
  axix = guy.abaxix // 50
  axiy = guy.abaxiy // 50
  if guy.abaxix//50 != 0:
        axix +=1
  if guy.abaxiy//50 != 0:
        axiy +=1
  bloc = Find(liss,axix,axiy)
  return bloc


#USER INTERFACE       
sg.theme("Dark Amber")


def NewGame():
    
    layout2=[[sg.Text("Enter your username you fing mf lasagna")],
              [sg.InputText(key="username")],
                [sg.Button("Play")],
                [sg.Text("")],
                [sg.Button("Quit")]]
    pass
    window= sg.Window("Your Mum",layout2,size=(300,200),element_justification="center" ) 
    
  
    while True:
     event,values = window.read()
     user=values["username"]
     pass
     if event == sg.WIN_CLOSED  or event == "Quit": 
       print("Quit")
       
       window.close()
       pygame.quit()
       break
     elif user:
         if event=="Play":
             Ar=open("Progresso","bw")
             Ar.close()
             window.close()
             break   
   
     elif not user:
         print("enter a fucking username")
         if event =="Play":
             None     
        


def main():
 layout =[[sg.Text("")],
          [sg.Button("New Game",size=(20,2))],
          [sg.Text("")],
          [sg.Button("Continue",size=(20,2))],
          [sg.Text("")],
          [sg.Button("Tutorial",size=(20,2))],  #Dps vê se queres espaçado ou n os botoes e vê se queres meter tutorial
          [sg.Text("")],
          [sg.Button("Quit" ,size=(20,2))]]
 
 window=sg.Window("Your Mum",layout,size=(500,350),element_justification="center")


 while True:
     
     event,values = window.read()
     if event == sg.WIN_CLOSED  or event == "Quit": 
      print("Quit")
      
      window.close()
      pygame.quit()
      break
      
   
     elif event == "New Game":
      
      window.close()
      NewGame()

 window.close()
      


#INICIALIZAR


main()
savv = []
scran = []
sack = []

Inii(scran)#mete o ecrã todo com Sea
#REVE o SETT
Sett(scran,Square(scran,2,1,4),Land) #Sett muda o tipo de bloco para um novo(Land,Sea)
Sett(scran,Square(scran,5,5,8),Land) # Square(x,y que começa e o tamnho do quadrado)
Sett(scran,Square(scran,0,0,3),Land)
Sett(scran,Square(scran,11,7,7),Sand)
Sett(scran,Square(scran,15,2,5),Sand)
Sett(scran,Square(scran,20,10,4),Dirt)
Sett(scran,Square(scran,18,1,6),Dirt)
cguy = Cdude()
guy = Dude()
#items
wlvl1 = Wand('Wand for novince',5,30)
wlvl1.img = pygame.image.load(r"C:\Users\luyao\OneDrive\Desktop\YAOI\wand lvl1.png")
wlvl2 = Wand('Old Wand',10,40)
wlvl2.img = pygame.image.load(r"C:\Users\luyao\OneDrive\Desktop\YAOI\wand lvl2.png")
#chests
ches1 = Chest(20,20,wlvl1)
ches2 = Chest(600,350,wlvl2)
cheses = [(20,20,ches1),(600,350,ches2)]
#monsters
slims = Mcountainer(Slime_W,Slime_W,Slime_W)

#current equipment
equi = []
monmon = [Monsta(120,120,Slime_W,slims),Monsta(600,340,Slime_W,slims)]


pygame.init()
screen = pygame.display.set_mode((1300, 700))
clock = pygame.time.Clock()
running = True

#inicializar
locked = False
battle = False
myturn = True
Loadg()
Iniim(scran,cheses,monmon) 
#meter os objetos 

screen.blit(guy.imag,(guy.abaxix,guy.abaxiy))

#A TUA MAE
pygame.display.set_caption('A TUA MAE')

while running == True:
  
 # screen.blit(map,idkrect)
 # screen.blit(scran[1].type.imag,scran[1].type.imag.get_rect())
  events = pygame.event.get()
  for event in events:
     if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_1:
            screen.fill((255, 0, 0))
     if event.type == pygame.QUIT:
         running = False    
  if locked == False:
    Move_d(guy,events,screen,scran,cheses,monmon)       
  Fetch(sack,cheses,guy,events) 
  Encount(monmon,guy)
  if battle == True:
    Battlem1(screen,Encountw(monmon,guy), equi,events,Encountwi(monmon,guy))  
  pygame.display.flip()
  
pygame.quit() 

#FAz o pickle BOA SORTE VAIS PRECISAR
Saveg()

