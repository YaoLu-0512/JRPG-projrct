import pygame
import math
import PySimpleGUI as sg
# meth is better


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

#FUNÇÕES MAMADAS

def Inii(liss): #coordenadas
        #iniciar
        for yi in range(14):# 0-13
            for xi in range (26): #0-25
             liss.append(Bloc(xi,13-yi,Sea)) #mete o ecrã todo com Sea
def Iniim(liss): #iniciar o MAPA TODA
        
        Pintbloc(liss) 
        screen.blit(ches1.imag,(20,20))  


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
     liss[select[b]].type = typp           # o .type tem haver com a class Bloc q muda o tipo


#Mexe Mexe
def Move_d(guy,events,screen,liss):
       
    image = guy.imag
    #backg = Land.imag
    for event in events:
     if event.type == pygame.KEYDOWN :
         if event.key == pygame.K_w  :
            #mexe para cima
             print('moved up')
             guy.abaxiy -=1   
             #ver se podemos andar
             if Waka(liss,guy.abaxix,guy.abaxiy) == True:
             #para a personagem n aparecer 2 vezes:
              Iniim(liss)
              screen.blit(image,(guy.abaxix,guy.abaxiy))
             else:
                 guy.abaxiy +=1
                 print('no lol')
             
         if event.key == pygame.K_s :
                 #mexe para baixo
             print('moved down')
             guy.abaxiy +=1
             if Waka(liss,guy.abaxix,guy.abaxiy) == True:
              Iniim(liss)
              screen.blit(image,(guy.abaxix,guy.abaxiy))
             else:
                 guy.abaxiy -=1
                 print('no lol')
     
         if event.key == pygame.K_a :
          #mexe para esquerda
             print('moved left')
             guy.abaxix -=1
             if Waka(liss,guy.abaxix,guy.abaxiy) == True:
              Iniim(liss)
              screen.blit(image,(guy.abaxix,guy.abaxiy))
             else:
                 guy.abaxix +=1
                 print('no lol')
     
     
         if event.key == pygame.K_d :
              #mexe para direita
             print('moved right')
             guy.abaxix +=1
             if Waka(liss,guy.abaxix,guy.abaxiy) == True:
              Iniim(liss)
              screen.blit(image,(guy.abaxix,guy.abaxiy))
             else:
                 guy.abaxix -=1
                 print('no lol')
    # if event.type == pygame.KEYUP:
     #    if event.key in [pygame.K_w, pygame.K_s ]:
      #       guy.abaxiy=0
       #  if event.key in [pygame.K_a, pygame.K_d]:
        #     guy.abaxix=0
def Waka(liss,raxix,raxiy):  # dá-nos a coordenada do bloco que queremos ir, e verifica se podemos, de facto, andar nele
    #Tá com uns erros
    axix = raxix // 50
    axiy = raxiy // 50
    if raxix//50 != 0:
        axix +=1
    if raxiy//50 != 0:
        axiy +=1
    bloc = Find(liss,axix,axiy)
    if liss[bloc].type.walk == False:
        return False
    else:
        return True     

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


#INICIALIZAR
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

guy = Dude()
wlvl1 = Wand('Wand for novince',5,30)
wlvl1.img = pygame.image.load(r"C:\Users\luyao\OneDrive\Desktop\YAOI\wand lvl1.png")
ches1 = Chest(20,20,wlvl1)
cheses = [(20,20,ches1)]

pygame.init()
screen = pygame.display.set_mode((1300, 700))
clock = pygame.time.Clock()
running = True


Iniim(scran) 
#meter os objetos 
screen.blit(guy.imag,(60,60))
screen.blit(ches1.imag,(20,20))
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
  Move_d(guy,events,screen,scran)       
  Fetch(sack,cheses,guy,events)  
  pygame.display.flip()

pygame.quit() 
