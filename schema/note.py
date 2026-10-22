from typing import Any


def noteEntity(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": str(item["_id"]),
        "title": item.get("title") or "Note",
        "desc": item.get("desc", item.get("note", item.get("notes", ""))),
        "important": item.get("important", False),
    }


def notesEntity(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [noteEntity(item) for item in items]