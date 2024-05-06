from selenium import webdriver
from bs4 import BeautifulSoup

def scrape_minube_info(city_name):
    # Generar la URL en función del nombre de la ciudad
    if city_name.lower() == "cali":
        minube_url = "https://www.minube.com.co/que_ver/colombia/valle_del_cauca/cali"
    else:
        minube_url = "https://www.minube.com.co/que_ver/colombia/antioquia/medellin"
    
    # Configurar el driver de Selenium 
    driver = webdriver.Chrome() 

    # Cargar la página de Minube en el navegador
    driver.get(minube_url)

    # Esperar a que la página se cargue completamente
    driver.implicitly_wait(10)  # Espera máximo 10 segundos

    # Obtener el contenido HTML de la página después de que se haya cargado completamente
    html_content = driver.page_source

    # Crear el objeto BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Encontrar todos los divs que contienen la información de cada lugar
    divs = soup.find_all('div', class_='baseCard riverCard poiCard gridCard')

    # Lista para almacenar la información de cada lugar
    minube_info = []

    # Iterar sobre los divs
    for index, div in enumerate(divs, start=1):
        # Inicializar un diccionario para almacenar la información del lugar actual
        place_data = {}
        
        # Asignar el puesto basado en el orden de lectura
        place_data['puesto'] = str(index)
        
        # Extraer el nombre del lugar
        nombre_a = div.find('a', class_='titleItem')
        place_data['nombre'] = nombre_a.text.strip() if nombre_a else f"No se encontró nombre para el lugar {index}"
        
        # Extraer el rating del lugar
        rating_span = div.find('div', class_='starsRatingMeter').find('span')['style']
        rating_percentage = float(rating_span.split(':')[-1].replace('%', ''))
        rating = round(rating_percentage / 20, 1)
        place_data['rating'] = rating
        
        # Extraer las calificaciones del lugar
        calificaciones_div = div.find('div', class_='ratingTextShown')
        place_data['calificaciones'] = calificaciones_div.text.strip() if calificaciones_div else f"No se encontraron calificaciones para el lugar {index}"
        
        # Extraer la URL de la imagen del lugar
        image_div = div.find('div', class_='imageCard')
        image_url = image_div['data-src'] if image_div else "No se encontró imagen para el lugar {index}"
        place_data['imagen'] = image_url
        
        # Agregar el diccionario del lugar actual a la lista
        minube_info.append(place_data)

    # Cerrar el navegador después de terminar
    driver.quit()

    return minube_info

if __name__ == "__main__":
    city_name = input("Ingrese el nombre de la ciudad: ")
    info = scrape_minube_info(city_name)
    for place_data in info:
        print("Puesto:", place_data['puesto'])
        print("Nombre:", place_data['nombre'])
        print("Rating:", place_data['rating'])
        print("Calificaciones:", place_data['calificaciones'])
        print("Imagen:", place_data['imagen'])
        print()
