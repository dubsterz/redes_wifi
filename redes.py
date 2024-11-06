import subprocess

def obtener_redes_wifi_guardadas():
    comando = "netsh wlan show profiles"
    resultado = subprocess.check_output(comando, shell=True).decode("utf-8")
    redes = [linea.strip() for linea in resultado.splitlines() if "Perfil de " in linea]
    valor = []
    for nombres in redes:
        valor.append(nombres.split(":")[1].strip())
    return valor

def obtener_contrasenas_wifi():
    redes = obtener_redes_wifi_guardadas()
    contrasenas = []
    for red in redes:
        comando = f"netsh wlan show profile {red} key=clear"
        resultado = subprocess.check_output(comando,text=True, shell=True)
        contrasena = [linea.strip() for linea in resultado.splitlines() if "Contenido de la clave" in linea]
        if contrasena:
            contrasena = contrasena[0].split(":")[1].strip()
        else:
            contrasena = "No disponible"
        contrasenas.append((red, contrasena))
    return contrasenas

redes_y_contrasenas = obtener_contrasenas_wifi()
print("A continuacion se mostraran las redes con su respectiva contraseña\n")
for red, contrasena in redes_y_contrasenas:
    print(f"Red: {red}\nContraseña: {contrasena}\n")
