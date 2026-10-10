import csv
from pathlib import Path
import random

categorias = ["Eletrónicos", "Vestuário", "Alimentos", "Livros", "Móveis"]
arquivo_saida = Path.cwd() / "vendas_brutas.csv"

with open(arquivo_saida, mode="w", encoding="utf-8", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(["ID_Venda", "Categoria", "Valor", "Data"])

    for i in range(1, 101):
        cat = random.choice(categorias)
        val = round(random.uniform(20.0, 1500.0), 2)
        escritor.writerow([i, cat, val, "2026-10-10"])

print(f"Ficheiro de teste '{arquivo_saida.name}' criado com sucesso!")