lat = 34.5
lon = 45.6
posicion = [lat, lon]

historial = [
    [34.5, 45.6, "2022/02/02 17:20:24"],
    [35.5, 46.6, "2022/02/02 17:20:34"],
    [36.5, 48.6, "2022/02/02 17:20:44"],
    [37.5, 49.6, "2022/02/02 17:20:54"],
    [38.5, 51.6, "2022/02/02 17:21:04"],
    [39.5, 57.6, "2022/02/02 17:21:14"],
    [30.5, 70.6, "2022/02/02 17:21:24"],
    [31.5, 99.6, "2022/02/02 17:21:34"],
]

indiceLongitud = 0
indiceLatitud = 1
indiceFecha = 2

for coordenada in historial:

    print(coordenada[indiceLongitud],coordenada[indiceLatitud],coordenada[indiceFecha]) #Per a mostrar els valors de l'array bidimensional.

    #[0] = Posicio 1 de l'array i [2] el camp 3 el qual es la data.