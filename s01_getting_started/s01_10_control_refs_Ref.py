import flet
from flet import Column, ElevatedButton, Page, Text, TextField, Ref 
# from flet import 

def main(page: Page):
    txt_first_name = Ref[TextField]()
    txt_last_name = Ref[TextField]()
    col_controles = Ref[Column]()

    def saludar_clicked(Event):
        col_controles.current.controls.append(Text(f'Hola, {txt_first_name.current.value} {txt_last_name.current.value}'))

        txt_first_name.current.value = ''
        txt_last_name.current.value = ''

        page.update()
        txt_first_name.focus()

    btn_saludar = ElevatedButton('Saludar',on_click=saludar_clicked)

    page.add(
        TextField(ref=txt_first_name, label='Nombre',autofocus=True),
        TextField(ref=txt_last_name, label='Apellido'),
        btn_saludar,
        Column(ref=col_controles)
    )

# Ejecucion en modo escritorio
flet.app(target=main)