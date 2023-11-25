def draw_triangle(height):
    for i in range(height):
        print(' ' * (height - i - 1) + '/' + '_' * (2 * i) + '\\')
hauteur_triangle = int(input("Entrez la hauteur du triangle : "))
draw_triangle(hauteur_triangle)
