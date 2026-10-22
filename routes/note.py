from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

from models.note import Note
from config.db import conn
from schema.note import notesEntity

note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    new_docs = notesEntity(list(conn.notes.notes.find({})))
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"newDocs": new_docs},
    )


@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    title = form.get("title")
    desc = form.get("desc")

    if not isinstance(title, str) or not isinstance(desc, str):
        raise HTTPException(status_code=422, detail="Title and description are required.")

    try:
        note_data = Note(
            title=title.strip(),
            desc=desc.strip(),
            important=form.get("important") == "on",
        )
    except ValidationError as error:
        raise HTTPException(status_code=422, detail=error.errors()) from error

    conn.notes.notes.insert_one(note_data.model_dump())
    return RedirectResponse(url="/", status_code=303)