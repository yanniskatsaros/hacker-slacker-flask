from flask import current_app as app
from flask import render_template

@app.route('/')
def home():
    """Landing page"""
    nav = [
        {'name': 'Home', 'url': 'https://example.com/1'},
        {'name': 'About', 'url': 'https://example.com/2'},
        {'name': 'Contact', 'url': 'https://example.com/3'}
    ]
    return render_template(
        'home.html.jinja',
        title='Jinja Demo Site',
        description='Flask & Jinja Tutorial',
        nav=nav
    )