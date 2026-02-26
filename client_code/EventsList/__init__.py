from ._anvil_designer import EventsListTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class EventsList(EventsListTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    query = """
      SELECT 
        events.title,
        events.date,
        events.location,
      FROM events
      LEFT JOIN users ON users.user_id == events.created_by
    """
    returnValue = anvil.server.call('query_database', query)
    data = []
    for v in returnValue:
      print(v)
      data.append({'title': v[1], 'location': v[3]})

    self.events_panel.items = data
