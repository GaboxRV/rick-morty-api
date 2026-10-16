import requests
import time

"""URL de la API de Rick and Morty y endpoint de personajes"""
url  = "https://rickandmortyapi.com/api/character"

personajes_vivos = []
contador_vivos = 0
personajes_muertos = []
contador_muertos = 0
numero_pagina = 1
limite_intentos = 3

while url is not None:
    response:requests.Response = requests.get(url, timeout=10)

    print(f"Página {numero_pagina}: HTTP {response.status_code} - Tiempo de respuesta: {response.elapsed.total_seconds() * 1000} ms")

    if response.status_code == 429:
        retry_after = response.headers.get("Retry-After")

        if retry_after is None:
            print("No se incluye Retry-After en la respuesta. No se puede reintentar.")
            break

        try:
            retry_after = int(retry_after)
        except ValueError:
            print ("No fue posible convertir Retry-After a entero. No se puede reintentar.")
            break

        if limite_intentos > 0:
            print(f"Esperando {retry_after} segundos antes de reintentar...")
            time.sleep(retry_after)
            limite_intentos -= 1
            continue
        else:
            print(f"La solicitud falló y se detuvo en la página: {numero_pagina}")
            break

    elif response.status_code != 200:
        print(f"Error en la solicitud: HTTP {response.status_code}")
        print(f"La solicitud falló y se detuvo en la página: {numero_pagina}")
        break

    
    datos = response.json()
    assert isinstance(datos, dict)
    assert isinstance(datos["info"], dict)
    assert isinstance(datos["results"], list)

    limite_intentos = 3

    for personaje in datos["results"]:
        assert isinstance(personaje, dict)
        assert isinstance(personaje["name"], str)
        assert isinstance(personaje["status"], str)
        assert personaje["status"] in {"Alive", "Dead", "unknown"}

        if personaje["status"]=="Alive":
            personajes_vivos.append(personaje["name"])
            contador_vivos += 1
        elif personaje["status"]=="Dead":
            personajes_muertos.append(personaje["name"])
            contador_muertos += 1

    url = datos["info"]["next"]
    numero_pagina += 1


print("==========Personajes vivos==========")
print(f"Total: {contador_vivos}")
print(personajes_vivos)

print("\n==========Personajes muertos==========")
print(f"Total: {contador_muertos}")
print(personajes_muertos)
