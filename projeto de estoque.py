import json
arquivo_estoque = open("arquivo do estoque.json" , "r")
estoque = json.load(arquivo_estoque)
arquivo_estoque.close()
maior_id = 0

for id in estoque:
    if int(id) > maior_id:
        maior_id = int(id)

proximo_id = maior_id + 1

while True:
    print(f'\n\n\n          _____________________________________________________ PRODUTOS _____________________________________________________          \n')

    if not estoque:
        print("\n                                                       Ainda não há produtos!!!\n")

    for leitor_max in estoque:
        
        if estoque[leitor_max]["quantidade"] == 0:
            alerta = " ❌ ESTOQUE ZERADO"
        elif estoque[leitor_max]["quantidade"] <= 3:
            alerta = " ⚠️ ESTOQUE BAIXO"
        else:
            alerta = ""
        print(f'          ID: {leitor_max} | {estoque[leitor_max]["produto"]} --- {estoque[leitor_max]["quantidade"]} unidades{alerta}')

    print("\nDeseja acessar o Menu ?")
    acesso = input("Digite S (para Sim) ou N (para Não): ").lower()

    if acesso == "s":

        print('\n\n          _____________________________________________________ MENU _____________________________________________________          \n\n          1 - Adicionar produto e estoque\n          2 - Remover produto do estoque\n          3 - Reduzir a quantidade de itens por venda\n          4 - Consultar produtos em estoque\n          5 - Sair\n\n')

        entrada = input("digite sua opção: ")

        if not entrada.isdigit():
            print("\nDigite apenas números!\n")
            input("Aperte ENTER para continuar: ")
            continue

        entrada = int(entrada)

        if entrada == 1:

            for leitor_max in estoque:
        
                if estoque[leitor_max]["quantidade"] == 0:
                    alerta = " ❌ ESTOQUE ZERADO"
                elif estoque[leitor_max]["quantidade"] <= 3:
                    alerta = " ⚠️ ESTOQUE BAIXO"
                else:
                    alerta = ""
                print(f'          ID: {leitor_max} | {estoque[leitor_max]["produto"]} --- {estoque[leitor_max]["quantidade"]} unidades{alerta}')


            produto_adicionar = input("Digite seu produto a ser adicionado: ")

            if produto_adicionar.strip() == "" or not produto_adicionar.strip()[0].isalpha():
                print("\nRegistro de produto invalido! O nome deve começar com uma letra.\n")
                input("Aperte ENTER para continuar: ")
                continue

            quantidade_adicionar = input("Digite a quantidade do produto: ")

            if not quantidade_adicionar.isdigit():
                print("\nDigite apenas números!\n")
                input("Aperte ENTER para continuar: ")
                continue

            quantidade_adicionar = int(quantidade_adicionar)

            id_existente = None
            for id in estoque:
                if estoque[id]["produto"].lower() == produto_adicionar.strip().lower():
                    id_existente = id
                    break

            if id_existente:
                estoque[id_existente]["quantidade"] += quantidade_adicionar
                print(f"\nProduto já existente! Quantidade atualizada para {estoque[id_existente]['quantidade']} unidades (ID {id_existente}).\n")
            else:
                estoque[str(proximo_id)] = {
                    "produto": produto_adicionar.strip(),
                    "quantidade": quantidade_adicionar
                }
                proximo_id += 1
                print("\nNovo produto adicionado ao estoque!\n")

            arquivo_estoque = open("arquivo do estoque.json", "w")
            json.dump(estoque, arquivo_estoque)
            arquivo_estoque.close()

            input("Aperte ENTER para continuar: ")

        elif entrada == 2:

            for leitor_max in estoque:
        
                if estoque[leitor_max]["quantidade"] == 0:
                    alerta = " ❌ ESTOQUE ZERADO"
                elif estoque[leitor_max]["quantidade"] <= 3:
                    alerta = " ⚠️ ESTOQUE BAIXO"
                else:
                    alerta = ""
                print(f'          ID: {leitor_max} | {estoque[leitor_max]["produto"]} --- {estoque[leitor_max]["quantidade"]} unidades{alerta}')


            produto_remover = input("\nDigite o id do produto:\n ")

            if not produto_remover.isdigit():
                print("\nDigite apenas números!\n")
                input("Aperte ENTER para continuar: ")
                continue

            if estoque.get(produto_remover) != None:

                confirmacao = input(f"\nTem certeza que deseja remover '{estoque[produto_remover]['produto']}'? (S/N): ").lower()

                if confirmacao == "s":
                    del estoque[produto_remover]

                    arquivo_estoque = open("arquivo do estoque.json", "w")
                    json.dump(estoque, arquivo_estoque)
                    arquivo_estoque.close()

                    print(f"\nProduto removido do estoque.\n")
                else:
                    print("\nRemoção cancelada.\n")
                input("Aperte ENTER para continuar: ")

            else:
                print("\nNão encontrado\n")
                input("Aperte ENTER para continuar: ")

        elif entrada == 3:

            for leitor_max in estoque:
        
                if estoque[leitor_max]["quantidade"] == 0:
                    alerta = " ❌ ESTOQUE ZERADO"
                elif estoque[leitor_max]["quantidade"] <= 3:
                    alerta = " ⚠️ ESTOQUE BAIXO"
                else:
                    alerta = ""
                print(f'          ID: {leitor_max} | {estoque[leitor_max]["produto"]} --- {estoque[leitor_max]["quantidade"]} unidades{alerta}')


            produto_remover_quantidade = input("\nDigite o id do produto: ")

            if not produto_remover_quantidade.isdigit():
                print("\nDigite apenas números!\n")
                input("Aperte ENTER para continuar: ")
                continue

            if estoque.get(produto_remover_quantidade) != None:

                produto_quantidade_sair = input("\nDigite a quantidade a ser removida: ")

                if not produto_quantidade_sair.isdigit():
                    print("\nDigite apenas números!\n")
                    input("Aperte ENTER para continuar: ")
                    continue

                produto_quantidade_sair = int(produto_quantidade_sair)

                if estoque[produto_remover_quantidade]["quantidade"] >= produto_quantidade_sair:

                    estoque[produto_remover_quantidade]["quantidade"] -= produto_quantidade_sair

                    arquivo_estoque = open("arquivo do estoque.json", "w")
                    json.dump(estoque, arquivo_estoque)
                    arquivo_estoque.close()

                    print("\nVenda realizada com sucesso!\n")

                else:
                    print("\nO estoque tem menos produtos do que o desejado a ser vendido\n")

            else:
                print("\nProduto não encontrado !!")

        elif entrada == 4:

            print("\n\n          _____________________________________________________ PRODUTOS EM ESTOQUE _____________________________________________________          \n")

            if not estoque:
                print("Nenhum produto cadastrado ainda.")
            else:
                total_produtos = 0
                total_unidades = 0
                for leitor_max in estoque:
        
                    if estoque[leitor_max]["quantidade"] == 0:
                        alerta = " ❌ ESTOQUE ZERADO"
                    elif estoque[leitor_max]["quantidade"] <= 3:
                        alerta = " ⚠️ ESTOQUE BAIXO"
                    else:
                        alerta = ""
                    print(f'          ID: {leitor_max} | {estoque[leitor_max]["produto"]} --- {estoque[leitor_max]["quantidade"]} unidades{alerta}')

                    total_produtos += 1
                    total_unidades += estoque[leitor_max]["quantidade"]
                print(f"\n Total de produtos cadastrados: {total_produtos}")
                print(f" Total de unidades gerais em estoque: {total_unidades}")

            input("\nAperte ENTER para continuar: ")

        elif entrada == 5:

            arquivo_estoque = open("arquivo do estoque.json", "w")
            json.dump(estoque, arquivo_estoque)
            arquivo_estoque.close()

            print("Saindo do menu...")
            break

        else:
            print("\nComando inválido!\n")
            input("Aperte ENTER para continuar: ")

    elif acesso == "n":

        arquivo_estoque = open("arquivo do estoque.json", "w")
        json.dump(estoque, arquivo_estoque)
        arquivo_estoque.close()

        print("\nPermanecendo na seção de produtos...\n")
        input("\nAperte ENTER para continuar: ")
        continue


    else:
        print("\nDigite apenas S ou N!\n")
        input("Aperte ENTER para continuar: ")