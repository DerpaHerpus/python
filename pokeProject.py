import random

select = {'1': 'Venusaur', '2': 'Charizard', '3': 'Blastoise', '4': 'Butterfree', '5': 'Beedrill', '6': 'Pidgeot', '7': 'Raticate', '8': 'Fearow', '9': 'Arbok', '10    ': 'Raichu', '11': 'Sandslash', '12': 'Nidoqueen', '13': 'Nidoking', '14': 'Clefable', '15': 'Ninetales', '16': 'Wigglytuff', '17': 'Golbat', '18': 'Vileplume', '19    ': 'Parasect', '20': 'Venomoth', '21': 'Dugtrio', '22': 'Persian', '23': 'Golduck', '24': 'Primeape', '25': 'Arcanine', '26': 'Poliwrath', '27': 'Alakazam', '28': '    Machamp', '29': 'Victreebel', '30': 'Tentacruel', '31': 'Golem', '32': 'Rapidash', '33': 'Slowbro', '34': 'Magneton', '35': "Farfetch'd", '36': 'Dodrio', '37': 'Dew    gong', '38': 'Muk', '39': 'Cloyster', '40': 'Gengar', '41': 'Onix', '42': 'Hypno', '43': 'Kingler', '44': 'Electode', '45': 'Exeggutor', '46': 'Marowak', '47': 'Hit    monlee', '48': 'Hitmonchan', '49': 'Lickitung', '50': 'Weezing', '51': 'Rhydon', '52': 'Chansey', '53': 'Tangela', '54': 'Kangaskhan', '55': 'Seadra', '56': 'Seakin    g', '57': 'Starmie', '58': 'Mr. Mime', '58': 'Scyther', '60': 'Jynx', '61': 'Electabuzz', '62': 'Magmar', '63': 'Pinsir', '64': 'Tauros', '65': 'Gyarados', '66': 'L    apras', '67': 'Ditto', '68': 'Vaporeon', '69': 'Jolteon', '70': 'Flareon', '71': 'Porygon', '72': 'Omastar', '73': 'Kabutops', '74': 'Aerodactyl', '75': 'Snorlax',     '76': 'Articuno', '77': 'Zapdos', '78': 'Moltres', '79': 'Dragonite', '80': 'Mewtwo'}

for x in select:
    print(x,':', select[x])
def pokePick():
    global Poke1
    global Poke2
    global Poke3
    print('')
    Poke1 = input('Select first pokemon number:' )
    print('')
    Poke2 = input('Select second pokemon number:' )
    print('')
    Poke3 = input('Select third pokemon number:' )
    print('')
    print(select[Poke1] + ', ' + select[Poke2] + ', ' + select[Poke3])
    def confirmSelect():
        ready = input('Are these the pokemon you want?(Yes or No)' )
        if ready == 'No':
            print(pokePick())
        elif ready == 'N':
            print(pokePick())
        elif ready == 'no':
            print(pokePick())
        elif ready == 'n':
            print(pokePick())
        elif ready == 'Yes':
            print('Good Choice!')
            print(pokeBattle())
        elif ready == 'Y':
            print('Good Choice!')
            print(pokeBattle())
        elif ready == 'yes':
            print('Good Choice!')
            print(pokeBattle())
        elif ready == 'y':
            print('Good Choice!')
            print(pokeBattle())
        elif ready is not 'Yes' or 'No':
            print('')
            print('Please answer yes or no')
            return confirmSelect()
    print(confirmSelect())

def pokeBattle():
    Team = [select[Poke1], select[Poke2], select[Poke3]]
    print('')
    print("These are your Pokemon!")
    print('')
    print(Team)
    print('')
    print("Alright, now it's time to battle!")
    print('')
    print('Select your first pokemon')
    myPoke = input('1: ' + select[Poke1] + ' 2: ' + select[Poke2] + ' 3: ' + select[Poke3] + ' ' )
    if myPoke == '1':
        print('')
        print(((select[Poke1])['move1']) + ((select[Poke1])['move2']) + ((select[Poke1])['move3']) + ((select[Poke1])['move4']))

Venusaur = {'type1': 'Grass', 'type2': 'Poison', 'move1': 'Sludge Bomb', 'move2': 'Giga Drain', 'move3': 'Synthesis', 'move4': 'Earthquake', 'health': '..', 'speed'    : '..'}

Charizard = {'type1': 'Fire', 'type2': 'Flying', 'move1': 'Flare Blitz', 'move2': 'Dragon Claw', 'move3': 'Earthquake', 'move4': 'Roost', 'health': '..', 'speed': '    ..'}

