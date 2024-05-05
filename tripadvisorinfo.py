from selenium import webdriver
from bs4 import BeautifulSoup

# Configurar el driver de Selenium (debes tener instalado el driver del navegador correspondiente)
driver = webdriver.Chrome()  # Por ejemplo, para Chrome

# Cargar la página en el navegador
driver.get("https://www.tripadvisor.co/Attractions-g297475-Activities-oa0-Cali_Valle_del_Cauca_Department.html")

# Esperar a que la página se cargue completamente
driver.implicitly_wait(10)  # Espera máximo 10 segundos

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
    
    # Agregar el diccionario de la sección actual a la lista
    section_info.append(section_data)

# Imprimir la información de cada sección
#for section_data in section_info:
    #print("Puesto:", section_data['puesto'])
    #print("Rating:", section_data['rating'])
    #print("Nombre:", section_data['nombre'])
    #print("Calificaciones:", section_data['calificaciones'])
    #print()

# Cerrar el navegador después de terminar
driver.quit()
