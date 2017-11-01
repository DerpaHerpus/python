import random

Venusaur = {'name': 'Venusaur', 'type1': 'Grass', 'type2': 'Poison', 'move1': 'Sludge Bomb', 'move2': 'Giga Drain', 'move3': 'Synthesis', 'move4': 'Earthquake', 'health': '270', 'speed': '80'}

Charizard = {'name': 'Charizard', 'type1': 'Fire', 'type2': 'Flying', 'move1': 'Flare Blitz', 'move2': 'Dragon Claw', 'move3': 'Earthquake', 'move4': 'Roost', 'health': '266', 'speed': '100'}

Blastoise = {'name': 'Blastoise', 'type1': 'Water', 'type2': 'Water', 'move1': 'Water Pulse', 'move2': 'Ice Beam', 'move3': 'Dark Pulse', 'move4': 'Aura Sphere', 'health': '268', 'speed': '78'}

Butterfree = {'name': 'Butterfree', 'type1': 'Grass', 'type2': 'Flying', 'move1': 'Bug Buzz', 'move2': 'Energy Ball', 'move3': 'Psychic', 'move4': 'Air Slash', 'health': '230', 'speed': '70'}

Beedrill = {'name': 'Beedrill', 'type1':'Grass', 'type2':'Poison', 'move1':'Bug Buzz', 'move2':'Poison Jab', 'move3':'Pursuit', 'move4':'Drill Run', 'health':'240', 'speed':'75'}

Pidgeot = {'name': 'Pidgeot', 'type1':'Normal', 'type2':'Flying', 'move1':'Hurricane', 'move2':'Heat Wave', 'move3':'Roost', 'move4':'Pursuit', 'health':'276', 'speed':'101'}

Raticate = {'name': 'Raticate','type1':'Normal', 'type2':'Normal', 'move1':'Crunch', 'move2':'Hyper Fang', 'move3':'Shadow Claw', 'move4':'Wild Charge', 'health':'220', 'speed':'97'}

Fearow = {'name': 'Fearow', 'type1':'Normal', 'type2':'Flying', 'move1':'Drill Peck', 'move2':'Double Edge', 'move3':'Drill Run', 'move4':'Pursuit', 'health':'240', 'speed':'100'}

Arbok = {'name': 'Arbok', 'type1':'Poison', 'type2':'Poison', 'move1':'Gunk Shot', 'move2':'Crunch', 'move3':'Aqua Tail', 'move4':'Earthquake', 'health':'230', 'speed':'80'}

Raichu = {'name': 'Raichu', 'type1':'Electric', 'type2':'Eletric', 'move1':'Thunderbolt', 'move2':'Focus Blast', 'move3':'Signal Beam', 'move4':'Surf', 'health':'230', 'speed':'110'}

Sandslash = {'name': 'Sandslash', 'type1':'Ground', 'type2':'Ground', 'move1':'Earthquake', 'move2':'Stone Edge', 'move3':'Night Slash', 'move4':'Chip Away', 'health':'260', 'speed':'65' }

Nidoqueen = {'name': 'Nidoqueen','type1':'Poison', 'type2':'Ground', 'move1':'Earth Power', 'move2':'Ice Beam', 'move3':'Sludge Wave', 'move4':'Flamethrower', 'health':'290', 'speed':'76'}

Nidoking = {'name': 'Nidoking', 'type1':'Poison', 'type2':'Ground', 'move1':'Sludge Wave', 'move2':'Earth Power', 'move3':'Ice Beam', 'move4':'Super Power', 'health':'272', 'speed':'85' }

Clefable = {'name': 'Clefable', 'type1':'Normal', 'type2':'Normal', 'move1':'Moonblast', 'move2':'Soft-Boiled', 'move3':'Focus Blast', 'move4':'Ice Beam', 'health':'300', 'speed':'60'}

Ninetales = {'name': 'Ninetales', 'type1':'Fire', 'type2':'Fire', 'move1':'Fire Blast', 'move2':'Psyshock', 'move3':'Energy Ball', 'move4':'Dark Pulse', 'health':'256', 'speed':'100'}

Wigglytuff = {'name': 'Wigglytuff', 'type1':'Normal', 'type2':'Normal', 'move1':'Hyper Voice', 'move2':'Dazzling Gleam', 'move3':'Fire Blast', 'move4':'Focus Blast', 'health':'390', 'speed':'45'}

