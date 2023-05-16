# PROYECTO SECADORA

El proyecto está enfocado a la obtención de los datos de diversos ERD's, y almacenarlos en un nuevo archivo .csv por cada ciclo que corre, el cuál guarda datos únicamente cuando el Erd_SystemState está en run. Además se tiene una bandera del Erd anterior, la cuál es un archivo csv adicional, en el cuál se escribe el status de la secadora en la primera celda del . Está basadp en el protocolo de comunicación GEA3 y el programa está desarrollado en Python.

## Requisitos del sistema
- Se requiere la última versión permitada de debian para la orange pi zero 2.
- En caso de no instalar la última versión, se requiere la instalación de cualquier versión de Python 3.9.
  - Para conocer la versión de python que se tiene, ejecutar el siguiente comando en la terminal **python --version** (para sistemas con python 2 o inferior) y el comando **python3 --version** (Para versiones de python 3 o superior).

## Requisitos de hardware
- Convertidor USB Serial FTDI.
- Roseta RJ45.
- Cable RJ45. 

## Configuración Puerto Serial
El puerto está programado en el USB0, por lo tanto el puerto debe ser siempre ttyUSB0.
  - Para conocer si está conectado en el puerto correcto se debe de ejecutar el siguiente comando en la terminal; ***dmesd | tail***  o ejecutar el siguiente comando:   ***dmesd | grep tty***.
  - En los resultados obtenidos ubica la línea que diga **FTDI USB SERIAL**, esta debería decir **FTDI USB SERIAL Device converter now attached to ttyUSB0**
  - En caso contrario donde no diga esto y diga que está desconectado, es porque se está usando en otro proceso por la orange pi.
  - Para detener estas desconexiones ejecuta el siguiente comando en la terminal ***sudo service brltty stop***.
  - El comando anterior pedirá la contraseña de usuario, se debe de poner y dar enter (en caso de no haber cambiado la contraseña, la que tiene por defecto es: *orangepi*).
  - Desconecta y conecta nuevamente el cable usb serial del puerto.
  - Realiza nuevamente el paso 1 y verifica que ahora si muestre esto **FTDI USB SERIAL Device converter now attached to ttyUSB0**
 
## Intrucciones para ejecutar el programa
