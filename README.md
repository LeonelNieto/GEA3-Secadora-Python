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
  - Para conocer si está conectado en el puerto correcto se debe de ejecutar el siguiente comando en la terminal; ***dmesg | tail***  o ejecutar el siguiente comando:   ***dmesg | grep tty***.
  - En los resultados obtenidos ubica la línea que diga **FTDI USB SERIAL**, esta debería decir **FTDI USB SERIAL Device converter now attached to ttyUSB0**
  - En caso contrario donde no diga esto y diga que está desconectado, es porque se está usando en otro proceso por la orange pi.
  - Para detener estas desconexiones ejecuta el siguiente comando en la terminal ***sudo service brltty stop***.
  - Después escribe el siguiente comando en la terminal ***sudo systemctl disable brltty*** y reinicia la orange pi.
  - El comando anterior pedirá la contraseña de usuario, se debe de poner y dar enter (en caso de no haber cambiado la contraseña, la que tiene por defecto es: *orangepi*).
  - Desconecta y conecta nuevamente el cable usb serial del puerto.
  - Realiza nuevamente el paso 1 y verifica que ahora si muestre esto **FTDI USB SERIAL Device converter now attached to ttyUSB0**
 
## Intrucciones para ejecutar el programa
**Es necesario ejecutar el programa en la terminal, ya que si se ejecuta el programa como cualquier otro comenzará a correr, pero no habrá ninguna ventana y se tendrá que terminar la ejecución del programa desde la terminal con el comando kill. Para ejecutar el programa desde la terminal, realiza los siguientes pasos:**
- Abre la terminal de comandos y direccionate a la ubicación del archivo con el comando **cd (direccion del programa)**
- Ejecuta el siguiente comando en la terminal: **./Main**


## Cómo crear el archivo ejecutable
Lo primero que se tiene que hacer es abrir una terminal en la carpeta contenedora del archivo Main.py *Ya que en este caso este es el archivo principal*.
En la terminal se debe de ejecutar el siguiente comando:
- pyinstaller --onefile -F Main.py

Este comando lo que realiza es lo siguiente:
**--onefile:** Hace que solo se cree y sea necesario un solo archivo que este caso es llamado como *Main*
**-F:** Va a contener todas las bibliotecas de python, lo que va a generar que el programa sea más pesado, sin embargo, esto ayuda a que el dispositivo en el que vaya a ejecutar, puedo corrar sin problemas de dependencias de bibliotecas.
**Main.py:** Es el nombre del archivo del cual se quiere crear el archivo ejecutable.
