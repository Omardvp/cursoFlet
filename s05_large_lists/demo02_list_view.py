import flet 
from flet import ListView, Page, Text

def main(page: Page):
    lvw_textos = ListView(expand=True, spacing=10)

    for i in range (5000):
        lvw_textos.controls.append(Text(f'Line{i}'))

    page.add(lvw_textos)

#Ejecutar modo escritorio
flet.app(target=main)