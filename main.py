liberado_1=set()
liberado_2=set()
original=set()

def lectura(archivo, set):
    with open(archivo, "r") as f:
        for line in f:
            set.add(int(line)) 
        return set


def run(): 
    lectura("2021_12_23.txt", liberado_1)
    lectura("2021_12_29.txt", liberado_2)
            
    liberados = set() 
    liberados = liberado_1 | liberado_2
    
    lectura("Corral_1.txt", original)
    
    final = original ^ liberados
    print(f"Los animales son{final}\n Y el total corresponde a:", len(final))
    

if __name__ == "__main__":
    run()
