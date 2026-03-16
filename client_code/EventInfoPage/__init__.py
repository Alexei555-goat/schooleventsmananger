from ._anvil_designer import EventInfoPageTemplate
from anvil import *
import anvil.server as backend
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class EventInfoPage(EventInfoPageTemplate):

  title = ""
  
  def __init__(self, input, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.title = input['title']
    description = backend.call("query_event_description", self.title)[0][0]
    date = input['date']
    location = input['location']
    created_by = input['created_by']
    category = input['category']
    
    self.label_title.text = f"{self.title} {description} {date} {location} {created_by} {category}"
    

  @handle("btn_back", "click")
  def btn_back_click(self, **event_args):
    open_form('EventsPage')
    pass

  @handle("b_delete", "click")
  def b_delete_click(self, **event_args):
    """This method is called when the button is clicked"""

    if self.title != "":
      backend.call("delete_event", self.title)
  
    alert("Event deleted!")
  
    open_form("MainPage")
