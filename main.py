from lexer import lexer
from parser import Parser
from generador import generar_html

with open("ejemplos/inicio.ken") as f:
    codigo = f.read()

tokens = lexer(codigo)
parser = Parser(tokens)
pagina = parser.parse()

html = generar_html(pagina)
print(html)
#print(tokens)