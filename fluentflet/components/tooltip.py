import flet as ft


class ToolTip(ft.Tooltip):
    def __init__(self, **kwargs):
        super().__init__(
            padding=6,
            border_radius=4,
            text_style=ft.TextStyle(size=11, color=ft.Colors.WHITE),
            bgcolor="#2d2d2d",
            border=ft.border.all(1, ft.Colors.with_opacity(0.6, ft.Colors.BLACK)),
            prefer_below=False,
            wait_duration=300,
            **kwargs
        )
