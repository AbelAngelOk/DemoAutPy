@echo off

REM Activar el entorno virtual
call %cd%\venv\Scripts\activate.bat

REM Ejecutar el proyecto
python -m pytest --allure "%cd%\src\allure-results\results"
python serve "%cd%\src\allure-results\results"