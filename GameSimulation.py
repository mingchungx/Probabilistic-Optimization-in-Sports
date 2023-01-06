import math
import numpy as np
import random
import csv

def save(results):
    with open("/Users/mingchungxia/Desktop/Coding/Math IA/Math IA Data/ttgamesim.csv","w",newline="") as file:
        writer = csv.writer(file)
        writer.writerows(results)

def main():

    probabilityA = [i for i in range(50,101)] # Probability list of A

    # If T=225
    tg_tm = [(1,225),(3,75),(5,45),(9,25),(15,15)]
    # Symmetry; approximately equals, (15,15 is optimized)

    results = [] # Each result is (probability, n, m, winner)

    for pgsystem in tg_tm:
        # Calculating (n,m)
        n = math.ceil(pgsystem[0]/2)
        m = math.ceil(pgsystem[1]/2)

        # Initializing scores of players
        pointsA = 0
        pointsB = 0
        gamesA  = 0
        gamesB  = 0

        for p in probabilityA: # play a point -> check if the game is done -> (if it is) check if the match is done
            playing = True
            while playing:
                if random.randint(1,101) < p: # Each point
                    pointsA += 1
                else:
                    pointsB += 1
                
                if pointsA == n: # If a game is over and A wins
                    gamesA += 1
                    pointsA = 0 # After each game, points are reset
                    pointsB = 0
                    if (gamesA or gamesB) == m: # If the match is over, check who won
                        if gamesA > gamesB:
                            winner = 'A'
                        else:
                            winner = 'B'
                        result = [p, n, m, winner]
                        results.append(result)
                        playing = False 
                        gamesA = 0 # After each match, reset everything
                        gamesB = 0
                        break

                elif pointsB == n: # If a game is over and B wins
                    gamesB += 1
                    pointsA = 0
                    pointsB = 0
                    if (gamesA or gamesB) == m:
                        if gamesA > gamesB:
                            winner = 'A'
                        else:
                            winner = 'B'
                        result = [p, n, m, winner]
                        results.append(result)
                        playing = False
                        gamesA = 0
                        gamesB = 0
                        break
        
    save(results) #saves in format (p,n,m,winner)

if __name__ == "__main__":
    # Repeat 100 times and compute average for number of times 'B' appears at each (n,m) for all p
    main()