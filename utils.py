"""Служебный функции."""

import json
from pathlib import Path

PATH = "tasks.json"


def write_tasks(tasks: list[dict[str, str | int]], path: str = PATH) -> None:
    """_summary_.

    Args:
    ----
        tasks (list[dict[str, str  |  int]]): _description_
        path (str, optional): _description_. Defaults to PATH.

    """
    path = Path.resolve.parent / path
    with path.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)


def read_tasks(path: str = PATH) -> list[dict[str, str | int]]:
    """_summary_.

    Args:
    ----
        path (str, optional): _description_. Defaults to PATH.

    Returns:
    -------
        list[dict[str, str | int]]: _description_

    """
    path = Path.resolve.parent / path
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def filter_tasks(
    tasks: list[dict[str, str | int]],
    priority: int,
) -> list[dict[str, str | int]]:
    """_summary_.

    Args:
    ----
        tasks (list[dict[str, str  |  int]]): _description_
        priority (int): _description_

    Returns:
    -------
        list[dict[str, str | int]]: _description_

    """
    return [task for task in tasks if task.get("priority") == priority]
