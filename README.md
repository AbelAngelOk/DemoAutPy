# DemoAutPy
Demo Automation Python

Dependencias Instaladas
- Selenium
- Unittest
- PyTest
- Allure
- Allure-PyTest

## Para Ejecutar
### Ejecutar toda la bateria desde index.py

Ingresar al archivo index.py dentro de la carpeta test y ejecutar el __main__ del archivo.

### Ejecutar desde consola 
Para ejecutar toda la bateria de pruebas abrir el CMD en el directorio del proyecto y luego ingresar el comando
```
python -m unittest
```
Si se desea ejecutar un conjunto especifico deberia abrirse el CMD sobre el directorio que contenga el conjunto a ejecutar

### Ejecutar desde consola y generar un reporte
Para ejecutar la bateria de pruebas y generar un reporte se realizan dos pasos:
1- Nos debemos posicionar sobre la carpeta de los test
```
cd "./src/test"
```
2- ejecutamos python con el directorio en donde se generá el reporte
```
python -m pytest test_login.py --alluredir "..\allure-results\demo"
```

Para visualizar el reporte deberas ejecutar 
```
allure serve "(direccion absoluta)"
```
### Opcion deprecada
Para ejecutar todos los casos de un .py ingresar a un archivo ./test/*.py y ejecutar el archivo:
```
if __name__ == "__main__":
    unittest.main()
```
