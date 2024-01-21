Este proyecto se basa en el curso de Data Engineer de Alexander Bolaño y consiste en automatizar el envío de mensajes de texto informando el pronostico de lluvias diario en cierta ubicacion, en este caso de mi ciudad San Salvador de Jujuy. En primer lugar se extraen los datos desde la API de Weatherapi (www.weatherapi.com) y cargan en un Dataframe. Se filtran y extraen los datos necesarios, para obtener un posible listado de horarios y condicion climatica lluviosa durante el dia. En un principio lo realizé en Jupyter para poder realizar las primeras pruebas con la API y las transformaciones con Pandas, luego lo pasé a un script en Python para facilitar la ejecución final. Por ultimo cloné el repositorio desde una maquina virtual EC2 de AWS instalé las dependencias para poder ejecutar y automatizar el script con Crontab. Para enviar los mensajes utilice Twilio.
Proximamente voy a implementar la traduccion al español de las condiciones climaticas mediante un json con las traducciones en varios idiomas que provee Weatherapi.
Algunas capturas:

![Untitled](https://github.com/pgb287/twilio-rain-forecast/assets/44307296/fac542fe-569d-493e-95a7-6d8e246307cb)

![Untitled3](https://github.com/pgb287/twilio-rain-forecast/assets/44307296/a54e7388-725f-44c6-bf01-868449f0a9a3)

![Untitled2](https://github.com/pgb287/twilio-rain-forecast/assets/44307296/d53965a1-b1c5-4c25-8970-60f46fb00bde)

![Untitled4](https://github.com/pgb287/twilio-rain-forecast/assets/44307296/992f0a3e-e9d2-48a4-954c-eddc3afd6aad)

![Untitled5](https://github.com/pgb287/twilio-rain-forecast/assets/44307296/79c10175-d089-49c8-96de-d1bc8360611c)

![WhatsApp Image 2024-01-21 at 2 04 04 AM](https://github.com/pgb287/twilio-rain-forecast/assets/44307296/42ccbab2-e33b-4cf3-99c5-101669a1fdc8)
