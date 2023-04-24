# Django store. Test task.

## Requirements
- For deploy this application a docker-engine is needed.

## Deploy
To deploy this application, you need to perform the following steps:
1. Run build containers from docker-compose file: `docker-compose build`;
2. Then deploy containers by command: `docker-compose up -d`;
3. Now you need to connect to containers with django projects - store and warehouse. You can connect to containers
through interactive console in docker-engine, or you can connect with this command: 
`docker container exec -it <container-name-or-id> /bin/bash` (the name of the container may be different, so I do not give it).
When you connected to the container, the following commands should be executed (for both django projects):
   1. `python manage.py migrate` - for initializing db;
   2. `python manage.py createsuperuser` - to access the admin panel.

## Start application

- `docker-compose start` - starts application;
- `docker-compose stop` - stops;
- http://localhost:8001/admin - access to the admin panel of the app store;
- http://localhost:8002/admin - access to the admin panel of the warehouse store.
