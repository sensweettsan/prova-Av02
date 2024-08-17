from models.produtos_pizzas import Pizza

def main():
  
    while True:
        opcao = int(input('Escolha o sabor da pizza \n'
                            '\n1- Para Calabresa'
                            '\n2- Para Bacon'
                            '\n3- Para Baiana'
                            '\n4- Para Portuguesa'
                            '\n Escolha sua opção ->'
                                                        
                        ))
        if opcao == 1:
            print('Calabresa')
        if opcao == 2:
            print('Bacon')
        if opcao == 3:
            print('Baiana')
        if opcao == 4:
            print('Portuguesa')
        else:
            print('Opção inválida!')

            sair = input('Digite s para sair ou enter para continuar: ')
            if sair.upper() == 'S':
                break
        
        opcao = int(input('Escolha o tamanho ds Pizza \n '
                            '\n1- G'
                            '\n2- M'
                            '\n3- P'
                            '\n Escolha o tamanho desejado ->'
                          ))
        if opcao == 1:
            print('G')
        if opcao == 2:
            print('M')
        if opcao == 3:
            print('P')
        else:
            print('Opção inválida!')

            sair = input('Digite s para sair ou enter para continuar: ')
            if sair.upper() == 'S':
                break
        
       
    
if __name__ == '__main__':
    main()