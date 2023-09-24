from math import factorial
import matplotlib.pyplot as plt 

# Combination Formula
def c_n_m(total_count, valid_count):
    fact_n    = factorial(total_count)
    fact_m    = factorial(valid_count)
    fact_n_m  = factorial(total_count - valid_count)
    c_n_m_num = fact_n / (fact_m * fact_n_m) # C(n,m)=(n!)/(m!(n-m)!)
    return c_n_m_num

def main():
    p   = 0.5    # The probability of player A to win a point
    q   = 1 - p  # The probability of player B to win a point
    pg  = 0      # The probability of player A to win a game by winning n points
    qg  = 1 - pg # The probability of player B to win a game
    pm  = 0      # The probability of player A to win a match by winning m games
    qm  = 1 - pm # The probability of player B to win a match

    # The probability scale of player A to win a point 0.5-1 with step 0.01
    pl   = [i/100 for i in range(50,101,1)]  
    
    # (point,game,linestyle,linecolor,linewidth) are the types of n,m combination lines
    ptgm = [
            (11, 4,'-','g',2,'(n,m) = (11,4) Current Table Tennis Rules'),      # Current Table Tennis Rules
            (4, 11,'--','r',1,'(n,m) = (4,11) Reversed Current Table Tennis Rules'), # Reverse Current Table Tennis Rules Cur=Rev because of 99-1, 1-99 logic
            (21, 3,':','g',3,'(n,m) = (21,3) Old Table Tennis Rules'),  # Old Table Tennis Rules
            (1,  1,'-.','g',1,'(n,m) = (1,1) Minimized Probability') # (n,m)=(1,1) condition
            ] 

    # Create a output csv file
    file = open("/Users/mingchungxia/Desktop/Coding/Math IA/Math IA Data/mathiadata.csv","w") # HIDE NAME IN IA

    # First row of output csv file is the probability list
    file_header = "p"
    for p in pl:
        file_header += "," + str(p)
    file.write(file_header)

    # For each match set (point,game)
    for n,m,ls,col,lw,lb in ptgm: 
        pgl = [] # The probability of player A to win a game by winning n points
        pml = [] # The probability of player A to win a match by winning m games

        # For each probability from 0.5-1
        for p in pl:
            q = 1 - p

            a = 0
            for i in range(n): #THIS IS n
                a += c_n_m(n-1+i,i) * (q**i)

            # The probability of player A to win a game by winning n points
            pg = (p**n) * a # prob. point
            qg = 1 - pg
            pgl.append(pg) # Probability of each game; this is from f(P)

            b = 0 
            for j in range(m): #M
                b += c_n_m(m-1+j,j) * (qg**j) # This is probability of a match, from f(P)

            # The probability of player A to win a match by winning m games
            pm = (pg**m) * b # prob. game
            pml.append(pm)

        file_line = f"\nn={n}"
        for p in pgl:
            file_line += "," + str(p)
        file.write(file_line)

        file_line = f"\nm={m}"
        for p in pml:
            file_line += "," + str(p)
        file.write(file_line)
        
        # Draw a line of the probability of player A to win a match
        plt.plot(pl, pml, linestyle=ls, color=col, linewidth=lw, label = lb)
        plt.xlabel("Point win probability p")
        plt.ylabel("Match win probability F(f(p))")
        plt.title("Probability distribution of stronger competitor - Competitor A")
        
    file.write("\n")
    file.close()

    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()