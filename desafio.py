# Questão 1

def fibonacci(num):

    fibonacci_numero_1 = 0
    fibonacci_numero_2 = 1
    fibonacci_proximo_numero = fibonacci_numero_1 + fibonacci_numero_2

    if num < 0 :
        print("o numero não pertence a sequencia de fibonacci")
    elif ( num == fibonacci_numero_1)  or (num ==  fibonacci_numero_2) or (num == fibonacci_proximo_numero):
        print("o numero pertence a sequencia de fibonacci")
    else:
        while(num > fibonacci_proximo_numero):
            fibonacci_numero_1 = fibonacci_numero_2
            fibonacci_numero_2 = fibonacci_proximo_numero
            fibonacci_proximo_numero = fibonacci_numero_1 + fibonacci_numero_2

        if num == fibonacci_proximo_numero:
            print("o numero pertence a sequencia de fibonacci")
        else:
            print("o numero nao pertence a sequencia de fibonacci")    

fibonacci(-5)       # Não pertence
fibonacci(250)      # Não pertence
fibonacci(1)        # Pertence
fibonacci(233)      # Pertence
         
# Questão 2

def procurandoLetraA(texto):
    contador = 0
    for i in texto:
        if i == 'A' or i == 'a':
            contador+=1
    
    if contador > 0: 
        print('Essa string possui '+str(contador)+' letra a ')
    else:
        print('Essa string nao possui letra a')

procurandoLetraA('hoje tem jogo do gremio')   # Não Possui 
procurandoLetraA('hoje o dia esta quente')    # Possui