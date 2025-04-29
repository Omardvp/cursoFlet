import flet
from flet import IconButton, Page, Row, TextField, icons, Text

def main(page: Page):
    lbl_texto = Text(
        value='Fletes y algo',
        size=30,
        color='green',
        bgcolor='black',
        weight='bold',
        italic=True
    )
    page.title = 'Contador'
    page.vertical_alignment = 'center'

    txt_numero = TextField(value='0', text_align='right',width=100)

    def reducir_clicked(event):
        txt_numero.value = int(txt_numero.value) - 1
        page.update()

    def aumentar_Clicked(event): 
        txt_numero.value = int(txt_numero.value) + 1
        page.update()

    page.add(
        Row(
            [
                lbl_texto,
                IconButton(icons.REMOVE, 
                on_click=reducir_clicked),
                txt_numero,
                IconButton(icons.ADD,
                on_click=aumentar_Clicked)
            ]
        )
    )    


# Modo escritorio
flet.app(target=main)