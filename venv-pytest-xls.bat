@echo off

REM Precondicion: tener entorno virtual llamado venv
REM Precondicion: tener instalado modulos de requirements.txt

REM Observacion: el comando para activar el entorno virtual solo funcion desde el pipeline.

REM Activar el entorno virtual
call %cd%\venv\Scripts\activate.bat

REM Ejecutar el proyecto y generar archivo excel
py.test --excelreport=report.xls