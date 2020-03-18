## game to  play akkad bakkad bambe bo

import time, sys

players = []

print('Akkad, Bakkad, Bambe, Bo !')
print("Let's Play !\n")

N = int(input('How many players are there?'))

for i in range(N):
    player = input(f'Player {i+1} :')
    players.append(player)

# for player in players:
#     print(player + '\t', end="")

rhyme = ['AKKAD', 'BAKKAD', 'BAMBE', 'BO', 'ASSI', 'NABBE', 'PURE', 'SAU', 'SAU', 'SE', 'NIKLA', 'DHAGA',
         'CHOR', 'NIKAL', 'KAR', 'BHAGA']



while(len(players) > 1):    
    for i in range(len(rhyme)):        
        print((i % len(players)) * '\t' + rhyme[i])
        
        for player in players:
            print(player + '\t', end="")
        
        print("\n\n\n")
        time.sleep(.5)

    print(f"{players[i % len(players)]} eliminated !")
    
    del(players[ i % len(players)])
    
    if len(players) == 1:
        break
    
    try:
        input('Press Enter to continue or Ctrl + C to quit')
    except KeyboardInterrupt:
        sys.exit()




if len(players) == 1:
    print(f"\nCongratulation {players[0]}, you are the winner!")  

