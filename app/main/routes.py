from flask import render_template
from app.main import main_blueprint

@main_blueprint.route('/')
def home():
    return render_template('index.html')

@main_blueprint.route('/projects')
def projects():
    return render_template('projects.html')

@main_blueprint.route('/experience')
def experience():
    return render_template('experience.html')
