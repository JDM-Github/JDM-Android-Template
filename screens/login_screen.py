import threading
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.clock import Clock

from kivy.metrics import dp, sp
from kivy.utils import get_color_from_hex as GetColor
from kivy.graphics import Rectangle, RoundedRectangle, Color

from widgets import CircleImage, RoundedTextInput, CustomButton, LoadingPopup, BackButton, Utility, ThemedPopup
from handle_requests import RequestHandler


class LoginScreen(Screen):

	def display_design(self):
		self.size = self.manager.size
		with self.canvas.before:
			Color(rgba=GetColor(self.manager.theme.main_color))
			Rectangle(size=self.size)

			Color(rgba=GetColor("#ffffff"))
			RoundedRectangle(
				size=(self.width, Utility.get_value_percentage(self.height, 0.25)),
				radius=[dp(30), dp(30), 0, 0])

		self.display_widget()



	def display_widget(self):
		self.clear_widgets()
		widget = Widget(size=self.manager.size, pos=(0, 0))

		layout    = BoxLayout(orientation='vertical', padding=Utility.get_value_percentage(self.height, 0.03), spacing=Utility.get_value_percentage(self.height, 0.03), size=self.manager.size)
		self.logo = CircleImage(source=self.manager.main_config['icon'], size_hint=(None, None), pos_hint={"center_x": 0.5}, size=(self.width * 0.65, self.width * 0.65))
		layout.add_widget(self.logo)

		self.email = RoundedTextInput(hint_text="Email", icon_source='assets/email.png')
		self.password = RoundedTextInput(hint_text="Password", password=True,
			icon_source='assets/pass.png',
			eye_icon_source='assets/close.png')

		login_btn    = CustomButton(self.manager, text="Login", on_press=self.login)
		register_btn = CustomButton(self.manager, text="Create an account", on_press=self.go_to_register)

		layout.add_widget(Label(text="Japan", font_size=sp(56), bold=True, size_hint_y=None, height=dp(20)))
		layout.add_widget(Widget(size_hint_y=None, height=dp(10)))

		layout.add_widget(self.email)
		layout.add_widget(self.password)

		forgot_password_label = Label(
			text="[b][ref=forgot_password]Forgot password?[/ref][/b]",
			size_hint_y=None,
			height=dp(30),
			valign='top',
			halign='center',
			markup=True,
			font_size=sp(14),
		)
		forgot_password_label.bind(size=forgot_password_label.setter('text_size'))
		layout.add_widget(forgot_password_label)

		layout.add_widget(login_btn)
		layout.add_widget(register_btn)
		layout.add_widget(Widget(size_hint_y=None, height=dp(5)))

		widget.add_widget(layout)
		self.add_widget(widget)


	def layout_on_ref_press(self, *args):
		if args[1] == "forgot_password":
			self.go_to_login()

	def go_to_home(self):
		self.manager.home.all_middle_section = {}
		self.manager.current = 'home'
		self.manager.home.update_button_active('home')

	def go_to_register(self):
		self.manager.current = 'register'

	def show_error_popup(self, message):
		popup = ThemedPopup(
			self.manager,
			title='Login Failed',
			message=message)
		popup.open()


	def login(self):
		self.loading = LoadingPopup(self.manager)
		self.add_widget(self.loading)
		threading.Thread(target=self._login).start()

	def _login(self):
		result, response = RequestHandler.create_request(
			method="get",
			link="user/login",
			data={
				'email'   : self.email.input.text,
				'password': self.password.input.text
			}
		)
		if result:
			self.on_success(response)
		else:
			self.on_error(response)


	def on_success(self, result):
		Clock.schedule_once(lambda dt: self._on_success(result))

	def on_error(self, error):
		Clock.schedule_once(lambda dt: self._on_error(error))

	def _on_success(self, result):
		self.remove_widget(self.loading)
		if result and result.get('success', None):
			self.manager.main_state['already_login'] = True
			self.manager.main_state['user'] = result.get('user', {})
			# self.manager.save_json_config("state.json", self.manager.main_state)
			popup = ThemedPopup(
				self.manager,
				title='Login Success',
				message=result.get('message'))
			popup.open()

			self.go_to_home()			
		else:
			self.show_error_popup(result.get('message', 'Login failed.'))

	def _on_error(self, error):
		self.remove_widget(self.loading)
		self.show_error_popup(error.get('message'))