Blastoise = {'type1': 'Water', 'type2': 'Water', 'move1': 'Water Pulse', 'move2': 'Ice Beam', 'move3': 'Dark Pulse', 'move4': 'Aura Sphere', 'health': '..', 'speed'    : '..'}

Butterfree = {'type1': 'Grass', 'type2': 'Flying', 'move1': 'Bug Buzz', 'move2': 'Energy Ball', 'move3': 'Psychic', 'move4': 'Air Slash', 'health': '..', 'speed': '    ..'}

Beedrill = {'type1':'Grass', 'type2':'Poison', 'move1':'Bug Buzz', 'move2':'Poison Jab', 'move3':'Pursuit', 'move4':'Drill Run', 'health':'..', 'speed':'..'}

Pidgeot = {'type1':'Normal', 'type2':'Flying', 'move1':'Hurricane', 'move2':'Heat Wave', 'move3':'Roost', 'move4':'Pursuit', 'health':'..', 'speed':'..'}

Raticate = {'type1':'Normal', 'type2':'Normal', 'move1':'Crunch', 'move2':'Hyper Fang', 'move3':'Shadow Claw', 'move4':'Wild Charge', 'health':'..', 'speed':'..'}

Fearow = {'type1':'Normal', 'type2':'Flying', 'move1':'Drill Peck', 'move2':'Double Edge', 'move3':'Drill Run', 'move4':'Pursuit', 'health':'..', 'speed':'..'}

Arbok = {'type1':'Poison', 'type2':'Poison', 'move1':'Gunk Shot', 'move2':'Crunch', 'move3':'Aqua Tail', 'move4':'Earthquake', 'health':'..', 'speed':'..'}

Raichu = {'type1':'Electric', 'type2':'Eletric', 'move1':'Thunderbolt', 'move2':'Focus Blast', 'move3':'Signal Beam', 'move4':'Surf', 'health':'..', 'speed':'..'}

Sandslash = {'type1':'Ground', 'type2':'Ground', 'move1':'Earthquake', 'move2':'Stone Edge', 'move3':'Night Slash', 'move4':'Chip Away', 'health':'..', 'speed':'..'    }

Nidoqueen = {'type1':'Poison', 'type2':'Ground', 'move1':'Earth Power', 'move2':'Ice Beam', 'move3':'Sludge Wave', 'move4':'Flamethrower', 'health':'..', 'speed':'.    .'}

Nidoking = {'type1':'Poison', 'type2':'Ground', 'move1':'Sludge Wave', 'move2':'Earth Power', 'move3':'Ice Beam', 'move4':'Super Power', 'health':'..', 'speed':'..'    }

Clefable = {'type1':'Normal', 'type2':'Normal', 'move1':'Moonblast', 'move2':'Soft-Boiled', 'move3':'Focus Blast', 'move4':'Ice Beam', 'health':'..', 'speed':'..'}

Ninetales = {'type1':'Fire', 'type2':'Fire', 'move1':'Fire Blast', 'move2':'Psyshock', 'move3':'Energy Ball', 'move4':'Dark Pulse', 'health':'..', 'speed':'..'}

Wigglytuff = {'type1':'Normal', 'type2':'Normal', 'move1':'Hyper Voice', 'move2':'Dazzling Gleam', 'move3':'Fire Blast', 'move4':'Focus Blast', 'health':'..', 'speed':'..'}

Golbat = {'type1':'Poison', 'type2':'Flying', 'move1':'Roost', 'move2':'Brave Bird', 'move3':'Super Fang', 'move4':'Zen Headbutt', 'health':'..', 'speed':'..'}

Vileplume = {'type1':'Grass', 'type2':'Poison', 'move1':'Giga Drain', 'move2':'Sludge Bomb', 'move3':'Synthesis', 'move4':'Stun Spore', 'health':'..', 'speed':'..'}

Parasect = {'type1':'Bug', 'type2':'Grass', 'move1':'Energy Ball', 'move2':'Giga Impact', 'move3':'X-Scissor', 'move4':'Sysnthesis', 'health':'..', 'speed':'..'}

Venomoth = {'type1':'Bug', 'type2':'Poison', 'move1':'Bug Buzz', 'move2':'Sludge Bomb', 'move3':'Energy Ball', 'move4':'Psychic', 'health':'..', 'speed':'..'}

Dugtrio = {'type1':'Ground', 'type2':'Ground', 'move1':'Earthquake', 'move2':'Pursuit', 'move3':'Stone Edge', 'move4':'Shadow Claw', 'health':'..', 'speed':'..'}

