async function Login(event){
    event.preventDefault();
    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;

    const response = await apiRequest("/api/verificaLogin", "POST", {nome: nome, email: email}, {"X-CSRFToken": "{{ csrf_token }}"})

    console.log(response)
    if(response.status == 200){
        window.location.href = "/home";
    }else{
        document.getElementById("mensagem").innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
    }
}


document.getElementById("loginForm").addEventListener("submit",Login);