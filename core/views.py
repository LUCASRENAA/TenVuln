import datetime
import subprocess

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import models
from datetime import  datetime, timezone, timedelta



import time

# Create your views here.



# Create your views here
#from core.models import Produto
from core.models import Senhas, Chat, Questao, QuestaoUsuario, Pontuacao


def login_user(request):
    return render(request,'login.html')


def registro(request):
    return render(request,'registro.html')



def logout_user(request):
    logout(request)
    return redirect('/')
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username,password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/')
        else:
            messages.error(request,"Usuário ou senha invalido")


    return  redirect('/')

def submit_registro(request):
    print(request.POST)
    if request.POST:
        senha = request.POST.get('password')
        usuario = request.POST.get ( 'username' )
        email =   request.POST.get ( 'email' )
        try:
            print("e aqui?")
            user = User.objects.create_user ( str(usuario), str(email) ,  str(senha) )




        except:
            User.objects.get(usuario = usuario)
            User.objects.get(email = email)


            return HttpResponse('<h1> Usuario já cadastrado </h1>')

        print("hey")
        return redirect('/')
    return HttpResponse('<h1> faça um post </h1>')



@login_required(login_url='/login/')
def resposta(request,pagina):

    if int(pagina) == 1:
        resposta = request.POST.get('resposta')
        if resposta == "546789":
            resposta = "Você acertou"
            print("resposta")
            questao = QuestaoUsuario.objects.get(questao= Questao.objects.get(questao="Quebra de controle de acesso"), usuario = User.objects.get(id= request.user.id))
            if  questao.boleean == False:
                questao.boleean = True
                questao.save()
                pontuacao = Pontuacao.objects.get(usuario = User.objects.get(id= request.user.id))
                pontuacao.pontuacao = pontuacao.pontuacao + 10
                pontuacao.save()


        else:
            resposta = "Você errou"

        return HttpResponse(f'{resposta}')

    if int(pagina) == 2:
        resposta = request.POST.get('resposta')
        resposta2 = request.POST.get('resposta2')

        if resposta == "miau123":
            resposta = "Você acertou a primeira questão"
        else:
            resposta = "Você errou a primeira questão"
        if resposta2 == "asfgasfasfsa":
            resposta2 = "Você acertou a segunda questão"
        else:
            resposta2 = "Você errou a segunda questão"
        return HttpResponse(f'{resposta} : {resposta2} ')

def funcaoCriarPontuacao(usuario):
    print(usuario)
    questoes_objetos = Questao.objects.all()

    for questoes in questoes_objetos:
        verificarExistenciaQuestaoJogador(User.objects.get(id = usuario),questoes)

    try:
        Pontuacao.objects.get(usuario = User.objects.get(id = usuario) )
    except:
        Pontuacao.objects.create(usuario = User.objects.get(id = usuario), pontuacao = 0 )




def verificarExistenciaQuestao(questao):
    try:
        Questao.objects.get(questao = questao)
    except:
        Questao.objects.create(questao = questao)
def verificarExistenciaQuestaoJogador(usuario,questao):

    try:
        QuestaoUsuario.objects.get(usuario = usuario,questao = questao )
    except:
        QuestaoUsuario.objects.create(usuario = usuario, questao = questao, boleean= False)
def criarQuestoes():
    questoes = []
    questoes.append("Quebra de controle de acesso")
    questoes.append("Falhas criptográficas")
    questoes.append("Falhas criptográficas 2")

    for questao in questoes:
        verificarExistenciaQuestao(questao)


