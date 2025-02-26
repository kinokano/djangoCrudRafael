async function getUrlParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

// Função para carregar os dados do aluno
async function carregarAluno() {
    // Ao carregar a página, verificar se há um ID de aluno na URL
    const alunoId = await getUrlParameter('id');

    if (alunoId) {
        try {
            // Fazer uma requisição para pegar os dados do aluno
            const response = await fetch(`/api/alunos/${alunoId}`);
            const data = await response.json();

            // Preencher o formulário com os dados do aluno
            document.getElementById('nome').value = data.nome;
            document.getElementById('email').value = data.email;
        } catch (error) {
            console.error('Erro ao carregar os dados do aluno:', error);
        }
    }
}

// Função para enviar os dados do aluno (cadastro ou edição)
async function enviarFormularioAluno(event) {
    event.preventDefault(); // Impede o recarregamento da página

    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;

    // Verifique se o ID do aluno está presente na URL ou em algum outro lugar
    const alunoId = new URLSearchParams(window.location.search).get("id");

    try {
        if (alunoId) {
            // Se o ID estiver presente, significa que é uma edição, então usamos o método PUT
            const response = await fetch(`/api/alunos/${alunoId}/`, {
                method: "PUT", // Método PUT para editar
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": "{{ csrf_token }}" // CSRF necessário para requisições PUT no Django
                },
                body: JSON.stringify({ nome: nome, email: email }) // Enviando os dados atualizados em JSON
            });

            if (response.ok) {
                const data = await response.json();
                document.getElementById("mensagem").innerHTML = `<div class="alert alert-success">Aluno editado com sucesso!</div>`;
                window.location.href = "/home"; // Redireciona após edição
            } else {
                throw new Error("Erro ao editar aluno");
            }
        } else {
            // Se não houver ID, significa que é um cadastro, então usamos o método POST
            const response = await fetch("/api/alunos/", {
                method: "POST", // Método POST para cadastrar
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": "{{ csrf_token }}" // CSRF necessário para requisições POST no Django
                },
                body: JSON.stringify({ nome: nome, email: email }) // Enviando os dados em JSON
            });

            if (response.ok) {
                const data = await response.json();
                document.getElementById("mensagem").innerHTML = `<div class="alert alert-success">Aluno cadastrado com sucesso!</div>`;
                document.getElementById("alunoForm").reset();
                window.location.href = "/home"; // Redireciona após cadastro
            } else {
                throw new Error("Erro ao cadastrar aluno");
            }
        }
    } catch (error) {
        document.getElementById("mensagem").innerHTML = `<div class="alert alert-danger">${error.message}</div>`;
    }
}

// Ao carregar a página, chama a função de carregamento do aluno
carregarAluno();

// Adiciona o evento ao formulário
document.getElementById("alunoForm").addEventListener("submit", enviarFormularioAluno);
