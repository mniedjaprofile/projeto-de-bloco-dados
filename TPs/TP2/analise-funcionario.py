import pandas as pd
import os

# Função para ler o arquivo CSV - 1
def ler_base_csv():
    """
    Função para ler um arquivo CSV localizado no mesmo diretório do script.
    
    O arquivo deve estar no mesmo diretório em que o script está sendo executado,
    e seu nome deve ser 'funcionarios.csv'. Caso o arquivo não exista, será retornado
    um erro. Caso o arquivo esteja vazio ou com formato incorreto, também será exibida
    uma mensagem de erro detalhada.
    
    Returns:
        pd.DataFrame: DataFrame contendo os dados do arquivo CSV ou None caso ocorra um erro.
    """
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio_atual, 'funcionarios.csv')

    # Verifica se o arquivo existe no diretório atual
    if os.path.exists(caminho_arquivo):
        try:
            # Carregar o arquivo CSV com encoding explicitamente definido para evitar problemas de leitura em diferentes sistemas
            # Realizada consulta no gpt para cobrir este item
            df = pd.read_csv(caminho_arquivo, encoding='utf-8')
            print(f"Arquivo '{caminho_arquivo}' carregado com sucesso.")
            return df
        except pd.errors.EmptyDataError:
            print("Erro: O arquivo está vazio.")
        except pd.errors.ParserError:
            print("Erro: O arquivo contém dados inválidos ou com formato incorreto.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
    else:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    return None

# Função para filtrar funcionários do departamento de TI - 2
def filtrar_ti(df):
    """Filtra e exibe funcionários do departamento de TI"""
    if df is not None:
        funcionarios_ti = df[df['Departamento'] == 'TI']
        print("Funcionários do departamento de TI:")
        print(funcionarios_ti)
    else:
        print("Não foi possível carregar os dados.")

# Função para calcular a média salarial por departamento - 3
def media_salarial(df):
    """Calcula e exibe a média salarial por departamento"""
    if df is not None:
        media = df.groupby("Departamento")['Salário'].mean()
        print("Média salarial por departamento:")
        print(media)
    else:
        print("Não foi possível carregar os dados.")

# Função para filtrar funcionários com mais de 5 anos de empresa - 4
def filtrar_tempo_empresa(df):
    """Filtra e exibe funcionários com mais de 5 anos de empresa"""
    if df is not None:
        funcionarios_5_anos = df[df['Tempo_Empresa'] > 5]
        print("Funcionários com mais de 5 anos de empresa:")
        print(funcionarios_5_anos)
    else:
        print("Não foi possível carregar os dados.")

# Função para filtrar funcionários em home office - 5
def filtrar_home_office(df):
    """Filtra e exibe funcionários que trabalham em home office"""
    if df is not None:
        funcionarios_home_office = df[df['Home_Office'] == 1]
        print("Funcionários em Home Office:")
        print(funcionarios_home_office)
    else:
        print("Não foi possível carregar os dados.")

# Função para encontrar o funcionário mais bem pago - 6
def funcionario_mais_bem_pago(df):
    """Encontra o funcionário com o maior salário"""
    if df is not None:
        funcionario = df.loc[df['Salário'].idxmax()]
        print(f"Funcionário mais bem pago: {funcionario['Nome']}")
        print(f"Salário: {funcionario['Salário']}")
    else:
        print("Não foi possível carregar os dados.")

# Função para calcular o salário total da empresa - 7
def salario_total_empresa(df):
    """Calcula a soma total dos salários dos funcionários"""
    if df is not None:
        total_salarios = df['Salário'].sum()
        print(f"Salário total da empresa: R${total_salarios:,.2f}")
    else:
        print("Não foi possível carregar os dados.")

# Função para distribuição por idade
def distribuicao_por_idade(df):
    """Exibe a distribuição dos funcionários por faixas etárias"""
    if df is not None:
        faixa_30 = df[df['Idade'] < 30]
        faixa_30_40 = df[(df['Idade'] >= 30) & (df['Idade'] <= 40)]
        faixa_40 = df[df['Idade'] > 40]

        print(f"Funcionários com menos de 30 anos: {len(faixa_30)}")
        print(f"Funcionários entre 30 e 40 anos: {len(faixa_30_40)}")
        print(f"Funcionários com mais de 40 anos: {len(faixa_40)}")
    else:
        print("Não foi possível carregar os dados.")

# Função para adicionar a coluna Novo_Salário
def aumento_salarial(df):
    """Adiciona uma coluna 'Novo_Salário' com aumento de 10%"""
    if df is not None:
        df['Novo_Salário'] = df['Salário'] * 1.10
        print("Coluna 'Novo_Salário' adicionada com aumento de 10%.")
        print(df[['Nome', 'Salário', 'Novo_Salário']].head())  # Exibe as primeiras linhas para verificação
    else:
        print("Não foi possível carregar os dados.")

# Função para calcular correlação entre tempo de empresa e salário
def correlacao_temporal_salario(df):
    """Calcula a correlação entre o tempo de empresa e o salário"""
    if df is not None:
        correlacao = df['Tempo_Empresa'].corr(df['Salário'])
        print(f"Correlação entre tempo de empresa e salário: {correlacao:.2f}")
    else:
        print("Não foi possível carregar os dados.")

# Função para exibir o menu de opções
def exibir_menu():
    """
    Exibe um menu interativo para o usuário escolher a ação que deseja realizar.
    
    Returns:
        int: Opção escolhida pelo usuário.
    """
    print("\nEscolha uma opção:")
    print("1 - Identificar e carregar arquivo 'funcionarios.csv'")
    print("2 - Filtrar funcionários do departamento de TI")
    print("3 - Ver média salarial por departamento")
    print("4 - Filtrar funcionários com mais de 5 anos de empresa")
    print("5 - Filtrar funcionários em Home Office")
    print("6 - Ver o funcionário mais bem pago")
    print("7 - Calcular o salário total da empresa")
    print("8 - Distribuição por idade")
    print("9 - Adicionar aumento salarial de 10%")
    print("10 - Calcular correlação entre tempo de empresa e salário")
    print("11 - Sair")

    try:
        opcao = int(input("Digite o número da opção desejada: "))
        return opcao
    except ValueError:
        print("Por favor, digite um número válido.")
        return None

# Função principal
def main():
    """
    Função principal que carrega os dados, exibe o menu e executa as ações escolhidas pelo usuário.
    """
    df = ler_base_csv()

    if df is not None:
        while True:
            opcao = exibir_menu()

            if opcao == 1:
                # A primeira opção agora é verificar e carregar o arquivo
                df = ler_base_csv()  # Recarrega os dados
            elif opcao == 2:
                filtrar_ti(df)
            elif opcao == 3:
                media_salarial(df)
            elif opcao == 4:
                filtrar_tempo_empresa(df)
            elif opcao == 5:
                filtrar_home_office(df)
            elif opcao == 6:
                funcionario_mais_bem_pago(df)
            elif opcao == 7:
                salario_total_empresa(df)
            elif opcao == 8:
                distribuicao_por_idade(df)
            elif opcao == 9:
                aumento_salarial(df)
            elif opcao == 10:
                correlacao_temporal_salario(df)
            elif opcao == 11:
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Não foi possível iniciar o programa devido a erro na leitura dos dados.")

# Executar o script
if __name__ == "__main__":
    main()