Persian = {'type1':'Normal', 'type2':'Normal', 'move1':'Hyper Voice', 'move2':'Water Pulse', 'move3':'Night Slash', 'move4':'Power Gem', 'health':'..', 'speed':'..'}

Vileplume = {'type1':'Grass', 'type2':'Poison', 'move1':'Giga Drain', 'move2':'Sludge Bomb', 'move3':'Synthesis', 'move4':'Power', 'health':'..', 'speed':'..'}
print(pokePick())

    play_again = True
    while play_again:
        winner = None
        myPokeHP = 100
        opponentPokeHP = 100

        myPokeMoveset = myActivePokeMoves
        opponentPokeMoveset = oppActivePokeMoves

        if myPokeSpd > oppPokeSpd:
            myPokeTurn = True
            oppPokeTurn = False
        elif oppPokeSpd > myPokeSpd:
            myPokeTurn = False
            oppPokeTurn = True
        else:
            turn = random.randint(1,2)
            if turn == 1:
                myPokeTurn = True
                oppPokeTurn = False
            else:
                myPokeTurn = False
                oppPokeTurn = True

        while (myPokeHP != 0 or oppPokeHP != 0 or myPokeHP <= 0 or oppPokeHP <= 0)
            if myPokeTurn:
                print("\nPlease select a move:")
                print(myPokeMoveset)
                myPokeMove = input
                moveMiss = random.randint(1,15)
                if moveMiss = 1:
                    print('You Missed')
                else:
                    if myPokeStatus = Paralyzed or Frozen:
                        turnParalyze = random.randint(1,4)
                        if turnParalyze = 1:
                            print('Your Pokemon cannot move')
                        else:
                            pass
                        if myPokeConfusion = True:
                            confusion = random.randint(1,2)
                            if confusion = 1:
                                myPokeHP = myPokeHP - 40
                                print('Your pokemon hit itself in its confusion')
                            else:
                                moveCrit = random.randint(1,10000)
                                if moveCrit <= 625:
                                    crit = True
                                else:
                                    crit = False

                                if crit:
                                    myPokeMove = myPokeMove * 2
                                    oppPokeHP - myPokeMove
                                else:
                                    oppPokeHP - myPokeMove
                        else:
                                moveCrit = random.randint(1,10000)
                                if moveCrit <= 625:
                                    crit = True
                                else:
                                    crit = False
                                    if crit:
                                    myPokeMove = myPokeMove * 2
                                    oppPokeHP - myPokeMove
                                else:
                                    oppPokeHP - myPokeMove
            else:
                oppPokeMove = oppPokeMoveset[random.randint(1,4)]
                moveMiss = random.randint(1,15)
                if moveMiss = 1:
                    print('You Missed')
                else:
                    if oppPokeStatus = Paralyzed or Frozen:
                        turnParalyze = random.randint(1,4)
                        if turnParalyze = 1:
                            print('Your Pokemon cannot move')
                        else:
                            pass
                        if oppPokeConfusion = True:
                            confusion = random.randint(1,2)
                            if confusion = 1:
                                oppPokeHP = oppPokeHP - 40
                                print('Your pokemon hit itself in its confusion')
                            else:
                                moveCrit = random.randint(1,10000)
                                if moveCrit <= 625:
                                    crit = True
                                else:
                                    crit = False

                                if crit:
                                    oppPokeMove = oppPokeMove * 2
                                    myPokeHP - oppPokeMove
                                else:
                                    myPokeHP - oppPokeMove
                        else:
                                moveCrit = random.randint(1,10000)
                                if moveCrit <= 625:
                                    crit = True
                                else:
                                    crit = False

                                if crit:
                                    oppPokeMove = oppPokeMove * 2
                                    myPokeHP - oppPokeMove
                                else:
                                    myPokeHP - oppPokeMove
            if myPokeStatus = Burned:
                myPokeHP = myPokeHP - (myPokeHP * 0.0625)
            else:
                pass

            if myPokeStatus = Poisoned:
                myPokeHP = myPokeHP - (myPokeHP * 0.0625)
            else:
                pass
                 
            if oppPokeStatus = Burned:
                oppPokeHP = oppPokeHP - (oppPokeHP * 0.0625)
            else:
                pass

             if oppPokeStatus = Poisoned:
                 oppPokeHP = oppPokeHP - (oppPokeHP * 0.0625)
             else:
                 pass

         if oppPokeHP <= 0:
             winner = player
         elif myPokeHP <= 0:
             winner = opponent
