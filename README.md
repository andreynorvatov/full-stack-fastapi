# full-stack-fastapi

## App
`uvicorn main:app --reload --host 127.0.0.1 --port 8008`

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

## TODO

#### FastAPI
- [ ] БД 
  - [x] Модели с alembic
  - [x] alembic новый file_template для миграций
  - [ ] Заполнение данных
  - [ ] Использование DTO ??
  - [ ] Использование SQLModel
  - [ ] Запросы CRUD
- [ ] Роутинг
- [ ] Расположение директорий и файлов
- [ ] Swagger офлайн

#### Streamlit
- [ ] Мультистраничное приложение


## links
[https://github.com/zhanymkanov/fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices)

[https://github.com/tiangolo/full-stack-fastapi-template/tree/master/backend](https://github.com/tiangolo/full-stack-fastapi-template/tree/master/backend)

[https://www.youtube.com/watch?v=1Ag3RoOjNI0&list=PLeLN0qH0-mCVQKZ8-W1LhxDcVlWtTALCS&index=10](https://www.youtube.com/watch?v=1Ag3RoOjNI0&list=PLeLN0qH0-mCVQKZ8-W1LhxDcVlWtTALCS&index=10)

[УРОКИ FASTAPI НА БОЕВОМ СЕРВИСЕ](https://www.youtube.com/watch?v=UkwpJyvf8CA&list=PLlKID9PnOE5jiWTTsshCXdz5qvg8JWezX)

[fastapi-onion](https://github.com/artemonsh/fastapi-onion-architecture/)


