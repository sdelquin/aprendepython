# Run development server
serve: clean
    uv run zensical serve

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
