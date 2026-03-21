from flet import *
# from plyer import flash
def view(page:Page):
    page.window.width = 390
    page.window.height = 740
    page.window.top = 1
    page.window.left = 960
    page.theme_mode = "light"

    flash = Flashlight()
    page.overlay.append(flash)

    PH = PermissionHandler()
    page.overlay.append(PH)

    def open_setting():
        PH.open_app_settings()

    page.add(
        AppBar(
            title= Text("Flash app [OmD]"),
            bgcolor= "pink",
            actions=[
                IconButton(icon=Icons.SETTINGS, on_click=open_setting)
            ]),
        
        Row(
            [Text("\n\n Flash Light App",size=26)],alignment="center"
        ),

        Text("\n"),


        Row([
            ElevatedButton("ON", bgcolor= Colors.PINK , color=Colors.WHITE , icon= Icons.PLAY_ARROW, on_click=lambda _: flash.turn_on),
            ElevatedButton("OFF", bgcolor= Colors.PINK , color=Colors.WHITE, icon=Icons.PLAY_DISABLED_SHARP, on_click=lambda _: flash.turn_off),


        ],alignment="center")

        )
    



app(target = view)
