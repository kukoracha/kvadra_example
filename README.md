# kvadra_example

## Инструкция по развертыванию dev версии

1.Скопируйте репозиторий на компьютер

    https://github.com/kukoracha/kvadra_example.git

2.Создайте виртуальное окружение 
    
    virtual env name_env

3.Активируйте виртуальное окружение 

4.Перейдите в папку с проектом и установите все пакеты указанные в файле requirements.txt 
    
    pip freeze > requirements.txt
5.В файле example1/settings.py установите настройки подключения к базе данных

6.Выполните миграцию 
    
    python manage.py migrate
7.Создайте суперпользователя 
    
    python manage.py createsuperuser
8.Запустите dev сервер 
    
    python manage.py runserver
