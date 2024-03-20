"""Точка входа в приложение."""

<<<<<<< HEAD
from datetime import datetime, timezone
=======
from datetime import datetime
>>>>>>> 4ff00fa (test2)

from fastapi import (
    FastAPI,
    Request,
)
from fastapi.responses import JSONResponse as Response

from utils import filter_tasks, read_tasks, write_tasks

app = FastAPI()


@app.get("/")
def get(r: Request) -> Response:
<<<<<<< HEAD
    """_summary_.

    Args:
    ----
        r (Request): _description_

    Returns:
    -------
        Response: _description_

    """
=======
    """Функция получения задач по приоритету."""
>>>>>>> 4ff00fa (test2)
    priority = r.query_params.get("priority")
    data = read_tasks()
    if priority:
        data = filter_tasks(data, int(priority))
    return Response(content=data, status_code=200)


@app.post("/")
async def post(r: Request) -> Response:
<<<<<<< HEAD
    """_summary_.
=======
    """Описание.
>>>>>>> 4ff00fa (test2)

    Args:
    ----
        r (Request): _description_

    Returns:
    -------
        Response: _description_

    """
    data = await r.json()
    errors = [
        f"Нет поля {item}"
        for item in ("title", "description", "priority")
        if not data.get(item)
    ]
<<<<<<< HEAD
=======

>>>>>>> 4ff00fa (test2)
    if not isinstance(data.get("priority"), int):  # и тут
        errors.append("Поле priority должно быть числом")
    if errors:
        return Response(content=errors, status_code=400)
    task = {
        "title": data.get("title"),
        "description": data.get("description"),
        "priority": int(data.get("priority")),
<<<<<<< HEAD
        "date": datetime.now(tz=timezone.utc).strftime("%Y.%m.%d %H:%M"),
=======
        "date": datetime.now(datetime.timezone.utc).strftime("%Y.%m.%d %H:%M"),
>>>>>>> 4ff00fa (test2)
    }
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)
    return Response(content=task, status_code=201)


@app.delete("/")
def delete(r: Request) -> Response:
<<<<<<< HEAD
    """safdsaf.
=======
    """_summary_.
>>>>>>> 4ff00fa (test2)

    Args:
    ----
        r (Request): _description_

    Returns:
    -------
        Response: _description_

    """
    title = r.query_params.get("title")
    if not title:
        return Response(content=["Нет поля title"], status_code=400)
    tasks = read_tasks()
    new_tasks = [task for task in tasks if task.get("title") != title]
    if len(new_tasks) == len(tasks):
        return Response(content=["Нет такой task"], status_code=404)
    write_tasks(new_tasks)
    return Response(content=None, status_code=204)
