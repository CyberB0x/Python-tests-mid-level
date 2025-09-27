from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base

# Создание таблиц при первом запуске
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Note Taking API")

# Зависимость для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинт: создать заметку
@app.post("/notes/", response_model=schemas.NoteRead)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db, note)

# Эндпоинт: получить заметку по ID
@app.get("/notes/{note_id}", response_model=schemas.NoteRead)
def read_note(note_id: int, db: Session = Depends(get_db)):
    db_note = crud.get_note(db, note_id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

# Эндпоинт: обновить заметку
@app.put("/notes/{note_id}", response_model=schemas.NoteRead)
def update_note(note_id: int, note: schemas.NoteCreate, db: Session = Depends(get_db)):
    db_note = crud.update_note(db, note_id, note)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

# Эндпоинт: удалить заметку
@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    db_note = crud.delete_note(db, note_id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"detail": "Note deleted"}
