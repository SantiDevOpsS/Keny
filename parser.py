from ast import PageNode, ContainerNode, TextNode, ButtonNode, AlertNode, StyleNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def actual(self):
        return self.tokens[self.pos]

    def consumir(self, tipo):
        if self.actual()[0] != tipo:
            raise SyntaxError(
                f"Se esperaba {tipo}, se encontró {self.actual()}"
            )
        valor = self.actual()[1]
        self.pos += 1
        return valor

    def parse(self):
        return self.pagina()

    def pagina(self):
        self.consumir("PAGINA")
        nombre = self.consumir("IDENT")
        self.consumir("LBRACE")

        self.consumir("FUNCION")
        self.consumir("RENDER")
        self.consumir("LPAREN")
        self.consumir("RPAREN")
        self.consumir("LBRACE")

        elementos = self.elementos()

        self.consumir("RBRACE")
        self.consumir("RBRACE")

        return PageNode(nombre, elementos)

    def elementos(self):
        elementos = []
        while self.actual()[0] != "RBRACE":
            elementos.append(self.elemento())
        return elementos

    def elemento(self):
        token, valor = self.actual()

        if token == "IDENT" and valor == "contenedor":
            self.consumir("IDENT")
            self.consumir("LBRACE")
            
            estilos = {}
            elementos = []

            if self.actual()[0] == "ESTILO":
                estilos = self.estilo()

            while self.actual()[0] != "RBRACE":
                elementos.append(self.elemento())
            
            self.consumir("RBRACE")
            return ContainerNode(elementos, estilos)

        if token == "IDENT" and valor == "texto":
            self.consumir("IDENT")
            texto = self.consumir("TEXTO")
            return TextNode(texto.strip('"'))

        if token == "BOTON":
            self.consumir("BOTON")
            texto = self.consumir("TEXTO")
            self.consumir("LBRACE")

            self.consumir("AL_CLIC")
            self.consumir("LBRACE")

            acciones = []
            while self.actual()[0] != "RBRACE":
                acciones.append(self.accion())

            self.consumir("RBRACE")
            self.consumir("RBRACE")

            return ButtonNode(texto.strip('"'), acciones)

        raise SyntaxError(f"Elemento inesperado: {self.actual()}")

    def accion(self):
        token, valor = self.actual()

        if token == "ALERTA":
            self.consumir("ALERTA")
            mensaje = self.consumir("TEXTO")
            return AlertNode(mensaje.strip('"'))

        raise SyntaxError(f"Acción desconocida: {self.actual()}")
    
    def estilo(self):
        self.consumir("ESTILO")
        self.consumir("LBRACE")

        propiedades = {}

        while self.actual()[0] != "RBRACE":
            token, valor = self.actual()
            if token in (
                "FONDO", "COLOR_TEXTO", "PADDING",
                "MARGEN", "ANCHO", "ALTO"
            ):
                self.consumir(token)
                valor_prop = self.consumir("TEXTO") \
                    if self.actual()[0] == "TEXTO" \
                    else self.consumir("IDENT")
                propiedades[token] = valor_prop.strip('"')
            
            else:
                raise SyntaxError(
                    f"Propiedad de estilo inválida: {self.actual()}"
                )
        self.consumir("RBRACE")
        return propiedades
