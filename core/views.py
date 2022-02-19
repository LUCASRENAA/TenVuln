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
import urllib.parse


import time

# Create your views here.



# Create your views here
#from core.models import Produto
from core.models import Senhas, Chat, QuestaoResposta, QuestaoUsuario, Pontuacao, OWASP, TextoHtml


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

def somarPontuacao(usuario):
    pontuacao = Pontuacao.objects.get(usuario=usuario)
    pontuacao.pontuacao = pontuacao.pontuacao + 10
    pontuacao.save()
    return pontuacao

def pegarResposta(questao,usuario):
    questao = QuestaoUsuario.objects.get(questao=questao, usuario=usuario)
    if questao.boleean == False:
        questao.boleean = True
        questao.save()
        pontuacao = somarPontuacao(usuario)

def verificarResposta(pagina,resposta,questao,usuario):
    print(resposta)
    print(questao.resposta)
    if resposta == questao.resposta:
            resposta = "Você acertou"
            print("resposta")
            pegarResposta(questao,usuario)

    else:
            resposta = "Você errou"


    return resposta

@login_required(login_url='/login/')
def submit_teste(request, pagina):
    usuario = User.objects.get(id=request.user.id)
    if int(pagina) == 7:
        resposta = request.POST.get('resposta')
        questao = QuestaoResposta.objects.get(questao="Falhas de Identificação e Autenticação(BruteForce)")
        resposta = verificarResposta(int(pagina),resposta,questao,usuario )
        return HttpResponse(f'{resposta}')
@login_required(login_url='/login/')
def resposta(request,pagina,ano):
    usuario = User.objects.get(id= request.user.id)
    print("entrei aqui")
    if int(pagina) == 1:
        resposta = request.POST.get('resposta')
        questao = QuestaoResposta.objects.get(questao="Quebra de controle de acesso")
        resposta = verificarResposta(int(pagina),resposta,questao,usuario )
        return HttpResponse(f'{resposta}')
    """
    if int(pagina) == 2:
        resposta = request.POST.get('resposta')
        questao = QuestaoResposta.objects.get(questao="Falhas criptográficas")
        resposta = verificarResposta(int(pagina), resposta, questao, usuario)
        resposta2 = request.POST.get('resposta2')
        questao2 = QuestaoResposta.objects.get(questao="Falhas criptográficas 2")
        resposta2 = verificarResposta(int(pagina), resposta2, questao2, usuario)


        return HttpResponse(f'{resposta} : {resposta2} ')


    if int(pagina) == 7:
        resposta = request.POST.get('user')
        resposta2 = request.POST.get('password')

        questao = QuestaoResposta.objects.get(questao="Falhas de Identificação e Autenticação")
        resposta = verificarResposta(int(pagina),f'{resposta}:{resposta2}',questao,usuario )
        return HttpResponse(f'{resposta}')
    """
    texto = ""
    print("testeaaaaa")
    for a in dict(request.POST) :
        print(a)
        if "resposta" in a:
            if texto == "":
                texto = texto  + request.POST.get(a)
            else:
                texto = texto + ":" + request.POST.get(a)

    print("aqui")
    print(texto)
    try:
        resposta = request.POST.get('resposta')
        id = request.POST.get('id')
        print(id)
        questao = QuestaoResposta.objects.get(id=int(id))
        print(questao)
        resposta = verificarResposta(int(pagina), f'{resposta}', questao, usuario)

        return HttpResponse(f'{resposta}')

    except:

        return HttpResponse(f'erro')

def funcaoCriarPontuacao(usuario):
    print(usuario)
    questoes_objetos = QuestaoResposta.objects.all()

    for questoes in questoes_objetos:
        verificarExistenciaQuestaoJogador(User.objects.get(id = usuario),questoes)

    try:
        Pontuacao.objects.get(usuario = User.objects.get(id = usuario) )
    except:
        Pontuacao.objects.create(usuario = User.objects.get(id = usuario), pontuacao = 0 )




def verificarExistenciaQuestao(questao,resposta,owasp):
    try:
        QuestaoResposta.objects.get(questao = questao,resposta=resposta)
    except:
        QuestaoResposta.objects.create(questao = questao,resposta=resposta,owasp = owasp,descricao=" ")
def verificarExistenciaOwasp(titulo,posicao,ano):
    try:
        OWASP.objects.get(titulo = titulo,posicao=posicao,ano=ano)
    except:
        OWASP.objects.create(titulo = titulo,posicao=posicao,ano=ano)
def verificarExistenciaQuestaoJogador(usuario,questao):

    try:
        QuestaoUsuario.objects.get(usuario = usuario,questao = questao )
    except:
        QuestaoUsuario.objects.create(usuario = usuario, questao = questao, boleean= False)
def criarQuestoes():
    questoes = []
    owasp_vetor = []
    class Questao_Formar:
        def __init__(self, titulo, resposta):
            self.name = titulo
            self.resposta = resposta


    owasp_vai = OWASP.objects.get(titulo = "Quebra de controle de acesso",ano = 2021)
    owasp_vetor.append(owasp_vai)
    questao_teste = Questao_Formar("Quebra de controle de acesso","546789")
    questoes.append(questao_teste)

    questao_teste = Questao_Formar("Falhas criptográficas", "miau123")
    questoes.append(questao_teste)

    owasp_vai = OWASP.objects.get(titulo="Falhas criptográficas", ano=2021)
    owasp_vetor.append(owasp_vai)

    questao_teste = Questao_Formar("Falhas criptográficas 2", "asfgasfasfsa")
    questoes.append(questao_teste)

    owasp_vai = OWASP.objects.get(titulo="Falhas criptográficas", ano=2021)
    owasp_vetor.append(owasp_vai)

    questao_teste = Questao_Formar("Falhas de Identificação e Autenticação(BruteForce)", "admin:admin")
    questoes.append(questao_teste)

    owasp_vai = OWASP.objects.get(titulo="Falhas de Identificação e Autenticação", ano=2021)
    owasp_vetor.append(owasp_vai)

    questao_teste = Questao_Formar("Configuração Incorreta de Segurança", "suporte:suporte")
    questoes.append(questao_teste)

    owasp_vai = OWASP.objects.get(titulo="Configuração Incorreta de Segurança", ano=2021)
    owasp_vetor.append(owasp_vai)
    contador = 0
    for questao in questoes:
        print(questao)
        verificarExistenciaQuestao(questao.name,questao.resposta,owasp_vetor[contador])
        contador = contador + 1

