#!/usr/bin/env python
# coding: utf-8

# In[3]:


from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot


# In[34]:


from datetime import datetime

atividades = []

def get_comands(pre_resposta):
    data = datetime.now()
    
    _resposta = str(pre_resposta)
    
    _resposta = _resposta.replace('c{horas}', str(data.hour))
    
    if 'c{novaativ}' in _resposta:
        print('My Bot: Qual atividade?')
        nova_atividade = input("Usuário: ")
        atividades.append(nova_atividade)
        print('My Bot: ok, vou adicionar essa tarefa na sua lista')
        _resposta = None
    
    elif 'c{falartarefas}' in _resposta:
        if len(atividades) == 0:
            print('My Bot: Não, você está livre para conversar comigo!!')
        else:
            print('My Bot: Infelizmente sim :(, você ainda tem que:')
            for tarefa in atividades:
                print(f'- {tarefa}')
        _resposta = None
    
    elif 'c{acabartarefa}' in _resposta:
        print('My Bot: Ebaa, qual tarefa?')
        tarefa_finalizada = input('Usuário: ')
        if tarefa_finalizada in atividades:
            atividades.remove(tarefa_finalizada)
            print('My Bot: Boaa, já risquei ela da lista')
        else:
            print('My Bot: Hum, não achei essa tarefa na sua lista')
        _resposta = None
    
    return _resposta


# In[35]:


bot = ChatBot('My bot')

conversa = ['Oi', 'Olá', 
            'Tudo bem?', 'Tudo ótimo', 
            'Você gosta de programar?', 'Sim, eu programo em Python',
            'Que horas são?', 'São c{horas}',
            'Você gosta de ler?', "Sim, meu livro favorito é Harry Potter",
            'Eu tenho uma atividade nova para fazer', 'Qual atividade?c{novaativ}',
            'Eu tenho alguma tarefa?', 'c{falartarefas}',
            'Eu acabei uma tarefa!', 'c{acabartarefa}']

trainer = ListTrainer(bot)
trainer.train(conversa)

while True:
    pergunta = input("Usuário: ")    
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.2:
        if get_comands(resposta) != None:
            print('My Bot: ', get_comands(resposta))
    else:
        print('My Bot: Ainda não sei responder esta pergunta')


# In[12]:




