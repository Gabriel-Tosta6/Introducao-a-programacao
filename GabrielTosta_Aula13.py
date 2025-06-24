contatos = {}

while True:
    print("""\nx-x-x-OPÇÕES-x-x-x\n
1 - Adicionar Contato\n
2 - Remover Contato\n
3 - Alterar Contato\n
4 - Exibir todos os contatos\n
5 - Sair\n""")
    
    try:
        o = int(input('Selecione uma opção:\n'))

    except ValueError:
        print("\nOps! Entrada inválida. Por favor, digite um número de 1 a 5.\n")
        continue

    match o:

        case 1:
            nome = input('\nQual o nome do contato que você deseja adicionar?: ').strip().upper()

            if not nome:
                print("\nNome do contato não pode ser vazio.\n")
                continue
            
            numero = input(f'\nQual o número de telefone para {nome}?: ').strip()

            if not numero:
                print("\nNúmero de telefone não pode ser vazio.\n")
                continue
            
            contatos[nome] = numero
            print(f"\nContato '{nome}' adicionado/atualizado com sucesso!\n")

        case 2:
            remover = input('\nQual o nome do contato que você quer remover?: ').strip().upper()
            if not remover:
                print("\nNome do contato não pode ser vazio.\n")
                continue

            if remover in contatos:

                del contatos[remover]
                print(f'\nContato {remover} removido com sucesso!\n')
            else:
                print(f'\nContato {remover} não encontrado na lista.\n')

        case 3:
            oque = input('\nO que você deseja alterar? (NOME) (TELEFONE): ').strip().upper()

            if oque == 'NOME':
                nome_antigo = input('\nQual o NOME do contato que você deseja alterar?: ').strip().upper()
                if not nome_antigo:
                    print("\nNome antigo do contato não pode ser vazio.\n")
                    continue

                if nome_antigo in contatos:
                    novo_nome = input('\nQual o NOVO NOME para o contato?: ').strip().upper()
                    if not novo_nome:
                        print("\nNovo nome do contato não pode ser vazio.\n")
                        continue

                    telefone = contatos[nome_antigo]
                    contatos[novo_nome] = telefone

                    del contatos[nome_antigo]
                    print(f'\nNome do contato "{nome_antigo}" alterado para "{novo_nome}" com sucesso!\n')

                else:
                    print(f'\nContato "{nome_antigo}" não encontrado na lista.\n')

            elif oque == 'TELEFONE':
                nome_do_contato = input('\nQual o NOME do contato que você deseja alterar o TELEFONE?: ').strip().upper()
                if not nome_do_contato:
                    print("\nNome do contato não pode ser vazio.\n")
                    continue

                if nome_do_contato in contatos:
                    novo_numero = input(f'\nQual o NOVO NÚMERO de telefone para {nome_do_contato}?: ').strip()
                    if not novo_numero:
                        print("\nNovo número de telefone não pode ser vazio.\n")
                        continue
                    
                    contatos[nome_do_contato] = novo_numero
                    print(f'\nTelefone do contato "{nome_do_contato}" alterado para "{novo_numero}" com sucesso!\n')
                else:
                    print(f'\nContato "{nome_do_contato}" não encontrado na lista.\n')
            else:
                print("\nOpção de alteração inválida. Por favor, digite 'NOME' ou 'TELEFONE'.\n")

        case 4:
            print('\n--- Aqui estão todos os seus contatos: ---\n')
            if not contatos:
                print("Nenhum contato na lista.")
            else:

                for nome in sorted(contatos.keys()):
                    print(f"Nome: {nome}, Telefone: {contatos[nome]}")
            print("\n-----------------------------------------\n")

        case 5:
            print("\nPrograma encerrado!\n")
            break

        case _:
            print("\nOpção inválida. Por favor, escolha uma opção de 1 a 5.\n")