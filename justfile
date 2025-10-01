# Run dirty development server
rundirty port="8000":
    uv run mkdocs serve -a localhost:{{ port }} --dirty

# Run development server
runserver port="8000":
    uv run mkdocs serve -a localhost:{{ port }}

alias b:=build
# Build docs
build:
    uv run mkdocs build --clean
