import flet as ft

# Стилизация

defaultBgColor = "#731d14"
defaultFontColor = "#fabb00"

secondBgColor = "#de7d73"
secondFontColor = "#ffffff"

inputBgColor = ""
hoverBgColor = "#e0c600"

# Экран

defaultWidthWindow = "1000"
defaultHeightWindow = "600"

# Поле с ошибкой
errorFieldBgColor = "#b15204"

# Стиль меню
style_meny = ft.ButtonStyle(color={ft.ControlState.HOVERED: ft.colors.WHITE,
                                   ft.ControlState.DEFAULT: ft.colors.YELLOW
                                   }, icon_size=20, overlay_color=hoverBgColor, shadow_color=hoverBgColor)



