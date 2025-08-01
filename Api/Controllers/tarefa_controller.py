from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from Services.tarefa_service import TarefaService
from datetime import datetime

tarefa_bp = Blueprint('tarefas', __name__)

def tarefa_to_dict(tarefa):
    return {
        "id": tarefa.id,
        "nome": tarefa.nome,
        "custo": tarefa.custo,
        "data_limite": tarefa.data_limite.strftime("%Y-%m-%d"),
        "ordem": tarefa.ordem
    }

@tarefa_bp.route('/', methods=['GET'])
@cross_origin()
def listar():
    tarefas = TarefaService.listar()
    return jsonify([tarefa_to_dict(t) for t in tarefas])

@tarefa_bp.route('/', methods=['POST', 'OPTIONS'])
@cross_origin()
def criar():
    if request.method == 'OPTIONS':
        return '', 200

    data = request.json
    try:
        nome = data['nome']
        custo = float(data['custo'])
        data_limite = datetime.strptime(data['data_limite'], "%Y-%m-%d").date()
    except Exception:
        return jsonify({"erro": "Dados inválidos"}), 400

    try:
        tarefa = TarefaService.criar(nome, custo, data_limite)
        return jsonify(tarefa_to_dict(tarefa)), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@tarefa_bp.route('/<int:id>', methods=['PUT', 'OPTIONS'])
@cross_origin()
def editar(id):
    if request.method == 'OPTIONS':
        return '', 200

    data = request.json
    try:
        nome = data['nome']
        custo = float(data['custo'])
        data_limite = datetime.strptime(data['data_limite'], "%Y-%m-%d").date()
    except Exception:
        return jsonify({"erro": "Dados inválidos"}), 400

    try:
        tarefa = TarefaService.editar(id, nome, custo, data_limite)
        return jsonify(tarefa_to_dict(tarefa))
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@tarefa_bp.route('/<int:id>', methods=['DELETE', 'OPTIONS'])
@cross_origin()
def excluir(id):
    if request.method == 'OPTIONS':
        return '', 200

    try:
        TarefaService.excluir(id)
        return jsonify({"mensagem": "Tarefa excluída"}), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@tarefa_bp.route('/<int:id>/subir', methods=['POST', 'OPTIONS'])
@cross_origin()
def subir(id):
    TarefaService.subir_ordem(id)
    return jsonify({"mensagem": "Ordem alterada"}), 200

@tarefa_bp.route('/<int:id>', methods=['GET'])
@cross_origin()
def buscar(id):
    tarefa = TarefaService.buscar_por_id(id)
    if tarefa:
        return jsonify(tarefa_to_dict(tarefa))
    else:
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    
@tarefa_bp.route('/<int:id>/descer', methods=['POST', 'OPTIONS'])
@cross_origin()
def descer(id):
    if request.method == 'OPTIONS':
        return '', 200

    TarefaService.descer_ordem(id)
    return jsonify({"mensagem": "Ordem alterada"}), 200
