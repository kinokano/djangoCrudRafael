async function deletarAluno(id) {
    try {
        const response = await fetch(`/api/alunos/${id}`, {
            method: 'DELETE',
            headers: {
                "X-CSRFToken": "{{ csrf_token }}"
            }
        });

        if (response.ok) {
            // Se a exclusão for bem-sucedida, remove a linha da tabela
            var alunoRow = document.getElementById(`aluno-${id}`);
            if (alunoRow) {
                alunoRow.remove();
            }
            alert("Aluno excluído com sucesso.");
        } else {
            alert("Erro ao excluir o aluno.");
        }
    } catch (error) {
        console.error('Erro:', error);
        alert("Erro ao tentar excluir o aluno.");
    }
}
