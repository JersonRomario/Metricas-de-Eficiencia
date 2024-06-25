import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    inicio = time.time() 
    iteraciones = 0
    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            iteraciones += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    fin = time.time()
    return inicio, fin, iteraciones

tiempos = []
iteraciones_list = []

for i in range(50):
    arr = [random.randint(1, 100) for _ in range(10000)]
    
    print(f"\nRepetición {i + 1}:")
    print("Arreglo original:", arr)
    
    inicio, fin, iteraciones = bubble_sort(arr)
    
    print("Arreglo ordenado:", arr) 
    print(f"Tiempo total: {fin - inicio} segundos")
    print(f"Número de iteraciones: {iteraciones}")
    
    tiempos.append(fin - inicio)
    iteraciones_list.append(iteraciones)

fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('Repeticiones')
ax1.set_ylabel('Tiempo total (segundos)', color=color)
ax1.plot(range(1, 51), tiempos, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('Número de iteraciones', color=color)  
ax2.plot(range(1, 51), iteraciones_list, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  
plt.title('Tiempo total y número de iteraciones de Bubble Sort')
plt.show()
