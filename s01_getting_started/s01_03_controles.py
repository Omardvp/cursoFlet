import flet 
from flet import Page, Text

def main(page: Page):
    lbl_texto = Text(value="Dale Rojo!", color="Red") 
    page.controls.append(lbl_texto)
    page.update()



# Lanza la aplicacion en modo escritorio: 
flet.app(target=main)


# Lanza la aplicación en modo Web:
# flet.app(target=main, view=flet.WEB_BROWSER)
# 