Golbat = {'name': 'Golbat', 'type1':'Poison', 'type2':'Flying', 'move1':'Roost', 'move2':'Brave Bird', 'move3':'Super Fang', 'move4':'Zen Headbutt', 'health':'260', 'speed':'90'}

Vileplume = {'name': 'Vileplume', 'type1':'Grass', 'type2':'Poison', 'move1':'Giga Drain', 'move2':'Sludge Bomb', 'move3':'Synthesis', 'move4':'Stun Spore', 'health':'260', 'speed':'50'}

Parasect = {'name': 'Parasect', 'type1':'Bug', 'type2':'Grass', 'move1':'Energy Ball', 'move2':'Giga Impact', 'move3':'X-Scissor', 'move4':'Sysnthesis', 'health':'230', 'speed':'30'}

Venomoth = {'name': 'Venomoth', 'type1':'Bug', 'type2':'Poison', 'move1':'Bug Buzz', 'move2':'Sludge Bomb', 'move3':'Energy Ball', 'move4':'Psychic', 'health':'250', 'speed':'90'}

Dugtrio = {'name': 'Dugtrio', 'type1':'Ground', 'type2':'Ground', 'move1':'Earthquake', 'move2':'Pursuit', 'move3':'Stone Edge', 'move4':'Shadow Claw', 'health':'180', 'speed':'120'}

Persian = {'name': 'Persian', 'type1':'Normal', 'type2':'Normal', 'move1':'Hyper Voice', 'move2':'Water Pulse', 'move3':'Night Slash', 'move4':'Power Gem', 'health':'240', 'speed':'115'}

Golduck = {'name': 'Golduck', 'type1':'Water', 'type2':'Water', 'move1':'Ice Beam', 'move2':'Hydro Pump', 'move3':'Confuse Ray', 'move4':'Body Slam', 'health':'270', 'speed':'85'}

Primeape = {'name': 'Primape', 'type1':'Fighting', 'type2':'Fighting', 'move1':'Earthquake', 'move2':'Body Slam', 'move3':'Dynamic Punch', 'move4':'Fire Punch', 'health':'240', 'speed':'95'}

Arcanine = {'name': 'Arcanine', 'type1':'Fire', 'type2':'Fire', 'move1':'Fire Blast', 'move2':'Flare Blitz', 'move3':'Body Slam', 'move4':'Heat Wave', 'health':'290', 'speed':'95'}

Poliwrath = {'name': 'Poliwrath', 'type1':'Fighting', 'type2':'Water', 'move1':'Earthquake', 'move2':'Ice Punch', 'move3':'Scald', 'move4':'Dynamic Punch', 'health':'290', 'speed':'70'}

Alakazam = {'name': 'Alakazam', 'type1':'Psychic', 'type2':'Psychic', 'move1':'Psychic', 'move2':'Confusion', 'move3':'Psybeam', 'move4':'Tri Attack', 'health':'220', 'speed':'120'}

Machamp = {'name': 'Machamp', 'type1':'Fighting', 'type2':'Fighting', 'move1':'Dynamic Punch', 'move2':'Earthquake', 'move3':'Mega Kick', 'move4':'Mega Punch', 'health':'290', 'speed':'55'}

Victreebel = {'name': 'Victreebel', 'type1':'Grass', 'type2':'Poison', 'move1':'Giga Drain', 'move2':'Sludge Bomb', 'move3':'Leaf Blade', 'move4':'Power Whip', 'health':'270', 'speed':'70'}

Tentacruel = {'name': 'Tentacruel', 'type1':'Poison', 'type2':'Water', 'move1':'Confuse Ray', 'move2':'Sludge Bomb', 'move3':'Hydro Pump', 'move4':'Ice Beam', 'health':'270', 'speed':'100'}

Golem = {'name': 'Golem', 'type1':'Ground', 'type2':'Rock', 'move1':'Body Slam', 'move2':'Earthquake', 'move3':'Explosion', 'move4':'Rock Climb', 'health':'270', 'speed':'45'}

