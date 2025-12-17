def generar_html(pagina):
    cuerpo = "\n".join(
        render_elemento(e, 1) for e in pagina.elementos
    )

    return f"""<!DOCTYPE html>
<html>
<body>
{cuerpo}
</body>
</html>"""


def render_elemento(elemento, nivel):
    indent = "    " * nivel

    if elemento.__class__.__name__ == "ContainerNode":
        estilo = ""
        if elemento.estilos:
            estilo = f' style="{estilos_a_css(elemento.estilos)}"'

        contenido = "\n".join(
            render_elemento(e, nivel + 1)
            for e in elemento.elementos
        )
        return f"""{indent}<div{estilo}>
{contenido}
{indent}</div>"""

    if elemento.__class__.__name__ == "TextNode":
        return f"{indent}<span>{elemento.texto}</span>"

    if elemento.__class__.__name__ == "ButtonNode":
        js = "; ".join(
            f"alert('{a.mensaje}')"
            for a in elemento.acciones
        )
        return f'{indent}<button onclick="{js}">{elemento.texto}</button>'

    return ""

def estilos_a_css(estilos):
    mapa = {
        "FONDO": "background",
        "COLOR_TEXTO": "color",
        "PADDING": "padding",
        "MARGEN": "margin",
        "ANCHO": "width",
        "ALTO": "height",
    }

    css = []
    for k, v in estilos.items():
        css.append(f"{mapa[k]}:{v}px" if v.isdigit() else f"{mapa[k]}:{v}")

    return ";".join(css)
