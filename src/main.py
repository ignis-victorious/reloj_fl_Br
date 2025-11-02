#
#  Import LIBRARIES
from datetime import datetime

import flet as ft  # pyright: ignore[reportMissingTypeStubs]
from flet import (  # pyright: ignore[reportMissingTypeStubs]
    Page,
    app,  # pyright: ignore[reportUnknownVariableType]
)

#  Import FILES
# #


def main(page: Page) -> None:
    page.title = "Reloj"
    page.bgcolor = "black"

    hora = ft.Text(value="", color="purple", size=50)

    page.add(ft.Container(content=hora, alignment=ft.alignment.center, bgcolor="black"))

    while True:
        hora.value = datetime.now().strftime(format="%H:%M:%S")
        page.update()


if __name__ == "__main__":
    app(target=main)
