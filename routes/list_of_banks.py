import json
import os
from flask import Blueprint, jsonify

list_of_banks_bp = Blueprint('list_of_banks', __name__)

@list_of_banks_bp.route('/list_of_banks', methods=['GET'])

def get_list_of_banks():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'list_of_banks.json')

    with open(file_path, 'r') as f:
        list_of_banks = json.load(f)

    return jsonify(list_of_banks["banks"])