import flet 
from flet import Page, Row, Text

def main(page: Page):
    lenguajes = ['Python', 'Flet', 'Flutter']
    etiquetas = []

    for e in lenguajes:
        etiquetas.append(Text(e))

    row_datos = Row(controls=etiquetas)
    # row_datos = Row(controls=[Text('Python'), Text('Flet'), Text('Flutter')])
    page.add(row_datos)

flet.app(target=main)