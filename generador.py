import re

# =========================
# Interpolación {{estado}}
# =========================
def interpolar_texto(texto, estado):
    def reemplazo(match):
        nombre = match.group(1)
        return str(estado.get(nombre, ""))

    return re.sub(r"\{\{(\w+)\}\}", reemplazo, texto)


# =========================
# Generador principal
# =========================
def generar_html(pagina):
    # Estado de la página (si existe)
    estado = getattr(pagina, "estado", {})

    cuerpo = "\n".join(
        render_elemento(e, 1, estado)
        for e in pagina.elementos
    )

    return f"""<!DOCTYPE html>
<html>
<body>
{cuerpo}
</body>
</html>"""


# =========================
# Render de elementos
# =========================
def render_elemento(elemento, nivel, estado):
    indent = "    " * nivel

    # ---------- Contenedor ----------
    if elemento.__class__.__name__ == "ContainerNode":
        estilo = ""
        if elemento.estilos:
            estilo = f' style="{estilos_a_css(elemento.estilos)}"'

        contenido = "\n".join(
            render_elemento(e, nivel + 1, estado)
            for e in elemento.elementos
        )

        return f"""{indent}<div{estilo}>
{contenido}
{indent}</div>"""

    # ---------- Texto ----------
    if elemento.__class__.__name__ == "TextNode":
        texto = interpolar_texto(elemento.texto, estado)
        return f"{indent}<span>{texto}</span>"

    # ---------- Botón ----------
    if elemento.__class__.__name__ == "ButtonNode":
        js = "; ".join(
            f"alert('{a.mensaje}')"
            for a in elemento.acciones
        )
        return f'{indent}<button onclick="{js}">{elemento.texto}</button>'

    return ""


# =========================
# Estilos → CSS
# =========================
def estilos_a_css(estilos):
    mapa = {
        "FONDO": "background",
        "COLOR_TEXTO": "color",
        "RELLENO": "padding",
        "MARGEN": "margin",
        "ANCHO": "width",
        "ALTO": "height",
    }

    css = []
    for k, v in estilos.items():
        if v.isdigit():
            css.append(f"{mapa[k]}:{v}px")
        else:
            css.append(f"{mapa[k]}:{v}")

    return ";".join(css)