Rapidash = {'name': 'Rapidash', 'type1':'Fire', 'type2':'Fire', 'move1':'Flamethrower', 'move2':'Flare Blitz', 'move3':'Mega Horn', 'move4':'Inferno', 'health':'240', 'speed':'105'}

Slowbro = {'name': 'Slowbro', 'type1':'Psychic', 'type2':'Water', 'move1':'Aqua Tail', 'move2':'Confusion', 'move3':'Headbutt', 'move4':'Ice Beam', 'health':'300', 'speed':'30'}

Magneton = {'name': 'Magneton', 'type1':'Eletric', 'type2':'Steel', 'move1':'Spark', 'move2':'Thunder', 'move3':'Thunderwave', 'move4':'Wild Charge', 'health':'210', 'speed':'70'}

Farfetchd = {'name': "Farfetch'd", 'type1':'Normal', 'type2':'Flying', 'move1':'Aerial Ace', 'move2':'Air Cutter', 'move3':'Headbutt', 'move4':'Leaf Blade', 'health':'214', 'speed':'60'}

Dodrio = {'name': 'Dodrio', 'type1':'Flying', 'type2':'Normal', 'move1':'Aerial Ace', 'move2':'Brave Bird', 'move3':'Drill Peck', 'move4':'Feint Attack', 'health':'230', 'speed':'110'}

Dewgong = {'name': 'Dewgong', 'type1':'Ice', 'type2':'Water', 'move1':'Aqua Tail', 'move2':'Drill Run', 'move3':'Ice Beam', 'move4':'Slam', 'health':'290', 'speed':'70'}

Muk = {'name': 'Muk', 'type1':'Poison', 'type2':'Poison', 'move1':'Explosion', 'move2':'Gunk Shot', 'move3':'Poison Gas', 'move4':'Lick', 'health':'320', 'speed':'50'}

Cloyster = {'name': 'Cloyster', 'type1':'Ice', 'type2':'Water', 'move1':'Frost Breath', 'move2':'Hydro Pump', 'move3':'Ice Beam', 'move4':'Self-Destruct', 'health':'210', 'speed':'70'}

Gengar = {'name': 'Gengar', 'type1':'Ghost', 'type2':'Poison', 'move1':'Dark Pulse', 'move2':'Shadow Claw', 'move3':'Shadow Punch', 'move4':'Sludge Bomb', 'health':'230', 'speed':'110'}

Onix = {'name': 'Onix', 'type1':'Ground', 'type2':'Rock', 'move1':'Body Slam', 'move2':'Double Edge', 'move3':'Earthquake', 'move4':'Explosion', 'health':'180', 'speed':'70'}

Hypno = {'name': 'Hypno', 'type1':'Psychic', 'type2':'Psychic', 'move1':'Confusion', 'move2':'Mega Punch', 'move3':'Tri Attack', 'move4':'Zen Headbutt', 'health':'280', 'speed':'67'}

Kingler = {'name': 'Kingler', 'type1':'Water', 'type2':'Water', 'move1':'Crabhammer', 'move2':'Ice Beam', 'move3':'Scald', 'move4':'Surf', 'health':'220', 'speed':'75'}

Electrode = {'name': 'Electrode', 'type1':'Electric', 'type2':'Electric', 'move1':'Thunder', 'move2':'Thunderbolt', 'move3':'Thunderwave', 'move4':'Wild Charge', 'health':'230', 'speed':'150'}

Exeggutor = {'name': 'Exeggutor', 'type1':'Grass', 'type2':'Psychic', 'move1':'Confusion', 'move2':'Double Edge', 'move3':'Egg Bomb', 'move4':'Explosion', 'health':'300', 'speed':'55'}

Marowak = {'name': 'Marowak', 'type1':'Ground', 'type2':'Ground', 'move1':'Bonemerang', 'move2':'Double Edge', 'move3':'Dyanmic Punch', 'move4':'Earthquake', 'health':'..', 'speed':'..'}

Hitmonlee = {'name': 'Hitmonlee', 'type1':'Fighting', 'type2':'Fighting', 'move1':'Blaze Kick', 'move2':'High Jump Kick', 'move3':'Mega Kick', 'move4':'Low Kick', 'health':'..', 'speed':'..'}

