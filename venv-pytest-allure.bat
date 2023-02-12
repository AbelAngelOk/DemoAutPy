@echo off

REM Precondicion: tener entorno virtual llamado venv
REM Precondicion: tener instalado modulos de requirements.txt

REM Observacion: el comando para activar el entorno virtual solo funcion desde el pipeline.


REM Crear Carpeta 
md results

REM Activar el entorno virtual
call %cd%\venv\Scripts\activate.bat

REM Ejecutar el proyecto con pytest-allure 
REM python -m pytest --allure "%cd%\results"

REM Ejecutar proyecto con allure-pytest 2.12.0
py.test --alluredir=results

REM ver proyecto
python serve "%cd%\results"

REM eliminar carpeta con archivos
rm /q /s results

REM eliminar carpeta vacia
rm results