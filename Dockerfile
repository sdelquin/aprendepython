FROM debian:bullseye

ENV DEBIAN_FRONTEND=noninteractive
ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1

ENV APRENDEPYTHON_DIR=/usr/share/aprendepython

ENV PYTHONPATH=$APRENDEPYTHON_DIR
ENV PYTHONDONTWRITEBYTECODE=1
ENV VIRTUAL_ENV=/opt/venv

ENV SPHINX_PORT=8000
ENV ALLSPHINXOPTS="--host 0.0.0.0 --port $SPHINX_PORT"

EXPOSE $SPHINX_PORT

WORKDIR $APRENDEPYTHON_DIR

RUN apt-get update && apt-get install -qy \
        build-essential \
        python3 \
        python3-venv \
        texlive-fonts-extra \
        latexmk \
        texlive-luatex \
        git \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt requirements-dev.txt ./

RUN pip install --disable-pip-version-check -r requirements.txt && \
    pip install --disable-pip-version-check -r requirements-dev.txt

RUN git clone https://github.com/sdelquin/emojitex.sty.git /root/texmf/tex/latex/local/emojitex.sty/

CMD ["make", "livehtml"]
