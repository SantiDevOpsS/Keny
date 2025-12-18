import re

TOKENS = [
    # Palabras clave
    ("PAGINA", r"\bpagina\b"),
    ("FUNCION", r"\bfuncion\b"),
    ("RENDER", r"\brender\b"),
    ("BOTON", r"\bboton\b"),
    ("AL_CLIC", r"\bal_clic\b"),
    ("ALERTA", r"\balerta\b"),
    ("ESTADO", r"\bestado\b"),

    # Estilos
    ("ESTILO", r"\bestilo\b"),
    ("FONDO", r"\bfondo\b"),
    ("COLOR_TEXTO", r"\bcolor_texto\b"),
    ("RELLENO", r"\brelleno\b"),
    ("MARGEN", r"\bmargen\b"),
    ("ANCHO", r"\bancho\b"),
    ("ALTO", r"\balto\b"),

    #NUMEROS
    ("NUMERO", r"\b\d+(\.\d+)?\b"),

    # Símbolos
    ("LBRACE", r"\{"),
    ("RBRACE", r"\}"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("IGUAL", r"="),

    # Literales
    ("TEXTO", r'"[^"\n]*"'),

    # Identificadores
    ("IDENT", r"[A-Za-z_][A-Za-z0-9_]*"),

    ("ESPACIO", r"[ \t\n]+"),
]



def lexer(codigo):
    tokens = []
    pos = 0

    while pos < len(codigo):
        match = None

        for tipo, patron in TOKENS:
            regex = re.compile(patron)
            match = regex.match(codigo, pos)
            if match:
                if tipo != "ESPACIO":
                    tokens.append((tipo, match.group(0)))
                pos = match.end()
                break

        if not match:
            raise SyntaxError(
                f"Token inválido en posición {pos}: '{codigo[pos]}'"
            )

    return tokens
