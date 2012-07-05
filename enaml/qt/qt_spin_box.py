#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
import re

from .qt.QtGui import QSpinBox, QValidator
from .qt_constraints_widget import QtConstraintsWidget

class EnamlQSpinBox(QSpinBox):
    """ A QSpinBox sublcass with hooks for user supplied validation.

    """
    #: The internal storage for the Enaml validator object. 
    _validator = None

    def validator(self):
        """ Returns the Enaml validator assigned to this spin box.

        """
        return self._validator
    
    def setValidator(self, validator):
        """ Set the validator for this spin box.

        """
        self._validator = validator
        self.interpretText()

    def textFromValue(self, value):
        """ Converts the given integer to a string for display using the 
        user supplied validator object. 

        If the conversion fails due to the converter raising a ValueError
        then simple unicode(...) conversion is used.

        """
        if self.validator():
            # XXX needs to be actually implemented
            text = unicode(value)
            return text

    def valueFromText(self, text):
        """ Converts the user typed string into an integer for the
        control using the user supplied validator.

        """
        # XXX needs to be actually implemented
        return int(text)

    def validate(self, text, pos):
        """ Validates whether or not the given text can be converted
        to an integer.

        """
        valid = re.match(self.validator(), text)
        if valid is not None:
            res = QValidator.Acceptable
        else:
            res = QValidator.Invalid
        return (res, text, pos)
    

class QtSpinBox(QtConstraintsWidget):
    """ A Qt4 implementation of a SpinBox

    """
    def create(self):
        """ Create the underlying widget

        """
        self.widget = EnamlQSpinBox(self.parent_widget)

    def initialize(self, init_attrs):
        """ Initialize the widget's attributes

        """
        super(QtSpinBox, self).initialize(init_attrs)
        self.set_validator(init_attrs.get('validator', '^[0-9]+$'))
        self.set_maximum(init_attrs.get('maximum', 100))
        self.set_minimum(init_attrs.get('minimum', 0))
        self.set_single_step(init_attrs.get('single_step', 1))
        self.set_tracking(init_attrs.get('tracking', True))
        self.set_value(init_attrs.get('value', 0))
        self.set_wrap(init_attrs.get('wrap', False))

    def bind(self):
        """ Bind the widget's events

        """
        super(QtSpinBox, self).bind()
        self.widget.valueChanged.connect(self.on_value_changed)

    #--------------------------------------------------------------------------
    # Event Handlers
    #--------------------------------------------------------------------------
    def on_value_changed(self):
        """ Event handler for value_changed

        """
        self.send({'action':'set_value','value':self.widget.value()})
        
    #--------------------------------------------------------------------------
    # Message Handlers
    #--------------------------------------------------------------------------
    def receive_set_maximum(self, ctxt):
        """ Message handler for set_maximum

        """
        return self.set_maximum(ctxt['maximum'])

    def receive_set_minimum(self, ctxt):
        """ Message handler for set_minimum

        """
        return self.set_minimum(ctxt['minimum'])

    def receive_set_single_step(self, ctxt):
        """ Message handler for set_single_step

        """
        return self.set_single_step(ctxt['single_step'])

    def receive_set_tracking(self, ctxt):
        """ Message handler for set_tracking

        """
        self.set_tracking(ctxt['tracking'])

    def receive_set_validator(self, ctxt):
        """ Message handler for set_validator

        """
        return self.set_validator(ctxt['validator'])

    def receive_set_value(self, ctxt):
        """ Message handler for set_value

        """
        return self.set_value(ctxt['value'])

    def receive_set_wrap(self, ctxt):
        """ Message handler for set_wrap

        """
        return self.set_wrap(ctxt['wrap'])

    #--------------------------------------------------------------------------
    # Widget Update Methods
    #--------------------------------------------------------------------------
    def set_maximum(self, maximum):
        """ Set the widget's maximum value

        """
        self.widget.setMaximum(maximum)
        return True

    def set_minimum(self, minimum):
        """ Set the widget's minimum value

        """
        self.widget.setMinimum(minimum)
        return True

    def set_single_step(self, step):
        """ Set the widget's single step value

        """
        self.widget.setSingleStep(step)
        return True

    def set_tracking(self, tracking):
        """ Set the keyboard tracking of the widget

        """
        self.widget.setKeyboardTracking(tracking)
        return True

    def set_validator(self, validator):
        """ Set the validator for the spin box

        """
        self.widget.setValidator(validator)
        return True

    def set_value(self, value):
        """ Set the spin box's value

        """
        self.widget.setValue(value)
        return True

    def set_wrap(self, wrap):
        """ Set whether or not to allow the spin box to wrap at its
        extreme values

        """
        self.widget.setWrapping(wrap)
        return True