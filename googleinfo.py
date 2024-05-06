from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.parse

def scrape_google_info(city_name):
    # Generar la URL en función del nombre de la ciudad
    if city_name.lower() == "cali":
        google_url = "https://www.google.com/search?q=cali+atracciones&sca_esv=017e3c382dac1d65&rlz=1C1ALOY_esCO1084CO1084&sxsrf=ADLYWILc_Fcn2k3xYCvG-nRiXw6YNW3hxQ:1714938810453&udm=15&sa=X&ved=2ahUKEwjf6u70pPeFAxWSQjABHf42ANoQxN8JegQIERAb&biw=1366&bih=607&dpr=1"
    else:
        google_url = "https://www.google.com/search?q=medellin+atracciones&sca_esv=1fcec3f5e0b15e20&rlz=1C1ALOY_esCO1084CO1084&sxsrf=ADLYWIK8aZ4BPotrDXKyUO9nL8bB_m9P1g:1714953193669&udm=15&sa=X&ved=2ahUKEwjX16i_2veFAxWQfjABHXymADsQxN8JegQIERAb&biw=1366&bih=607&dpr=1"
    # Configurar el driver de Selenium
    driver = webdriver.Chrome() 

    # Cargar la página de Google en el navegador
    driver.get(google_url)

    # Esperar a que la página se cargue completamente
    driver.implicitly_wait(10)  # Espera máximo 10 segundos

    # Obtener el contenido HTML de la página después de que se haya cargado completamente
    html_content = driver.page_source

    # Crear el objeto BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Encontrar todos los divs que contienen la información de cada lugar
    divs = soup.find_all('div', class_='Z8r5Gb ZVHLgc', attrs={'jsname': 'jXK9ad'})

    # Lista para almacenar la información de cada lugar
    google_info = []

    # Iterar sobre los divs
    for index, div in enumerate(divs, start=1):
        # Inicializar un diccionario para almacenar la información del lugar actual
        place_data = {}

        # Asignar el puesto basado en el orden de lectura
        place_data['puesto'] = str(index)
        
        # Extraer el nombre del lugar
        nombre_span = div.find('span', class_='Yt787')
        place_data['nombre'] = nombre_span.text.strip() if nombre_span else f"No se encontró nombre para el lugar {index}"
        
        # Extraer el rating del lugar
        rating_span = div.find('span', class_='yi40Hd YrbPuc')
        place_data['rating'] = rating_span.text.strip() if rating_span else f"No se encontró rating para el lugar {index}"
        
        # Extraer las calificaciones del lugar
        calificaciones_span = div.find('span', class_='RDApEe YrbPuc')
        place_data['calificaciones'] = calificaciones_span.text.strip() if calificaciones_span else f"No se encontraron calificaciones para el lugar {index}"
        
        # Agregar el diccionario del lugar actual a la lista
        google_info.append(place_data)

    # Cerrar el navegador después de terminar
    driver.quit()

    return google_info

if __name__ == "__main__":
    city_name = input("Ingrese el nombre de la ciudad: ")
    info = scrape_google_info(city_name)
    for place_data in info:
        print("Puesto:", place_data['puesto'])
        print("Nombre:", place_data['nombre'])
        print("Rating:", place_data['rating'])
        print("Calificaciones:", place_data['calificaciones'])
        print()
