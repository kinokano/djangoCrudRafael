async function enviarFormularioAluno(event) {
    event.preventDefault(); // Impede o recarregamento da página

    const nome = document.getElementById("nome").value;
    const senha = document.getElementById("senha").value;

    const path = window.location.pathname;
    const parts = path.split('/');
    const id = parts[parts.length - 1];
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let response

    if (id) {
        response = await apiRequest(`/api/user/${id}`, "PUT", { username: nome, password: senha }, { "X-CSRFToken": csrfToken })
    } else {
        response = await apiRequest("/api/user", "POST", { username: nome, password: senha }, { "X-CSRFToken": csrfToken })
    }

    if (response) {
        window.location.href = "/home"; // Redireciona após cadastro
    } else {
        throw new Error("Erro ao cadastrar aluno");
    }
}

document.getElementById("alunoForm").addEventListener("submit", enviarFormularioAluno);
