# Roteiro de Teste para Gestão de Tarefas 📝

Este roteiro tem como objetivo sugerir uma sequencia de testes que cubra todas as funcionalidades do programa de **Gestão de Tarefas** para garantirmos que as mesmas estejam funcionando corretamente. Cada seção apresenta o objetivo do teste, passos para executá-lo e o resultado esperado.

---

### 1. Testar Adição de Tarefa ➕

- **Objetivo**: Verificar se o programa permite adicionar uma nova tarefa.
- **Passos**:
  1. Escolha a opção `1` (Adicionar Tarefa).
  2. Digite o título da tarefa, por exemplo, `Revisar o relatório`.
- **Resultado Esperado**: O programa deve confirmar a adição da tarefa com uma mensagem como: `"Tarefa 'Revisar o relatório' adicionada com sucesso!"`.

---

### 2. Testar Listagem de Tarefas 📋

- **Objetivo**: Verificar se o programa exibe corretamente a lista de tarefas pendentes e concluídas.
- **Passos**:
  1. Adicione algumas tarefas usando a opção `1`.
  2. Escolha a opção `2` (Listar Tarefas).
- **Resultado Esperado**: O programa deve mostrar todas as tarefas, com cada uma numerada e com o status (`Pendente` ou `Concluída`).

---

### 3. Testar Marcação de Tarefa como Concluída ✅

- **Objetivo**: Verificar se o programa permite marcar uma tarefa como concluída.
- **Passos**:
  1. Liste as tarefas e anote o número de uma tarefa pendente.
  2. Escolha a opção `3` (Marcar Tarefa como Concluída).
  3. Digite o número da tarefa anotada.
- **Resultado Esperado**: O programa deve confirmar que a tarefa foi marcada como concluída. Ao listar novamente, o status da tarefa deve estar como `Concluída`.

---

### 4. Testar Remoção de Tarefa 🗑️

- **Objetivo**: Verificar se o programa permite remover uma tarefa da lista.
- **Passos**:
  1. Liste as tarefas e anote o número de uma tarefa.
  2. Escolha a opção `4` (Remover Tarefa).
  3. Digite o número da tarefa anotada.
- **Resultado Esperado**: O programa deve confirmar a remoção da tarefa. Ao listar novamente, a tarefa removida não deve mais aparecer.

---

### 5. Testar Saída do Programa 🚪

- **Objetivo**: Verificar se o programa encerra corretamente.
- **Passos**:
  1. Escolha a opção `5` (Sair).
- **Resultado Esperado**: O programa deve exibir uma mensagem de saída e encerrar sem erros.

---

Este roteiro de teste proporciona uma verificação completa de cada funcionalidade do programa de **Gestão de Tarefas**. Boa sorte  🚀
