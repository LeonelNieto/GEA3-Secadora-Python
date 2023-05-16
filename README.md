**PROYECTO SECADORA**

El puerto está programado en el USB0, por lo tanto el puerto debe ser siempre ttyUSB0.
- Para conocer si está conectado en el puerto correcto se debe de ejecutar el siguiente comando en la terminal; ***dmesd | tail***  o ejecutar el siguiente comando:   ***dmesd | grep tty***.
- En los resultados obtenidos ubica la línea que diga **FTDI USB SERIAL**, esta debería decir **FTDI USB SERIAL Device converter now attached to ttyUSB0**
- En caso contrario donde no diga esto y diga que está desconectado, es porque se está usando en otro proceso por la orange pi.
- Para detener estas desconexiones ejecuta el siguiente comando en la terminal ***sudo service brltty stop***.
- El comando anterior pedirá la contraseña de usuario, se debe de poner y dar enter (en caso de no haber cambiado la contraseña, la que tiene por defecto es: *orangepi*).
- Desconecta y conecta nuevamente el cable usb serial del puerto.
- Realiza nuevamente el paso 1 y verifica que ahora si muestre esto **FTDI USB SERIAL Device converter now attached to ttyUSB0**
