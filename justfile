runserver port="8000":
    uv run mkdocs serve -a localhost:{{ port }}

rundirty port="8000":
    uv run mkdocs serve -a localhost:{{ port }} --dirty

build:
    uv run mkdocs build --clean
