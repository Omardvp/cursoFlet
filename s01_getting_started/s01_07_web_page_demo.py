import flet 
from flet import Page, Text, Column, Row, TextField, ElevatedButton, AppBar, IconButton, icons

def main(page: Page):
    page.title = "Página Web Genérica"
    
    # Barra de navegación
    app_bar = AppBar(
        title=Text("Mi Página Web"),
        actions=[
            IconButton(icon=icons.HOME, tooltip="Inicio"),
            IconButton(icon=icons.INFO, tooltip="Acerca de"),
            IconButton(icon=icons.CONTACT_PAGE, tooltip="Contacto"),
        ]
    )
    
    # Campo de búsqueda
    txt_buscar = TextField(label='Buscar...', width=300)
    btn_buscar = ElevatedButton(text='Buscar', on_click=lambda e: print(f'Buscando: {txt_buscar.value}'))
    buscador = Row(controls=[txt_buscar, btn_buscar])
    
    # Contenido principal
    titulo = Text("Bienvenido a mi página web", size=24, weight="bold")
    descripcion = Text("Esta es una página web estándar hecha con Flet y Python.")
    contenido = Column(controls=[titulo, descripcion, buscador], alignment="center")
    
    page.appbar = app_bar
    page.add(contenido)

flet.app(target=main)


