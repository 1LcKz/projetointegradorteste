import cadastrar

def main():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    ca = int(input("Digite o custo de aquisição: "))
    cf = int(input("Digite o custo fixo: "))
    cv = int(input("Digite o custo variável: "))
    iv = int(input("Digite o imposto sobre vendas: "))
    ml = int(input("Digite a margem de lucro: "))
    
    cadastrar.cadastroProduto(codigo, nome, descricao, ca, cf, cv, iv, ml)

if __name__ == "__main__":
    main()
