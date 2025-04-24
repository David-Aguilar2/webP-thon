import reflex as rx

from proyectoWeb.componentes.navbar import navbar,State

# Estilo común para las páginas
def contenido(*children) -> rx.Component:
    return rx.flex(
        navbar(),
        rx.flex(
            rx.vstack(
                *children,
                align_items="center",
                spacing="4",
                width="100%",
                max_width="1200px",
                padding_x="1em"
            ),
            justify="center",
            align="center",
            width="100%",
            height="100%",
            padding_top="6em"
        ),
        direction="column",
        width="100%",
        min_height="100vh",
        bg=""
    )

# Página de inicio
def index() -> rx.Component:
    return contenido(
        rx.heading("Bienvenido a nuestra página web", color="", size="8"),
    )
# Página Introducción a python
def introduccion() -> rx.Component:
    return contenido(
        rx.heading("Introducció a python", color="", size="4"),
        rx.text("Información", color=""),
        rx.text("Primeros pasos", color="")
    )

# Página Desafíos
def juegos() -> rx.Component:
    return contenido(
        rx.heading("Desafíos", color="", size="4"),
        rx.text("Desafíos", color=""),
        rx.text("Desafíos", color="")
    )

# Página 404
def no_encontrado() -> rx.Component:
    return contenido(
        rx.heading("404 - Página no encontrada", color="", size="4"),
        rx.link("Volver al inicio", href="/", color="")
    )

# Configuración de la aplicación
app = rx.App()

# Añadir páginas
app.add_page(index, route="/")
app.add_page(introduccion, route="/intro")
app.add_page(juegos, route="/desafio")
app.add_page(no_encontrado, route="/404")
