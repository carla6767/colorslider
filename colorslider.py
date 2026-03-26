import flet as ft


def main(page: ft.Page):
    
    page.title = "RGB Color Mixer"

    # Text
    rgb_text = ft.Text("RGB(0, 0, 0)")

    def update_color(e):
        # Slider values
        r = int(red_slider.value)
        g = int(green_slider.value)
        b = int(blue_slider.value)

        
        color = f"#{r:02x}{g:02x}{b:02x}"
        page.bgcolor = color

        #values
        rgb_text.value = f"RGB({r}, {g}, {b})"

       
        page.update()

    # Sliders

    red_slider = ft.Slider(
        min=0,
        max=255,
        divisions=255,
        value=10,
        label="Red",
        on_change=update_color
    )
        


    green_slider = ft.Slider(
        min=0,
        max=255,
        divisions=255,
        value=0,
        label="Green",
        on_change=update_color
    )

    blue_slider = ft.Slider(
        min=0,
        max=255,
        divisions=255,
        value=0,
        label="Blue",
        on_change=update_color
    )

    page.add(
        ft.Text("Move the sliders to mix colors"),
        red_slider,
        green_slider,
        blue_slider,
        rgb_text
    )


ft.app(target=main)

