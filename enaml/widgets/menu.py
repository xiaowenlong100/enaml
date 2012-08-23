#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from traits.api import Unicode, Property, cached_property

from .action import Action
from .action_group import ActionGroup
from .widget_component import WidgetComponent


class Menu(WidgetComponent):
    """ A widget used as a menu in a MenuBar.

    """
    #: The title to use for the menu.
    title = Unicode
    
    #: The items in the menu: Menu | Action | ActionGroup
    items = Property(depends_on='children[]')

    #--------------------------------------------------------------------------
    # Initialization
    #--------------------------------------------------------------------------
    def snapshot(self):
        """ Returns the snapshot dict for the Menu.

        """
        snap = super(Menu, self).snapshot()
        snap['item_ids'] = self._snap_item_ids()
        snap['title'] = self.title
        return snap

    def bind(self):
        """ Bind the change handlers for the menu.

        """
        super(Menu, self).bind()
        self.publish_attributes('title')

    #--------------------------------------------------------------------------
    # Private API
    #--------------------------------------------------------------------------
    @cached_property
    def _get_items(self):
        """ The getter for the 'items' property.

        Returns
        -------
        result : tuple
            The tuple of menu items for this menu.

        """
        isinst = isinstance
        allowed = (Action, ActionGroup, Menu)
        items = (child for child in self.children if isinst(child, allowed))
        return tuple(items)

    def _snap_item_ids(self):
        """ Returns the list of widget ids for the menu items.

        """
        return [item.widget_id for item in self.items]

