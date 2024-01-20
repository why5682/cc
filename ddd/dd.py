import random

def pri(*args):
    for arg in args:
        print(arg)
    input()

sd=1
bd=10
cri_my=50
hp=100
mhp=100
life=True
mb={'타우로':(30,100)}


def att(mon,mond):
    critical=False
    mon_life=True
    global hp
    while mon_life == True:
        damage = random.randint(sd, bd)
        cri=random.randint(1,100)
        if cri_my > cri :
            critical==True
            print('크리티컬!')
            damage=damage*2
        else:
            critical==False
        pri(damage,'의 피해를 주었습니다.')
        mon=mon-damage
        if mon <= 0:
            mon_life=False
        else:
            mond = mond + random.randint(-5, 5)
            print(f"{mond} suffered damage.")
            hp = hp - mond
                if hp <= 0:
                    life = False
                    mon_life = False 
    return damage





pri('어느날 대머리 도적이 살았습니다.')

pri('대머리 도적은 오늘 어디서 사냥을 할지 고민을 하고 있었습니다.')

pri('한 시청자는 황갑충이나 캐라며 타우를 잡으러 가라 권했고 다른 시청자는 파티사냥을 통해 레벨업이나 하라고 말했습니다.')

pri('대머리 도적은 ')

pri('그래 결정했어')

sc='st'

목표달성=False
while 목표달성 != True:
    if sc=='st':
        dd1=input('황갑충을 캐러 타우로 가야겠어:타우, 파티원과 레벨업을 하러 가야겠어:요람')
        if dd1 == '타우':
            print('좋아 타우를 잡으러 가야겠어!')
            sc='jj1' 
        elif dd1 == '요람':
            print('dyf')   
        else:
            sc='st'
    elif life == False:
        pri('Game Over')
    elif sc=='jj1':
        pri('그렇게 대머리 도적은 저주받은 신전2에 도착했습니다.')
        pri('여기가 저주받은 신전이구나.')
        pri('대머리 도적은 자신의 황갑충을 매만지며 창을들고 설쳐대는 타우로마시스의 대가리에 뇌전수리검을 던졌다.')
        att(*mb['타우로'])
        pri('전투 종료. 남은',hp)
        sc=5
        

    elif sc==5:
        print("일비 표창을 획득했다",'공격력이 3증가했다')
        sd= sd+3
        목표달성=True



     
     def defense():
    
       
        elif hp<=0:
            life == False
            pri('사망')
            break
        else:
            mond=mond+random.randint(-5,5)
            pri(mond,'의 피해를 입었다.')
            hp=hp-mond