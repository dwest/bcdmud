#!/usr/bin/python

import urwid
import sys
from MapView import MapView
from ChatView import ChatView
from InventoryView import InventoryView

class MainView(urwid.WidgetWrap):
    
    def __init__(self, views):

        # explode the views, should be passed as tuple
        (self.chatView, self.mapView, self.inventoryView) = views

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

