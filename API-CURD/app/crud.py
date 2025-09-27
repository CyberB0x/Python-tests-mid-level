from sqlalchemy.orm import Session
from . import models, schemas

# Создание новой заметки
def create_note(db: Session, note: schemas.NoteCreate):
    db_note = models.Note(**note.model_dump())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

# Получение заметки по ID
def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()

# Обновление заметки
def update_note(db: Session, note_id: int, note: schemas.NoteCreate):
    db_note = get_note(db, note_id)
    if db_note:
        db_note.title = note.title
        db_note.content = note.content
        db.commit()
        db.refresh(db_note)
    return db_note

# Удаление заметки
def delete_note(db: Session, note_id: int):
    db_note = get_note(db, note_id)
    if db_note:
        db.delete(db_note)
        db.commit()
    return db_note
