@echo off

REM Precondicion: tener entorno virtual llamado venv
REM Precondicion: tener el archivo requirements.txt

REM Observacion: el comando para activar el entorno virtual solo funcion desde el pipeline.

REM Activar el entorno virtual
call %cd%\venv\Scripts\activate.bat

REM Instalar listado de modulos dsde requirements.txt
pip install -r requirements.txt