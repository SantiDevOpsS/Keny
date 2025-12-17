class PageNode:
    def __init__(self, nombre, elementos):
        self.nombre = nombre
        #self.render = None
        #self. contenido = contenido
        self.elementos = elementos #lista

class ContainerNode:
    def __init__(self, elementos, estilos=None):
        #self.contenido = contenido
        self.elementos = elementos
        self.estilos = estilos or {}

class TextNode:
    def __init__(self, texto):
        self.texto = texto

class ButtonNode:
    def __init__(self, texto, acciones):
        self.texto = texto
        self.acciones = acciones

class ClickNode:
    def __init__(self, acciones):
        self.acciones = acciones

class AlertNode:
    def __init__(self, mensaje):
        self.mensaje = mensaje

class StyleNodes:
    def __init__(self, propiedades):
        self.propiedades = propiedades # dict