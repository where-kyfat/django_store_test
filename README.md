# Django store. Test task.

## Task text:
It would be great if you can create a Django project and provide us with a link to a git repository.
Please, be aware that it's a test task, so we are not expecting a robust solution, and it's up to you how stable you want to make it.
This is a technical requirement for this project:
* Create two applications. (Store and Warehouse)
* (Store) One application should provide Orders (should be able to create order from admin page)
* (Warehouse) Another application should be able to receive these orders via the API and push back the information to the (Store).
* So when you create and order in Store, this should be synced to the Warehouse. If in warehouse you change some information this will update the information in Store (i.e. status)
* Make sure these applications can only communicate via Rest API and don't share a same database (two separate databases).


## Requirements
- For deploy this application a docker-engine is needed

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
- [http://localhost:8001/admin]() - access to the admin panel of the app store;
- [http://localhost:8002/admin]() - access to the admin panel of the app store.