@login_required(login_url='/login/')
def inicio(request,pagina):
    criarQuestoes()
    funcaoCriarPontuacao(request.user.id)


    print("alouuu")

    titulo = "Quebra de controle de acesso"
    try:
        id = int(request.GET['id'])
    except:
        id = request.user.id
        return redirect(f'/inicio/{pagina}/?id={id}')
    try:
        roberto = User.objects.create_user(str("Roberto"),"" , str("Teste1234564"))
        lucas = User.objects.create_user(str("Lucas"),"" , str("78997"))
        alo = User.objects.create_user(str("Alo"),"" , str("45678979"))
        capotei = User.objects.create_user(str("Qualquercoisa"),"" , str("415465163"))

        Chat.objects.create(titulo = "Senha", de= roberto,para=alo,mensagem="Minha senha é: 546789")
        Chat.objects.create(titulo = "Senha", de= alo,para=capotei,mensagem="Minha senha é: 546789")
        Chat.objects.create(titulo = "Senha", de= capotei,para=lucas,mensagem="Minha senha é: 546789")
        Chat.objects.create(titulo = "Senha", de= lucas,para=roberto,mensagem="Minha senha é: 546789")

        return render(request,'inicio.html',{'pagina':1,'titulo':titulo})

    except:
        if int(pagina) == 1:
            questao = "Quebra de controle de acesso"
            resposta = QuestaoUsuario.objects.get(usuario = User.objects.get(id=request.user.id),questao=Questao.objects.get(questao = "Quebra de controle de acesso"))


            chat = Chat.objects.filter(para=User(id))

            return render(request,'inicio.html',{'pagina':1,'chat':chat,'titulo':titulo,'questao':questao,'resposta':resposta})
        if int(pagina) == 2:
            titulo = "Falhas Criptograficas"

            return render(request, 'inicio.html', {'titulo': titulo, 'pagina': 2})

        if int(pagina) == 3:
            titulo = "Injeção"

            return render(request, 'inicio.html', {'titulo': titulo, 'pagina': 3})



        if int(pagina) == 4:
            titulo = "Design Inseguro"


            return render(request, 'inicio.html', {'pagina': 4, 'titulo': titulo})

        if int(pagina) == 5:
            titulo = "Configuração Incorreta de Segurança"


            return render(request, 'inicio.html', {'pagina': 5, 'titulo': titulo})

        if int(pagina) == 6:
            titulo = "Componentes Vulneráveis e Desatualizados"
            return render(request, 'inicio.html', {'pagina': 6,  'titulo': titulo})

        if int(pagina) == 7:
            titulo = "Falhas de Identificação e Autenticação"

            return render(request, 'inicio.html', {'pagina': 7,  'titulo': titulo})

        if int(pagina) == 8:
            titulo = "Falhas de integridade de software e dados"

            return render(request, 'inicio.html', {'pagina': 8,  'titulo': titulo})

        if int(pagina) == 9:
            titulo = "Falhas de registro e monitoramento de segurança"

            return render(request, 'inicio.html', {'pagina': 9,  'titulo': titulo})

        if int(pagina) == 10:
            titulo = "Falsificação de solicitação do lado do servidor (SSRF)"
            return render(request, 'inicio.html', {'pagina': 10,  'titulo': titulo})



@login_required(login_url='/login/')
def telainicial(request):
    return render(request, 'telainicial.html')


@login_required(login_url='/login/')
def vuln1(request):
    ola = "alo"
    titulo = "Quebra de controle de acesso"
    try:
        id = int(request.GET['id'])
    except:
        id = request.user.id
        return redirect(f'/vuln1/?id={id}')

    chat = Chat.objects.filter(para=User(id))

    return render(request,'inicio.html',{'pagina':1,'chat':chat,'titulo':titulo})
@login_required(login_url='/login/')
def vuln2(request):
    titulo = "Falhas Criptograficas"

    return render(request,'inicio.html',{'titulo':titulo,'pagina':2})

@login_required(login_url='/login/')
def vuln4(request,id):
    if id == 1:
        pass
    titulo = "Injeção"

    """
    # código para testar o sql injection
    import psycopg2
    con = psycopg2.connect(host='localhost', database='senhas',
                           user='postgres', password='postgresql')
    cur = con.cursor()
    sql = "select * from core_senhas "

    cur.execute(sql)
    recset = cur.fetchall()
    for rec in recset:
        print(rec)
    con.close()
    """

    return render(request,'inicio.html',{'titulo':titulo,'pagina':3})

@login_required(login_url='/login/')
def vuln3_submit(request):
    titulo = "Injeção"
    import os
    if request.POST:
        ip = request.POST.get('ip')
        res = subprocess.check_output(f'ping -n 1 {ip}', shell=True)
        print(res)
        print(type(str(res)))

    return render(request,'inicio.html',{'titulo':titulo,'pagina':3,'saida':str(res)})

def adminsite(request):
    """
    Senhas.extra(
    select = {'val': "select col from sometable where othercol = %s"},
    select_params = (someparam,),
                 )
    """
    return render(request,'vuln1.html')
