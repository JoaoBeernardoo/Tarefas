from Repositories.tarefa_repository import TarefaRepository
from Models.tarefa_model import Tarefa

class TarefaService:

    @staticmethod
    def listar():
        return TarefaRepository.listar_tarefas()

    @staticmethod
    def criar(nome, custo, data_limite):
        if TarefaRepository.buscar_por_nome(nome):
            raise ValueError("Nome da tarefa já existe")

        todas = TarefaRepository.listar_tarefas()
        max_ordem = max([t.ordem for t in todas], default=0)
        nova_ordem = max_ordem + 1

        tarefa = Tarefa(nome=nome, custo=custo, data_limite=data_limite, ordem=nova_ordem)
        TarefaRepository.adicionar(tarefa)
        return tarefa

    @staticmethod
    def editar(tarefa_id, nome, custo, data_limite):
        tarefa = TarefaRepository.buscar_por_id(tarefa_id)
        if not tarefa:
            raise ValueError("Tarefa não encontrada")

        if tarefa.nome != nome and TarefaRepository.buscar_por_nome(nome):
            raise ValueError("Nome da tarefa já existe")

        tarefa.nome = nome
        tarefa.custo = custo
        tarefa.data_limite = data_limite
        TarefaRepository.salvar()
        return tarefa

    @staticmethod
    def excluir(tarefa_id):
        tarefa = TarefaRepository.buscar_por_id(tarefa_id)
        if not tarefa:
            raise ValueError("Tarefa não encontrada")
        TarefaRepository.remover(tarefa)

    @staticmethod
    def subir_ordem(tarefa_id):
        tarefa = TarefaRepository.buscar_por_id(tarefa_id)
        if not tarefa or tarefa.ordem == 1:
            return

        anterior = TarefaRepository.buscar_por_ordem(tarefa.ordem - 1)
        if anterior:
            
            anterior.ordem = 0
            TarefaRepository.salvar()

            
            tarefa.ordem = tarefa.ordem - 1
            TarefaRepository.salvar()

            
            anterior.ordem = tarefa.ordem + 1
            TarefaRepository.salvar()

    @staticmethod
    def descer_ordem(tarefa_id):
            tarefa = TarefaRepository.buscar_por_id(tarefa_id)
            if not tarefa:
                return

            tarefas = TarefaRepository.listar_tarefas()
            max_ordem = max([t.ordem for t in tarefas], default=0)
            if tarefa.ordem == max_ordem:
                return

            proxima = TarefaRepository.buscar_por_ordem(tarefa.ordem + 1)
            if proxima:
             
                proxima.ordem = 0
                TarefaRepository.salvar()

            
                tarefa.ordem += 1
                TarefaRepository.salvar()

            
                proxima.ordem = tarefa.ordem - 1
                TarefaRepository.salvar()
                
    @staticmethod
    def buscar_por_id(tarefa_id):
        return TarefaRepository.buscar_por_id(tarefa_id)
