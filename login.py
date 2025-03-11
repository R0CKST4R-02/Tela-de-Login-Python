from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (360, 640)

KV = """
ScreenManager:
    LoginScreen:
    HomeScreen:

<LoginScreen>:
    name: "login"
    
    MDLabel:
        text: "RockStar"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0.4, 0.6, 1, 1  # Azul Marinho
        font_style: "H3"
        pos_hint: {"center_x": 0.5, "center_y": 0.85}

    MDTextField:
        id: email
        icon_left: "account"
        mode: "rectangle"
        hint_text: "Digite o seu email"
        pos_hint: {"center_x": 0.5, "center_y": 0.65}
        size_hint_x: 0.8

    MDTextField:
        id: senha
        icon_left: "key"
        mode: "rectangle"
        hint_text: "Digite a sua senha"
        password: True  # Esconde os caracteres
        pos_hint: {"center_x": 0.5, "center_y": 0.55}
        size_hint_x: 0.8

    MDRaisedButton:
        text: "Entrar"
        size_hint_x: 0.8
        size_hint_y: None
        height: 50
        md_bg_color: 0.2, 0.6, 1, 1  # Azul bonito
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        on_release: app.login()

<HomeScreen>:
    name: "home"

    MDLabel:
        text: "Crair App com Python ;)"
        halign: "center"
        font_style: "H4"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}

    MDRaisedButton:
        text: "Terminar Sessao"
        size_hint_x: 0.6
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        on_release: app.root.current = "login"
"""

class LoginScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class LoginApp(MDApp):
    def build(self):
        self.dialog = None  # Evita recriação da caixa de diálogo
        return Builder.load_string(KV)
    
    def login(self):
        login_screen = self.root.get_screen("login")  # Pega a tela de login
        email = login_screen.ids.email
        senha = login_screen.ids.senha

        if email.text == "eze" and senha.text == "1234":
            self.root.current = "home"  # Redireciona para a HomeScreen
        else:
            if not self.dialog:
                self.dialog = MDDialog(title="Erro", text="Senha inválida")
            self.dialog.open()
            
            # 🔥 Limpa os campos após erro
            email.text = ""
            senha.text = ""

LoginApp().run()
