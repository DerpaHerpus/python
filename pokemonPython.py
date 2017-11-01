select = {'1':'Venusaur', '2':'Charizard', '3':'Blastoise', '4':'Butterfree', '5': 'Beedrill', '6':'Pidgeot', '7':'Raticate', '8':'Fearow', '9':'Arbok', '10':'Raichu', '11':'Sandslash', '12':'Nidoqueen', '13':'Nidoking', '14':'Clefable', '15':'Ninetales', '16':'Wigglytuff', '17':'Golbat', '18':'Vileplume', '19':'Parasect', '20':'Venomoth', '21':'Dugtrio', '22':'Persian', '23':'Golduck', '24':'Primeape', '25':'Arcanine', '26':'Poliwrath', '27':'Alakazam', '28':'Machamp', '29':'Victreebel', '30':'Tentacruel', '31':'Golem', '32':'Rapidash', '33':'Slowbro', '34':'Magneton', '35':"Farfetch'd", '36':'Dodrio', '37':'Dewgong', '38':'Muk', '39':'Cloyster', '40':'Gengar', '41':'Onix', '42':'Hypno', '43':'Kingler', '44':'Electode', '45':'Exeggutor', '46':'Marowak', '47':'Hitmonlee', '48':'Hitmonchan', '49':'Lickitung', '50':'Weezing', '51':'Rhydon', '52':'Chansey', '53':'Tangela', '54':'Kangaskhan' '55':'Seadra', '56':'Seaking', '57':'Starmie', '58':'Mr. Mime', '58':'Scyther', '60':'Jynx', '61':'Electabuzz', '62':'Magmar', '63':'Pinsir', '64':'Tauros', '65':'Gyarados', '66':'Lapras', '67':'Ditto', '68':'Vaporeon', '69':'Jolteon', '70':'Flareon', '71':'Porygon', '72':'Omastar', '73':'Kabutops', '74':'Aerodactyl', '75':'Snorlax', '76':'Articuno', '77':'Zapdos', '78':'Moltres', '79':'Dragonite', '80':'Mewtwo'}
 
import random

def battle():
    print('\tWelcome to the Pokemon Battle Simulator! Each pokemon will have the best moveset for the current meta and will each be given their own stats. Choose wi    sely.')
    print('\tChoose your pokemon!')

    play_again = True
    while play_again:           #this is a test
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
