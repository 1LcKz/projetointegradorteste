def cadastroProduto(codigo, nome, descricao, ca, cf, cv, iv, ml):
    def print_table(data):
        print("| {:<1}  {:<23} | {:<1}  {:<14} |".format("Nome:", nome, "Código:", codigo))
        print("| {:<30} | {:<10} | {:<10} |".format("Descrição", "Valor", "%"))
        print("-" * 55)
        for row in data:
            print("| {:<30} | {:<10.2f} | {:<10.2f} |".format(*row))

    data = [
        ["Preço de venda", 100, 0],
        ["Custo de aquisição(fornecedor)", ca, 0],
        ["Receita bruta(A-B)", ml, 0],
        ["Custo fixo/administrativo", cf, 0],
        ["Comissão de vendas", cv, 0],
        ["Impostos", iv, 0],
        ["Rentabilidade(C-G)", 2, 0],
    ]

    print_table(data)
