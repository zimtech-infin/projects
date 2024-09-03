from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.core.window import Window
from model import UserManager  # Import UserManager


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.email_input = TextInput(hint_text='Enter email')
        self.password_input = TextInput(hint_text='Enter password', password=True)
        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.login)
        self.create_account_button = Button(text='Create Account')
        self.create_account_button.bind(on_press=self.create_account)
        self.layout.add_widget(self.email_input)
        self.layout.add_widget(self.password_input)
        self.layout.add_widget(self.login_button)
        self.layout.add_widget(self.create_account_button)
        self.add_widget(self.layout)
        Window.bind(on_key_down=self._on_key_down)

    def login(self, instance):
        email = self.email_input.text
        password = self.password_input.text
        if self.manager.user_manager.validate_user(email, password):
            self.manager.current = 'user_home'
            self.manager.get_screen('user_home').set_user(email)
        else:
            print("Invalid login credentials")

    def create_account(self, instance):
        self.manager.current = 'create_account'

    def focus_next(self):
        self.focus_next_widget(self.email_input)

    def focus_next_widget(self, widget):
        next_widget = widget.focus_next
        if next_widget:
            next_widget.focus = True

    def _on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 9:  # Tab key
            self.focus_next()


class CreateAccountScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.first_name_input = TextInput(hint_text='Enter first name')
        self.last_name_input = TextInput(hint_text='Enter last name')
        self.email_input = TextInput(hint_text='Enter email')
        self.title_input = TextInput(hint_text='Enter title')
        self.password_input = TextInput(hint_text='Enter password', password=True)
        self.create_button = Button(text='Create Account')
        self.create_button.bind(on_press=self.create_account)
        self.layout.add_widget(self.first_name_input)
        self.layout.add_widget(self.last_name_input)
        self.layout.add_widget(self.email_input)
        self.layout.add_widget(self.title_input)
        self.layout.add_widget(self.password_input)
        self.layout.add_widget(self.create_button)
        self.add_widget(self.layout)
        Window.bind(on_key_down=self._on_key_down)

    def create_account(self, instance):
        first_name = self.first_name_input.text
        last_name = self.last_name_input.text
        email = self.email_input.text
        title = self.title_input.text
        password = self.password_input.text
        self.manager.user_manager.create_user(first_name, last_name, email, title, password)
        self.manager.current = 'login'  # Navigate back to login screen

    def focus_next(self):
        self.focus_next_widget(self.first_name_input)

    def focus_next_widget(self, widget):
        next_widget = widget.focus_next
        if next_widget:
            next_widget.focus = True

    def _on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 9:  # Tab key
            self.focus_next()


class UserHomePage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.welcome_label = Label(text='Welcome')
        self.view_kanban_button = Button(text='View Kanban')
        self.view_kanban_button.bind(on_press=self.view_kanban)
        self.view_account_button = Button(text='View Account')
        self.view_account_button.bind(on_press=self.view_account)
        self.change_password_button = Button(text='Change Password')
        self.change_password_button.bind(on_press=self.change_password)
        self.layout.add_widget(self.welcome_label)
        self.layout.add_widget(self.view_kanban_button)
        self.layout.add_widget(self.view_account_button)
        self.layout.add_widget(self.change_password_button)
        self.add_widget(self.layout)

    def set_user(self, email):
        self.user = self.manager.user_manager.get_user(email)
        if self.user:
            self.welcome_label.text = f"Welcome, {self.user.first_name} {self.user.last_name}"

    def view_kanban(self, instance):
        self.manager.current = 'kanban'

    def view_account(self, instance):
        self.manager.current = 'user_account'

    def change_password(self, instance):
        self.manager.current = 'change_password'


class KanbanScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.summary_label = Label(text='Summary')
        self.layout.add_widget(self.summary_label)
        self.add_widget(self.layout)

    def set_user(self, email):
        self.user = self.manager.user_manager.get_user(email)
        self.update_summary()

    def update_summary(self):
        summary = self.user.get_summary()
        self.summary_label.text = f"Total Tasks: {summary['total_tasks']}, Milestones: {summary['milestones']}, Roadblocks: {summary['roadblocks']}"


class UserAccountScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.user_info_label = Label(text='User Information')
        self.layout.add_widget(self.user_info_label)
        self.add_widget(self.layout)

    def set_user(self, email):
        self.user = self.manager.user_manager.get_user(email)
        self.update_user_info()

    def update_user_info(self):
        self.user_info_label.text = (
            f"Name: {self.user.first_name} {self.user.last_name}\n"
            f"Email: {self.user.email}\n"
            f"Title: {self.user.title}"
        )


class ChangePasswordScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.email_input = TextInput(hint_text='Enter email')
        self.new_password_input = TextInput(hint_text='Enter new password', password=True)
        self.change_button = Button(text='Change Password')
        self.change_button.bind(on_press=self.change_password)
        self.layout.add_widget(self.email_input)
        self.layout.add_widget(self.new_password_input)
        self.layout.add_widget(self.change_button)
        self.add_widget(self.layout)

    def change_password(self, instance):
        email = self.email_input.text
        new_password = self.new_password_input.text
        self.manager.user_manager.change_password(email, new_password)
        self.manager.current = 'login'  # Navigate back to login screen


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.user_manager = UserManager()  # Initialize UserManager
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(CreateAccountScreen(name='create_account'))
        sm.add_widget(UserHomePage(name='user_home'))
        sm.add_widget(KanbanScreen(name='kanban'))
        sm.add_widget(UserAccountScreen(name='user_account'))
        sm.add_widget(ChangePasswordScreen(name='change_password'))
        return sm


if __name__ == '__main__':
    MyApp().run()
