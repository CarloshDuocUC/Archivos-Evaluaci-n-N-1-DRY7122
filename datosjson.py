import os
import json
from datetime import datetime, timedelta
import base64

if os.name == "nt":  
    ruta_archivo = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'myfile.json')
elif os.name == "posix": 
    ruta_archivo = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', 'myfile.json')
else:
    print("Sistema operativo no compatible.")
    exit()

try:
    with open(ruta_archivo, "r") as archivo:
        data = json.load(archivo)
        access_token = data.get("access_token")
        expires_in = data.get("expires_in")

        if access_token is not None and expires_in is not None:
            print("Valor del token de acceso:", access_token)
            
            try:
                access_token_decoded = base64.b64decode(access_token).decode('utf-8')
                print("Token de acceso decodificado:", access_token_decoded)
            except:
                pass
            
            expiracion = datetime.now() + timedelta(seconds=expires_in)
            tiempo_restante = expiracion - datetime.now()
            print("Tiempo restante antes de que caduque el token:", tiempo_restante)

        else:
            print("No se encontró información completa sobre el token en el archivo JSON.")

except FileNotFoundError:
    print(f"No se pudo encontrar el archivo en el escritorio.")
except json.JSONDecodeError:
    print("Error al decodificar el archivo JSON.")
except Exception as e:
    print(f"Se produjo un error: {e}")


