from datetime import date, datetime  # Importa as classes date e datetime do módulo datetime
from Pessoa import Pessoa, Endereco, PessoaFisica, PessoaJuridica  # Importa as classes Pessoa, Endereco e PessoaFisica do módulo Pessoa

def main():
    lista_pf = []  # Inicializa uma lista vazia para armazenar objetos PessoaFisica
    lista_pj = []  # Inicializa uma lista vazia para armazenar objetos PessoaJuridica

    print("Bem vindo ao sistema de cadastro de Pessoa Física e Pessoa Jurídica")  # Mensagem de boas-vindas

    while True:  # Loop principal
        opcao = int(input("Escolha uma opção: 1 - Pessoa Física / 2 - Pessoa Jurídica / 0 - Sair: "))  # Solicita a opção do usuário

        if opcao == 1:  # Se a opção for 1 (Pessoa Física)
            while True:  # Loop para opções de Pessoa Física
                opcao_pf = int(input("Escolha uma opção: 1 - Cadastrar Pessoa Física / 2 - Listar Pessoa Física / 3 - Remover Pessoa Física / 4 - Atualizar Pessoa Física / 0 - Voltar ao menu anterior: "))  # Solicita a opção para Pessoa Física

                if opcao_pf == 1:  # Se a opção for 1 (Cadastrar Pessoa Física)
                    novapf = PessoaFisica()  # Cria um novo objeto PessoaFisica
                    novo_end_pf = Endereco()  # Cria um novo objeto Endereco

                    novapf.nome = input("Digite o nome da pessoa física: ")  # Solicita o nome da pessoa física
                    novapf.cpf = input("Digite o CPF: ")  # Solicita o CPF da pessoa física
                    novapf.rendimento = float(input("Digite o rendimento mensal (Digite somente número): "))  # Solicita o rendimento mensal

                    data_nascimento_str = input("Digite a data de Nascimento (dd/MM/aaaa): ")  # Solicita a data de nascimento
                    novapf.data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()  # Converte a string da data de nascimento para um objeto date
                    idade = (date.today() - novapf.data_nascimento).days // 365  # Calcula a idade da pessoa

                    if idade >= 18:  # Verifica se a pessoa tem mais de 18 anos
                        print("A pessoa tem mais de 18 anos")
                    else:  # Se a pessoa tem menos de 18 anos
                        print("A pessoa tem menos de 18 anos. Retornando ao menu...")
                        continue  # Retorna ao início do loop

                    novo_end_pf.logradouro = input("Digite o logradouro: ")  # Solicita o logradouro do endereço
                    novo_end_pf.numero = input("Digite o número: ")  # Solicita o número do endereço

                    end_com = input("Este endereço é comercial? S/N: ")  # Solicita se o endereço é comercial
                    novo_end_pf.endereco_comercial = end_com.strip().upper() == 'S'  # Define se o endereço é comercial com base na resposta

                    novapf.endereco = novo_end_pf  # Atribui o endereço ao objeto PessoaFisica

                    lista_pf.append(novapf)  # Adiciona o objeto PessoaFisica à lista

                    print("Cadastro realizado com sucesso!")  # Mensagem de sucesso

                elif opcao_pf == 2:  # Se a opção for 2 (Listar Pessoa Física)
                    if lista_pf:  # Verifica se a lista não está vazia
                        for cada_pf in lista_pf:  # Itera sobre cada PessoaFisica na lista
                            print(f"\nNome: {cada_pf.nome}")
                            print(f"CPF: {cada_pf.cpf}")
                            print(f"Endereço: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}")
                            print(f"Data de Nascimento: {cada_pf.data_nascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposto a ser pago: {cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print("\nDigite 0 para continuar")
                            input()  # Aguarda o usuário pressionar Enter
                    else:  # Se a lista estiver vazia
                        print("Lista vazia")
                        
                          # 3 - Remover Pessoa Física
                # 3 - Remover Pessoa Física
                elif opcao_pf == 3:
                    # Solicita ao usuário o CPF da pessoa física que deseja remover
                    cpf_para_remover = input("Digite o CPF da pessoa física que deseja remover: ")
                    
                    # Inicializa uma variável para verificar se a pessoa foi encontrada
                    pessoa_encontrada = False
                    
                    # Itera sobre cada objeto PessoaFisica na lista_pf
                    for cada_pf in lista_pf:
                        # Verifica se o CPF do objeto atual corresponde ao CPF fornecido pelo usuário
                        if cada_pf.cpf == cpf_para_remover:
                            # Remove o objeto PessoaFisica da lista se os CPFs coincidirem
                            lista_pf.remove(cada_pf)
                            
                            # Define que a pessoa foi encontrada e removida
                            pessoa_encontrada = True
                            
                            # Exibe uma mensagem de sucesso ao usuário
                            print(f"Pessoa Física com CPF {cpf_para_remover} removida com sucesso!")
                            
                            # Interrompe a iteração, pois a pessoa já foi encontrada e removida
                            break
                    
                    # Verifica se nenhuma pessoa foi encontrada com o CPF fornecido
                    if not pessoa_encontrada:
                        # Exibe uma mensagem informando que não foi encontrada nenhuma pessoa com o CPF especificado
                        print(f"Nenhuma pessoa física com CPF {cpf_para_remover} foi encontrada.")
                        
                elif opcao_pf == 4:
                        # Solicita ao usuário o CPF da pessoa física que deseja atualizar
                    cpf_para_atualizar = input("Digite o CPF da pessoa física que deseja atualizar: ")
                        
                        # Inicializa uma variável para verificar se a pessoa foi encontrada
                    pessoa_encontrada = False
                    
                    # Itera sobre cada objeto PessoaFisica na lista_pf
                    for cada_pf in lista_pf:
                        # Verifica se o CPF do objeto atual corresponde ao CPF fornecido pelo usuário
                        if cada_pf.cpf == cpf_para_atualizar:
                            # Marca que a pessoa foi encontrada
                            pessoa_encontrada = True
                            
                            # Mostra as opções de atributos que podem ser atualizados
                            print("Escolha o dado que deseja atualizar:")
                            print("N - Nome")
                            print("R - Rendimento")
                            print("L - Logradouro")
                            print("M - Número do endereço")
                            print("E - Endereço comercial (S/N)")
                            
                            # Solicita ao usuário a inicial do atributo que deseja atualizar
                            escolha = input("Digite a inicial do atributo que deseja atualizar: ").strip().upper()
                            
                            # Atualiza o atributo com base na escolha do usuário
                            if escolha == 'N':
                                novo_nome = input(f"Digite o novo nome (atual: {cada_pf.nome}): ")
                                cada_pf.nome = novo_nome 
                            elif escolha == 'R':
                                novo_rendimento = input(f"Digite o novo rendimento mensal (atual: {cada_pf.rendimento}): ")
                                cada_pf.rendimento = float(novo_rendimento) 
                            elif escolha == 'L':
                                novo_logradouro = input(f"Digite o novo logradouro (atual: {cada_pf.endereco.logradouro}): ")
                                cada_pf.endereco.logradouro = novo_logradouro 
                            elif escolha == 'M':
                                novo_numero = input(f"Digite o novo número do endereço (atual: {cada_pf.endereco.numero}): ")
                                cada_pf.endereco.numero = novo_numero 
                        
                            else:
                                print("Opção inválida. Nenhuma atualização foi feita.")
                                continue
                            
                            # Exibe uma mensagem de sucesso ao usuário
                            print(f"Cadastro da pessoa física com CPF {cpf_para_atualizar} atualizado com sucesso!")
                            break
                    
                    # Verifica se nenhuma pessoa foi encontrada com o CPF fornecido
                    if not pessoa_encontrada:
                        # Exibe uma mensagem informando que não foi encontrada nenhuma pessoa com o CPF especificado
                        print(f"Nenhuma pessoa física com CPF {cpf_para_atualizar} foi encontrada.")


                elif opcao_pf == 0:  # Se a opção for 0 (Voltar ao menu anterior)
                    print("Voltando ao menu anterior")
                    break  # Sai do loop de opções de Pessoa Física

                else:  # Se a opção for inválida1
                    print("Opção inválida, por favor digite uma opção válida!")

        elif opcao == 2:  # Se a opção for 2 (Pessoa Jurídica)
           while True:  
                opcao_pj = int(input("Escolha uma opção: 1 - Cadastrar Pessoa Jurídica / 2 - Listar Pessoa Jurídica / 3 - Remover Pessoa Jurídica / 4 - Atualizar Pessoa Jurídica 0 - Voltar ao menu anterior: "))  

                if opcao_pj == 1:  # Cadastrar Pessoa Jurídica
                    novapj = PessoaJuridica()  # Cria um novo objeto PessoaJuridica
                    novo_end_pj = Endereco()  # Cria um novo objeto Endereco

                    novapj.nome = input("Digite o nome da empresa: ")  
                    novapj.cnpj = input("Digite o CNPJ: ")  
                    novapj.rendimento = float(input("Digite o rendimento anual (Digite somente números): "))  

                    data_fundacao_str = input("Digite a data de fundação (dd/MM/aaaa): ")  
                    novapj.data_fundacao = datetime.strptime(data_fundacao_str, '%d/%m/%Y').date()  

                    novo_end_pj.logradouro = input("Digite o logradouro: ")  
                    novo_end_pj.numero = input("Digite o número: ")  

                    end_com = input("Este endereço é comercial? S/N: ")  
                    novo_end_pj.endereco_comercial = end_com.strip().upper() == 'S'  

                    novapj.endereco = novo_end_pj  

                    lista_pj.append(novapj)  

                    print("Cadastro realizado com sucesso!")  

                elif opcao_pj == 2:  # Listar Pessoa Jurídica
                    if lista_pj:  
                        for cada_pj in lista_pj:  
                            print(f"\nNome: {cada_pj.nome}")
                            print(f"CNPJ: {cada_pj.cnpj}")
                            print(f"Endereço: {cada_pj.endereco.logradouro}, {cada_pj.endereco.numero}")
                            print(f"Data de Fundação: {cada_pj.data_fundacao.strftime('%d/%m/%Y')}")
                            print(f"Imposto a ser pago: {cada_pj.calcular_imposto(cada_pj.rendimento)}")
                            print("\nDigite 0 para continuar")
                            input()  
                    else:  
                        print("Lista vazia")
                
                elif opcao_pj == 3:  # Remover Pessoa Jurídica
                    cnpj_para_remover = input("Digite o CNPJ da empresa que deseja remover: ")
                    empresa_encontrada = False
                    
                    for cada_pj in lista_pj:
                        if cada_pj.cnpj == cnpj_para_remover:
                            lista_pj.remove(cada_pj)
                            empresa_encontrada = True
                            print(f"Pessoa Jurídica com CNPJ {cnpj_para_remover} removida com sucesso!")
                            break
                    
                    if not empresa_encontrada:
                        print(f"Nenhuma empresa com CNPJ {cnpj_para_remover} foi encontrada.")


                elif opcao_pj == 0:  
                    print("Voltando ao menu anterior")
                    break  

                else:  
                    print("Opção inválida, por favor digite uma opção válida!")


        elif opcao == 0:  # Se a opção for 0 (Sair)
            print("Obrigado por utilizar o nosso sistema! Forte abraço!")
            break  # Sai do loop principal

        else:  # Se a opção for inválida
            print("Opção inválida, por favor digite uma opção válida!")

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    main()  # Chama a função principal
