import random

select = {'1': 'Venusaur', '2': 'Charizard', '3': 'Blastoise', '4': 'Butterfree', '5': 'Beedrill', '6': 'Pidgeot', '7': 'Raticate', '8': 'Fearow', '9': 'Arbok', '10    ': 'Raichu', '11': 'Sandslash', '12': 'Nidoqueen', '13': 'Nidoking', '14': 'Clefable', '15': 'Ninetales', '16': 'Wigglytuff', '17': 'Golbat', '18': 'Vileplume', '19    ': 'Parasect', '20': 'Venomoth', '21': 'Dugtrio', '22': 'Persian', '23': 'Golduck', '24': 'Primeape', '25': 'Arcanine', '26': 'Poliwrath', '27': 'Alakazam', '28': '    Machamp', '29': 'Victreebel', '30': 'Tentacruel', '31': 'Golem', '32': 'Rapidash', '33': 'Slowbro', '34': 'Magneton', '35': "Farfetch'd", '36': 'Dodrio', '37': 'Dew    gong', '38': 'Muk', '39': 'Cloyster', '40': 'Gengar', '41': 'Onix', '42': 'Hypno', '43': 'Kingler', '44': 'Electode', '45': 'Exeggutor', '46': 'Marowak', '47': 'Hit    monlee', '48': 'Hitmonchan', '49': 'Lickitung', '50': 'Weezing', '51': 'Rhydon', '52': 'Chansey', '53': 'Tangela', '54': 'Kangaskhan', '55': 'Seadra', '56': 'Seaking', '57': 'Starmie', '58': 'Mr. Mime', '58': 'Scyther', '60': 'Jynx', '61': 'Electabuzz', '62': 'Magmar', '63': 'Pinsir', '64': 'Tauros', '65': 'Gyarados', '66': 'Lapras', '67': 'Ditto', '68': 'Vaporeon', '69': 'Jolteon', '70': 'Flareon', '71': 'Porygon', '72': 'Omastar', '73': 'Kabutops', '74': 'Aerodactyl', '75': 'Snorlax',     '76': 'Articuno', '77': 'Zapdos', '78': 'Moltres', '79': 'Dragonite', '80': 'Mewtwo'}

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
    if myPoke == 1 or select[Poke1]:
        print('')
        print("These are your Pokemon's moves")
        print(((select[Poke1])['move1']) + ((select[Poke1])['move2']) + ((select[Poke1])['move3']) + ((select[Poke1])['move4']))
    if myPoke == 2 or select[Poke2]:
        print('')
        print(((select[Poke2])['move1']) + ((select[Poke2])['move2']) + ((select[Poke2])['move3']) + ((select[Poke2])['move4']))
    if myPoke == 3 or select[Poke3]:
        print('')
        print(((select[Poke3])['move1']) + ((select[Poke3])['move2']) + ((select[Poke3])['move3']) + ((select[Poke3])['move4']))

Venusaur = {'type1': 'Grass', 'type2': 'Poison', 'move1': 'Sludge Bomb', 'move2': 'Giga Drain', 'move3': 'Synthesis', 'move4': 'Earthquake', 'health': '270', 'speed': '80'}

Charizard = {'type1': 'Fire', 'type2': 'Flying', 'move1': 'Flare Blitz', 'move2': 'Dragon Claw', 'move3': 'Earthquake', 'move4': 'Roost', 'health': '266', 'speed': '100'}

Blastoise = {'type1': 'Water', 'type2': 'Water', 'move1': 'Water Pulse', 'move2': 'Ice Beam', 'move3': 'Dark Pulse', 'move4': 'Aura Sphere', 'health': '268', 'speed': '78'}

Butterfree = {'type1': 'Grass', 'type2': 'Flying', 'move1': 'Bug Buzz', 'move2': 'Energy Ball', 'move3': 'Psychic', 'move4': 'Air Slash', 'health': '230', 'speed': '70'}

Beedrill = {'type1':'Grass', 'type2':'Poison', 'move1':'Bug Buzz', 'move2':'Poison Jab', 'move3':'Pursuit', 'move4':'Drill Run', 'health':'240', 'speed':'75'}

