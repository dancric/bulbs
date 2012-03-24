# -*- coding: utf-8 -*-
#
# Copyright 2011 James Thornton (http://jamesthornton.com)
# BSD License (see LICENSE for details)
#
"""
Bulbs supports plugabble type systems.

"""
# Python 3
import six
import sys
if sys.version > '3':
    long = int
    unicode = str

from .utils import to_timestamp, to_datetime


class TypeSystem(object):
    """Abstract base class for plugabble database type systems."""

    #: The backend client's content type.
    content_type = None

    #: Converter object used to convert Python values to database values.
    database = None

    #: Converter object used to covert database values to Python values.
    python = None


class Converter(object):
    """Abstract base class of conversion methods called by DataType classes."""

    def to_string(self,value):
        raise NotImplementedError

    def to_integer(self,value):
        raise NotImplementedError
    
    def to_long(self,value):
        raise NotImplementedError

    def to_float(self,value):
        raise NotImplementedError

    def to_list(self,value):
        raise NotImplementedError

    def to_dictionary(self,value):
        raise NotImplementedError

    def to_null(self,value):
        raise NotImplementedError


#
# The JSON Type System
#

class Database(Converter):
    """Converts Python values to database values."""

    # The JSON type system is just a simple pass through.

    def to_string(self, value):
        """
        Converts a Python byte string to a unicode string.
        
        :param value: Property value. 
        :type value: str

        :rtype unicode or None

        :raises: ValueError

        """
        # Using unicode instead of str
        if value is not None:
            return unicode(value)

    def to_integer(self, value):
        """
        Converts a JSON number to a Python integer.

        :param value: Property value. 
        :type value: int

        :rtype int or None

        :raises: ValueError

        """
        return value
    
    def to_long(self, value):
        return value

    def to_float(self, value):
        return value

    def to_list(self, value):
        return value

    def to_dictionary(self, value):
        return value

    def to_datetime(self, value):
        if value is not None:
            return to_timestamp(value)

    def to_null(self, value):
        return value


class Python(Converter):
    """Converts database values to Python values."""

    # TODO: Why are we checking if value is not None?
    # This is supposed to be handled elsewhere.
    # Conversion exceptions are now handled in Property.convert_to_python() 
    
    def to_string(self, value):
        """
        Converts a JSON string to a Python unicode string.
        
        :param value: Property value. 
        :type value: str

        :rtype unicode or None

        :raises: ValueError

        """
        if value is not None:
            return unicode(value)

    def to_integer(self, value):
        """
        Converts a JSON number to a Python integer.

        :param value: Property value. 
        :type value: int

        :rtype int or None

        :raises: ValueError

        """
        if value is not None:
            return int(value)

    def to_long(self, value):
        """
        Converts a JSON number to a Python long.

        :param value: Property value. 
        :type value: long

        :rtype long or None

        :raises: ValueError

        """
        if value is not None:
            return long(value)

    def to_float(self, value):
        """
        Converts a JSON number to a Python float.

        :param value: Property value. 
        :type value: float

        :rtype float or None

        :raises: ValueError

        """
        if value is not None:
            return float(value)              

    def to_list(self, value):
        """
        Converts a JSON list to a Python list.

        :param value: Property value. 
        :type value: list

        :rtype list or None

        :raises: ValueError

        """
        if value is not None:
            return list(value)

    def to_dictionary(self, value):
        """
        Converts a JSON map to a Python dictionary.         

        :param value: Property value. 
        :type value: dict

        :rtype dict or None

        :raises: ValueError

        """
        if value is not None:
            return dict(value)

    def to_datetime(self, value):
        """
        Converts a JSON integer timestamp to a Python datetime object.

        :param value: Property value. 
        :type value: int

        :rtype datetime or None

        :raises: ValueError

        """
        if value is not None:
            return to_datetime(value)

    def to_null(self, value):
        """
        Converts a JSON null to a Python None.

        :param value: Property value. 
        :type value: None

        :rtype None

        :raises: ValueError

        """
        if value is not None:
            raise ValueError

        return None
    

class JSONTypeSystem(TypeSystem):
    """
    Converts database properties to and from their JSON representations.

    :cvar content_type: The backend client's content type.
    :cvar database: Converter object used to convert Python values to database values.
    :cvar python: Converter object used to covert database values to Python values.

    """
    content_type = "application/json"

    database = Database()
    python = Python()
    











