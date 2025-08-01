document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("modal-tarefa");
    const form = document.getElementById("form-tarefa");
    const btnIncluir = document.getElementById("btnAdicionar");
    const closeModal = document.getElementById("close-modal");
    const tarefasContainer = document.getElementById("tarefas-container");
    const modalTitle = document.getElementById("modal-title");

    const loader = document.getElementById("loader");
    const messageBox = document.getElementById("message-box");
    const messageText = document.getElementById("message-text");
    const closeMessageBtn = document.getElementById("close-message");

    const inputId = document.getElementById("tarefa-id");
    const inputNome = document.getElementById("nome");
    const inputCusto = document.getElementById("custo");
    const inputData = document.getElementById("data");

    const modalConfirm = document.getElementById("modal-confirm");
    const btnConfirmYes = document.getElementById("btn-confirm-yes");
    const btnConfirmNo = document.getElementById("btn-confirm-no");
    let tarefaIdParaExcluir = null;

    const API_URL = "http://localhost:5000/tarefas/";

    function showLoader() {
        loader.style.display = "block";
    }

    function hideLoader() {
        loader.style.display = "none";
    }

    function showMessage(text, tipo = "info") {
        messageText.innerText = text;
        if (tipo === "erro") {
            messageBox.style.background = "#e74c3c";
        } else if (tipo === "sucesso") {
            messageBox.style.background = "#27ae60";
        } else {
            messageBox.style.background = "#333";
        }
        messageBox.style.display = "block";
        setTimeout(() => {
            messageBox.style.display = "none";
        }, 4000);
    }

    closeMessageBtn.addEventListener("click", () => {
        messageBox.style.display = "none";
    });

    async function fetchAndRenderTarefas() {
        showLoader();
        try {
            const response = await fetch(API_URL);
            if (!response.ok) {
                throw new Error("Erro ao buscar as tarefas.");
            }
            const tarefas = await response.json();
            renderizarTarefas(tarefas);
        } catch (error) {
            console.error("Erro:", error);
            tarefasContainer.innerHTML = `<tr><td colspan="4">Erro ao carregar as tarefas. Tente novamente.</td></tr>`;
            showMessage("Erro ao carregar as tarefas. Tente novamente.", "erro");
        } finally {
            hideLoader();
        }
    }

    function renderizarTarefas(tarefas) {
        tarefasContainer.innerHTML = "";
        tarefas.forEach((tarefa, index) => {
            const tr = document.createElement("tr");
            tr.className = tarefa.custo >= 1000 ? "alta" : "";
            const isPrimeira = index === 0;
            const isUltima = index === tarefas.length - 1;
            tr.innerHTML = `
                <td>${tarefa.nome}</td>
                <td>R$ ${parseFloat(tarefa.custo).toFixed(2)}</td>
                <td>${tarefa.data_limite}</td>
                <td class="tarefa-botoes">
                    <button class="btn btn-small btn-warning" onclick="editarTarefa(${tarefa.id})">✏️</button>
                    <button class="btn btn-small btn-danger" onclick="confirmarExclusao(${tarefa.id})">🗑️</button>
                    ${!isPrimeira ? `<button class="btn btn-small" onclick="moverTarefa(${tarefa.id}, 'subir')">🔼</button>` : ""}
                    ${!isUltima ? `<button class="btn btn-small" onclick="moverTarefa(${tarefa.id}, 'descer')">🔽</button>` : ""}
                </td>
            `;
            tarefasContainer.appendChild(tr);
        });
    }

    async function abrirModal(tarefaId = null) {
        modal.style.display = "block";
        if (tarefaId) {
            modalTitle.innerText = "Editar Tarefa";
            try {
                showLoader();
                const response = await fetch(`${API_URL}${tarefaId}`);
                if (!response.ok) {
                    throw new Error("Tarefa não encontrada.");
                }
                const tarefa = await response.json();
                inputNome.value = tarefa.nome;
                inputCusto.value = tarefa.custo;
                inputData.value = tarefa.data_limite;
                inputId.value = tarefa.id;
            } catch (error) {
                console.error("Erro ao buscar tarefa para edição:", error);
                showMessage(error.message, "erro");
                fecharModal();
            } finally {
                hideLoader();
            }
        } else {
            modalTitle.innerText = "Nova Tarefa";
            form.reset();
            inputId.value = "";
        }
    }

    function fecharModal() {
        modal.style.display = "none";
    }

    form.addEventListener("submit", async function (e) {
        e.preventDefault();
        const id = inputId.value;
        const dados = {
            nome: inputNome.value.trim(),
            custo: parseFloat(inputCusto.value),
            data_limite: inputData.value
        };
        try {
            showLoader();
            let response;
            if (id) {
                response = await fetch(`${API_URL}${id}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(dados)
                });
            } else {
                response = await fetch(API_URL, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(dados)
                });
            }
            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.erro || 'Erro ao salvar a tarefa.');
            }
            fecharModal();
            showMessage(id ? "Tarefa alterada com sucesso!" : "Tarefa criada com sucesso!", "sucesso");
            await fetchAndRenderTarefas();
        } catch (error) {
            console.error("Erro ao salvar a tarefa:", error);
            showMessage(error.message, "erro");
        } finally {
            hideLoader();
        }
    });

    window.editarTarefa = function (id) {
        abrirModal(id);
    };

    window.confirmarExclusao = function (id) {
        tarefaIdParaExcluir = id;
        modalConfirm.style.display = "flex";
    };

    btnConfirmYes.addEventListener("click", async () => {
        modalConfirm.style.display = "none";
        if (tarefaIdParaExcluir !== null) {
            try {
                showLoader();
                const response = await fetch(`${API_URL}${tarefaIdParaExcluir}`, {
                    method: 'DELETE'
                });
                if (!response.ok) {
                    throw new Error("Erro ao excluir a tarefa.");
                }
                showMessage("Tarefa excluída com sucesso!", "sucesso");
                await fetchAndRenderTarefas();
            } catch (error) {
                console.error("Erro ao excluir:", error);
                showMessage(error.message, "erro");
            } finally {
                hideLoader();
                tarefaIdParaExcluir = null;
            }
        }
    });

    btnConfirmNo.addEventListener("click", () => {
        tarefaIdParaExcluir = null;
        modalConfirm.style.display = "none";
    });

    window.moverTarefa = async function (id, direcao) {
        try {
            showLoader();
            const endpoint = direcao === 'subir' ? `${API_URL}${id}/subir` : `${API_URL}${id}/descer`;
            const response = await fetch(endpoint, { method: 'POST' });
            if (!response.ok) {
                throw new Error("Erro ao mover a tarefa.");
            }
            showMessage("Ordem da tarefa atualizada!", "sucesso");
            await fetchAndRenderTarefas();
        } catch (error) {
            console.error("Erro ao mover tarefa:", error);
            showMessage(error.message, "erro");
        } finally {
            hideLoader();
        }
    };

    btnIncluir.addEventListener("click", () => abrirModal());
    closeModal.addEventListener("click", fecharModal);
    window.onclick = function (event) {
        if (event.target === modal) {
            fecharModal();
        }
    };

    fetchAndRenderTarefas();
});
