# AI_final

1.-Se carga imagen de entrenamiento para identificar lineas viales.

2.-Se hacen correcciones de color para resaltar las lineas y se aplica un filtro de escala de grises para mostrar la imagen en un solo canal e identificar más facilmente la diferencia entre lineas, camino y fuera del camino

3.-Se aplica un desenfoque Gaussiano para eliminar el ruido

4.- La funcion canny aplica un desenfoque gaussiano e identifica los cambios de intesidad entre pixeles, lo cual ayuda a identidicar las lineas viales y reconstruye la imagen a partir de esos parámetros

5.- con la libreria matplotlib generamos un plano en la imaen que nos ayudará a identificar más rápido las lineas viales

6.- una vez que se identificó el carril que nos corresponde, se crea una máscara con el area que nos interesa

7.- Con la ayuda del concepto bitwise (operaciones lógicas AND OR) vamos a comparar cada bit de la imagen entregada por la función canny y la máscara que hicimos en el paso anterior y con esto vamos a idicar cual va a ser el area de interés de la imagen

8.- Con ayuda de la transformada de Hough podemos identificar en que punto de la imagen hay líneas, puntos o figuras y así poder discriminar los resultados que nosostros querramos y quedarnos sólo con las líneas viales

9.- Una vez obtenidas la líneas, se combinan con la imagen original para comprobar que estas estén dibujadas correctamente