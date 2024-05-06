from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

def scrape_tripadvisor_info(city_name):
    # Generar la URL en función del nombre de la ciudad
    if city_name.lower() == "cali":
        tripadvisor_url="https://www.tripadvisor.co/Attractions-g297475-Activities-oa0-Cali_Valle_del_Cauca_Department.html"
    elif city_name.lower() == "medellin":
        tripadvisor_url = "https://www.tripadvisor.co/Attractions-g297478-Activities-oa0-Medellin_Antioquia_Department.html"
    elif city_name.lower() == "bogota":
        tripadvisor_url = "https://www.tripadvisor.co/Attractions-g294074-Activities-oa0-Bogota.html"
    elif city_name.lower() == "barranquilla":
        tripadvisor_url = "https://www.tripadvisor.co/Attractions-g297473-Activities-oa0-Barranquilla_Atlantico_Department.html"
    elif city_name.lower() == "cartagena":
        tripadvisor_url = "https://www.tripadvisor.co/Attractions-g297476-Activities-oa0-Cartagena_Cartagena_District_Bolivar_Department.html"
    else:
        tripadvisor_url = "https://www.tripadvisor.co/Attractions-g297484-Activities-oa0-Santa_Marta_Santa_Marta_Municipality_Magdalena_Department.html"

    # Configurar el driver de Selenium 
    def get_driver():
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")  # Esta opción es crucial
        chrome_options.add_argument("--disable-dev-shm-usage")  # Soluciona problemas de recursos limitados
        chrome_options.add_argument("--disable-gpu")  # Ayuda en ciertos casos, aunque en modo headless el GPU no se utiliza
        chrome_options.add_argument("--window-size=1920,1080")
    
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    # Usar la función para obtener una instancia del driver
    driver = get_driver()

    # Cargar la página en el navegador
    driver.get(tripadvisor_url)

    # Esperar a que la página se cargue completamente
    driver.implicitly_wait(15)  # Espera máximo 10 segundos

    # Obtener el contenido HTML de la página después de que se haya cargado completamente
    html_content = driver.page_source

    # Crear el objeto BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Encontrar todas las secciones con la clase "mowmC" y data-automation="WebPresentation_SingleFlexCardSection"
    sections = soup.find_all('section', class_='mowmC', attrs={'data-automation': 'WebPresentation_SingleFlexCardSection'})

    # Lista para almacenar la información de cada sección
    section_info = []

    # Iterar sobre las secciones
    for index, section in enumerate(sections, start=1):
        # Inicializar un diccionario para almacenar la información de la sección actual
        section_data = {}
        
        # Extraer el rating y procesar el texto para obtener solo el número
        rating_text = section.find('title').text.strip()
        rating = rating_text.split()[0]  # Tomar solo la primera palabra del texto
        
        # Extraer el nombre y el puesto
        nombre_div = section.find('div', class_=('XfVdV', 'YQJrd'))
        puesto_span = nombre_div.find('span')
        section_data['puesto'] = puesto_span.text.replace(".", "").strip() if puesto_span else f"No se encontró puesto para la sección {index}"
        section_data['nombre'] = nombre_div.text.replace(puesto_span.text.strip(), '').strip() if nombre_div else f"No se encontró nombre para la sección {index}"
        
        # Extraer las calificaciones
        calificaciones_span = section.find('div', class_='jVDab o W f u w JqMhy').find('span')
        section_data['calificaciones'] = calificaciones_span.text.strip() if calificaciones_span else f"No se encontraron calificaciones para la sección {index}"
        
        # Guardar el rating en el diccionario
        section_data['rating'] = rating

        img_tag = section.find('img')
        section_data['imagen'] = img_tag['src'] if img_tag else f"No se encontró imagen para la sección {index}"
        
        # Agregar el diccionario de la sección actual a la lista
        section_info.append(section_data)

    # Cerrar el navegador después de terminar
    driver.quit()

    return section_info

if __name__ == "__main__":
    city_name = input("Ingrese el nombre de la ciudad: ")
    info = scrape_tripadvisor_info(city_name)
    for section_data in info:
        print("Puesto:", section_data['puesto'])
        print("Rating:", section_data['rating'])
        print("Nombre:", section_data['nombre'])
        print("Imagen:", section_data['imagen'])
        print("Calificaciones:", section_data['calificaciones'])
        print()
