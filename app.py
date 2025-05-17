from flask import Flask, render_template, request, redirect, url_for, session
from config import Config
from database import init_app
from models import get_taches, get_projets
from routes.projet_routes import projet_bp
from routes.tache_routes import tache_bp

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'votre_cle_secrete'  # Pour la gestion de session

# Enregistrement des blueprints
app.register_blueprint(projet_bp)
app.register_blueprint(tache_bp)

# Initialisation de la base
init_app(app)

@app.route('/set_style/<style>')
def set_style(style):
    session['style'] = style
    return redirect(request.referrer or url_for('index'))

@app.route('/')
def index():
    style = session.get('style', 'nostyle')
    return render_template('index.html', taches=get_taches(), projets=get_projets(), style=style)

if __name__ == '__main__':
    app.run()