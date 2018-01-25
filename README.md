# kvadra_example

## Инструкция по развертыванию dev версии

Скопируйте репозиторий на компьютер

    https://github.com/kukoracha/kvadra_example.git

Создайте виртуальное окружение 
    
    virtual env name_env

Активируйте виртуальное окружение 

Перейдите в папку с проектом и установите все пакеты указанные в файле requirements.txt 
    
    pip freeze > requirements.txt
В файле example1/settings.py установите настройки подключения к базе данных

Выполните миграцию 
    
    python manage.py migrate
Создайте суперпользователя 
    
    python manage.py createsuperuser
Запустите dev сервер 
    
    python manage.py runserver
