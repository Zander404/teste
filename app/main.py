import flet
from flet import *
import requests
from time import sleep
import json


WIDTH_SCREEN = 660
HEIGHT_SCREEN = 500
BG_COLOR = '#851642'


class Login(UserControl):
    def __init__(self):
        # Instancia Objetos
        self.title = Text(
            value='Login', style=TextStyle(size=24, weight='bold'))

        self.main = Container(
            padding=10,
            width=0,
            height=HEIGHT_SCREEN,
            bgcolor=BG_COLOR,
            animate=animation.Animation(550, AnimationCurve.EASE_IN_OUT),
        )

        self.main_box = Row(
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.START,
            spacing=20,
            opacity=100,
            animate_opacity=800,
            visible=False,
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

        self.loading = ProgressRing(visible=False)

        self.error_message = Text(
            'Email ou Senha Inválido!', color='red', visible=False)

        super().__init__()

    # Metodos
    def open(self):
        sleep(0.35)
        self.main.width = WIDTH_SCREEN
        self.main.update()
        sleep(0.75)
        self.main_box.visible = True
        self.main_box.update()

    def close(self):
        sleep(0.35)
        self.main_box.visible = False
        self.main.update()
        sleep(0.5)
        self.main.width = 0
        self.main.update()
        sleep(0.75)

        self.page.controls.remove(self)
        self.main_page = MainPage()

        self.page.controls.insert(0, self.main_page)
        self.page.update()
        sleep(0.35)
        self.main_page.open()

    def login(self):
        user_name = self.user_name_tf.value
        user_password = self.user_password_tf.value

        self.loading.visible = True
        self.loading.update()

        self.error_message.visible = False
        self.error_message.update()

        try:

            print(user_name)
            print(user_password)
            request = requests.post(
                'http://localhost:8000/login/', json={'email': user_name, 'password': user_password})

            if request.status_code == 200:
                print('Foi')
                self.loading.visible = False
                self.loading.update()
                self.close()

            else:
                self.loading.visible = False
                self.loading.update()

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
            self.loading,
            self.error_message
        ]

        for item in content_box_items:
            self.content_box.controls.append(item)

        self.main_box.controls.append(self.content_box)
        self.main.content = self.main_box
        return self.main


class MainPage(UserControl):
    def __init__(self):
        self.main = Container(
            padding=10,
            width=0,
            height=HEIGHT_SCREEN,
            bgcolor=BG_COLOR,
            animate=animation.Animation(550, AnimationCurve.EASE_IN_OUT),
        )

        self.main_box = Row(alignment=MainAxisAlignment.CENTER,
                            vertical_alignment=CrossAxisAlignment.START,
                            spacing=20,
                            opacity=100,
                            animate_opacity=800,
                            visible=False,)

        self.content_box = Column(
            alignment=MainAxisAlignment.END,
            horizontal_alignment=CrossAxisAlignment.END,
            spacing=20,
            animate_offset=800,
            visible=True,
        )

        self.title = Text(value='Lobby')

        self.btns = Row(
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.START,
            spacing=20,
            opacity=100,
            animate_opacity=800,
            visible=True,

            controls=[
                self.button(text='Return',
                            btn_function=lambda x: self.route(text='back')),
                self.button(text='Animes',
                            btn_function=lambda x: self.route('anime')),
                self.button(text='Rick and Morty',
                            btn_function=lambda x: self.route('ram')),

            ]

        )

        super().__init__()

    # Metodos de Controle

    def open(self):
        sleep(0.35)
        self.main.width = WIDTH_SCREEN
        self.main.update()

        sleep(0.75)
        self.main_box.visible = True
        self.main_box.update()

    def close(self):
        self.main_box.visible = False
        self.main_box.update()
        sleep(0.35)

        self.main.width = 0
        self.main.update()
        sleep(0.75)

        self.page.controls.remove(self)
        sleep(0.35)

        self.login = Login()
        self.page.controls.insert(0, self.login)
        self.page.update()

        self.login.open()

    def button(self, text: str, btn_function):
        return ElevatedButton(
            icon=icons.BACK_HAND_OUTLINED,
            text=text,
            on_click=btn_function
        )

    def route(self, text: str):

        self.main_box.visible = False
        self.main_box.update()
        sleep(0.35)

        self.main.width = 0
        self.main.update()
        sleep(0.75)

        self.page.controls.remove(self)

        if text == 'ram':
            ram = Rick_and_Morty()
            self.page.controls.insert(0, ram)
            self.page.update()
            ram.open()

        elif text == 'anime':
            anime = Anime()
            self.page.controls.insert(0, anime)
            self.page.update()
            anime.open()

        else:
            ...

    # Metodos da Classe

    def build(self):

        main_box_items = [

            self.btns
        ]

        for item in main_box_items:
            self.content_box.controls.append(item)

        self.main_box.controls.append(self.title)
        self.main_box.controls.append(self.content_box)
        self.main.content = self.main_box
        return self.main


