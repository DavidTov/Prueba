# Calcular PI por el metodo de Basilea 

cont = 0

for i in range(1,10000):
    cont += 1.0/i**2
    
print((cont*6)**0.5)

