# Questão 1
#  Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor 
# sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a
#  sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência

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
# Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja 
# maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre. 

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


# Questão 3 

# resposta   SOMA = 77

# Questão 4 

#   a) resposta = 9
#   b) resposta = 128
#   c) resposta = 49
#   d) resposta = 100
#   e) resposta = 13
#   f) resposta = ___ 

# Questão 5) 


# Partindo do ponto que eu so tenho 2 idas a uma sala independente de qual sala seja, eu ligaria o primeiro e o segundo 
# interruptor, após 30 minutos eu desligaria o interruptor 2 e iria ate a sala da lampada 1, caso ela esteja acessa 
# o interruptor 1 seria da lampada 1, caso ela estivesse apaga eu tocaria ela, se a lampada estivesse quente o
# interruptor 2 seria da lampada 1, caso ela ela estivesse apaga eu tocaria ela, se a lampada estivesse fria
# o interruptor 3 seria da lampada 1. Supondo que a lampada 1 estava apagada e fria ja sei que ela esta ligada com o
# interruptor 3, após isso iria para a sala da lampada 2, caso ela estivesse apagada ela seria ligada com o interruptor 2 e caso 
# estivesse acessa estaria ligada ao interruptor 1, sabendo o resultado da lampada 2 o interruptor da lampada 3 seria o que sobrou,
# supondo que a lampada 2 também estava apagada teriamos o seguinte resultado.
# lampada 1 => interruptor 3 , lampada 2 => interruptor 2 , lamnpada 3 => interruptor 1
 