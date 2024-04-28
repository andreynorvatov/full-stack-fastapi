# full-stack-fastapi

## App
`uvicorn src/main:app --reload --host 127.0.0.1 --port 8008`

## alembic
Для накатывания миграций, если файла alembic.ini ещё нет, нужно запустить в терминале команду:
`alembic init alembic`
После этого будет создана папка с миграциями и конфигурационный файл для алембика.

В alembic.ini нужно задать адрес базы данных, в которую будем катать миграции.
Дальше идём в папку с миграциями и открываем env.py, там вносим изменения в блок, где написано
`from myapp import mymodel`

Далее создание миграции (делается при любых изменениях моделей): 
`alembic revision --autogenerate -m"db create"` 

Далее накатывание миграции
`alembic upgrade heads`

## links
[https://github.com/zhanymkanov/fastapi-best-practices](https://github.com/tiangolo/full-stack-fastapi-template/tree/master/backend)
[https://github.com/tiangolo/full-stack-fastapi-template/tree/master/backend](https://github.com/tiangolo/full-stack-fastapi-template/tree/master/backend)

[https://www.youtube.com/watch?v=1Ag3RoOjNI0&list=PLeLN0qH0-mCVQKZ8-W1LhxDcVlWtTALCS&index=10](https://github.com/tiangolo/full-stack-fastapi-template/tree/master/backend)


