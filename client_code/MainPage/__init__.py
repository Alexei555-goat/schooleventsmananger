from ._anvil_designer import MainPageTemplate
from anvil import *
import anvil.server as backend
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class MainPage(MainPageTemplate):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  @handle("button_2", "click")
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('EventsPage')
    

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = backend.call('get_logged_user')
    if user:
      open_form('AddEventPage')
    else:
      alert('Please log in')

  @handle("button_3", "click")
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("StatisticPage")
