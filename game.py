import random
import time
class Character(object):
    def __init__(self,name,attack,pp,hp,mp):
        self.name = name
        self.attack = attack
        self.pp = pp
        self.hp = hp
        self.mp = mp


class Enemy(object):
    def __init__(self,name,attack,hp):
        self.name = name
        self.attack = attack
        self.hp = hp

greek_name = ['Alpha','Beta','Gamma','Delta']
                 #(name,attack,pp,hp,mp)
figaro = Character('Figaro',70,150,105,110)
jugalo = Character('Jugalo',180,50,180,120)
eagalo = Character('Eagalo',100,100,100,100)
randalo = Character('Randalo',random.randint(60,150),random.randint(50,150),random.randint(80,150),random.randint(50,150))

charlist = [figaro,jugalo,eagalo,randalo]
#bosses
monster = Enemy('Monster',40,random.randint(2000,3000))
monster2 = Enemy('Retsnom',60,random.randint(2000,2550))
monster3 = Enemy('Stermon',30,random.randint(2000,3551))
monster4= Enemy('Nomrets',40,random.randint(2000,3551))

monlist = [monster,monster2,monster3,monster4]

#normal enemies
monton = Enemy('Monton',20,500)
mondeen = Enemy('Mondeen',30,500)
big_spider = Enemy('Giant Spider',40,2000)
small_spider = Enemy('Spider',20,300)
slime = Enemy('Slime',10, 600 )
bats = Enemy('Bat',14, 655)
ghost = Enemy('Ghost',50,700)
snakes = Enemy('Snakes',45, 450)
rock = Enemy('Rock',5,10)
mushroom = Enemy('Mushroom',10, 400)
posion_mushroom = Enemy('Dark Mushroom',25,600)
def heal(person):
    if p1.pp > 0:
        recovered = (person.mp + person.attack) * 0.5
        person.pp -= 5
        return round(recovered)
    else:
        print p1.name + ' is out of PP.'
def action_statement(person, action):
    print person.name,action+'!'
def att(p1):
    attack = p1.attack + random.randint(2,6)
    return attack


def mag(p1):
    if p1.pp > 0:
        magic = (p1.attack + p1.mp) + random.randint(2,3)
        p1.pp -= 5
        return magic
    else:
        print p1.name+' is out of PP!'

def mon_att(mon,p1,p2,p3,p4):
    crit = random.randint(1,100)
    turn = 0
    if crit > 20:
        num = random.randint(1,11)

        if num == 1 or num == 5:
            dmg = att(mon)
            p1.hp -= dmg
            print('The enemy attacks '+p1.name)
            turn +=1
        elif num == 2 or num == 6:
            dmg = att(mon)
            p2.hp -= dmg
            print('The enemy attacks '+p2.name)
            turn +=1
        elif num == 3 or num == 7:
            dmg = att(mon)
            p3.hp -= dmg
            print('The enemy attacks '+p3.name)
            turn +=1
        elif num == 4 or num == 8:
            dmg = att(mon)
            p4.hp -= dmg
            print('The enemy attacks '+p4.name)
            turn +=1
        else:
            print( 'The enemy missed!')
            turn +=1
    else:
        dmg = mon.attack * 4
        greek = greek_name[random.randint(0,3)]
        print( mon.name+' used ' + greek+' attack!')
        if greek == greek_name[0] or greek_name[2]:
            p1.hp -= dmg
            p3.hp -= dmg
            
        elif greek == greek_name[1] or greek_name[3]:
            p2.hp -= dmg
            p4.hp -= dmg



def player_status(person):
    print(person.name + " | HP = " + str(person.hp) + " | PP = " + str(person.pp))

