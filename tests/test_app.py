import sys
import os
 
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app
from dash import html, dcc

def test_header(): 
    headers= [c for c in app.layout.children if isinstance(c, html.H1)]
    assert len(headers) > 0

def test_graph():
    graphs= [i for i in app.layout.children if isinstance(i , dcc.Graph)]
    assert len(graphs) >0


def test_radio():
    radio = [i for i in app.layout.children if isinstance(i , dcc.RadioItems)]
    assert len(radio) >0
