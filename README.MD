# dcftest

postgres launched by docker:
```sh
# postgres launched in docker
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
# to obtain the python env
poetry shell
# init of django in dcftest folder
./manage.py migrate
./manage.py createsuperuser
./mange.py runserver
```

then access admin: 
http://127.0.0.1:8000/admin

add a model A object.

then add a model B object (choose the previously created modelA object for the foreign key)

and here it crash ! the sql query generated is:
```sql
SELECT DISTINCT "dcfapp_modela"."id", "dcfapp_modela"."name", "dcfapp_modela"."number_of_model_a_objects" FROM "dcfapp_modela" INNER JOIN "dcfapp_modelb" ON ("dcfapp_modela"."id" = "dcfapp_modelb"."model_a_id") WHERE "dcfapp_modelb"."id" = '00000000-0000-0000-0000-000000000003'::uuid  LIMIT 21; args=(UUID('00000000-0000-0000-0000-000000000003'),)
```

(i've activated logging of sql queries in settings.py)

