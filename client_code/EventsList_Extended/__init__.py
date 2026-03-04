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
        users.name
      FROM events
      LEFT JOIN users ON users.user_id == events.created_by
      ORDER BY events.date
    """
    returnValue = anvil.server.call("query_database", query)
    data = []
    for v in returnValue:
      data.append({"title": v[0], "location": v[1], "date": v[2], "user": v[3]})

    self.events_panel.items = data
