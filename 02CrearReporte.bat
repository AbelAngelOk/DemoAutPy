@echo off

REM Activar el entorno virtual
call %cd%\venv\Scripts\activate.bat

REM Ejecutar el proyecto
python -m pytest --allure "%cd%\results"
python serve "%cd%\results"