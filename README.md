# 📊 Automação de Relatórios & Consolidação de Dados

Um utilitário em Python desenvolvido para processar bases de dados brutas de vendas (`.csv`), calcular métricas financeiras essenciais e gerar um relatório consolidado estruturado, totalmente compatível com o Microsoft Excel e Google Sheets, sem a necessidade de instalar bibliotecas externas.

## 🚀 Recursos Principais

* **Zero Dependências Externas**: Construído utilizando exclusivamente os módulos nativos do Python (`csv`, `collections`, `pathlib`), garantindo execução imediata em qualquer ambiente.
* **Processamento Dinâmico**: Lê arquivos de dados brutos e realiza agrupamentos automáticos por categoria de produto.
* **Métricas Consolidadas**:
  * Faturamento Total (R\$)
  * Volume Total de Pedidos
  * Total Vendido por Categoria (R\$)
  * Quantidade de Pedidos por Categoria
  * Ticket Médio por Categoria (R\$)
* **Compatibilidade Nativa com Excel**: O arquivo de saída `.csv` é gerado com cabeçalhos limpos e formatação decimal adequada para abertura direta em planilhas eletrônicas.

## 🔍 Como Funciona o Processamento?

1. **Leitura Eficiente**: O script `main.py` utiliza `csv.DictReader` para mapear os dados do arquivo `vendas_brutas.csv` linha a linha, garantindo baixo consumo de memória.
2. **Agregação em Memória**: Através de estruturas `collections.defaultdict`, o script acumula os totais e contagens por categoria à medida que lê os registros.
3. **Cálculo de Indicadores**: Realiza a consolidação geral e calcula o ticket médio ($Ticket\ Médio = \frac{\text{Total Faturado}}{\text{Quantidade de Pedidos}}$) para cada segmento.
4. **Exportação Formatada**: O relatório é estruturado em blocos bem definidos (Visão Geral e Resumo por Categoria) e salvo como `relatorio_consolidado.csv`.

## 🗂️ Estrutura dos Dados

### Arquivo de Entrada (`vendas_brutas.csv`)

| Coluna | Descrição | Exemplo |
| :--- | :--- | :--- |
| `ID_Venda` | Identificador único da transação | `1` |
| `Categoria` | Categoria do produto | `Eletrónicos` |
| `Valor` | Valor numérico da venda | `1250.50` |
| `Data` | Data do registro | `2026-10-10` |

### Arquivo de Saída (`relatorio_consolidado.csv`)

O relatório final é dividido em duas seções principais:

1. **Visão Geral**: Apresenta os indicadores globais do negócio (Faturamento Total e Total de Pedidos).
2. **Resumo por Categoria**: Tabela detalhada contendo Categoria, Total de Vendas, Quantidade de Pedidos e Ticket Médio.

## 💻 Como Executar

1. Certifique-se de que o arquivo `vendas_brutas.csv` esteja na mesma pasta do script.
2. Execute o script principal no terminal:

```bash
python main.py
```

O arquivo `relatorio_consolidado.csv` será gerado automaticamente no mesmo diretório.

## 🧪 Ambiente de Testes (`gen.py`)

Para testar o pipeline de geração de relatórios, o projeto inclui o utilitário `gen.py`.

Ele gera automaticamente uma base simulada contendo 100 transações distribuídas aleatoriamente entre diversas categorias e faixas de preço, criando o arquivo `vendas_brutas.csv` pronto para o processamento.

### Passo a Passo de Teste Completo:

1. **Gerar a base de dados sintética**:
   ```bash
   python gen.py
   ```

2. **Executar a automação do relatório**:
   ```bash
   python main.py
   ```

3. **Visualizar os resultados**:
   Abra o arquivo `relatorio_consolidado.csv` no Excel, Google Sheets ou em qualquer leitor de planilhas.

## 🛠️ Tecnologias Utilizadas

* **`csv`**: Leitura e escrita otimizada de dados delimitados.
* **`collections.defaultdict`**: Manipulação eficiente de agrupamentos e dicionários de acúmulo.
* **`pathlib`**: Gerenciamento de caminhos do sistema de arquivos de forma multiplataforma.
* **`random`**: Geração de dados estocásticos para o script de teste (`gen.py`).