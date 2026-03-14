import asyncio
import base64
import os
import flet as ft

async def main(page: ft.Page):
    page.title = 'My clicker'
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.TRANSPARENT
    with open(r'ClickerTelega/utils/assets/BG_forest_coin1.png', 'rb') as f:
        img = f.read()
    image_BG = base64.b64encode(img)
    page.decoration = ft.BoxDecoration(
        image=ft.DecorationImage(
            src_base64=image_BG.decode(),
            fit=ft.ImageFit.COVER
        ),
        bgcolor="#141221"
    )
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    async def score_up(event: ft.ContainerTapEvent):
        score.data += 1
        score.value = str(score.data)
        image.scale = 0.95
        progress_bar.value += (1 / 20)

        page.update()
        await asyncio.sleep(0.1)
        if score.data % 20 == 0:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value='+20 point',
                    size=30,
                    color=ft.colors.YELLOW,
                    text_align=ft.TextAlign.CENTER
                ),
                open=True,
                bgcolor=ft.colors.TRANSPARENT
            )
            progress_bar.value = 0
        image.scale = 1
        page.update()

    with open(r'ClickerTelega/utils/assets/rec.png', 'rb') as f:
        img = f.read()
        image_base = base64.b64encode(img)

    score = ft.Text(value='0', size=100, data=0, color=ft.colors.YELLOW)
    score_counter = ft.Text(size=50, animate_opacity=ft.Animation(duration=600,
                                                                  curve=ft.AnimationCurve.BOUNCE_IN))
    image = ft.Image(
        src_base64=image_base.decode(),
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)
    )
    progress_bar = ft.ProgressBar(
        value=0,
        width=page.width - 200,
        bar_height=30,
        color='#fcf803',
        bgcolor='#94fc03'
    )

    await page.add_async(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click=score_up,
            margin=ft.Margin(0, 0, 0, 30)
        ),
        ft.Container(
            content=progress_bar,
            border_radius=ft.BorderRadius(10, 10, 10, 10)
        )
    )


if __name__ == "__main__":
    ft.app(
        target=main,
        assets_dir='assets',
        host='127.0.0.1',
        port=4444
    )