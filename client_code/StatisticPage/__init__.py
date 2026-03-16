from ._anvil_designer import StatisticPageTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server as backend
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class StatisticPage(StatisticPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.show_month_plot()

  @handle("b_cancel", "click")
  def b_cancel_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("MainPage")

  @handle("b_category", "click")
  def b_category_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.show_category_plot()

  def show_category_plot(self):

    data = backend.call("events_per_category")

    categories = [x[0] for x in data]
    counts = [x[1] for x in data]
  
    self.p_stats.data = [{
      "labels": categories,
      "values": counts,
      "type": "pie"
    }]
  
    self.p_stats.layout = {
      "title": "Events by Category"
    }

  @handle("b_month", "click")
  def b_month_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.show_month_plot()
    

  def show_month_plot(self):
    data = backend.call("events_per_month")

    months = [x[0] for x in data]
    counts = [x[1] for x in data]

    self.p_stats.data = [{
      "x": months,
      "y": counts,
      "type": "bar"
    }]

    self.p_stats.layout = {
      "title": "Events per Month",
      "xaxis": {"title": "Month"},
      "yaxis": {"title": "Number of Events"}
    }