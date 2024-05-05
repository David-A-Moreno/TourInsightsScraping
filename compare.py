from tripadvisorinfo import section_info as tripadvisor_info
from googleinfo import google_info

# Función para comparar la información de TripAdvisor y Google
def comparar_info(tripadvisor_info, google_info):
    for tripadvisor_place, google_place in zip(tripadvisor_info, google_info):
        print("Comparando información de lugar:")
        print("TripAdvisor:")
        print("Puesto:", tripadvisor_place['puesto'])
        print("Nombre:", tripadvisor_place['nombre'])
        print("Rating:", tripadvisor_place['rating'])
        print("Calificaciones:", tripadvisor_place['calificaciones'])
        print("Google:")
        print("Puesto:", google_place['puesto'])
        print("Nombre:", google_place['nombre'])
        print("Rating:", google_place['rating'])
        print("Calificaciones:", google_place['calificaciones'])
        print()
        # Agrega aquí cualquier lógica de comparación que necesites
        # Por ejemplo, comparar si los nombres son iguales, los ratings son similares, etc.

# Llamar a la función para comparar la información
comparar_info(tripadvisor_info, google_info)
