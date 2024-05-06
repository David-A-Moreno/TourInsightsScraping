from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_google_info(city_name):
    # Generar la URL en función del nombre de la ciudad
    if city_name.lower() == "cali":
        google_url = "https://www.google.com/search?q=cali+atracciones&sca_esv=017e3c382dac1d65&rlz=1C1ALOY_esCO1084CO1084&sxsrf=ADLYWILc_Fcn2k3xYCvG-nRiXw6YNW3hxQ:1714938810453&udm=15&sa=X&ved=2ahUKEwjf6u70pPeFAxWSQjABHf42ANoQxN8JegQIERAb&biw=1366&bih=607&dpr=1"
    elif city_name.lower() == "medellin":
        google_url = "https://www.google.com/search?q=medellin+atracciones&sca_esv=1fcec3f5e0b15e20&rlz=1C1ALOY_esCO1084CO1084&sxsrf=ADLYWIK8aZ4BPotrDXKyUO9nL8bB_m9P1g:1714953193669&udm=15&sa=X&ved=2ahUKEwjX16i_2veFAxWQfjABHXymADsQxN8JegQIERAb&biw=1366&bih=607&dpr=1"
    elif city_name.lower() == "bogota":
        google_url = "https://www.google.com/search?q=bogota+atracciones&sca_esv=017e3c382dac1d65&rlz=1C1ALOY_esCO1084CO1084&udm=15&biw=1366&bih=607&sxsrf=ADLYWILQNBo1QHPHhVW9UgDYZyiy_ERYjw%3A1715033861764&ei=BVc5ZrahLoaXwbkPjPOQqA4&ved=0ahUKEwj2t-6Ah_qFAxWGSzABHYw5BOUQ4dUDCBA&uact=5&oq=bogota+atracciones&gs_lp=Egxnd3Mtd2l6LXNlcnAiEmJvZ290YSBhdHJhY2Npb25lczIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIIEAAYBxgIGB4yCBAAGAcYCBgeMggQABgHGAgYHjIIEAAYBxgIGB4yCBAAGAcYCBgeMggQABgHGAgYHjIIEAAYBxgIGB5I-UJQqzNYikJwA3gBkAEAmAGrAaABpAqqAQMwLjm4AQPIAQD4AQGYAgmgApIHwgIKEAAYsAMY1gQYR8ICChAjGIAEGCcYigXCAgoQABiABBhDGIoFmAMAiAYBkAYIkgcDMy42oAe7SA&sclient=gws-wiz-serp"
    elif city_name.lower() == "barranquilla":
        google_url = "https://www.google.com/search?q=barranquilla+atracciones&sca_esv=017e3c382dac1d65&rlz=1C1ALOY_esCO1084CO1084&udm=15&biw=1366&bih=607&sxsrf=ADLYWIKqbv311g_VoSXJQ6duK7fH1xWYjg%3A1715033999661&ei=j1c5ZtiIKN_-wbkPzbOFqAc&ved=0ahUKEwiYjM_Ch_qFAxVffzABHc1ZAXUQ4dUDCBA&uact=5&oq=barranquilla+atracciones&gs_lp=Egxnd3Mtd2l6LXNlcnAiGGJhcnJhbnF1aWxsYSBhdHJhY2Npb25lczIFEAAYgAQyBRAAGIAEMgYQABgIGB4yBhAAGAgYHjIGEAAYCBgeMgYQABgIGB4yBhAAGAgYHjIGEAAYCBgeMggQABiABBiiBEjeDlAAWPcMcAB4AZABAJgBwgGgAbEOqgEEMC4xMrgBA8gBAPgBAZgCBqACsQfCAgYQABgHGB7CAggQABgHGB4YD8ICCBAAGAcYCBgewgIHEAAYgAQYDcICChAAGAcYCBgeGA-YAwCSBwMwLjagB61h&sclient=gws-wiz-serp"
    elif city_name.lower() == "cartagena":
        google_url = "https://www.google.com/search?q=cartagena+atracciones&sca_esv=017e3c382dac1d65&rlz=1C1ALOY_esCO1084CO1084&udm=15&biw=1366&bih=607&sxsrf=ADLYWIKqbv311g_VoSXJQ6duK7fH1xWYjg%3A1715033999661&ei=j1c5ZtiIKN_-wbkPzbOFqAc&ved=0ahUKEwiYjM_Ch_qFAxVffzABHc1ZAXUQ4dUDCBA&uact=5&oq=cartagena+atracciones&gs_lp=Egxnd3Mtd2l6LXNlcnAiFWNhcnRhZ2VuYSBhdHJhY2Npb25lczIHEAAYgAQYDTIGEAAYBxgeMgYQABgHGB4yCBAAGAcYCBgeMggQABgHGAgYHjIIEAAYBxgIGB4yCBAAGAcYCBgeMggQABgHGAgYHjIIEAAYBxgIGB4yCBAAGAcYCBgeSKAKUABYjwlwAHgBkAEAmAGgAaABnwmqAQMwLji4AQPIAQD4AQGYAgSgAtsEwgIIEAAYBxgKGB6YAwCSBwMwLjSgB5U_&sclient=gws-wiz-serp"
    else:
        google_url = "https://www.google.com/search?q=santa+marta+atracciones&sca_esv=017e3c382dac1d65&rlz=1C1ALOY_esCO1084CO1084&udm=15&biw=1366&bih=607&sxsrf=ADLYWIIWVBSVy2VoBRMlnsuBSwtaYliKRw%3A1715034734463&ei=blo5ZoPxG-yJwbkPscWrkA4&ved=0ahUKEwiD4P-givqFAxXsRDABHbHiCuIQ4dUDCBA&uact=5&oq=santa+marta+atracciones&gs_lp=Egxnd3Mtd2l6LXNlcnAiF3NhbnRhIG1hcnRhIGF0cmFjY2lvbmVzMgUQABiABDIEEAAYHjIGEAAYCBgeMgYQABgIGB4yBhAAGAgYHjIIEAAYgAQYogQyCBAAGIAEGKIESMcaULABWL8YcAR4AZABAJgBpAGgAeQPqgEEMC4xNLgBA8gBAPgBAZgCDKACognCAgoQABiwAxjWBBhHwgIGEAAYBxgewgIGEAAYDRgewgIIEAAYCBgNGB7CAggQABgHGAgYHsICCBAAGAUYBxgemAMAiAYBkAYIkgcDNC44oAeyWw&sclient=gws-wiz-serp"
    
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
