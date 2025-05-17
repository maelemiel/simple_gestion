from flask import Blueprint, request, redirect, url_for
from models import add_tache, update_statut

tache_bp = Blueprint('tache', __name__)

@tache_bp.route('/ajouter_tache', methods=['POST'])
def ajouter_tache():
    projet_id = request.form['projet_id']
    description = request.form['description']
    statut = request.form['statut']
    date_limite = request.form['date_limite']
    add_tache(projet_id, description, statut, date_limite)
    return redirect(url_for('index'))

@tache_bp.route('/modifier_statut/<int:id>/<statut>')
def modifier_statut(id, statut):
    update_statut(id, statut)
    return redirect(url_for('index'))