def player_moves(player,mon,p2,p3,p4):
    turn = True
    attack = ['a','attack','Attack']
    magic = ['m','magic','MAGIC', 'Magic']
    heals = ['h','heal','HEAL','Heal']
    skip = ['skip','s','SKIP']
    while turn:
        if player.hp < 0:
            print (player.name+' is unable to battle.')
            turn = False

        else:
            action = raw_input('What will '+player.name+' do? (Attack, Magic, Heal, Skip)')
            
            if action in attack:
                damage = att(player)
                mon.hp -= damage
                print (player.name+' did '+str(damage)+' damage.')
                turn = False
            
            elif action in magic:
                try:
                    damage = mag(player)
                    mon.hp -= damage
                    print (player.name+' did '+str(damage))
                    turn = False
                except:
                    print
            
            elif action in skip:
                print (player.name+ ' decided to skip.')
                turn = False
            
            elif action in heals:
                try:
                    print (player.name+ ' is going to heal who?')
                    print '1:'
                    player_status(player)
                    print '2:'
                    player_status(p2)
                    print '3:'
                    player_status(p3)
                    print '4:'
                    player_status(p4)

                    user_heal = raw_input('Who will he heal? (Type in the number above them)')
                    if user_heal == 'himself' or user_heal== player.name or user_heal =='1':
                        recovered = heal(player)
                        player.hp += recovered
                        action_statement(player,'healed himself '+' '+str(recovered))
                        turn = False
                    elif user_heal == p2.name or user_heal=='2':
                        recovered = heal(player)
                        p2.hp += recovered
                        action_statement(player,'healed '+p2.name+' '+str(recovered))
                        turn = False
                    elif user_heal == p3.name or user_heal =='3':
                        recovered = heal(player)
                        p3.hp += recovered
                        action_statement(player,'healed '+p3.name+' '+str(recovered))
                        turn = False
                    elif user_heal == p4.name or user_heal == '4':
                        recovered = heal(player)
                        p4.hp += recovered
                        action_statement(player,'healed '+p4.name+' '+str(recovered))
                        turn = False
                    else:
                        print 'His mind slipped and the healing went nowhere!'
                        turn = False
                except:
                    print ('Out of PP!')

            else:
                print ('Please try that again')

def battle_system(p1,p2,p3,p4,mon):
    
    orginalhp = mon.hp
    alive = True
    while alive:
        print (mon.name+" | HP "+str(mon.hp))
        print()
        player_status(p1)
        player_status(p2)
        player_status(p3)
        player_status(p4)
        
        player_moves(p1,mon,p2,p3,p4)
        player_moves(p2,mon,p1,p3,p4)
        mon_att(mon,p1,p2,p3,p4)
        player_moves(p3,mon,p1,p2,p4)
        player_moves(p4,mon,p1,p2,p3)
        if p1.hp <= 0 and p2.hp <= 0 and p3.hp <= 0:
            print('You lose')
            alive = False
            player_status(p1)
            player_status(p2)
            player_status(p3)
            player_status(p4)
    
            break

        if mon.hp <= 0:
            print('YOU WON')
            alive = False
            mon.hp = orginalhp

def area(area,num_floors,boss):
    place = True
    while place:
        ran_num = random.randint(1,100)
        print "There are "+str(num_floors)+ " floors in",area
        if num_floors == 1:
            print '''
            *************
            *Final floor*
            *************
            '''
            time.sleep(2)

            battle_system(figaro,jugalo,eagalo,randalo,boss)
            place = False
        else:
            direction = raw_input('Up/Down/Left/Right')
            
            if direction == 'up' or direction == 'u':
                print 'Your team moved up'
                if ran_num <= 33:
                    battle_system(figaro,jugalo,eagalo,randalo,monton)
                    num_floors -= 1
                elif ran_num >33 and ran_num <66:
                    num_floors -= 1
                elif ran_num >= 66:
                    battle_system(figaro,jugalo,eagalo,randalo,mondeen)
                    num_floors -= 1
            elif direction == 'down' or direction =='d':
                print 'Your team moved down'
                if ran_num <= 15:
                    battle_system(figaro,jugalo,eagalo,randalo,big_spider)
                    num_floors -= 1
                elif ran_num >15 and ran_num <=33:
                    battle_system(figaro,jugalo,eagalo,randalo,ghost)
                    num_floors -= 1
                elif ran_num >33 and ran_num <66:
                    num_floors -= 1
                elif ran_num >= 66:
                    battle_system(figaro,jugalo,eagalo,randalo,slime)
                    num_floors -= 1
            elif direction == 'left' or direction =='l':
                print 'Your team moved left'
                if ran_num <= 33:
                    battle_system(figaro,jugalo,eagalo,randalo,posion_mushroom)
                    num_floors -= 1
                elif ran_num >33 and ran_num <66:
                    num_floors -= 1
                elif ran_num >= 66:
                    battle_system(figaro,jugalo,eagalo,randalo,snakes)
                    num_floors -= 1
            elif direction == 'right' or direction =='r':
                print 'Your team moved right'
                if ran_num <= 33:
                    battle_system(figaro,jugalo,eagalo,randalo,bats)
                    num_floors -= 1
                elif ran_num >33 and ran_num <66:
                    num_floors -= 1
                elif ran_num >= 66:
                    battle_system(figaro,jugalo,eagalo,randalo,mushroom)
                    num_floors -= 1
            else:
                print 'Wait... where?'

area('Dungeon',3,monster)
print 'Our friends now move onto the woods'
time.sleep(1)
area('Woods Dungeon',5,monster2)
time.sleep(1)
print 'There it is. The tower.'
area('Tower',10,monster3)