Hitmonchan = {'name': 'Hitmonchan', 'type1':'Fighting', 'type2':'Fighting', 'move1':'Drain Punch', 'move2':'Ice Punch', 'move3':'Mach Punch', 'move4':'Fire Punch', 'health':'..', 'speed':'..'}

Lickitung = {'name': 'Lickitung', 'type1':'Normal', 'type2':'Normal', 'move1':'Aqua Tail', 'move2':'Body Slam', 'move3':'Dynamic Punch', 'move4':'Headbutt', 'health':'..', 'speed':'..'}

Weezing = {'name': 'Weezing', 'type1':'Poison', 'type2':'Poison', 'move1':'Explosion', 'move2':'Sludge Bomb', 'move3':'Poison Gas', 'move4':'Self Destruct', 'health':'..', 'speed':'..'}

Rhydon = {'name': 'Rhydon', 'type1':'Ground', 'type2':'Rock', 'move1':'Earthquake', 'move2':'Double Edge', 'move3':'Drill Run', 'move4':'Headbutt', 'health':'..', 'speed':'..'}

Chansey = {'name': 'Chansey', 'type1':'Normal', 'type2':'Normal', 'move1':'Body Slam', 'move2':'Drain Punch', 'move3':'Egg Bomb', 'move4':'Headbutt', 'health':'..', 'speed':'..'}

Tangela = {'name': 'Tangela', 'type1':'Grass', 'type2':'Grass', 'move1':'Giga Drain', 'move2':'Double Team', 'move3':'Headbutt', 'move4':'Leaf Storm', 'health':'..', 'speed':'..'}

Kangaskhan = {'name': 'Kangaskhan', 'type1':'Normal', 'type2':'Normal', 'move1':'Body Slam', 'move2':'Ice Punch', 'move3':'Dynamic Punch', 'move4':'Earthquake', 'health':'..', 'speed':'..'}

Seadra = {'name': 'Seadra', 'type1':'Water', 'type2':'Water', 'move1':'Dragon Breath', 'move2':'Hydro Pump', 'move3':'Ice Beam', 'move4':'Scald', 'health':'..', 'speed':'..'}

Seaking = {'name': 'Seaking', 'type1':'Water', 'type2':'Water', 'move1':'Aqua Tail', 'move2':'Double Edge', 'move3':'Horn Attack', 'move4':'Ice Beam', 'health':'..', 'speed':'..'}

Starmie = {'name': 'Starmie','type1':'Psychic', 'type2':'Water', 'move1':'Scald', 'move2':'Hydro Pump', 'move3':'Power Gem', 'move4':'Swift', 'health':'..', 'speed':'..'}

Mr_Mime = {'name': 'Mr. Mime', 'type1':'Psychic', 'type2':'Psychic', 'move1':'Confusion', 'move2':'Focus Punch', 'move3':'Psybeam', 'move4':'Psyshock', 'health':'..', 'speed':'..'}

Scyther = {'name': 'Scyther', 'type1':'Bug', 'type2':'Flying', 'move1':'Roost', 'move2':'Air Slash', 'move3':'Double Edge', 'move4':'Night Slash', 'health':'..', 'speed':'..'}

Jynx = {'name': 'Jynx', 'type1':'Ice', 'type2':'Psychic', 'move1':'Confusion', 'move2':'Focus Punch', 'move3':'Icebeam', 'move4':'Psyshock', 'health':'..', 'speed':'..'}

Electabuzz = {'name': 'Electabuzz', 'type1':'Electric', 'type2':'Electric', 'move1':'Thunder', 'move2':'Thunder Punch', 'move3':'Spark', 'move4':'Headbutt', 'health':'..', 'speed':'..'}

Magmar = {'name': 'Magmar', 'type1':'Fire', 'type2':'Fire', 'move1':'Fire Punch', 'move2':'Fire Blast', 'move3':'Double Edge', 'move4':'Flare Blitz', 'health':'..', 'speed':'..'}

Pinsir = {'name': 'Pinsir', 'type1':'Bug', 'type2':'Bug', 'move1':'Body Slam', 'move2':'Double Edge', 'move3':'Fury Cutter', 'move4':'X-Scissor', 'health':'..', 'speed':'..'}

