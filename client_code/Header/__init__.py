from ._anvil_designer import HeaderTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Header(HeaderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    anvil.server.call("login_user", 'Ben Schmidt', '1234')
    self.refresh_auth_ui()

  def refresh_auth_ui(self):
    user = anvil.server.call("get_logged_user")

    if user:
      self.label_user.text = f"Hello, {user}"
      self.btn_login.visible = False
      self.btn_register.visible = False
    else:
      self.label_user.text = ""
      self.btn_login.visible = True
      self.btn_register.visible = True

  @handle("btn_login", "click")
  def btn_login_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('LoginPage')

  @handle("btn_register", "click")
  def btn_register_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('RegisterPage')
