# DEF__INIT__

Для БД
	```SQL
		CREATE USER definituser WITH PASSWORD 'definitpass';
		ALTER ROLE definituser WITH CREATEDB;
		CREATE DATABASE definitdb WITH OWNER definituser;
	```
Зависимости
	```SH
		pip install -r requirements.txt
	```
Миграции
	```SH
		python manage.py migrate
	```