Tauros = {'name': 'Tauros', 'type1':'Normal', 'type2':'Normal', 'move1':'Double Edge', 'move2':'Fire Blast', 'move3':'Horn Attack', 'move4':'Stone Edge', 'health':'..', 'speed':'..'}

Gyarados = {'type1':'Flying', 'type2':'Water', 'move1':'Hydro Pump', 'move2':'Dragon Pulse', 'move3':'Hurricane', 'move4':'Ice Beam', 'health':'..', 'speed':'..'}

Lapras = {'type1':'Ice', 'type2':'Water', 'move1':'Ice Beam', 'move2':'Aqua Tail', 'move3':'COnfuse Ray', 'move4':'Hydro Pump', 'health':'..', 'speed':'..'}

Ditto = {'type1':'Normal', 'type2':'Normal', 'move1':'Transform', 'move2':'Transform', 'move3':'Transform', 'move4':'Transform', 'health':'..', 'speed':'..'}

Vaporeon = {'type1':'Water', 'type2':'Water', 'move1': 'Water Pulse', 'move2':'Water Fall', 'move3':'Swift', 'move4':'Ice Beam', 'health':'..', 'speed':'..'}

Jolteon = {'type1':'Electric', 'type2':'Electric', 'move1':'Thunderbolt', 'move2':'Discharge', 'move3':'Thunder Fang', 'move4':'Thunder Wave', 'health':'..', 'speed':'..'}

Flareon = {'type1':'Fire', 'type2':'Fire', 'move1':'Flare Blitz', 'move2':'Fire Blast', 'move3':'Lava Plume', 'move4':"Will-O-Wisp", 'health':'..', 'speed':'..'}

Porygon = {'type1':'Normal', 'type2':'Normal', 'move1':'Double Edge', 'move2':'Aerial Ace', 'move3':'Ice Beam', 'move4':'Psychic', 'health':'..', 'speed':'..'}

Omastar = {'type1':'Rock', 'type2':'Water', 'move1':'Hydro Pump', 'move2':'Ice Beam', 'move3':'Scald', 'move4':'Waterfall', 'health':'..', 'speed':'..'}

Kabutops = {'type1':'Rock', 'type2':'Water', 'move1':'Double Edge', 'move2':'Aqua Tail', 'move3':'Night SLash', 'move4':'Mega Kick', 'health':'..', 'speed':'..'}

Aerodactyl = {'type1':'Rock', 'type2':'Flying', 'move1':'Air Cutter', 'move2':'Aerial Ace', 'move3':'Dragon Pulse', 'move4':'Fire Blast', 'health':'..', 'speed':'..'}

Snorlax = {'type1':'Normal', 'type2':'Normal', 'move1':'Dynamic Punch', 'move2':'Earthquake', 'move3':'Headbutt', 'move4':'Iron Head', 'health':'..', 'speed':'..'}

Articuno = {'type1':'Ice', 'type2':'FLying', 'move1':'Ice Beam', 'move2':'Hurricane', 'move3':'Roost', 'move4':'DOuble Edge', 'health':'..', 'speed':'..'}

Zapdos = {'type1':'Electric', 'type2':'Flying', 'move1':'Roost', 'move2':'Aerial Ace', 'move3':'Thunder', 'move4':'Thunder Wave', 'health':'..', 'speed':'..'}

Moltres = {'type1':'Fire', 'type2':'Flying', 'move1':'Flare Blitz', 'move2':'Aerial Ace', 'move3':'Fire Blast', 'move4':'Hurricane', 'health':'..', 'speed':'..'}

Dragonite = {'type1':'Dragon', 'type2':'Flying', 'move1':'Dragon Pulse', 'move2':'Earthquake', 'move3':'Draco meteor', 'move4':'Dynamic Punch', 'health':'..', 'speed':'..'}

Mewtwo = {'type1':'Psychic', 'type2':'Psychic', 'move1':'Confusion', 'move2':'Psystrike', 'move3':'Tri Attack', 'move4':'Shadow Ball', 'health':'..', 'speed':'..'}

