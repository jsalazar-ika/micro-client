import logging

from flask import Blueprint, request, jsonify

from entities.model import Client
from usecases import use_cases_client


client_bp = Blueprint("client_bp", __name__)
request_mapping = "/client"

@client_bp.route(request_mapping, methods=["POST"])
def insert():
    data = request.get_json()

    if not data:
        logging.warning("empty body insert")
        return dict(message="empty body"), 400
    
    try:
        if use_cases_client.insert(
            Client(
                **data
            )
        ):
            logging.info("Ok Insert")
            return dict(message="client created"), 201
    except Exception as error:
        logging.error(f"ERROR INSERT {error}")

    return dict(message="Internal server error"), 500

@client_bp.route(request_mapping, methods=['GET'])
def select():
    try:
        client_list = use_cases_client.select_all()
        if client_list:
            logging.info("GET ALL CLIENTS OK")
            return jsonify([{"name": client.name, "email": client.email, "id": client.id, "address": client.address} for client in client_list]), 200
    except Exception as error:
        logging.error(f"ERROR GET ALL CLIENTS {error}")
    
    return dict(message="Internal server error"), 500

@client_bp.route(request_mapping, methods=["DELETE"])
def delete():
    id = request.args['id']

    if not id:
        logging.warning("QUERY PARAMETER ID DOES NOT EXISTE DELETE")
        return dict(message="Must be exists query parameter id"), 400
    
    try:
        if use_cases_client.delete_by_id(id):
            logging.info("DELETE OK")
            return dict(message="Delete client succesfully"), 200
        else:
            logging.info(f"ID {id} DOES NOT EXIST CLIENT")
            return jsonify(dict(message=f"Client with id -> {id} does not exist")), 404

    except Exception as error:
        logging.error(f"ERROR DELETE CLIENT {error}")

    return dict(message="Internal server error"), 500


@client_bp.route(request_mapping, methods=["PUT"])
def update():
    data = request.get_json()

    if not data:
        logging.warning("empty body insert")
        return dict(message="empty body"), 400
    
    try:
        if use_cases_client.update(
            Client(
                **data
            )
        ):
            logging.info("Ok update")
            return dict(message="client updated"), 200
        else:
            logging.info(f"ID {data['id']} DOES NOT EXIST CLIENT")
            return jsonify(dict(message=f"Client with id -> {data['id']} does not exist")), 404
    except Exception as error:
        logging.error(f"ERROR UPDATE {error}")

    return dict(message="Internal server error"), 500
