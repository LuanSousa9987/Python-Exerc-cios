# Definindo a temperatura do paciente em graus Celsius

temperatura = 38.5

# Definindo a função para verificar se o paciente está febril 

def verificar_febril(temperatura):

 if temperatura >= 37.5:
 
    return True

 else:


   return False

# Chamando a função e exibindo o resultado

if verificar_febril(temperatura):
    print("O paciente está febril.")
else:
    print("O paciente não está febril.")
    