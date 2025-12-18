from lexer import lexer
from parser import Parser
from generador import generar_html

with open("ejemplos/inicio.ken", encoding="utf-8") as f:
    codigo = f.read()

tokens = lexer(codigo)
parser = Parser(tokens)
pagina = parser.parse()

pagina.estado = {
    "nombre":"santi"
}

html = generar_html(pagina)


with open("salida.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Archivo HTML generado: salida.html")
