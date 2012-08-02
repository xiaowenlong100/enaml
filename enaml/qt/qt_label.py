#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from .qt.QtGui import QLabel
from .qt_constraints_widget import QtConstraintsWidget


class QtLabel(QtConstraintsWidget):
    """ A Qt4 implementation of an Enaml Label.

    """
    def create(self):
        """ Create the underlying widget.

        """
        self.widget = QLabel(self.parent_widget)

    def initialize(self, attrs):
        """ Initialize the widget's attributes.

        """
        super(QtLabel, self).initialize(attrs)
        self.set_text(attrs['text'])

    #--------------------------------------------------------------------------
    # Message Handlers
    #--------------------------------------------------------------------------
    def on_action_set_text(self, content):
        """ Handle the 'set_text' action from the Enaml widget.

        """
        # XXX trigger a relayout if the size hint has changed.
        self.set_text(content['text'])

    #--------------------------------------------------------------------------
    # Widget Update Methods
    #--------------------------------------------------------------------------
    def set_text(self, text):
        """ Set the text in the underlying widget.

        """
        self.widget.setText(text)

