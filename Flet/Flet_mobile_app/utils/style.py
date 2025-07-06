import flet as ft

PageBgColor: str = "#1A1B20"
PageWidth: int = 620
PageHeight: int = 800

PageFont: dict = {
    "Roboto": "assets/fonts/Roboto.ttf",
    "Roboto-italic": "assets/fonts/Roboto-Italic.ttf"
}

TextColor = "#4E70D4"

ButtonWhiteStyle: dict = {
    "bgcolor": {ft.ControlState.HOVERED: "#ffffff", ft.ControlState.DEFAULT: "#1A1B20"},
    "color": {ft.ControlState.HOVERED: "#1F222B", ft.ControlState.DEFAULT: "#ffffff"},
    "side": ft.BorderSide(color="#ffffff", width=2),
    "shape": ft.RoundedRectangleBorder(radius=5)
}

ButtonBlueStyle: dict = {
    "bgcolor": "#4E70D4",
    "color": "#ffffff",
    "shape": ft.RoundedRectangleBorder(radius=5)
}