Pidgeot = {'type1':'Normal', 'type2':'Flying', 'move1':'Hurricane', 'move2':'Heat Wave', 'move3':'Roost', 'move4':'Pursuit', 'health':'276', 'speed':'101'}

Raticate = {'type1':'Normal', 'type2':'Normal', 'move1':'Crunch', 'move2':'Hyper Fang', 'move3':'Shadow Claw', 'move4':'Wild Charge', 'health':'220', 'speed':'97'}

Fearow = {'type1':'Normal', 'type2':'Flying', 'move1':'Drill Peck', 'move2':'Double Edge', 'move3':'Drill Run', 'move4':'Pursuit', 'health':'240', 'speed':'100'}

Arbok = {'type1':'Poison', 'type2':'Poison', 'move1':'Gunk Shot', 'move2':'Crunch', 'move3':'Aqua Tail', 'move4':'Earthquake', 'health':'230', 'speed':'80'}

Raichu = {'type1':'Electric', 'type2':'Eletric', 'move1':'Thunderbolt', 'move2':'Focus Blast', 'move3':'Signal Beam', 'move4':'Surf', 'health':'230', 'speed':'110'}

Sandslash = {'type1':'Ground', 'type2':'Ground', 'move1':'Earthquake', 'move2':'Stone Edge', 'move3':'Night Slash', 'move4':'Chip Away', 'health':'260', 'speed':'65' }

Nidoqueen = {'type1':'Poison', 'type2':'Ground', 'move1':'Earth Power', 'move2':'Ice Beam', 'move3':'Sludge Wave', 'move4':'Flamethrower', 'health':'290', 'speed':'76'}

Nidoking = {'type1':'Poison', 'type2':'Ground', 'move1':'Sludge Wave', 'move2':'Earth Power', 'move3':'Ice Beam', 'move4':'Super Power', 'health':'272', 'speed':'85' }

Clefable = {'type1':'Normal', 'type2':'Normal', 'move1':'Moonblast', 'move2':'Soft-Boiled', 'move3':'Focus Blast', 'move4':'Ice Beam', 'health':'300', 'speed':'60'}

Ninetales = {'type1':'Fire', 'type2':'Fire', 'move1':'Fire Blast', 'move2':'Psyshock', 'move3':'Energy Ball', 'move4':'Dark Pulse', 'health':'256', 'speed':'100'}

Wigglytuff = {'type1':'Normal', 'type2':'Normal', 'move1':'Hyper Voice', 'move2':'Dazzling Gleam', 'move3':'Fire Blast', 'move4':'Focus Blast', 'health':'390', 'speed':'45'}

Golbat = {'type1':'Poison', 'type2':'Flying', 'move1':'Roost', 'move2':'Brave Bird', 'move3':'Super Fang', 'move4':'Zen Headbutt', 'health':'260', 'speed':'90'}

Vileplume = {'type1':'Grass', 'type2':'Poison', 'move1':'Giga Drain', 'move2':'Sludge Bomb', 'move3':'Synthesis', 'move4':'Stun Spore', 'health':'260', 'speed':'50'}

Parasect = {'type1':'Bug', 'type2':'Grass', 'move1':'Energy Ball', 'move2':'Giga Impact', 'move3':'X-Scissor', 'move4':'Sysnthesis', 'health':'230', 'speed':'30'}

Venomoth = {'type1':'Bug', 'type2':'Poison', 'move1':'Bug Buzz', 'move2':'Sludge Bomb', 'move3':'Energy Ball', 'move4':'Psychic', 'health':'250', 'speed':'90'}

Dugtrio = {'type1':'Ground', 'type2':'Ground', 'move1':'Earthquake', 'move2':'Pursuit', 'move3':'Stone Edge', 'move4':'Shadow Claw', 'health':'180', 'speed':'120'}

Persian = {'type1':'Normal', 'type2':'Normal', 'move1':'Hyper Voice', 'move2':'Water Pulse', 'move3':'Night Slash', 'move4':'Power Gem', 'health':'240', 'speed':'115'}

