# AI_final

1.-Se carga imagen de entrenamiento para identificar lineas viales.

2.-Se hacen correcciones de color para resaltar las lineas y se aplica un filtro de escala de grises para mostrar la imagen en un solo canal e identificar más facilmente la diferencia entre lineas, camino y fuera del camino

3.-Se aplica un desenfoque Gaussiano para eliminar el ruido

4.- La funcion canny aplica un desenfoque gaussiano e identifica los cambios de intesidad entre pixeles, lo cual ayuda a idenyidicar las lineas viales