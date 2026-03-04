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
