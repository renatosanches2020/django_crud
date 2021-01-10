from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    # return HttpResponse('Ola Mundo') #antigo que retonava texto
    return render(request, 'index.html') #retornando para o template index.html

def articles(request, year):
    return HttpResponse('O ano passado foi: '+ str(year))

def lerDoBanco(nome):
    lista_nomes = [{'nome': 'Ana', 'idade': 25}, 
    {'nome': 'Renato', 'idade': 49},
    {'nome': 'Ale', 'idade': 47}
    ]
    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'Não Encontrado', 'idade': 0 }        

def fname(request, nome):
    result = lerDoBanco(nome)
    print(result)
    return HttpResponse('A pessoa encontrada: ' + result['nome'] + ', ela tem ' + str(result['idade']) + ' Anos')    


def fname2(request, nome):  
    nome = lerDoBanco(nome)["nome"]
    idade = lerDoBanco(nome)["idade"]    
    return render(request, 'pessoa.html', {'v_nome' : nome, 'v_idade': idade}) 