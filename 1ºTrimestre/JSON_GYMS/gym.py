import requests
from bs4 import BeautifulSoup
import csv

# Función para obtener gimnasios de una página
def obtener_gimnasios(pagina):
    url = f'https://degimnasios.com/sevilla?page={pagina}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    gyms = soup.find_all('article', class_='property-item property-col-list mb-4')
    datos = []

    for gym in gyms:
        nombre_tag = gym.find('h5', class_='property-title')
        nombre = nombre_tag.get_text(strip=True) if nombre_tag else 'N/D'

        direccion_tag = gym.find('address', class_='property-address')
        direccion = direccion_tag.get_text(strip=True) if direccion_tag else 'N/D'

        servicios = []
        servicios_container = gym.find('div', class_='property-lable')
        if servicios_container:
            servicios = [span.get_text(strip=True) for span in servicios_container.find_all('span', class_='badge')]
        servicios_str = ', '.join(servicios) if servicios else 'N/D'

        datos.append([nombre, direccion, servicios_str])

    return datos

# Recoger datos de varias páginas
todos_gimnasios = []
pagina = 1
while True:
    resultado = obtener_gimnasios(pagina)
    if not resultado:  # Si no hay más gimnasios en la página, terminar
        break
    todos_gimnasios.extend(resultado)
    print(f'Página {pagina} completada, {len(resultado)} gimnasios.')
    pagina += 1

# Guardar en CSV
with open('gimnasios_sevilla_completo.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Nombre', 'Dirección', 'Servicios'])
    writer.writerows(todos_gimnasios)

print('Todos los gimnasios han sido guardados en gimnasio_sevilla_completo.csv')
