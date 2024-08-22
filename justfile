runserver port='8000':
    sphinx-autobuild --port {{ port }} . _build/html

cleanrun port='8000': clean
    just runserver {{ port }}

clean:
    make clean

html:
    make dirhtml

ideas:
    open ideas.pdf
