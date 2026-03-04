from ._anvil_designer import LoginPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class LoginPage(LoginPageTemplate):
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
    password = self.txt_password.text
    success = anvil.server.call("login_user", nickname, password)

    if success:
      open_form("MainPage")   # 👈 THIS switches to MainPage
    else:
      alert("Invalid login")
