# Python-tests-mid-level

## 📁 Структура проекта
```commandline
API-CRUD/
├── app/
│   ├── __init__.py
│   ├── main.py         # Точка входа (FastAPI)
│   ├── models.py       # SQLAlchemy модели
│   ├── schemas.py      # Pydantic схемы (DTO)
│   ├── database.py     # Настройка SQLite и сессии
│   └── crud.py         # CRUD-операции
├── tests/
│   └── test_notes.py   # Pytest тесты
├── requirements.txt
└── README.md

```

## Установка зависимостей:
```bash
   pip install -r requirements.txt
```

## Запуск сервера:
```commandline
   uvicorn app.main:app --reload
```

## Запуск тестов:
```bash
   pytest
```
