import gif_pygame

from settings import *

from .VentanaView import VentanaView


class MiembrosView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self._botones = {}
        self._visible = True
        self.__fondo = None
        self.__fotos_integrantes = {}

    def mostrar(self):
        mousex, mousey = pygame.mouse.get_pos()
        self._botones = {}
        pygame.display.set_caption("Desarroladores HDB")
        self._pantalla.fill(ROJO_CLARO)
        self.__fondo.render(self._pantalla, (0, 0))
        texto = get_fuente(70).render("Desarolladores Heroes del Balon", True, BLANCO)
        self._pantalla.blit(texto, (int(ANCHO * 0.21), int(ALTO * 0.05)))

        # BOTONES
        tolerancia = 35
        MIEMBROS_ATRAS = self._mostrar_boton(
            flechita2
            if (ANCHO * 0.045 - tolerancia <= mousex <= ANCHO * 0.045 + tolerancia)
            and (ALTO * 0.08 - tolerancia <= mousey <= ALTO * 0.08 + tolerancia)
            else flechita,
            (ANCHO * 0.045, ALTO * 0.08),
            "",
            pygame.font.Font(EMOJIS, 50),
            NEGRO,
            BLANCO,
        )
        self._botones["atras"] = MIEMBROS_ATRAS
        boton_mostrar = self._mostrar_boton(
            boton_negro,
            (ANCHO * 0.1, ALTO * 0.93),
            "Mostrar Miembros",
            get_fuente(35),
            BLANCO,
            VERDE,
        )
        tolerancia2 = 110
        tolerancia3 = 45
        if (ANCHO * 0.1 - tolerancia2 <= mousex <= ANCHO * 0.1 + tolerancia2) and (
            ALTO * 0.93 - tolerancia3 <= mousey <= ALTO * 0.93 + tolerancia3
        ):
            # Imagenes
            bruno = self.__fotos_integrantes["bruno"]
            angelo = self.__fotos_integrantes["angelo"]
            dani = self.__fotos_integrantes["daniace"]
            leo = self.__fotos_integrantes["leo"]
            valentin = self.__fotos_integrantes["valentin"]
            axel = self.__fotos_integrantes["axel"]
            dani2 = self.__fotos_integrantes["daniel"]
            walter = self.__fotos_integrantes["walter"]
            pelu = self.__fotos_integrantes["pelu"]
            # Primera Fila Imagenes
            self._pantalla.blit(bruno, (int(ANCHO * 0.23), int(ALTO * 0.18)))
            self._pantalla.blit(angelo, (int(ANCHO * 0.43), int(ALTO * 0.18)))
            self._pantalla.blit(dani, (int(ANCHO * 0.63), int(ALTO * 0.18)))
            # Segunda Fila Imagenes
            self._pantalla.blit(leo, (int(ANCHO * 0.23), int(ALTO * 0.48)))
            self._pantalla.blit(valentin, (int(ANCHO * 0.43), int(ALTO * 0.48)))
            self._pantalla.blit(axel, (int(ANCHO * 0.63), int(ALTO * 0.48)))
            # Tercera Fila Imagenes
            self._pantalla.blit(pelu, (int(ANCHO * 0.23), int(ALTO * 0.78)))
            self._pantalla.blit(dani2, (int(ANCHO * 0.43), int(ALTO * 0.78)))
            self._pantalla.blit(walter, (int(ANCHO * 0.63), int(ALTO * 0.78)))
            # Textos
            texto_bruno = get_fuente(35).render("Bruno Aguinaga", True, CIAN)
            texto_angelo = get_fuente(35).render("  Angelo Duarte", True, CIAN)
            texto_dani = get_fuente(35).render(" Daniel Acevedo", True, CIAN)
            texto_leo = get_fuente(35).render("  Leonel Canario", True, CIAN)
            texto_valentin = get_fuente(35).render("Valentin Gonzalez", True, CIAN)
            texto_axel = get_fuente(35).render("  Axel De la Torre", True, CIAN)
            texto_pelu = get_fuente(35).render("  Franco Berro", True, CIAN)
            texto_dani2 = get_fuente(35).render(" Daniel Enegron", True, CIAN)
            texto_walter = get_fuente(35).render("   Walter Williams", True, CIAN)
            # Primera Fila
            self._pantalla.blit(texto_bruno, (int(ANCHO * 0.223), int(ALTO * 0.13)))
            self._pantalla.blit(texto_angelo, (int(ANCHO * 0.423), int(ALTO * 0.13)))
            self._pantalla.blit(texto_dani, (int(ANCHO * 0.623), int(ALTO * 0.13)))
            # Segunda Fila
            self._pantalla.blit(texto_leo, (int(ANCHO * 0.223), int(ALTO * 0.43)))
            self._pantalla.blit(texto_valentin, (int(ANCHO * 0.423), int(ALTO * 0.43)))
            self._pantalla.blit(texto_axel, (int(ANCHO * 0.623), int(ALTO * 0.43)))
            # Tercera Fila
            self._pantalla.blit(texto_pelu, (int(ANCHO * 0.223), int(ALTO * 0.73)))
            self._pantalla.blit(texto_dani2, (int(ANCHO * 0.423), int(ALTO * 0.73)))
            self._pantalla.blit(texto_walter, (int(ANCHO * 0.623), int(ALTO * 0.73)))

    def gif(self):
        self.__fondo = gif_pygame.load("src/assets/images/gifs/fondo2.gif")

    def fotos_integrantes(self):
        marco = pygame.image.load("src/assets/images/cuadro.png")
        marco = pygame.transform.scale(marco, (150, 150))
        bruno = pygame.image.load("src/assets/images/bruno.png")
        bruno = pygame.transform.scale(bruno, (150, 150))
        marco2 = pygame.image.load("src/assets/images/cuadro.png")
        marco2 = pygame.transform.scale(marco, (150, 150))
        daniel = pygame.image.load("src/assets/images/daniel.png")
        daniel = pygame.transform.scale(daniel, (150, 150))
        daniace = pygame.image.load("src/assets/images/daniace.png")
        daniace = pygame.transform.scale(daniace, (150, 150))
        angelo = pygame.image.load("src/assets/images/angelo.png")
        angelo = pygame.transform.scale(angelo, (150, 150))
        pelu = pygame.image.load("src/assets/images/pelu.png")
        pelu = pygame.transform.scale(pelu, (150, 150))
        leo = pygame.image.load("src/assets/images/leo.png")
        leo = pygame.transform.scale(leo, (150, 150))
        axel = pygame.image.load("src/assets/images/axel.png") 
        axel = pygame.transform.scale(axel, (150, 150))
        valentin = pygame.image.load("src/assets/images/valentin.png")
        valentin = pygame.transform.scale(valentin, (150, 150))
        walter = pygame.image.load("src/assets/images/walter.png")
        walter = pygame.transform.scale(walter, (150, 150))
        self.__fotos_integrantes = {
            "bruno": bruno,
            "marco": marco,
            "daniel": daniel,
            "marco2": marco2,
            "daniace": daniace,
            "angelo": angelo,
            "pelu": pelu,
            "leo": leo,
            "axel": axel,
            "valentin": valentin,
            "walter": walter,

        }
