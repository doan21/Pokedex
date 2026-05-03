6
import csv #import the file
import sys 
import random
csv_file_path ='Pokemon.csv'
with open(csv_file_path, 'r') as csv_file: #open the file with the pokemon
  csv_reader = csv.reader(csv_file)
  pokedex_reader = csv.DictReader(csv_file)
def header():
  '''create header''' 
  print(f'{"No":<4} {"Name":<31}{"Type 1":<9}{"Type 2":<11}{"Total":<8}{"HP":<5}'
  f'{"Attack":<10}{"Defense":<10}{"Sp. Atk":<10}{"Sp. Def":<11}{"Speed":<9}' 
  f'{"Generation":<14}{"Legendary":<10}')

  
def table(row): 
  '''formatting the data from the csv file'''
  no0 = row.get('No', 0) #getting data for each columns and assign to a variable
  name0 = row.get('Name', 0)
  type10= row.get('Type 1', 0)
  type20= row.get('Type 2', 0)
  total0 = row.get("Total", 0)
  hp0 = row.get("HP", 0)
  atk0 = row.get("Attack", 0)
  def0 = row.get("Defense", 0)
  spatk0 = row.get("Sp. Atk", 0)
  spdef0 = row.get("Sp. Def", 0)
  speed0  = row.get("Speed", 0)
  gen0 = row.get("Generation", 0)
  legen0 = row.get("Legendary", 0)
  print(f'{no0:<4} {name0:<30} {type10:<8} {type20:<11} {total0:<6} {hp0:<7}'
          f'{atk0:<10}{def0:<10}{spatk0:<10}{spdef0:<10}{speed0:<12}{gen0:<12}{legen0:<10}')
  #formatting the spacing 
  print()
 
def ask_function(): 
  '''menu function to show user all the options'''
  print("1. Display selected number of Pokemons with their types and statistics")
  print("2. Display the first Pokemon of a Type of the trainer’s choice")
  print("3. Display all Pokemons with Total Base stat of the trainer’s choice")
  print("4. Display all Pokemons with a minimum set of stats")
  print("5. Display all legendary Pokemons of Types of the trainer’s choice")
  print("6. Grab another friend and battle! ")
  print("7. If u are smart then choose this")
  print("0. Quit")
  print()
  

