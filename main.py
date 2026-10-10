import csv
from collections import defaultdict
from pathlib import Path

pasta = Path.cwd()
arquivo_dados = pasta / "vendas_brutas.csv"

if not arquivo_dados.exists():
    print("Erro: Ficheiro 'vendas_brutas.csv' não encontrado!")
    input("\nPressione ENTER para sair...")
    exit()

totais_cat = defaultdict(float)
qtd_cat = defaultdict(int)
faturamento_total = 0.0
total_pedidos = 0

with open(arquivo_dados, mode="r", encoding="utf-8") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        categoria = linha["Categoria"]
        valor = float(linha["Valor"])

        totais_cat[categoria] += valor
        qtd_cat[categoria] += 1
        faturamento_total += valor
        total_pedidos += 1

arquivo_saida = pasta / "relatorio_consolidado.csv"

with open(arquivo_saida, mode="w", encoding="utf-8", newline="") as f:
    escritor = csv.writer(f)

    escritor.writerow(["--- VISÃO GERAL ---"])
    escritor.writerow(["Métrica", "Valor"])
    escritor.writerow(["Faturamento Total", f"R$ {faturamento_total:.2f}"])
    escritor.writerow(["Total de Pedidos", total_pedidos])
    escritor.writerow([])

    escritor.writerow(["--- RESUMO POR CATEGORIA ---"])
    escritor.writerow(
        ["Categoria", "Total Vendas (R$)", "Qtd Pedidos", "Ticket Médio (R$)"]
    )

    for cat in totais_cat:
        tot = totais_cat[cat]
        qtd = qtd_cat[cat]
        media = tot / qtd
        escritor.writerow([cat, f"{tot:.2f}", qtd, f"{media:.2f}"])

print(f"Relatório gerado em: {arquivo_saida.name}")
input("\nPressione ENTER para fechar...")