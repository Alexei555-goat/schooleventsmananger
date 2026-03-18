from ._anvil_designer import AddEventPageTemplate
from anvil import *
import anvil.server as backend
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class AddEventPage(AddEventPageTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    categories = backend.call("query_event_categories")

    self.dd_category.items = [(x[0], x[1]) for x in categories]

  @handle("b_cancel", "click")
  def b_cancel_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('MainPage')

  @handle("b_add", "click")
  def b_add_click(self, **event_args):
    """This method is called when the button is clicked"""
    title = self.t_title.text
    description = self.t_description.text
    location = self.t_location.text
    date = self.dp_date.date
    category_id = self.dd_category.selected_value
  
    backend.call(
      "add_event",
      title,
      description,
      location,
      date,
      category_id
    )
  
    alert("Event successfuly added!")
  
    open_form("MainPage")