def pokedex():
  '''main function of pokedex'''
  csv_file_path ='Pokemon.csv'
  with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    pokedex_reader = csv.DictReader(csv_file)
    
  #1st function, display certain number of pokemon
  if choose_function == '1':
          number_of_pokemon = int(input("Number of Pokemon? "))
          
          with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            pokedex_reader = csv.DictReader(csv_file)
            rows_printed=0
            
            for row in pokedex_reader:
              if 0 < number_of_pokemon <= 800:
                header()
                table(row)
                rows_printed+=1
                if rows_printed == number_of_pokemon:
                #printing the row until the desired number of pokemons is met
                  break
              else: 
                print("Invalid number of Pokemon")
                break
  #2nd function find the type of the pokemon
  elif choose_function == '2':
          type_of_pokemon = input("Type? ")
          with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            pokedex_reader = csv.DictReader(csv_file)
            
            for row in pokedex_reader: 
               #assign the value in Type 1 and Type 2 to 2 variables 
              type1= row["Type 1"].lower()
              type2 = row["Type 2"].lower()

              if type_of_pokemon.lower() in type1 or type_of_pokemon.lower() in type2:
                #print only the first pokemon that meet the criteria 
                header()
                table(row)
                break
            else:
              print(f"No match found for type '{type_of_pokemon}'.")
              print()

  #3rd function find the total base stat of the pokemon
  elif choose_function == '3':
          total_base_stat = input("Total Base stat? ")
          with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            pokedex_reader = csv.DictReader(csv_file)
            found_match = False
            header_printed = False
            for row in pokedex_reader:
              if total_base_stat in row["Total"]:
                #check for all the row with exact value of Total 
                if not header_printed:
                  header()
              
                table(row)
                header_printed = True
                found_match = True
            if not found_match:
                print("No pokemon with that total base stat.")
                print()
                

  #4th function find a certain pokemon given stats
  elif choose_function == '4':
          hp= int(input("Min HP? "))
          atk= int(input("Min Attack? "))
          defense = int(input("Min Defense? "))
          sp_atk = int(input("Min Special Attack? "))
          sp_def= int(input("Min Special Defense? "))
          speed = int(input("Min Speed? "))
          with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            pokedex_reader = csv.DictReader(csv_file)
            
            found_match = False
            header_printed = False
            for row in pokedex_reader:
              #check for pokemons with all the stats meeting the minimum value
               if (
                 int(row["HP"]) >= hp and
                 int(row["Attack"]) >= atk and
                 int(row["Defense"]) >= defense and
                 int(row["Sp. Atk"]) >= sp_atk and
                 int(row["Sp. Def"]) >= sp_def and
                 int(row["Speed"]) >= speed
               ) :
                 if not header_printed:
                   header()
                 
                 table(row)
                 header_printed = True
                 found_match = True
            if not found_match:
                 print("No Pokemon with stats meeting the specified criteria.")
                 print()
                 

  #5th function print all pokemon of certain type
  elif choose_function == '5':
        type_of_pokemon= input("Type? ")
        with open(csv_file_path, 'r') as csv_file:
          csv_reader = csv.reader(csv_file)
          pokedex_reader = csv.DictReader(csv_file)
          header_printed = False
          found_match = False
          for row in pokedex_reader:

            if row["Legendary"] == 'TRUE': #check if a pokemon is legendary
              #if yes then assign its respective types to two variables
              type1= row["Type 1"].lower()
              type2 = row["Type 2"].lower()

              if (
                type_of_pokemon.lower() in type1
                or type_of_pokemon.lower() in type2
                
                 ):
                if not header_printed:
                  header()
                
                table(row) #print the stat for all chosen pokemons
                
                found_match = True 
                header_printed = True

          if not found_match:
            print(f"No match found for type '{type_of_pokemon}'.")
            print()

  #6th function exit program
  elif choose_function == '0': 
    print("Goodbye!")
    sys.exit() #exit the program

  #surprise: pokemon battle
  elif choose_function == '6':
    def load_pokemon():
      '''load the pokemon data from csv file to a dictionary'''
      csv_file_path = 'Pokemon.csv'
      with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        pokedex_reader = csv.DictReader(csv_file)
        pokemons = {}
        for row in pokedex_reader:
          #the name of the pokemon is the key and the value is the dictionary of its stats
          pokemon_name = row['Name']
          pokemons[pokemon_name] = {
              'No': row['No'],
              'Type 1': row['Type 1'],
              'Type 2': row['Type 2'],
              'Total': row['Total'],
              'HP': row['HP'],
              'Attack': row['Attack'],
              'Defense': row['Defense'],
              'Sp. Atk': row['Sp. Atk'],
              'Sp. Def': row['Sp. Def'],
              'Speed': row['Speed'],
              'Generation': row['Generation'],
              'Legendary': row['Legendary']
          }
        return pokemons

    pokemons = load_pokemon()

    #check the types of chosen pokemons using the database dictionary
    p1 = input("Player 1 chooses Pokemon: ").capitalize()
    p2 = input("Player 2 chooses Pokemon: ").capitalize()
    

    #this is the list of types and their effects when fight against other types
    if p1 in pokemons and p2 in pokemons:
      csv_file_path = 'chart.csv'
      type11 = pokemons[p1]["Type 1"]
      type21 = pokemons[p1]["Type 2"]
      type12 = pokemons[p2]["Type 1"]
      type22 = pokemons[p2]["Type 2"]
      with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        types = csv.DictReader(csv_file)
        type_stat1_p1={}
        type_stat2_p1={}
        type_stat1_p2={}
        type_stat2_p2={}
        for row in types:

          #check if one of the pokemon doesnt have type 2
          if len(type21) == 0 or len(type22) == 0: 
            ovr_type2_p1= float(1)
            ovr_type2_p2= float(1)
          if type11 == row['Attacking']:
            #append stat of pokemon into a dictionary
            type_stat1_p1[p1] = {
                'Normal': row['Normal'],
                'Fire': row['Fire'],
                'Water': row['Water'],
                'Electric': row['Electric'],
                'Grass': row['Grass'],
                'Ice': row['Ice'],
                'Fighting': row['Fighting'],
                'Poison': row['Poison'],
                'Ground': row['Ground'],
                'Flying': row['Flying'],
                'Psychic': row['Psychic'],
                'Bug': row['Bug'],
                'Rock': row['Rock'],
                'Ghost': row['Ghost'],
                'Dragon': row['Dragon'],
                'Dark': row['Dark'],
                'Steel': row['Steel'],
                'Fairy': row['Fairy']
            }
          if len(type21) > 0 and len(type22) > 0 :  #need check if pokemon has type 2
            type_stat2_p1[p1] = {
              'Normal': row['Normal'],
              'Fire': row['Fire'],
              'Water': row['Water'],
              'Electric': row['Electric'],
              'Grass': row['Grass'],
              'Ice': row['Ice'],
              'Fighting': row['Fighting'],
              'Poison': row['Poison'],
              'Ground': row['Ground'],
              'Flying': row['Flying'],
              'Psychic': row['Psychic'],
              'Bug': row['Bug'],
              'Rock': row['Rock'],
              'Ghost': row['Ghost'],
              'Dragon': row['Dragon'],
              'Dark': row['Dark'],
              'Steel': row['Steel'],
              'Fairy': row['Fairy']
          }
            ovr_type2_p1 = float(type_stat2_p1[p1][type22])




          if type12 == row["Attacking"]:
            type_stat1_p2[p2] = {
                'Normal': row['Normal'],
                'Fire': row['Fire'],
                'Water': row['Water'],
                'Electric': row['Electric'],
                'Grass': row['Grass'],
                'Ice': row['Ice'],
                'Fighting': row['Fighting'],
                'Poison': row['Poison'],
                'Ground': row['Ground'],
                'Flying': row['Flying'],
                'Psychic': row['Psychic'],
                'Bug': row['Bug'],
                'Rock': row['Rock'],
                'Ghost': row['Ghost'],
                'Dragon': row['Dragon'],
                'Dark': row['Dark'],
                'Steel': row['Steel'],
                'Fairy': row['Fairy']
            }
          if len(type22) > 0 and len(type21)>0:  #need check if pokemon has type 2
            type_stat2_p2[p2] = {
              'Normal': row['Normal'],
              'Fire': row['Fire'],
              'Water': row['Water'],
              'Electric': row['Electric'],
              'Grass': row['Grass'],
              'Ice': row['Ice'],
              'Fighting': row['Fighting'],
              'Poison': row['Poison'],
              'Ground': row['Ground'],
              'Flying': row['Flying'],
              'Psychic': row['Psychic'],
              'Bug': row['Bug'],
              'Rock': row['Rock'],
              'Ghost': row['Ghost'],
              'Dragon': row['Dragon'],
              'Dark': row['Dark'],
              'Steel': row['Steel'],
              'Fairy': row['Fairy']
          }

            ovr_type2_p2 = float(type_stat2_p2[p2][type21])


      ovr_type1_p1 = float(type_stat1_p1[p1][type12])
      ovr_type1_p2 = float(type_stat1_p2[p2][type11])
    else: 
      print("Invalid Pokemon name.")
    
    def pokemon_duel(p1, p2):

      #extract and assign the stat of two pokemons from the dictionaries above
      p1_stat = pokemons[p1]
      p2_stat = pokemons[p2]
      p1_attack = float(p1_stat["Attack"])
      p1_defense = float(p1_stat["Defense"])
      p1_sp_atk = float(p1_stat["Sp. Atk"])
      p1_sp_def = float(p1_stat["Sp. Def"])
      p1_hp = float(p1_stat["HP"])
      p2_attack = float(p2_stat["Attack"])
      p2_defense = float(p2_stat["Defense"])
      p2_sp_atk = float(p2_stat["Sp. Atk"])
      p2_sp_def = float(p2_stat["Sp. Def"])
      p2_hp = float(p2_stat["HP"])

      print(p1,"'s stat:",p1_stat)
      print()
      print(p2,"'s stat:",p2_stat)
      
      #js need to embrace this :)))))))
      damage1 = (p1_attack**2 * ovr_type1_p1 * ovr_type2_p1*0.2) / p2_defense
      damage2 = (p2_attack**2 * ovr_type1_p1 * ovr_type2_p1*0.2) / p1_defense
      special_dam1 = (p1_sp_atk**2 * ovr_type1_p1 * ovr_type2_p1*0.2) / p2_sp_def
      special_dam2 = (p2_sp_atk**2 * ovr_type1_p1 * ovr_type2_p1*0.2) / p1_sp_def

      if int(p1_stat['Speed']) >= int(p2_stat['Speed']): #speed check for who goes first
        print(p1, "is going to start first!")

        round_no = 1
        while p1_hp > 0 and p2_hp > 0:
          chances= random.randint(1, 2)
          #50% chance special attack, 50% chance normal attack
          if chances == 1 :
            print("Round:",round_no)
            print(p1, "uses a normal attack!")
            print(p1,"deals",damage1,"damage to",p2)
            p2_hp -= damage1
            if p2_hp <= 0: #check if 2nd pokemon is dead
              print(p2, "HP is O")
              print(p1, "won!")
              print()
            else:  #if not then pokemon 2 will attack
              print(p2, "HP:", p2_hp)
              print()
              chances=random.randint(1, 2)
              if chances == 1 :
                print(p2, "uses a normal attack!")
                print(p2,"deals",damage2,"damage to",p1)
                p1_hp -= damage2
                if p1_hp<=0:
                  print(p1, "HP is O")
                  print(p2, "won!")
                  print()
                else:
                  print(p1, "HP:", p1_hp)
                  print()

              elif chances == 2 :
                print(p2, "uses a special attack!")
                p1_hp -= special_dam2
                print(p2,"deals",special_dam2,"damage to",p1)
                if p1_hp<=0:
                  print(p1, "HP is O")
                  print(p2, "won!")
                  print()
                else:
                  print(p1, "HP:", p1_hp)
                  print()
              round_no+=1
          elif chances == 2:
            print("Round:",round_no)
            round_no+=1
            print(p1, "uses a special attack!")
            print(p1,"deals",special_dam1,"damage to",p2)
            p2_hp -= special_dam1 
            if p2_hp <= 0:
              print(p2, "HP is O")
              print(p1, "won!")
              print()
            else: 
              print(p2, "HP:", p2_hp)
              print()
              chances =random.randint(1, 2)
              if chances == 1 :
                print(p2, "uses a normal attack!")
                print(p2,"deals",damage2,"damage to",p1)
                p1_hp -= damage2
                if p1_hp<=0:
                  print(p1, "HP is O")
                  print(p2, "won!")
                  print()
                else:
                  print(p1, "HP:", p1_hp)
                  print()
              elif chances == 2 :
                print(p2, "uses a special attack!")
                print(p2,"deals",special_dam2,"damage to",p1)
                p1_hp -= special_dam2
                if p1_hp<=0:
                  print(p1, "HP is O")
                  print(p2, "won!")
                  print()
                else:
                  print(p1, "HP:", p1_hp)
                  print()

      elif int(p1_stat['Speed']) < int(p2_stat['Speed']):
          print(p2, "is going to start first!")

          round_no = 1
          while p1_hp > 0 and p2_hp > 0:
            chances=random.randint(1, 2)

            if chances == 1:
              print("Round:",round_no)
              round_no+=1
              print(p2, "uses a normal attack!")
              print(p2,"deals",damage2,"damage to",p1)
              p1_hp -= damage2
              if p1_hp <= 0:
                print(p1, "HP is O")
                print(p2, "won!")
                print()
              else: 
                print(p1, "HP:", p1_hp)
                print()
                chances=random.randint(1, 2)
                if chances == 1 :
                  print(p1, "uses a normal attack!")
                  print(p1,"deals",damage1,"damage to",p2)
                  p2_hp -= damage1
                  if p2_hp <= 0:
                    print(p2, "HP is O")
                    print(p1, "won!")
                    print()
                  else:
                    print(p2, "HP:", p2_hp)
                    print()
                elif chances == 2 :
                  print(p1, "uses a special attack!")
                  p2_hp -= special_dam1
                  print(p1,"deals",special_dam1,"damage to",p2)
                  if p2_hp<=0:
                    print(p2, "HP is O")
                    print(p1, "won!")
                    print()
                  else:
                    print(p2, "HP:", p2_hp)
                    print()


            elif chances == 2:
              print("Round:",round_no)
              round_no+=1
              print(p2, "uses a special attack!")
              print(p2,"deals",special_dam2,"damage to",p1)
              p1_hp -= special_dam2
              if p1_hp <= 0:
                print(p1, "HP is O")
                print(p2, "won!")
                print()
              else: 
                print(p1, "HP:", p1_hp)
                print()
                chances = random.randint(1, 2)
                if chances == 1 :
                  print(p1, "uses a normal attack!")
                  print(p1,"deals",damage1,"damage to",p2)
                  p1_hp -= damage2
                  if p2_hp<=0:
                    print(p2, "HP is O")
                    print(p1, "won!")
                    print()
                  else:
                    print(p2, "HP:", p2_hp)
                    print()
                elif chances == 2 :
                  print(p1, "uses a special attack!")
                  print(p1,"deals",special_dam1,"damage to",p2)
                  p2_hp -= special_dam1
                  if p2_hp<=0:
                    print(p2, "HP is O")
                    print(p1, "won!")
                    print()
                  else:
                    print(p2, "HP:", p2_hp)
                    print()

    if p1 in pokemons and p2 in pokemons:
      pokemon_duel(p1,p2)

  elif choose_function == '7':
    def surprise2():
      print('01010000 01101111 01101011 01100101 01101101 01101111 01101110 00100000 01000111 01001111 00101110 01100101 01111000 01100101')
      ans=input('Key in password: ')
      while ans!='Pokemon GO.exe':
        ans=input('Try again: ')
      print('\nWELCOME!!!!!\nWorld dimension: 100x100\nMovement controls: \n1) Forward (w) \n2) Backwards (s) \n3) Left (a) \n4) Right (d) \n5) Sprint(r)\nSpecial surprise at the middle of the map~')
      x=50
      y=0
      alive=True
      coordinate=[x,y]
      i=1
      entitymovement=True

      #tree generator
      obstacles={}
      while i<=31:
        name='tree'+str(i)
        extra={name:[random.randint(0,100),random.randint(1,100)]}
        for a in obstacles:
          if obstacles[a]==extra:
            extra=None
        obstacles.update(extra)
        i+=1

      #Pokemon generator
      pokemonsloc={0:[55,3]}
      pokemonsname={0:'Bulbasaur',1:'Zubat',2:'Oddish',3:'Charmander',4:'Charmeleon',5:'Paras',6:'Squirtle',7:'Wartortle',8:'Caterpie',9:'Venemoth',10:'Butterfree',11:'Weedle',12:'Beedril',13:'Pidgey',14:'Psyduck',15:'Pidgeot',16:'Rattata',1:'Arcanine',17:'Spearow',18:'Poliwag',19:'Ekans',20:'Arbok',21:'Tentacool',22:'Golem',23:'Sandshrew',24:'Ponyta',25:'Slowbro',26:'Doduo',27:'Nidoqueen',28:'Grimer',29:'Nidoking'}
      i=0
      while i<30:
        extra={i:[random.randint(0,100),random.randint(1,100)]}
        pokemonsloc.update(extra)
        a=1
        while a<len(pokemonsloc):
          if pokemonsloc[a]==pokemonsloc[a-1]:
            pokemonsloc.pop(a)
          a+=1
        i+=1

      #Movement
      stamina=10
      chase=False
      exit=[(random.randint(0,99)),float(random.randint(0,99))]
      entity=[float(random.randint(48,52)),float(random.randint(48,52))]
      while alive==True: #check if user is able to move
        move=input('\nMove: ')
        d=1
        coordinate=[x,y]
        if move=='r':
          move=input('Which direction?: ')
          if stamina>1:
            d=2
            stamina-=2
          else:
            print('Not enough stamina!')
            d=1
        if move=='w': #movement in 4 directions
          y+=d
        elif move=='s':
          y-=d
        elif move=='a':
          x-=d
        elif move=='d':
          x+=d
        else:
          d=0
          print('Invalid move')
        coordinate=[x,y]
        if stamina<10 and d==1:
          stamina+=1
        print('\nYour coordinate: {} \nStamina left: {}'.format(coordinate,stamina))

        

        for i in obstacles: #colliding with obstacles
          if coordinate==obstacles[i]:
            y-=1
            coordinate=[x,y]
            print('Your new coordinate:',coordinate,'Can\'t move forward, there\'s a tree in front of you')

         #catching Pokemons
        inventory=[]
        for j in pokemonsloc:
          if coordinate[0] in range(pokemonsloc[j][0]-3,pokemonsloc[j][0]+3) and coordinate[1] in range(pokemonsloc[j][1]-3,pokemonsloc[j][1]+3):
            print('\n',pokemonsname[j],'is here at',pokemonsloc[j],'!!')
          if coordinate==pokemonsloc[j]:
            c=input('You found {}!! Catch it? [Y/N]: '.format(pokemonsname[j]))
            if c.upper()=='Y':
              numlst = list(range(10)) 
              random.shuffle(numlst)
              num=numlst[0:6]
              if int(input('\nEnter a number between 0-9: ')) in num:
                print('\nSuccess!! You caught{}'.format(pokemonsname[j]))
                inventory.append(pokemonsname[j])
                del pokemonsloc[j]
                break
              else:
                print('\n{} ran away womp womp!'.format(pokemonsname[j]))
                del pokemonsloc[j]
                break
            else:
              print('\nOk let\'s move on')
              break

        #Stamina replenishment
        if stamina==0:
          j=input('\nYou\'re currently a bit tired, let\'s eat a Pokemon to replenish your stamina!! [Y/N]:'  )
          if j.upper()=='Y':
            if len(inventory)>0:
              eat=inventory.pop(0)
              print('\nYou ate {}!'.format(eat))
              stamina+=10
              print('Stamina replenished!')
            else:
              print('\nYou don\'t have any Pokemon to eat!')
            
        #End game entity
        x1=coordinate[0]>entity[0]-5 and coordinate[0]<entity[0]+5
        x2=coordinate[0]>entity[0]-4 and coordinate[0]<entity[0]+4
        y1=coordinate[1]>entity[1]-5 and coordinate[1]<entity[1]+5
        y2=coordinate[1]>entity[1]-4 and coordinate[1]<entity[1]+4
        x3=coordinate[0]<=entity[0]-2 and coordinate[0]>=entity[0]+2
        y3=coordinate[1]<=entity[1]-2 and coordinate[1]>=entity[1]+2
        if x1==True and y1==True:
          print('You\'re within the range an unknown entity')
          if x2==True and y2==True:
            print('\ncongRatUlatioNs!!\nRun to {} now!!'.format(exit)) 
            print('The entity is [{},{}] away from you'.format(abs(entity[0]-coordinate[0]),abs(entity[1]-coordinate[1])))
            chase=True #initiating a chase
        
        #Entity tracking user motion
        if chase==True and alive==True and entitymovement==True:
          if entity[0]>coordinate[0]:
            if move=='a'or'd': #movement in 4 directions
              entity[0]-=1.2
          elif entity[0]<coordinate[0] and():
            if move=='d'or'a':
              entity[0]+=1.2
          if entity[1]>coordinate[1] and (move=='w' or move=='s'):
              entity[1]-=1.2
          elif entity[1]<coordinate[1] and (move=='s'or move=='w') :
              entity[1]+=1.2
          if x3==True and y3==True:
            entitymovement=True
          print('Entity: ',entity)
            
        #Entity closing up the gap
        if abs(entity[0]-coordinate[0])<1:
          entity[0]=coordinate[0]
        if abs(entity[1]-coordinate[1])<1:
          entity[1]=coordinate[1]
        if entity==coordinate:
          o=input('\nYou\'re hunted down by the unknown entity!! Sacrifece a Pokemon? [Y/N]: ')
          if o.upper=='Y':
            if len(inventory)>0:
              print(inventory)
              choice=input('Choose a Pokemon : ')
              while choice.capitalize() not in inventory:
                choice=input('No such Pokemon found')
              dead=inventory.pop(choice.capitalize())
              print('\n{} is dead~'.format(choice))
              print('The entity is stunned for 1 round')
              entitymovement=False
            else:
              print('\nUh oh, nowhere to hide?')
              alive=False
              chase=False
          else:  
            alive=False
            chase=False
        if coordinate==exit: #escaping
          print('You\'ve escaped the game!')
          break
        
        if x <0: #limit within 100x100
          print('you cannot ESCAPE!!')
          x=0
        elif y<0:
          print('you cannot ESCAPE!!')
          y=0
        elif x>100:
          print('you cannot ESCAPE!!')
          x=100
        elif y>100:
          print('you cannot ESCAPE!!')
          y=100
      if alive==False:
        print('\n...: Help, I\'ve been trapped in here for YEARS, let me out, LET ME O.......\n*****GAME OVER*****\n')
      else:
        print('Thanks for playing!!')
    surprise2()

ask_function()
choose_function = input("Function? ")
print()
pokedex()

while choose_function != '0' :
  #loop the main function until the user chooses to exit
  ask_function()
  choose_function = input("Function? ")
  print()
  pokedex()


  

      
      
    
      
  
  
  
        
      
  
    