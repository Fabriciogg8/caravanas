# Caravanas

En Uruguay se identifican los animales con caravanas, las cuales contienen un chip con una numeración de 8 digitos.

Se utiliza para llevar un registro de los animales, a nivel nacional, conociendo la procedencia y los distintos movimientos de cada uno.

Dentro de los establecimientos se pueden hacer lecturas, con distitnas finalidades. Cuando leemos las caravans con el lector, se genera un archivo txt con los número de los animales leídos. 

Este código en python se puede utilizar para comparar distintas lecturas. De esta manera podemos saber en que lote o grupo de animales se encontraba el que acabamos de leer, al compararlo con una lectura anterior.  

**setup.py** : Este archivo compara la lectura actual con la original, y nos dice cuantos animales de la lectura actual se encuentran en la lectura original. 

**main.py** : Este archivo compara distintas lecturas y finalmente nos retorna la cantidad de animales del grupo inicial que NO fueron leídos. 
