# jasonkena_cv

My CV based heavily on [Aras Güngöre's wonderful template](https://github.com/arasgungore/arasgungore-CV) and inspired by [JSON Resume's](https://jsonresume.org/) ease of use.

`render.py` uses `jinja2` to render `template.tex` with the data in `data.yaml`, generating `main.tex`.

## Compile pdf

```sh
python render.py
pdflatex main.tex
```
or
```sh
ls data.yaml template.tex | entr python render.py & latexmk -pvc -pdf main.tex
```
