# Run development server
serve port="8000": clean
    uv run zensical serve -a localhost:{{port}}

# Build site native-way
build: clean
    uv run zensical build

# Build site docker-way
docker: clean
    docker run --rm -it -v ${PWD}:/docs zensical/zensical build

# Clean temp files
clean:
    rm -fr .cache site

# Bump version: component = [major, minor, patch]
bump component:
    uv version --bump {{component}}
