default:
    just --list

render:
    ls *.tex *.yaml | entr uv run render.py

compile:
    latexmk -pvc -pdf main.tex
