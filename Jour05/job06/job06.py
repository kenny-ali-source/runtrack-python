def function (steps, height):
    distance_steps = 2 * height / 100  
    distance_day = distance_steps* steps
    distance_week = distance_day * 7
    return distance_week
nb_steps = int(input("Entrer le nombre de marche :"))
height_steps = int(input("Entrer la hauteur de chaque marche en cm :"))
totale = function(nb_steps, height_steps)
print(f'Pour {nb_steps} marches de {height_steps} cm, le gardien parcourt {totale:.2f} m par semaine.')
