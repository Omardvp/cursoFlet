import flet 
from flet import IconButton, Page, Row, TextField, icons

def main(page: Page):
    page.Title = 'Flet Counter'
    page.vertical_alignmet = 'center'

    txt_number = TextField(value='0', text_align='right', width=100)

    def minus_click(event):
        txt_number.value = int(txt_number.value) - 1
        page.update()

    def plus_click(event):
        txt_number.value = int(txt_number.value) + 1    
        page.update()

    page.add(
        Row(
            [
                IconButton(icons.REMOVE,
                        on_click=minus_click),
                        txt_number,
                        IconButton(icons.ADD, on_click=plus_click)
            ],
            alignment='center'
        )
    )

# Modo desktop
# flet.app(target=main)

# Modo web
flet.app(target=main, view=flet.WEB_BROWSER)

