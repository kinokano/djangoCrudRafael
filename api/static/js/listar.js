async function deletarAluno(id) {
    try {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const response = await apiRequest(`/api/user/${id}`,"DELETE",null,{"X-CSRFToken": csrfToken})
            if(response.status == 200){
                var alunoRow = document.getElementById(`aluno-${id}`);
                if (alunoRow) {
                    alunoRow.remove();
                }
            }
    } catch (error) {
        console.error('Erro:', error);
        alert("Erro ao tentar excluir o aluno.");
    }
}
