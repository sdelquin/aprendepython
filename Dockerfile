FROM debian

RUN apt-get update && \
    apt-get install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh

ENV UV_LINK_MODE=copy \
    PATH="/root/.local/bin:$PATH"

WORKDIR /docs
COPY . /docs

CMD ["uv", "run", "mkdocs", "build"]
