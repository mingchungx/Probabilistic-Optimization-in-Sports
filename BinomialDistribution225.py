from math import factorial
import matplotlib.pyplot as plt 

def c_n_m(total_count, valid_count):
    fact_n    = factorial(total_count)
    fact_m    = factorial(valid_count)
    fact_n_m  = factorial(total_count - valid_count)
    c_n_m_num = fact_n / (fact_m * fact_n_m) # C(n,m)=(n!)/(m!(n-m)!)
    return c_n_m_num

def main():
    p   = 0.5   
    q   = 1 - p  
    pg  = 0      
    qg  = 1 - pg 
    pm  = 0     
    qm  = 1 - pm 

    pl   = [i/100 for i in range(50,66,1)] # Restrict domain because curves are close
    
    # (point,game,linestyle,linecolor,linewidth) are the types of n,m combination lines
    ptgm = [
            (1, 113,'-','r',1,'(n,m) = 1,113'),   
            (2,  38,'-','y',1,'(n,m) = 2,38'), 
            (3,  23,'-','m',1,'(n,m) = 3,23'),
            (5,  13,'-','b',1,'(n,m) = 5,13'), 
            (8,   8,'-','g',1,'(n,m) = 8,8 (optimized)') # OPTIMIZED
            ] 

    for n,m,ls,col,lw,lb in ptgm: 
        pgl = [] 
        pml = [] 

        for p in pl:
            q = 1 - p

            a = 0
            for i in range(n): 
                a += c_n_m(n-1+i,i) * (q**i)

            pg = (p**n) * a
            qg = 1 - pg
            pgl.append(pg)

            b = 0 
            for j in range(m): #M
                b += c_n_m(m-1+j,j) * (qg**j)

            pm = (pg**m) * b 
            pml.append(pm)

        plt.plot(pl, pml, linestyle=ls, color=col, linewidth=lw, label = lb)
        plt.xlabel("Point win probability p")
        plt.ylabel("Match win probability F(f(p))")
        plt.title("Probability distribution of stronger competitor - Competitor A")

    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()