Golduck = {'type1':'Water', 'type2':'Water', 'move1':'Ice Beam', 'move2':'Hydro Pump', 'move3':'Confuse Ray', 'move4':'Body Slam', 'health':'270', 'speed':'85'}

Primeape = {'type1':'Fighting', 'type2':'Fighting', 'move1':'Earthquake', 'move2':'Body Slam', 'move3':'Dynamic Punch', 'move4':'Fire Punch', 'health':'240', 'speed':'95'}

Arcanine = {'type1':'Fire', 'type2':'Fire', 'move1':'Fire Blast', 'move2':'Flare Blitz', 'move3':'Body Slam', 'move4':'Heat Wave', 'health':'290', 'speed':'95'}

Poliwrath = {'type1':'Fighting', 'type2':'Water', 'move1':'Earthquake', 'move2':'Ice Punch', 'move3':'Scald', 'move4':'Dynamic Punch', 'health':'290', 'speed':'70'}

Alakazam = {'type1':'Psychic', 'type2':'Psychic', 'move1':'Psychic', 'move2':'Confusion', 'move3':'Psybeam', 'move4':'Tri Attack', 'health':'220', 'speed':'120'}

Machamp = {'type1':'Fighting', 'type2':'Fighting', 'move1':'Dynamic Punch', 'move2':'Earthquake', 'move3':'Mega Kick', 'move4':'Mega Punch', 'health':'290', 'speed':'55'}

Victreebel = {'type1':'Grass', 'type2':'Poison', 'move1':'Giga Drain', 'move2':'Sludge Bomb', 'move3':'Leaf Blade', 'move4':'Power Whip', 'health':'270', 'speed':'70'}

Tentacruel = {'type1':'Poison', 'type2':'Water', 'move1':'Confuse Ray', 'move2':'Sludge Bomb', 'move3':'Hydro Pump', 'move4':'Ice Beam', 'health':'270', 'speed':'100'}

Golem = {'type1':'Ground', 'type2':'Rock', 'move1':'Body Slam', 'move2':'Earthquake', 'move3':'Explosion', 'move4':'Rock Climb', 'health':'270', 'speed':'45'}

Rapidash = {'type1':'Fire', 'type2':'Fire', 'move1':'Flamethrower', 'move2':'Flare Blitz', 'move3':'Mega Horn', 'move4':'Inferno', 'health':'240', 'speed':'105'}

Slowbro = {'type1':'Psychic', 'type2':'Water', 'move1':'Aqua Tail', 'move2':'Confusion', 'move3':'Headbutt', 'move4':'Ice Beam', 'health':'300', 'speed':'30'}

Magneton = {'type1':'Eletric', 'type2':'Steel', 'move1':'Spark', 'move2':'Thunder', 'move3':'Thunderwave', 'move4':'Wild Charge', 'health':'210', 'speed':'70'}

Farfetchd = {'type1':'Normal', 'type2':'Flying', 'move1':'Aerial Ace', 'move2':'Air Cutter', 'move3':'Headbutt', 'move4':'Leaf Blade', 'health':'214', 'speed':'60'}

Dodrio = {'type1':'Flying', 'type2':'Normal', 'move1':'Aerial Ace', 'move2':'Brave Bird', 'move3':'Drill Peck', 'move4':'Feint Attack', 'health':'230', 'speed':'110'}

Dewgong = {'type1':'Ice', 'type2':'Water', 'move1':'Aqua Tail', 'move2':'Drill Run', 'move3':'Ice Beam', 'move4':'Slam', 'health':'290', 'speed':'70'}

Muk = {'type1':'Poison', 'type2':'Poison', 'move1':'Explosion', 'move2':'Gunk Shot', 'move3':'Poison Gas', 'move4':'Lick', 'health':'320', 'speed':'50'}

Cloyster = {'type1':'Ice', 'type2':'Water', 'move1':'Frost Breath', 'move2':'Hydro Pump', 'move3':'Ice Beam', 'move4':'Self-Destruct', 'health':'210', 'speed':'70'}

Gengar = {'type1':'Ghost', 'type2':'Poison', 'move1':'Dark Pulse', 'move2':'Shadow Claw', 'move3':'Shadow Punch', 'move4':'Sludge Bomb', 'health':'230', 'speed':'110'}

