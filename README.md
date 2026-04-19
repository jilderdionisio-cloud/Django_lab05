# CineSpoilers

## Descripción

CineSpoilers es una API REST desarrollada con Django y Django REST Framework que permite gestionar un catálogo de películas. El proyecto implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para el modelo de Película.

## Características

- **Modelo de Película**: Incluye campos como título, sinopsis, duración en minutos, fecha de lanzamiento, estado activo, y timestamps de creación y actualización.
- **API RESTful**: Endpoints para gestionar películas con operaciones CRUD completas.
- **Serialización**: Uso de serializers de DRF para validar y formatear los datos.
- **Base de Datos**: SQLite por defecto, con migraciones de Django.

## Modelo de Datos

### Movie
- `id`: Identificador único (auto-generado)
- `title`: Título de la película (CharField, max 255 caracteres)
- `synopsis`: Sinopsis de la película (TextField)
- `duration_minutes`: Duración en minutos (PositiveIntegerField)
- `release_date`: Fecha de lanzamiento (DateField)
- `is_active`: Estado activo (BooleanField, por defecto True)
- `created_at`: Fecha de creación (DateTimeField, auto_now_add)
- `updated_at`: Fecha de actualización (DateTimeField, auto_now)

## Endpoints de la API

La API está disponible bajo el prefijo `/api/`. Los endpoints para películas son:

- `GET /api/movies/`: Lista todas las películas activas
- `POST /api/movies/`: Crea una nueva película
- `GET /api/movies/{id}/`: Obtiene detalles de una película específica
- `PUT /api/movies/{id}/`: Actualiza una película completa
- `PATCH /api/movies/{id}/`: Actualiza parcialmente una película
- `DELETE /api/movies/{id}/`: Elimina una película

## Probar con Postman

Sigue estos pasos para probar la API desde Postman:

1. Abre Postman.
2. Inicia el servidor de Django:
   ```bash
   python manage.py runserver
   ```
3. En Postman, crea una nueva petición `GET` a:
   ```text
   http://127.0.0.1:8000/api/movies/
   ```
4. Haz clic en `Send` para ver la lista de películas.

### Crear película (POST)

1. Crea una nueva petición `POST` a:
   ```text
   http://127.0.0.1:8000/api/movies/
   ```
2. En la pestaña `Body`, selecciona `raw` y `JSON`.
3. Ingresa los datos de la película.
4. Haz clic en `Send`.

### Actualizar película (PUT)

1. Crea una petición `PUT` a:
   ```text
   http://127.0.0.1:8000/api/movies/1/
   ```
2. En la pestaña `Body`, selecciona `raw` y `JSON`.
3. Ingresa todos los campos con los nuevos datos.
4. Haz clic en `Send`.

### Eliminar película (DELETE)

1. Crea una petición `DELETE` a:
   ```text
   http://127.0.0.1:8000/api/movies/1/
   ```
2. Haz clic en `Send`.

## Evidencia de Trabajo

### Jilder Dionisio ROJAS

#### Entregables

![Entregable 1](doc/entregable.png)
![Entregable 2](doc/entregable2.png)

#### Operaciones en Base de Datos - GET (Listar películas)

![DB GET](doc/db.get.png)
![GET Postman](doc/get.png)

#### Operaciones en Base de Datos - POST (Crear película)

![DB POST](doc/db.post.png)
![POST Postman](doc/Post.png)

#### Operaciones en Base de Datos - PUT (Actualizar película)

![DB PUT](doc/db.put.png)
![PUT Postman](doc/put.png)

#### Operaciones en Base de Datos - DELETE (Eliminar película)

![DB DELETE](doc/db.delete.png)
![DELETE Postman](doc/delete.png)

*Nota: Si alguna imagen no se muestra correctamente, verifica que el archivo esté en la carpeta `doc/` con el nombre exacto.*

## Equipo

- **Naomi Veliz**
- **Jilder Dionisio**
- **Adrina Chinchayguara**

Cada miembro contribuyó en las diferentes fases del desarrollo, incluyendo el diseño del modelo, implementación de la API y documentación.