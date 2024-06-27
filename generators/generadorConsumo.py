import random  
def generarDatos():
    datos= []
    for i in range(5000):
        dato={}
        id=random.randint(1,10000)
        referencia=random.choice(["ach01","ach22","ach43"])
        marca = random.choice(["sony","rico","kalley"])
        capacidad=random.randint(100,2000)
        cuidad=random.choice(["bello","medellin","sabaneta","envigado","itagui"])
        responsable=random.choice(["laura perez","sara arango","mariana gomez","tatiana restrepo","felipe Gomez"])
        
        dato=[id,referencia,marca,capacidad,cuidad,responsable]
        datos.append(dato)
    return datos
print(generarDatos())    