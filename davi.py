# Definindo o nome do aluno no programa
nome_no_programa = "João Silva"

# Definindo o número máximo de tentativas
tentativas_max = 6
tentativas = 0

# Perguntando ao usuário o modo de verificação
modo = input("Deseja verificar o nome letra por letra? (s/n): ").lower()

# Loop para controlar as tentativas
while tentativas < tentativas_max:
    tentativas += 1
    
    if modo == 's':
        # Verificação letra por letra
        nome_digitado = input("Digite o nome letra por letra (sem espaços, pressione Enter após cada letra): ")
        acertou = True
        
        # Comparando cada letra
        if len(nome_digitado) != len(nome_no_programa):
            acertou = False
        else:
            for i in range(len(nome_no_programa)):
                if i < len(nome_digitado) and nome_digitado[i] != nome_no_programa[i]:
                    acertou = False
                    break
        
        if acertou:
            print(f"Parabéns! O nome digitado é igual ao nome no programa em {tentativas} tentativa(s)!")
            break
        else:
            tentativas_restantes = tentativas_max - tentativas
            if tentativas_restantes > 0:
                print(f"Nome incorreto. Você tem {tentativas_restantes} tentativa(s) restante(s).")
            else:
                print("Você esgotou todas as tentativas. O nome no programa era:", nome_no_programa)
    else:
        # Verificação do nome completo
        nome_digitado = input("Digite o nome completo: ")
        
        if nome_digitado == nome_no_programa:
            print(f"Parabéns! O nome digitado é igual ao nome no programa em {tentativas} tentativa(s)!")
            break
        else:
            tentativas_restantes = tentativas_max - tentativas
            if tentativas_restantes > 0:
                print(f"Nome incorreto. Você tem {tentativas_restantes} tentativa(s) restante(s).")
            else:
                print("Você esgotou todas as tentativas. O nome no programa era:", nome_no_programa)