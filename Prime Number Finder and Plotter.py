import sympy
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(10,10))

lower=1          
upper=200        
prime_list=list(sympy.primerange(lower,upper+1))  
print(prime_list)

x=np.zeros((len(prime_list)))
result=np.arange(1,2*(len(prime_list)),2)

plt.plot(result,prime_list,'rs',markersize=3)
plt.title("Primes Numbers Plot",fontsize=30)
plt.xlabel("Position of Prime in List of Primes",fontsize=25)
plt.ylabel("Value of Prime",fontsize=25)
plt.grid(color='black', linestyle='--', linewidth=1) 
plt.show() #shows the final plot