select = {'1': Venusaur['name'], '2': Charizard['name'], '3': Blastoise['name'], '4': Butterfree['name'], '5': Beedrill['name'], '6': Pidgeot['name'], '7': Raticate['name'], '8': Fearow['name'], '9': Arbok['name'], '10': Raichu['name'], '11': Sandslash['name'], '12': Nidoqueen['name'], '13': Nidoking['name'], '14': Clefable['name'], '15': Ninetales['name'], '16': Wigglytuff['name'], '17': Golbat['name'], '18': Vileplume['name'], '19': Parasect['name'], '20': Venomoth['name'], '21': Dugtrio['name'], '22': Persian['name'], '23': Golduck['name'], '24': Primeape['name'], '25': Arcanine['name'], '26': Poliwrath['name'], '27': Alakazam['name'], '28': Machamp['name'], '29': Victreebel['name'], '30': Tentacruel['name'], '31': Golem['name'], '32': Rapidash['name'], '33': Slowbro['name'], '34': Magneton['name'], '35': Farfetchd['name'], '36': Dodrio['name'], '37': Dewgong['name'], '38': Muk['name'], '39': Cloyster['name'], '40': Gengar['name'], '41': Onix['name'], '42': Hypno['name'], '43': Kingler['name'], '44': Electrode['name'], '45': Exeggutor['name'], '46': Marowak['name'], '47': Hitmonlee['name'], '48': Hitmonchan['name'], '49': Lickitung['name'], '50': Weezing['name'], '51': Rhydon['name'], '52': Chansey['name'], '53': Tangela['name'], '54': Kangaskhan['name'], '55': Seadra['name'], '56': Seaking['name'], '57': Starmie['name'], '58': Mr_Mime['name'], '58': Scyther['name'], '60': Jynx['name'], '61': Electabuzz['name'], '62': Magmar['name'], '63': Pinsir['name'], '64': Tauros['name'], '65': Gyarados['name'], '66': Lapras['name'],'67': Ditto['name'], '68': Vaporeon['name'], '69': Jolteon['name'], '70': Flareon['name'], '71': Porygon['name'], '72': Omastar['name'], '73': Kabutops['name'], '74': Aerodactyl['name'], '75': Snorlax['name'], '76': Articuno['name'], '77': Zapdos['name'], '78': Moltres['name'], '79': Dragonite['name'], '80': Mewtwo['name']}

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
    print('1: ' + select[Poke1] + ' 2: ' + select[Poke2] + ' 3: ' + select[Poke3] + ' ' )
    myPoke = input('Please type number of the pokemon you want to be first: ')

    if myPoke == 1 or select[Poke1]:
        print('')
        print("These are your Pokemon's moves")
        myActivePoke = select[Poke1]
        myActivePokeMoves = ((select[Poke1]['move1']) + (select[Poke1]['move2']) + (select[Poke1]['move3']) + (select[Poke1]['move4']))
        print(myActivePokeMoves)
    elif myPoke == 2 or select[Poke2]:
        print('')
        print("These are your Pokemon's moves")
        myActivePoke = select[Poke2]
        myActivePokeMoves = ((select[Poke2]['move1']) + (select[Poke2]['move2']) + (select[Poke2]['move3']) + (select[Poke2]['move4']))
        print(myActivePokeMoves)
    elif myPoke == 3 or select[Poke3]:
        print('')
        print("These are your Pokemon's moves")
        myActivePoke = select[Poke3]
        myActivePokeMoves = ((select[Poke3]['move1']) + (select[Poke3]['move2']) + (select[Poke3]['move3']) + (select[Poke3]['move4']))
        print(myActivePokeMoves)

print(pokePick())

def battle():
    play_again = True
    while play_again:
        winner = None
        oppTeam = [select[random.randint(1,80)], select[random.randint(1,80)], select[random.randint(1,80)]]
        myPokeHP = myPoke['health']
        opponentPokeHP = select[oppTeam[1]]['health']

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

            if myPokeHP == 0 or myPokeHP <= 0:
                print('')
                print('Your active pokemon has fainted')
                print(Team - myActivePoke)
                myActivePoke = input('Please pick from your remaining pokemon to set as your active pokemon: ')

            if oppPokeHP == 0 or oppPokeHP <= 0:
                print('')
                print('Your opponents pokemon has fainted')
                oppTeam = [::-1]
                oppActivePoke = oppTeam[1]

#Things that we do not have:
    #Moves
        #When the moves inflict a status
        #Move typing
    #Switching Pokemon and when your active pokemon dies, to change it
    



