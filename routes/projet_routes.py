from flask import Blueprint, request, redirect, url_for
from models import add_projet

projet_bp = Blueprint('projet', __name__)

@projet_bp.route('/ajouter_projet', methods=['POST'])
def ajouter_projet():
    nom = request.form['nom']
    add_projet(nom)
    return redirect(url_for('index'))