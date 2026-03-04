from ._anvil_designer import EventsList_ExtendedTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class EventsList_Extended(EventsList_ExtendedTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    query = """
      SELECT 
        events.title,
        events.date,
        events.location,
        users.name,
        categories.name
      FROM events
      LEFT JOIN users ON users.user_id == events.created_by
      LEFT JOIN categories ON categories.category_id == events.category_id
      ORDER BY events.date
    """
    returnValue = anvil.server.call("query_database", query)
    data = []
    for v in returnValue:
      data.append(
        {
          "title": v[0], 
          "date": v[1], 
          "location": v[2], 
          "created_by": v[3],
          "category": v[4]
        })

    self.repeating_panel_events.items = data

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('MainPage')
