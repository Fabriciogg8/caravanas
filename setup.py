def comparacion():
    liberar=set()
    with open("2021_12_29.txt", "r") as f:
        for line in f:
            liberar.add(int(line))
        print("La canidad de animales en el archivo es: ",len(liberar))

    corral=set()
    file = "Corral_1.txt"
    with open(file, "r") as f:
        for line in f:
            corral.add(int(line))
        print(f"\nLa cantidad de animales del corral {file} es: ",len(corral))

    final_set1 = liberar & corral
    print(f"\nLos animales que pertenecen al corral {file} son {final_set1} \nY el total corresponde a:", len(final_set1))
    

    
if __name__ == "__main__":
    comparacion()

