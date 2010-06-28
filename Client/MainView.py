#!/usr/bin/python

"""
Another attempt at a Client UI.  This one is a little easier to
understand since I am using the WidgetWrap class. 

MainView basically throws all the other views together. The views are 
piled and columned.  The Map view and Chat view are stacked together 
creating a single widget.  That widget is then 'columned' with 
the Inventory view.  A screen reference is passed between all views.
That is pretty much all MainView handles. 

Check http://excess.org/urwid/reference.html for info on urwid.

"""


import urwid
import sys
from MapView import MapView
from ChatView import ChatView
from InventoryView import InventoryView

class MainView(urwid.WidgetWrap):
    
    def __init__(self, screen, proxy):
        self.screen = screen
        (cols, rows) = screen.get_cols_rows()
        self.mapChatView = urwid.Text("Columns: "+str(cols)+" Rows: "+str(rows))

        # Load views
        self.chatView = ChatView(screen)
        self.mapView = MapView(screen, proxy)
        self.inventoryView = InventoryView(screen)

        # Draw pretty box around views
        mapBox = urwid.LineBox(self.mapView)
        chatBox = urwid.LineBox(self.chatView)
        inventoryBox = urwid.LineBox(self.inventoryView)

        #
        # Pack views together
        # 
        # Map and Chat views will be stacked (piled)
        # The mapChatPile will be a column along with 
        # the Inventory view
        #
        # The Map view will take up 2/3 of Pile and Column
        #
        mapChatPile = urwid.Pile([('weight', 2, mapBox),
                                  ('weight', 1, chatBox)])

        self.allColumn = urwid.Columns([('weight',2,mapChatPile),
                                        ('weight',1,inventoryBox)])
        urwid.WidgetWrap.__init__(self, self.allColumn)