Onix = {'type1':'Ground', 'type2':'Rock', 'move1':'Body Slam', 'move2':'Double Edge', 'move3':'Earthquake', 'move4':'Explosion', 'health':'180', 'speed':'70'}

Hypno = {'type1':'Psychic', 'type2':'Psychic', 'move1':'Confusion', 'move2':'Mega Punch', 'move3':'Tri Attack', 'move4':'Zen Headbutt', 'health':'280', 'speed':'67'}

Kingler = {'type1':'Water', 'type2':'Water', 'move1':'Crabhammer', 'move2':'Ice Beam', 'move3':'Scald', 'move4':'Surf', 'health':'220', 'speed':'75'}

Electrode = {'type1':'Electric', 'type2':'Electric', 'move1':'Thunder', 'move2':'Thunderbolt', 'move3':'Thunderwave', 'move4':'Wild Charge', 'health':'230', 'speed':'150'}

<<<<<<< HEAD
Exeggutor = {'type1':'Grass', 'type2':'Psychic', 'move1':'Confusion', 'move2':'Double Edge', 'move3':'Egg Bomb', 'move4':'Explosion', 'health':'..', 'speed':'..'}
=======
Exeggutor = {'type1':'Grass', 'type2':'Psychic', 'move1':'Confusion', 'move2':'Double Edge', 'move3':'Egg Bomb', 'move4':'Explosion', 'health':'300', 'speed':'55'}
>>>>>>> f9ae442bad5f231af79d10a668682336504e07ef

Marowak = {'type1':'Ground', 'type2':'Ground', 'move1':'Bonemerang', 'move2':'Double Edge', 'move3':'Dyanmic Punch', 'move4':'Earthquake', 'health':'..', 'speed':'..'}

Hitmonlee = {'type1':'Fighting', 'type2':'Fighting', 'move1':'Blaze Kick', 'move2':'High Jump Kick', 'move3':'Mega Kick', 'move4':'Low Kick', 'health':'..', 'speed':'..'}

Hitmonchan = {'type1':'Fighting', 'type2':'Fighting', 'move1':'Drain Punch', 'move2':'Ice Punch', 'move3':'Mach Punch', 'move4':'Fire Punch', 'health':'..', 'speed':'..'}

Lickitung = {'type1':'Normal', 'type2':'Normal', 'move1':'Aqua Tail', 'move2':'Body Slam', 'move3':'Dynamic Punch', 'move4':'Headbutt', 'health':'..', 'speed':'..'}

Weezing = {'type1':'Poison', 'type2':'Poison', 'move1':'Explosion', 'move2':'Sludge Bomb', 'move3':'Poison Gas', 'move4':'Self Destruct', 'health':'..', 'speed':'..'}

Rhydon = {'type1':'Ground', 'type2':'Rock', 'move1':'Earthquake', 'move2':'Double Edge', 'move3':'Drill Run', 'move4':'Headbutt', 'health':'..', 'speed':'..'}

Chansey = {'type1':'Normal', 'type2':'Normal', 'move1':'Body Slam', 'move2':'Drain Punch', 'move3':'Egg Bomb', 'move4':'Headbutt', 'health':'..', 'speed':'..'}
<<<<<<< HEAD

Tangela = {'type1':'Grass', 'type2':'Grass', 'move1':'Giga Drain', 'move2':'Double Team', 'move3':'Headbutt', 'move4':'Leaf Storm', 'health':'..', 'speed':'..'}

Kangaskhan = {'type1':'Normal', 'type2':'Normal', 'move1':'Body Slam', 'move2':'Ice Punch', 'move3':'Dynamic Punch', 'move4':'Earthquake', 'health':'..', 'speed':'..'}

Seadra = {'type1':'Water', 'type2':'Water', 'move1':'Dragon Breath', 'move2':'Hydro Pump', 'move3':'Ice Beam', 'move4':'Scald', 'health':'..', 'speed':'..'}

Seaking = {'type1':'Water', 'type2':'Water', 'move1':'Aqua Tail', 'move2':'Double Edge', 'move3':'Horn Attack', 'move4':'Ice Beam', 'health':'..', 'speed':'..'}

