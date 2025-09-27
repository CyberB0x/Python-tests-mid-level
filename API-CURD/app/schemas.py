from pydantic import BaseModel, ConfigDict

# Схема для создания заметки (входные данные)
class NoteCreate(BaseModel):
    title: str
    content: str

# Схема для ответа (включает id)
class NoteRead(NoteCreate):
    id: int

    # Для работы с ORM-моделями (SQLAlchemy)
    model_config = ConfigDict(from_attributes=True)
