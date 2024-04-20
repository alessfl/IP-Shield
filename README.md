# IP-Shield

## Nombre del equipo: Error 404
### Nombre del proyecto: IP Shield.

####  APLICACION WEB : https://ipshield.bubbleapps.io/version-test 
#### APLICACION MOVIL : https://jonathan-tiros-team.adalo.com/alarms-app


####  Sumario:
####  Web site.
####  El website provee de información importante, cómo lo es el trabajo por desarrollar, y así mismo una demostración de cómo manejamos las fases de gestión de incidentes, potenciadas por la asistencia e implementación real de la API de open AI.

####  Sistema de notificaciones.
####  Las notificaciones son desplegadas a través de código disponible en Reflex, desarrollado para un ambiente en Python, así como el resto de la demostración disponible en la página web.

##Sobre la App:
### La aplicación consta de un sistema de clasificación de alertas, desde nivel 1 al 3, para las cuales:
#### En nivel 1:
#### No generan ninguna clase de notificación, pero si se añaden al registro.
### En nivel 2:
#### Genera notificaciones push (Móvil).
### En nivel 3:
#### Genera un desplegable que interrumpe toda actividad del dispositivo móvil, hasta que se interrumpa la misma.

#### Dicha aplicación genera correos electrónicos para toda alerta, además de que no posee la capacidad de enviar ningún paquete hacia el servidor, sólo funge como medio de notificación. Además se tiene en consideración para versiones posteriores la incorporación de notificaciones push en PC.

### Plataformas de desarrollo: 
### Para la página web, se utilizó el servicio de Bubble, y Adalo para la aplicación de notificaciones.
Se conectó la API de Open AI para analizar los datos del manejo de los incidentes, para obtener recomendaciones personalizadas según el problema de seguridad.
#### Se utilizó Python para la implementación de envio de emails, donde se especifican datos que nos pueden ayudar a comprender lo que sucedió, dando una pequeña descripción, además, se da el horario en el que sucedió, la dirección IP y una descripción de lo que se hizo para atacar o en este caso, lo que la IA puede dar como solución al problema. 