Starmie = {'type1':'Psychic', 'type2':'Water', 'move1':'Scald', 'move2':'Hydro Pump', 'move3':'Power Gem', 'move4':'Swift', 'health':'..', 'speed':'..'}

Mr._Mime = {'type1':'Psychic', 'type2':'Psychic', 'move1':'Confusion', 'move2':'Focus Punch', 'move3':'Psybeam', 'move4':'Psyshock', 'health':'..', 'speed':'..'}
=======
>>>>>>> f9ae442bad5f231af79d10a668682336504e07ef

print(pokePick())

def battle():
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

        while (myPokeHP != 0 or oppPokeHP != 0 or myPokeHP <= 0 or oppPokeHP <= 0):
            if myPokeTurn:
                print("\nPlease select a move:")
                print(myPokeMoveset)
                myPokeMove = input

                if myPokeMove[typing] == Bug:
                    if oppPokeType == (Psychic or Grass or Dark):
                        superEffective = True
                    elif oppPokeType == (Fighting or Fire or Flying or Ghost or Poison or Steel):
                        notEffective = True

                elif myPokeMove[typing] == Dark:
                    if oppPokeType == (Ghost or Psychic):
                        superEffective = True
                    elif oppPokeType == (Dark or Fighting):
                        notEffective = True

                elif myPokeMove[typing] == Dragon:
                    if oppPokeType == Dragon:
                        superEffective = True
                    elif oppPokeType == Steel:
                        notEffective = True

                elif myPokeMove[typing] == Electric:
                    if oppPokeType == (Flying or Water):
                        superEffective = True
                    elif oppPokeType == (Dragon or Electric or Grass):
                        notEffective = True
                    elif oppPokeType == Ground:
                        immune = True

                elif myPokeMove[typing] == Fighting:
                    if oppPokeType == (Dark or Ice or Normal or Rock or Steel):
                        superEffective = True
                    elif oppPokeType == (Bug or Flying or Poison or Psychic):
                        notEffective = True
                    elif oppPokeType == Ghost:
                        immune = True

                elif myPokeMove[typing] == Fire:
                    if oppPokeType == (Bug or Grass or Ice or Steel):
                        superEffective = True
                    elif oppPokeType == (Dragon or Fire or Rock or Water):
                        notEffective = True

                elif myPokeMove[typing] == Flying:
                    if oppPokeType == (Bug or Fighting or Grass):
                        superEffective = True
                    elif oppPokeType == (Electric or Rock or Steel):
                        notEffective = True

                elif myPokeMove[typing] == Ghost:
                    if oppPokeType == (Ghost or Psychic):
                        superEffective = True
                    elif oppPokeType == (Dark):
                        notEffective = True
                    elif oppPokeType == Normal:
                        immune = True

                elif myPokeMove[typing] == Grass:
                    if oppPokeType == (Ground or Rock or Water):
                        superEffective = True
                    elif oppPokeType == (Bug or Dragon or Fire or Flying or Grass or Poison or Steel):
                        notEffective = True

                elif myPokeMove[typing] == Ground:
                    if oppPokeType == (Electric or Fire or Poison or Rock or Steel):
                        superEffective = True
                    elif oppPokeType == (Bug or Grass):
                        notEffective = True
                    elif oppPokeType == Flying:
                        immune = True

                elif myPokeMove[typing] == Ice:
                    if oppPokeType == (Dragon or Flying or Grass or Ground):
                        superEffective = True
                    elif oppPokeType == (Fire or Ice or Steel or Water):
                        notEffective = True

                elif myPokeMove[typing] == Normal:
                    if oppPokeType == (Rock or Steel):
                        notEffective = True
                    elif oppPokeType == Ghost:
                        immune = True

                elif myPokeMove[typing] == Poison:
                    if oppPokeType == Grass:
                        superEffective = True
                    elif oppPokeType == (Ghost or Ground or Poison or Rock):
                        notEffective = True
                    elif oppPokeType == Steel:
                        immune = True

                elif myPokeMove[typing] == Psychic:
                    if oppPokeType == (Fighting or Poison):
                        superEffective = True
                    elif oppPokeType == (Psychic or Steel):
                        notEfffective = True
                    elif oppPokeType == Dark:
                        immune = True

                elif myPokeMove[typing] == Rock:
                    if oppPokeType == (Bug or Fire or Flying or Ice):
                        superEffective = True
                    elif oppPokeType == (Fighting or Ground or Steel):
                        notEffective = True

                elif myPokeMove[typing] == Steel:
                    if oppPokeType == (Ice or Rock):
                        superEffective = True
                    elif oppPokeType == (Electric or Fire or Steel or Water):
                        notEffective = True

                elif myPokeMove[typing] == Water:
                    if oppPokeType == (Fire or Ground or Rock):
                        superEffective = True
                    elif oppPokeType == (Dragon or Grass or Water):
                        notEffective = True

                moveMiss = random.randint(1,15)
                if moveMiss == 1:
                    print('You Missed')
                else:
                    if myPokeStatus == Paralyzed or Frozen:
                        turnParalyze = random.randint(1,4)
                        if turnParalyze == 1:
                            print('Your Pokemon cannot move')
                        else:
                            pass
                        if myPokeConfusion == True:
                            confusion = random.randint(1,2)
                            if confusion == 1:
                                myPokeHP = myPokeHP - 40
                                print('Your pokemon hit itself in its confusion')
                            else:
                                moveCrit = random.randint(1,10000)
                                if moveCrit <= 625:
                                    crit = True
                                else:
                                    crit = False

                                if crit:
                                    if superEffective:
                                        myPokeMove = myPokeMove * 4
                                        oppPokeHP = oppPokeHP - myPokeMove
                                    elif notEffective:
                                        oppPokeHP = oppPokeHP - myPokeMove
                                    else:
                                        myPokeMove = myPokeMove * 2
                                        oppPokeHP = oppPokeHP - myPokeMove
                                else:
                                    if superEffective:
                                        myPokeMove = myPokeMove * 2
                                        oppPokeHP = oppPokeHP - myPokeMove
                                    else:
                                        oppPokeHP = oppPokeHP - myPokeMove
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

                if oppPokeMove[typing] == Bug:
                    if myPokeType == (Psychic or Grass or Dark):
                        superEffective = True
                    elif myPokeType == (Fighting or Fire or Flying or Ghost or Poison or Steel):
                        notEffective = True

                elif oppPokeMove[typing] == Dark:
                    if myPokeType == (Ghost or Psychic):
                        superEffective = True
                    elif myPokeType == (Dark or Fighting):
                        notEffective = True

                elif oppPokeMove[typing] == Dragon:
                    if myPokeType == Dragon:
                        superEffective = True
                    elif myPokeType == Steel:
                        notEffective = True

                elif oppPokeMove[typing] == Electric:
                    if myPokeType == (Flying or Water):
                        superEffective = True
                    elif myPokeType == (Dragon or Electric or Grass):
                        notEffective = True
                    elif myPokeType == Ground:
                        immune = True

                elif oppPokeMove[typing] == Fighting:
                    if myPokeType == (Dark or Ice or Normal or Rock or Steel):
                        superEffective = True
                    elif myPokeType == (Bug or Flying or Poison or Psychic):
                        notEffective = True
                    elif myPokeType == Ghost:
                        immune = True

                elif oppPokeMove[typing] == Fire:
                    if myPokeType == (Bug or Grass or Ice or Steel):
                        superEffective = True
                    elif myPokeType == (Dragon or Fire or Rock or Water):
                        notEffective = True

                elif oppPokeMove[typing] == Flying:
                    if myPokeType == (Bug or Fighting or Grass):
                        superEffective = True
                    elif myPokeType == (Electric or Rock or Steel):
                        notEffective = True

                elif oppPokeMove[typing] == Ghost:
                    if myPokeType == (Ghost or Psychic):
                        superEffective = True
                    elif myPokeType == (Dark):
                        notEffective = True
                    elif myPokeType == Normal:
                        immune = True

                elif oppPokeMove[typing] == Grass:
                    if myPokeType == (Ground or Rock or Water):
                        superEffective = True
                    elif myPokeType == (Bug or Dragon or Fire or Flying or Grass or Poison or Steel):
                        notEffective = True

                elif oppPokeMove[typing] == Ground:
                    if myPokeType == (Electric or Fire or Poison or Rock or Steel):
                        superEffective = True
                    elif myPokeType == (Bug or Grass):
                        notEffective = True
                    elif myPokeType == Flying:
                        immune = True

                elif oppPokeMove[typing] == Ice:
                    if myPokeType == (Dragon or Flying or Grass or Ground):
                        superEffective = True
                    elif myPokeType == (Fire or Ice or Steel or Water):
                        notEffective = True

                elif oppPokeMove[typing] == Normal:
                    if myPokeType == (Rock or Steel):
                        notEffective = True
                    elif myPokeType == Ghost:
                        immune = True

                elif oppPokeMove[typing] == Poison:
                    if myPokeType == Grass:
                        superEffective = True
                    elif myPokeType == (Ghost or Ground or Poison or Rock):
                        notEffective = True
                    elif myPokeType == Steel:
                        immune = True

                elif oppPokeMove[typing] == Psychic:
                    if myPokeType == (Fighting or Poison):
                        superEffective = True
                    elif myPokeType == (Psychic or Steel):
                        notEfffective = True
                    elif myPokeType == Dark:
                        immune = True

                elif oppPokeMove[typing] == Rock:
                    if myPokeType == (Bug or Fire or Flying or Ice):
                        superEffective = True
                    elif myPokeType == (Fighting or Ground or Steel):
                        notEffective = True

                elif oppPokeMove[typing] == Steel:
                    if myPokeType == (Ice or Rock):
                        superEffective = True
                    elif myPokeType == (Electric or Fire or Steel or Water):
                        notEffective = True

                elif oppPokeMove[typing] == Water:
                    if myPokeType == (Fire or Ground or Rock):
                        superEffective = True
                    elif myPokeType == (Dragon or Grass or Water):
                        notEffective = True

                moveMiss = random.randint(1,15)
                if moveMiss == 1:
                    print('You Missed')
                else:
                    if oppPokeStatus == Paralyzed or Frozen:
                        turnParalyze = random.randint(1,4)
                        if turnParalyze == 1:
                            print('Your Pokemon cannot move')
                        else:
                            pass
                        if oppPokeConfusion == True:
                            confusion = random.randint(1,2)
                            if confusion == 1:
                                oppPokeHP = oppPokeHP - 40
                                print('Your pokemon hit itself in its confusion')
                            else:
                                moveCrit = random.randint(1,10000)
                                if moveCrit <= 625:
                                    crit = True
                                else:
                                    crit = False
                        else:
                                moveCrit = random.randint(1,10000)
                                if moveCrit <= 625:
                                    crit = True
                                else:
                                    crit = False
                                if crit:
                                    if superEffective:
                                        myPokeMove = myPokeMove * 4
                                        oppPokeHP = oppPokeHP - myPokeMove
                                    elif notEffective:
                                        myPokeMove = myPokeMove * 2
                                        oppPokeHP = oppPokeHP - myPokeMove
                                    else:
                                        myPokeMove = myPokeMove * 2
                                        oppPokeHP = oppPokeHP - myPokeMove
                                else:
                                    if superEffective:
                                        myPokeMove = myPokeMove * 2
                                        oppPokeHP = oppPokeHP - myPokeMove
                                    else:
                                        oppPokeHP = oppPokeHP - myPokeMove

            if myPokeStatus == Burned:
                myPokeHP = myPokeHP - (myPokeHP * 0.0625)
            else:
                pass

            if myPokeStatus == Poisoned:
                myPokeHP = myPokeHP - (myPokeHP * 0.0625)
            else:
                pass
                 
            if oppPokeStatus == Burned:
                oppPokeHP = oppPokeHP - (oppPokeHP * 0.0625)
            else:
                pass

            if oppPokeStatus == Poisoned:
                oppPokeHP = oppPokeHP - (oppPokeHP * 0.0625)
            else:
                pass

        if oppPokeHP <= 0:
            winner = player
        elif myPokeHP <= 0:
            winner = opponent
