from typing import List, Dict
from time import sleep
from colorama import Fore

from models.Produtos import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print(Fore.GREEN + "==============================")
    print("=======", Fore.RED + "Bem Vindo (A)", Fore.GREEN + "========")
    print("======", Fore.RED + "Espectral Tech", Fore.GREEN + "========")
    print(Fore.GREEN + "==============================")

    print("Seleciona uma Opção abaixo: ")
    print("[1] - Cadastrar Produto")
    print("[2] - Listar Produto")
    print("[3] - Comprar Produto")
    print("[4] - Visualizar Carrinho")
    print("[5] - Fechar Pedido")
    print("[6] - Sair do Sistema")

    opcao: int = int(input('-> '))

    if opcao == 1:
        cadastra_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print("Obrigado, volte sempre!!!")
        sleep(2)
        exit(0)
    else:
        print(Fore.RED + "Opção Inválida para o usuário, Tente de novo.")
        sleep(2)
        menu()


def cadastra_produto() -> None:
    while True:
        print("Cadastrar Produto")
        print("=================")

        nome: str = input("Digite o nome do produto: ").title()
        preco: float = float(input("Digite o valor do produto: "))

        produto = Produto(nome, preco)

        produtos.append(produto)
        print(f"O Produto {produto.nome.title()} foi adicionado com sucesso!")

        repetir: int = int(input("Deseja adicionar outro produto: [1 - SIM | 2- NÃO] "))

        if repetir == 1:
            sleep(1)
            cadastra_produto()
        else:
            sleep(1)
            menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print("Listagem de produtos")
        print("--------------------")
        for produto in produtos:
            print(produto)
            print("----------------")
            sleep(1)
    else:
        print(Fore.RED + "Ainda não existem produtos cadastrados".title())
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print("Informe código do produto que deseja adicionar ao carrinho: ")
        print('------------------------------------------------------------')
        print('================== Produtos Disponiveís ====================')
        for produto in produtos:
            print(produto)
            print('--------------------------------------------------------')
            sleep(1)
        codigo: int = int(input('-> '))

        produto: Produto = pegar_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f"O produto {produto.nome} foi adicionado ao carrinho.")
                    sleep(2)
                    menu()

            else:
                item = {produto: 1 }
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho!')
                sleep(2)
                menu()
        else:
            print(f'O produto com o código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print(Fore.RED + 'Ainda não existem produtos para vender!'.title())
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print("Produtos no Carrinho")
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f"Quantidade: {dados[1]}")
                sleep(1)
    else:
        print(Fore.RED + 'Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total = 0

        print("Produtos do carrinho")
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(dados[1])
                valor_total += dados[0].preco * dados[1]
                print('--------------------------------')
                sleep(1)
        print(f"A sua fatura é de {formata_float_str_moeda(valor_total)}")
        print("Obrigado, volte sempre!")
        carrinho.clear()
        sleep(5)

    else:
        print(Fore.RED + "Ainda não existem produtos no carrinho de compras".title())
    sleep(1)
    menu()


def pegar_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == "__main__":
    main()
