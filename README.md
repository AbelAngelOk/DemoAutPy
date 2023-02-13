# DemoAutPy
Demo Automation Python

Dependencias Instaladas
- Selenium
- Unittest
- PyTest
- Allure
- Allure-PyTest
- Allure-Excel

## Para Ejecutar

### Precondiciones
Antes de ejecutar las pruebas deben asegurarse de activar el entorno virtual llamado venv, dado que los modulos necesarios ya estan instalados en el entorno virtual.
Para esto se puede ejecutar:
```
./venv/Scripts/activate
```
En caso de que cmd o powerShell no reconozca el comando se pueden intentar tres pasos:
1. Movernos hasta el directorio:
```
cd "./venv/Scripts"
```
2. Activar el archivo activate del entorno virtual o el .bat con el mismo nombre
```
activate
```
3. Volver al directorio inicial
```
cd ../..
```
Tambien se puede obtar por ejecutarlo desde los .bat que se especificaran mas adelante.


### Ejecutar toda la bateria desde index.py

Ingresar al archivo index.py dentro de la carpeta test y ejecutar el __main__ del archivo.

### Ejecutar desde consola con unittest
Para ejecutar toda la bateria de pruebas abrir el CMD en el directorio del proyecto y luego ingresar el comando
```
python -m unittest
```
Si se desea ejecutar un conjunto especifico deberia abrirse el CMD sobre el directorio que contenga el conjunto a ejecutar

### Ejecutar toda la bateria con pytest (fallido)

Para ejecutar la bateria de pruebas se puede abrir el CMD en el directorio del proyecto y luego ingresar el comando
```
python -m pytest
```
En caso de no funcionar ejecutar el comando desde el directorio de las pruebas
```
cd src/test
python -m pytest
cd ../..
```
Como atajo se creó el archivo venv-pytest.bat el cual activa el entorno virtual y ejecuta las pruebas.

### Ejecutar desde consola y generar un reporte con allure-pytest

Para ejecutar la bateria de pruebas y generar un reporte se realizan dos pasos:
1. Debemos ejecutar pytest eligiendo la carpeta donde guardar el reporte a generar
```
py.test --alluredir=results
```
2- Visualizamos el reporte allure con el comando
```
allure serve "%cd%\results"
```
Como post condicion es recomendable eliminar la carpeta para volver a utilizar.
Como atajo se puede ejecutar el archivo venv-pytest-allure.bat

### Ejecutar desde consola y generar un reporte de excel

Para ejecutar el proyecto y generar archivo excel se debera utilizar el comando
```
py.test --excelreport=report.xls
```
Como atajo se puede ejecutar el archivo venv-pytest-xls.bat

## Sobre los .Bat

Actualmente el proyecto cuenta con algunos .bat para facilitar las tareas
- Create-requirements.bat crea el archivo requirements.bat este archivo devuelve una lista de los modulos instalados en el entorno virtual venv.
- Create-venv.bat crea el entorno virtual con el nombre de venv.
- Install.requirements.bat busca el archivo requirements.bat e instala la lista de modulos que contiene.
- Venv-pytest.bat ejecuta toda la bateria de pruebas desde pytest
- Venv-pytest-allure.bat ejecuta toda la bateria de pruebas y genera un reporte en allure.
- Venv-pytest-xls.bat ejecuta toda la bateria de pruebas y genera un reporte en un excel results.xls 

### Modo de uso y utilidades
- Al hacer doble click sobre un excel se ejecutarán los comandos emulando el comportamiento manual en el cmd.
- Desde el IDE al hacer click sobre un .bat no se ejecuta si no que facilitará visualizar su contenido. 
- Los .bat tienen precondiciones y observaciones detalladas en los archivos.
- Los .bat puede ejecutarse desde consola {nombre}.bat o call {nombre}.bat
- En caso de estar trabajando desde consola es util abrir los .bat para recordar los comando que se quieran utilizar.
