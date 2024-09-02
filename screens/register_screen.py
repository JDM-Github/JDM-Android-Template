from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.network.urlrequest import UrlRequest

class RegisterScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		layout = BoxLayout(orientation='vertical', padding=10)
		
		self.username = TextInput(hint_text="Username", multiline=False)
		self.email    = TextInput(hint_text="Email", multiline=False)
		self.password = TextInput(hint_text="Password", multiline=False, password=True)
		
		register_btn      = Button(text="Register", on_press=self.register)
		back_to_login_btn = Button(text="Back to Login", on_press=self.go_to_login)
		
		layout.add_widget(Label(text="Register"))
		layout.add_widget(self.username)
		layout.add_widget(self.email)
		layout.add_widget(self.password)
		layout.add_widget(register_btn)
		layout.add_widget(back_to_login_btn)
		self.add_widget(layout)

	def register(self, instance):
		data = {
			'username': self.username.text,
			'email': self.email.text,
			'password': self.password.text
		}
		UrlRequest(
			'https://test888.netlify.app/.netlify/functions/api/register',
			req_body=str(data), on_success=self.on_success, on_failure=self.on_failure, on_error=self.on_error)

	def on_success(self, request, result):
		self.show_success()

		print("Registration successful!")
		print(result)
		self.manager.current = 'login'

	def on_failure(self, request, result):
		print("Registration failed.")
		print(result)

	def on_error(self, request, error):
		print(f"Error: {error}")

	def go_to_login(self, instance):
		self.manager.current = 'login'

	def show_success(self):
		popup = Popup(title='Register successful',
					  content=Label(text='You successfuly register an account'),
					  size_hint=(0.8, 0.4))
		popup.open()
