import flet 
from flet import Page, TextField, Column

def main(page: Page):
    txt_firt_name = TextField()
    txt_last_name = TextField()
    # Propiedad disabled asignada de forma individual 
    txt_firt_name.disabled = True

    col_controles = Column(controls=[txt_firt_name,txt_last_name])

    # col_controles.disabled //Todo

    page.add(col_controles)

# Ejecucion de la aplicacion en modo escritorio
flet.app(target=main)