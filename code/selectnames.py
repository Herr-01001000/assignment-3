# -*- coding: utf-8 -*-
"""Define the selectnames functions for five subscales."""

# Define selectnames functions.
def selectnamesA(data):
    """Return a list of data's column names which are started with "antisocial_".
    """
    col = []
    for name in list(data):
        if name.startswith('antisocial_'):
            col.append(name)
        else:
            col = col
    
    return col

def selectnamesB(data):
    """Return a list of data's column names which are started with "anxiety_".
    """
    col = []
    for name in list(data):
        if name.startswith('anxiety_'):
            col.append(name)
        else:
            col = col
    
    return col

def selectnamesC(data):
    """Return a list of data's column names which are started with "headstrong_".
    """
    col = []
    for name in list(data):
        if name.startswith('headstrong_'):
            col.append(name)
        else:
            col = col
    
    return col

def selectnamesD(data):
    """Return a list of data's column names which are started with "hyperactive_".
    """
    col = []
    for name in list(data):
        if name.startswith('hyperactive_'):
            col.append(name)
        else:
            col = col
    
    return col

def selectnamesE(data):
    """Return a list of data's column names which are started with "peer_".
    """
    col = []
    for name in list(data):
        if name.startswith('peer_'):
            col.append(name)
        else:
            col = col
    
    return col