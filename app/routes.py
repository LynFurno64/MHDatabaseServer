from crypt import methods
from flask import abort
from flask import Flask, jsonify
from flask import make_response
from flask import request
from flask import url_for  # New
from app import app, db
import json

from app.models import Phylum, Subgroup

a = open('app/json/branch.json')
branch = json.load(a)

b = open('app/json/phylums.json')
phylums = json.load(b)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # Loop along json
    for subBranch in branch['branch']:
        division = subBranch['division']
    return jsonify({'branch': branch})


@app.route('/phylums/<int:phylum_id>', methods=['GET'])
def get_phylum(phylum_id):
    phylum = [phylum for phylum in phylums['phylums'] if phylum['id'] == phylum_id]
    if len(phylum) == 0:
        abort(404)
    return phylum[0]


@app.route('/phylums', methods=['GET'])
def get_phylums():
    return jsonify({'phylums': phylums})


@app.route('/branch/<int:sub_id>', methods=['GET'])
def get_branch(sub_id):
    subBranch = [subBranch for subBranch in branch['branch']
                 if subBranch['id'] == sub_id]
    if len(subBranch) == 0:
        abort(404)
    return jsonify({'branch': subBranch[0]})


@app.route('/branch', methods=['GET'])
def get_tree():
    return jsonify({'branch': branch})
