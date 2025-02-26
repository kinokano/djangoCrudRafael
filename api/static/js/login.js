document.getElementById("loginForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // Impede o recarregamento da página

    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;

    try {
        const response = await fetch("/api/verificaLogin", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": "{{ csrf_token }}" // CSRF necessário para requisições POST no Django
            },
            body: JSON.stringify({ nome: nome, email: email })
        });

        const data = await response.json();

        if (data.status === 200) {
            document.getElementById("mensagem").innerHTML = `<div class="alert alert-success">Login realizado com sucesso!</div>`;
            window.location.href = "/home"; // Redireciona para a página inicial
        } else {
            document.getElementById("mensagem").innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
        }
    } catch (error) {
        document.getElementById("mensagem").innerHTML = `<div class="alert alert-danger">Erro: ${error.message}</div>`;
    }
});
