# Faturamento Diário de uma Distribuidora

Este projeto tem como objetivo processar dados de faturamento diário de uma distribuidora. A partir dos dados fornecidos em um arquivo JSON, o programa realiza os seguintes cálculos:

- O menor valor de faturamento ocorrido em um dia do mês.
- O maior valor de faturamento ocorrido em um dia do mês.
- O número de dias em que o faturamento diário foi superior à média mensal, ignorando dias com faturamento igual a zero.

## Funcionalidades

1. Leitura de um arquivo JSON com os valores de faturamento diário.
2. Cálculo do menor e maior valor de faturamento.
3. Cálculo da média mensal de faturamento, ignorando dias sem faturamento.
4. Verificação e contagem de quantos dias o faturamento foi superior à média.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **JSON**: Formato de dados utilizado para armazenar o faturamento diário.

## Como Executar o Projeto

### Pré-requisitos

- Ter o **Python 3.x** instalado.
- Ter o arquivo `dados.json` contendo os dados de faturamento diário.

### Passos para Execução

1. Clone o repositório ou faça o download dos arquivos do projeto.
2. Certifique-se de que o arquivo `dados.json` esteja no diretório correto.
3. Abra o terminal e navegue até o diretório onde o script Python está salvo.
4. Execute o comando:

   ```bash
   python nome_do_arquivo.py
   ```

   Certifique-se de substituir `nome_do_arquivo.py` pelo nome correto do arquivo Python.

5. O script exibirá no terminal o menor e maior valor de faturamento, além do número de dias com faturamento superior à média mensal.

## Exemplo de Estrutura do Arquivo JSON

```json
[
    {
        "dia": 1,
        "valor": 22174.1664
    },
    {
        "dia": 2,
        "valor": 24537.6698
    },
    {
        "dia": 3,
        "valor": 26139.6134
    },
    ...
]
```

## Melhorias Futuras

- Implementar uma interface gráfica para facilitar o carregamento de arquivos e visualização dos resultados.
- Adicionar tratamento de exceções para melhorar a robustez do código.
- Permitir a escolha de arquivos XML como fonte de dados.

## Contato

Se você tiver dúvidas ou sugestões sobre o projeto, sinta-se à vontade para entrar em contato:

- **Nome**: Adam Richard Oliveira Mendes
- **E-mail**: adamrichardom@gmail.com
- **LinkedIn**: [Adam Richard](https://www.linkedin.com/in/adam-richardmendes/)
