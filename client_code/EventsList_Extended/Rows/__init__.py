from ._anvil_designer import RowsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Rows(RowsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("btn_info", "click")
  def btn_info_click(self, **event_args):
    open_form('EventInfoPage', self.item)
    pass
