from ._anvil_designer import RegisterPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RegisterPage(RegisterPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("btn_close", "click")
  def btn_close_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('MainPage')

  @handle("btn_loggin", "click")
  def btn_loggin_click(self, **event_args):
    """This method is called when the button is clicked"""
    nickname = self.txt_nickname.text
    email = self.txt_email.text
    password = self.txt_password.text
    confirm = self.txt_confirm.text
    role = self.drop_down_role.selected_value

    if not nickname or not password or not email:
      alert("Please fill all fields")
      return

    if password != confirm:
      alert("Passwords do not match")
      return
      
    result = anvil.server.call("register_user", nickname, password, email, role)

    if result == "exists":
      alert("User already exists")
    else:
      open_form("MainPage")
