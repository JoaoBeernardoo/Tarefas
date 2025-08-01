from Models.tarefa_model import Tarefa
from Infra.db import db

class TarefaRepository:

    @staticmethod
    def listar_tarefas():
        return Tarefa.query.order_by(Tarefa.ordem).all()

    @staticmethod
    def buscar_por_id(tarefa_id):
        return Tarefa.query.get(tarefa_id)

    @staticmethod
    def buscar_por_nome(nome):
        return Tarefa.query.filter_by(nome=nome).first()

    @staticmethod
    def buscar_por_ordem(ordem):
        return Tarefa.query.filter_by(ordem=ordem).first()

    @staticmethod
    def adicionar(tarefa: Tarefa):
        db.session.add(tarefa)
        db.session.commit()

    @staticmethod
    def remover(tarefa: Tarefa):
        db.session.delete(tarefa)
        db.session.commit()

    @staticmethod
    def salvar():
        db.session.commit()
