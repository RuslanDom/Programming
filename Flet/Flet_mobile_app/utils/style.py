import flet as ft

PageBgColor: str = "#1A1B20"
pageWidth: int = 620
pageHeight: int = 800

pageFont: dict = {
    "Roboto": "assets/fonts/Roboto.ttf",
    "Roboto-italic": "assets/fonts/Roboto-Italic.ttf"
}

textColor = "#4E70D4"

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

InputPhoneStyle: dict = {
    "border_width": '0',
    "filled": True,
    "fill_color": '#1F222B',
    "text_size": '12',
    'text_style': ft.TextStyle(font_family="Roboto", color="A6A7AA"),
    "border_radius": ft.border_radius.all(5),
    "height": 50
}