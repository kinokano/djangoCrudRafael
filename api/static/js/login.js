async function Login(event){
    event.preventDefault();
    const nome = document.getElementById("nome").value;
    const senha = document.getElementById("senha").value;

    const response = await apiRequest("/api/login", "POST", {nome: nome, senha: senha}, {"X-CSRFToken": "{{ csrf_token }}"})

    if(response.status == 200){
        window.location.href = "/home";
    }else{
        document.getElementById("mensagem").innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
    }
}


document.getElementById("loginForm").addEventListener("submit",Login);