from Infra.db import db

class Tarefa(db.Model):
    __tablename__ = 'tarefas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), unique=True, nullable=False)
    custo = db.Column(db.Float, nullable=False)
    data_limite = db.Column(db.Date, nullable=False)
    ordem = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return f"<Tarefa {self.nome}>"
