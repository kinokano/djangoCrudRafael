async function GetUserNameLogado(){
    // const response = await apiRequest("/api/GetDadosUsuarioLogado/")
    const response = await fetch("/api/GetDadosUsuarioLogado")
    const div = document.getElementById("username")
    const dados = await response.json()
    div.innerHTML = dados.username
}
GetUserNameLogado()