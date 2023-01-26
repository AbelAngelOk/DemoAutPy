@echo off
echo
cd ".\src\test"
echo EL REPORTE SE GUARDARA EN ./src/allure-results/{una_carpeta}
echo  POR FAVOR, INGRESE UN NOMBRE A LA CARPETA EL REPORTE.
set/p carpeta= 
echo EJECUTANDO PRUEBAS...
where python
echo C:\Users\Arbusta\AppData\Local\Microsoft\WindowsApps\python.exe python -m pytest --alluredir "..\allure-results\%carpeta%"
pause