def criarTop10Owasp():
        questoes = []



        class OWASP_teste:
            def __init__(self, titulo, posicao, ano):
                self.titulo = titulo
                self.posicao = posicao
                self.ano = ano

        questao_teste = OWASP_teste("Quebra de controle de acesso", "1","2021")
        questoes.append(questao_teste)

        questao_teste = OWASP_teste("Falhas criptográficas", "2", "2021")
        questoes.append(questao_teste)

        questao_teste = OWASP_teste("Injeção", "3", "2021")
        questoes.append(questao_teste)

        questao_teste = OWASP_teste("Design Inseguro", "4", "2021")
        questoes.append(questao_teste)

        questao_teste = OWASP_teste("Configuração Incorreta de Segurança", "5", "2021")
        questoes.append(questao_teste)

        questao_teste = OWASP_teste("Componentes Vulneráveis e Desatualizados", "6", "2021")
        questoes.append(questao_teste)

        questao_teste = OWASP_teste("Falhas de Identificação e Autenticação", "7", "2021")
        questoes.append(questao_teste)

        questao_teste = OWASP_teste("Falhas de integridade de software e dados", "8", "2021")
        questoes.append(questao_teste)

        questao_teste = OWASP_teste("Falhas de registro e monitoramento de segurança", "9", "2021")
        questoes.append(questao_teste)

        questao_teste = OWASP_teste("Falsificação de solicitação do lado do servidor (SSRF)", "10", "2021")
        questoes.append(questao_teste)
        for questao in questoes:
            verificarExistenciaOwasp(questao.titulo, questao.posicao,questao.ano)



@login_required(login_url='/login/')
def funcaoRespostas(request,titulo):
    titulo = titulo.replace('/','')

    return render(request, f'{titulo}')


@login_required(login_url='/login/')
def inicio(request,pagina,ano):
    criarTop10Owasp()


    criarQuestoes()
    funcaoCriarPontuacao(request.user.id)
    owasps = OWASP.objects.filter(ano=int(ano))
    pontuacao = Pontuacao.objects.get(usuario = User.objects.get(id = request.user.id)).pontuacao
    print("alouuu")
    ranking = Pontuacao.objects.all()[::-1]

    titulo = "Quebra de controle de acesso"
    try:
        id = int(request.GET['id'])
    except:
        id = request.user.id
        return redirect(f'/inicio/{pagina}/{ano}/?id={id}')
    try:
        roberto = User.objects.create_user(str("Roberto"),"" , str("Teste1234564"))
        lucas = User.objects.create_user(str("Lucas"),"" , str("78997"))
        alo = User.objects.create_user(str("Alo"),"" , str("45678979"))
        capotei = User.objects.create_user(str("Qualquercoisa"),"" , str("415465163"))

        Chat.objects.create(titulo = "Senha", de= roberto,para=alo,mensagem="Minha senha é: 546789")
        Chat.objects.create(titulo = "Senha", de= alo,para=capotei,mensagem="Minha senha é: 546789")
        Chat.objects.create(titulo = "Senha", de= capotei,para=lucas,mensagem="Minha senha é: 546789")
        Chat.objects.create(titulo = "Senha", de= lucas,para=roberto,mensagem="Minha senha é: 546789")

        return render(request,'inicio.html',{'respostas':QuestaoResposta.objects.filter(owasp=OWASP.objects.get(id=int(pagina)),ano=int(ano)),'pagina':1,'titulo':titulo,'pontuacao': pontuacao,'ano':ano,'owasp':owasps,'ranking':ranking})

    except:
        if int(pagina) == 1:

            chat = Chat.objects.filter(para=User(id))
            try:
                textos = TextoHtml.objects.filter(owasp=OWASP.objects.get(id=int(pagina),ano=int(ano)))
            except:
                textos = ""
            return render(request,'inicio.html',{'pagina':1,'chat':chat,'resposta':resposta,'pontuacao': pontuacao,'ano':ano,
                                                 'owasp':owasps,'ranking':ranking,'respostas':QuestaoResposta.objects.filter(owasp=OWASP.objects.get(posicao=int(pagina),ano=int(ano))),
                                                 'textos':textos})

        textos = TextoHtml.objects.filter(
            owasp=OWASP.objects.get(posicao=int(pagina),ano=int(ano)))

        return render(request, 'inicio.html', {'pagina': int(pagina),'pontuacao': pontuacao,'ano':ano,'owasp':owasps,
                                               'ranking':ranking,'respostas':QuestaoResposta.objects.filter(owasp=OWASP.objects.get(posicao=int(pagina),ano=int(ano))),'textos':textos})



@login_required(login_url='/login/')
def telainicial(request):

    ano  = 2021
    return render(request, 'telainicial.html',{'ano': ano})



@login_required(login_url='/login/')
def telainicial(request):
    ano = 2021
    return render(request, 'telainicial.html',{'ano':ano})



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
