from ._anvil_designer import EventInfoPageTemplate
from anvil import *
import anvil.server as backend
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class EventInfoPage(EventInfoPageTemplate):

  id = ""
  
  def __init__(self, input, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    title = input['title']
    description = backend.call("query_event_description", title)[0][0]
    date = input['date']
    location = input['location']
    created_by = input['created_by']
    category = input['category']
    self.id = input['id']
    
    self.l_title.text = f"{title}"
    self.ta_description.text = description
    self.l_category.text = category
    self.l_date.text = date
    self.l_location.text = location
    self.l_organizer.text = created_by

    self.load_comments()

  def load_comments(self):

    comments = backend.call("get_comments", self.id)
    self.rp_comments.items = comments
    

  @handle("btn_back", "click")
  def btn_back_click(self, **event_args):
    open_form('EventsPage')
    pass
    
  @handle("b_post", "click")
  def b_post_click(self, **event_args):
    """This method is called when the button is clicked"""
    text = self.tb_comment.text
    user = backend.call('get_logged_user')

    if not text:
      alert("Please write a comment")
      return

    if not user:
      alert("Please log in")
      return
  
    backend.call("add_comment", self.id, text)
  
    self.tb_comment.text = ""
  
    self.load_comments()

  def d_delete_click(self, **event_args):
    user = backend.call('get_logged_user')
    if user:
      if self.id:
        backend.call("delete_event", self.id)

        alert("Event was deleted!")

        open_form("MainPage")
    else:
      alert('Please log in')
