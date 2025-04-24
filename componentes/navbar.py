import reflex as rx

class State(rx.State):
    active_tab: str = "home"

    def set_active_tab(self, tab: str):
        self.active_tab = tab

def navbar() -> rx.Component:
    def nav_link(name: str, href: str) -> rx.Component:
        return rx.link(
            name,
            href=href,
            on_click=lambda: State.set_active_tab(name.lower()),
            padding="1em",
            color=rx.cond(
                State.active_tab == name.lower(),
                "",  # Color activo
                ""   # Color normal
            ),
            _hover={"text_decoration": "none", "color": ""}
        )
    
    return rx.hstack(
        nav_link("Inicio", "/"),
        nav_link("Introducción a python", "/intro"),
        nav_link("Desafíos", "/desafio"),
        position="fixed",
        top="0",
        width="100%",
        bg="",
        backdrop_filter="blur(10px)",
        padding="1em",
        z_index="999",
        justify="center"
    )