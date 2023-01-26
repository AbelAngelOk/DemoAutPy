@echo off

echo EJECUTANDO...

echo PRUEBA UNO: SABER EL DIRECTORIO ACTUAL...
%cd%

pause

echo PRUEBA DOS: MOVERSE A DIRECTORIO DE REPORTES
cd %cd%\src\allure-results
echo %cd%

pause

echo PRUEBA TRES: CREAR CARPETA PARA GUARDAR NUEVO REPORTE
set /p var1="Ingrese el nombre de la carpeta: "
md %var1%
set /p DirReport=%cd%\%var1%
pause

echo PRUEBA CUATRO: VOLVER A DIRECTORIO PRINCIPAL
cd..
cd..
echo %cd%

pause

echo PRUEBA CINCO: CREAR ENTORNO VIRTUAL
where python
set /p env="Ingresar nombre para el entorno virtual: "
C:\Python311\python.exe python3 -m venv %env%
echo se creó un entorno virtual de nombre %env%

pause

echo PRUEBA SEIS: ACTIVAR ENTORNO VIRUAL
%env%\Scripts\activate.bat

pause

echo PRUEBA SIETE: DESCARGAR LIBRERIAS
pip install -r requirements.txt

echo PRUEBA OCHO: EJECUTAR PRUEBAS
echo si no funciona podemos poner: %cd%\src\allure-results\%var1%
echo la ruta del reporte es "%DirReport%"
python -m pytest --alluredir "%DirReport%"

pause

echo PRUEBA NUEVE: EJECUTAR Y GUARDAR RESULTADOS DE LAS PRUEBAS
echo la ruta del reporte es "%DirReport%"
allure serve "%DirReport%"

pause
