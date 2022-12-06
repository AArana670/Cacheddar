## Cómo ejecutar Cacheddar

Para poder hacer interactuar con Cacheddar mediante el terminal, es necesario separar la construcción de la orquestación Docker de su arranque. Para lo primero hay que ejecutar el siguiente comando:

> docker compose build

Y una vez construidos los servicios, se arranca con el siguiente comando:

> docker compose run cacheddar