class Anime(UserControl):
    def __init__(self):
        self.num_page = 1

        self.main = Container(
            width=0,
            height=HEIGHT_SCREEN,
            bgcolor=BG_COLOR,
            padding=50,
            animate=animation.Animation(
                550, animation.AnimationCurve.EASE_IN_OUT)

        )

        self.main_box = Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=20,
            opacity=100,
            animate_opacity=800,
            visible=False,
        )

        self.content_box = Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            opacity=100,
            animate_opacity=800,
            visible=True,
            height=HEIGHT_SCREEN-100,

        )

        self.title = Text(value='ANIMES')

        self.return_btn = self.btn('Voltar', lambda x: self.close())

        # Componente de image
        self.images_anime = GridView(
            expand=1,
            runs_count=1,
            max_extent=76,
            child_aspect_ratio=0.6,
            spacing=5,
            run_spacing=5,
            height=HEIGHT_SCREEN-300

        )

        self.btns = Row(
            alignment=MainAxisAlignment.CENTER,
            height=100,
            controls=[
                self.btn(text='previous', btn_function=lambda x: self.page_control(
                    direction='previous'), icons=icons.SKIP_PREVIOUS),
                self.btn(text='next', btn_function=lambda x: self.page_control(
                    direction='next'), icons=icons.SKIP_NEXT_OUTLINED),
            ]
        )

        super().__init__()

    def open(self):
        sleep(0.35)
        self.main.width = WIDTH_SCREEN
        self.main.update()

        sleep(0.75)
        self.main_box.visible = True
        self.main_box.update()
        self.page_control()

    def close(self):
        self.main_box.visible = False
        self.main_box.update()
        sleep(0.35)

        self.main.width = 0
        self.main.update()
        sleep(0.75)

        self.page.controls.remove(self)
        main_page = MainPage()
        self.page.controls.insert(0, main_page)
        self.page.update()
        main_page.open()

    def btn(self, text, btn_function, icons=icons.UNDO):
        return ElevatedButton(
            icon=icons,
            text=text,
            on_click=btn_function,
            # style={'': RoundedRectangleBorder(0)}
        )

    def page_control(self, direction: str = 'init'):
        if direction == 'next':
            self.num_page += 1
            response = self.request(self.num_page)
            self.images_anime.clean()


        elif direction == 'previous':
            self.num_page -= 1
            response = self.request(self.num_page)
            self.images_anime.clean()

        else:
            response = self.request(self.num_page)
            self.images_anime.clean()


        count = self.num_page*10

        for i in range(0, len(response)):
            self.images_anime.controls.append(
                Container(
                    content=Image(
                        src=response[i]['image'],
                        fit=ImageFit.COVER,
                        repeat=ImageRepeat.NO_REPEAT,
                        border_radius=border_radius.all(10),
                        data=response[i]['name']

                    ),
                    key=count,

                    on_click=lambda x: print(x.control.content.data)
                )
            )
            count += 1

        self.images_anime.update()

    def request(self, page:int=1):
        response = requests.get(
            f'https://rickandmortyapi.com/api/character/?page={page}')
        data = response.json()['results']
        return data

    def build(self):
        content_items = [
            self.return_btn,
            self.images_anime,
            self.btns,

        ]

        for i in content_items:
            self.content_box.controls.append(i)

        self.main_box.controls.append(self.title)
        self.main_box.controls.append(self.content_box)
        self.main.content = self.main_box

        return self.main


class Rick_and_Morty(UserControl):
    def __init__(self):

        self.main = Container(
            width=0,
            height=HEIGHT_SCREEN,
            bgcolor=BG_COLOR,
            animate=animation.Animation(
                550, animation.AnimationCurve.EASE_IN_OUT)
        )

        self.main_box = Row(
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER,
            spacing=20,
            opacity=100,
            animate_opacity=800,
            visible=False
        )

        self.content_box = Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=20
        )

        self.title = Text(value='RICK AND MORTY')

        self.return_btn = self.btn(
            text='Voltar', btn_function=lambda x: self.close())

        super().__init__()

    def open(self):

        sleep(0.35)
        self.main.width = WIDTH_SCREEN
        self.main.update()

        sleep(0.75)
        self.main_box.visible = True
        self.main_box.update()

    def close(self):
        self.main_box.visible = False
        self.main_box.update()
        sleep(0.35)

        self.main.width = 0
        self.main.update()
        sleep(0.75)

        self.page.controls.remove(self)
        main_page = MainPage()
        self.page.controls.insert(0, main_page)
        self.page.update()
        main_page.open()

    def btn(self, text: str, btn_function, icons=icons.UNDO):
        return ElevatedButton(
            text=text,
            on_click=btn_function,
            icon=icons,

        )

    def build(self):

        content_box_items = [
            self.return_btn,

        ]

        for i in content_box_items:
            self.content_box.controls.append(i)

        self.main_box.controls.append(self.title)
        self.main_box.controls.append(self.content_box)
        self.main.content = self.main_box
        return self.main


class PlaceHolder(UserControl):
    def __init__(self):
        ...

    def build(self):
        ...


def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = 'center'

    # teste = Login()
    # page.add(teste)
    # page.update()
    # teste.open()

    # main_page = MainPage()
    # page.add(main_page)
    # page.update()
    # main_page.open()

    anime = Anime()
    page.add(anime)
    page.update()
    anime.open()
    anime.page_control()

    # ram = Rick_and_Morty()
    # page.add(ram)
    # page.update()
    # ram.open()


if __name__ == '__main__':
    flet.app(target=main)
