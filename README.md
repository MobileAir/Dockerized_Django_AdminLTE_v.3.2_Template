# Dockerized_Django_AdminLTE_v.3.2_Template
Dockerized Django AdminLTE 3.20 Template with PostgreSql
## Components
+   Docker
+   PostgreSql
+   Redis
+   Nginx
+   Gunicorn

## Basic Docker Compose Commands

### Start Docker Container in Development mode
+ docker-compose up -d --build
+ docker-compose logs -f

### Development Server is located at[localhost:8000](http://localhost:8000 "localhost")

### Create superuser:
+ docker-compose exec web python manage.py createsuperuser

### Stop Docker Containers
+ docker-compose down -v

### Start Docker Container in Production mode:
+ docker-compose -f prod.yml up -d --build

### Check Docker Container (Production) logs:
+ docker-compose -f prod.yml logs -f
