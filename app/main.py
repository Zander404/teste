import flet
from flet import *
import requests


WEIGHT_SCREEN = 660
HEIGHT_SCREEN = 500
BG_COLOR = '#851642'


class Login(UserControl):
    def __init__(self):
        # Instancia Objetos
        self.title = Text(
            value='Login', style=TextStyle(size=24, weight='bold'))

        self.main = Container(
            padding=10,
            width=WEIGHT_SCREEN,
            height=HEIGHT_SCREEN,
            bgcolor=BG_COLOR,
            animate=animation.Animation(550, AnimationCurve.EASE_IN_OUT)

        )
        self.main_box = Row(
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.START,
            spacing=20,
            opacity=100,
            animate_opacity=800,
            visible=True,
        )

        self.content_box = Column(
            opacity=100,
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            animate_opacity=800,
            visible=True,
        )

        self.user_name_tf = TextField(
            value='',
            label='Nome de Usuário',
            color='white',
            border='underline',
            cursor_color='white',
            cursor_width=2,
            border_color='white',
        )

        self.user_password_tf = TextField(
            label='Senha',
            border='underline',
            border_color='white',
            color='white',
            cursor_color='white',
            cursor_width=2,
            password=True,
            can_reveal_password=True)

        self.login_bt = ElevatedButton(
            icon=icons.LOGIN,
            color='red',
            bgcolor='white',
            text='Login',
            height=34,
            style=ButtonStyle(shape={'': RoundedRectangleBorder(radius=8)}),
            on_click=lambda x: self.login()
        )

        self.error_message = Text('Email ou Senha Inválido!', color='red', visible=False)

        super().__init__()

    # Metodos
    def login(self):
        user_name = self.user_name_tf.value
        user_password = self.user_password_tf.value

        self.error_message.visible = False
        self.error_message.update()

        try:
            print(user_name)
            print(user_password)
            request = requests.post(
                'http://localhost:8000/login/', json={'email': user_name, 'password': user_password})

            if request.status_code == 200:
                print('Foi')

            else:
                self.error_message.visible = True
                self.error_message.update()

        except Exception as e:
            print(e)

    def build(self):

        content_box_items = [
            self.title,
            Divider(),
            self.user_name_tf,
            self.user_password_tf,
            Divider(),
            self.login_bt,
            self.error_message
        ]


        for item in content_box_items:
            self.content_box.controls.append(item)


        self.main_box.controls.append(self.content_box)
        self.main.content = self.main_box
        return self.main


class MainPage(UserControl):
    def __init__(self):
        ...

    def build(self):
        ...


class PlaceHolder(UserControl):
    def __init__(self):
        ...

    def build(self):
        ...


def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = 'center'

    teste = Login()

    page.add(teste)


if __name__ == '__main__':
    flet.app(target=main)
