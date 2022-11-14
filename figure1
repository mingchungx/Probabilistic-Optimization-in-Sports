from math import factorial
import matplotlib.pyplot as plt
 
def c_n_m(total_count, valid_count):
   fact_n    = factorial(total_count)
   fact_m    = factorial(valid_count)
   fact_n_m  = factorial(total_count - valid_count)
   c_n_m_num = fact_n / (fact_m * fact_n_m)
   return c_n_m_num
 
def main():
   p   = 0.5    
   q   = 1 - p  
   pg  = 0      
   qg  = 1 - pg 
   pm  = 0      
   qm  = 1 - pm 
 
   pl   = [i/100 for i in range(50,101,1)] 
  
   ptgm = [
           (11, 4,'-','g',2,'(n,m) = (11,4) Current Table Tennis Rules'),      
           (4, 11,'--','r',1,'(n,m) = (4,11) Reversed Current Table Tennis Rules'), 
           (21, 3,':','g',3,'(n,m) = (21,3) Old Table Tennis Rules'),  
           (1,  1,'-.','g',1,'(n,m) = (1,1) Minimized Probability') 
           ]
 
   file = open("/Users/XXXX/Desktop/Coding/Math IA/Math IA Data/mathiadata.csv","w")
 
   file_header = "p"
   for p in pl:
       file_header += "," + str(p)
   file.write(file_header)
 
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
           for j in range(m): 
               b += c_n_m(m-1+j,j) * (qg**j) 
           
           pm = (pg**m) * b 
           pml.append(pm)
 
       file_line = f"\nn={n}"
       for p in pgl:
           file_line += "," + str(p)
       file.write(file_line)
 
       file_line = f"\nm={m}"
       for p in pml:
           file_line += "," + str(p)
       file.write(file_line)
      
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
