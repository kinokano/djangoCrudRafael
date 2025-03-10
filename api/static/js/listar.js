async function deletarAluno(id) {
    try {
        const response = await apiRequest(`/api/user/${id}`,"DELETE",null,{"X-CSRFToken": "{{ csrf_token }}"})
            var alunoRow = document.getElementById(`aluno-${id}`);
            if (alunoRow) {
                alunoRow.remove();
            }
    } catch (error) {
        console.error('Erro:', error);
        alert("Erro ao tentar excluir o aluno.");
    }
}
