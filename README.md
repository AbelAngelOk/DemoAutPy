# DemoAutPy
Demo Automation Python

Dependencias Instaladas
- Selenium
- Unittest
- PyTest

## Para Ejecutar
### Ejecutar toda la bateria desde index.py

Ingresar al archivo index.py dentro de la carpeta test y ejecutar el __main__ del archivo.

### Ejecutar desde consola 
Para ejecutar toda la bateria de pruebas abrir el CMD en el directorio del proyecto y luego ingresar el comando
```
python -m unittest
```
Si se desea ejecutar un conjunto especifico deberia abrirse el CMD sobre el directorio que contenga el conjunto a ejecutar

### Opcion deprecada
Para ejecutar todos los casos de un .py ingresar a un archivo ./test/*.py y ejecutar el archivo:
```
if __name__ == "__main__":
    unittest.main()
```
