#!/usr/bin/python3
# coding: utf-8

import os
import time
import subprocess
from subprocess import Popen, PIPE, STDOUT


#################################################################
# Configurações do professor
# 
entradaDados = b"12\n13\n"
saidaDadosEsperada = "25"
limite_segundos = 3

def compilar():
    log = open('saida.log', 'a')
    log.write('=======================================================================\n');
    log.write('            Testar códigos que compilam  \n');
    log.write('=======================================================================\n');
    log.close()
    tarefasAcorrigir = os.popen('ls code/*.cpp').readlines()

    for indice, valor in enumerate(tarefasAcorrigir):
    	tarefasAcorrigir[indice] = tarefasAcorrigir[indice].replace('.cpp','')
    	tarefasAcorrigir[indice] = tarefasAcorrigir[indice].replace('code/','')
    	tarefasAcorrigir[indice] = tarefasAcorrigir[indice].replace('\n','')

    #################################################################
    # Compilar todos os arquivos .cpp da pasta code 
    # e gerar o executável na pasta executável
    # 
    print('Compilando os executáveis')
    for tarefa in tarefasAcorrigir:
    #    print('Tarefa: ' + tarefa)
        comando = 'g++ code/' + tarefa + '.cpp -o executavel/' + tarefa + '.exe'
    #    print(comando)

        try:
            subprocess.run(comando, shell=True, check=True)
            log = open('saida.log', 'a')
            log.write('Tarefa '+ tarefa + ' compilou\n');
            log.close()
        except subprocess.CalledProcessError:
            log = open('saida.log', 'a')
            log.write('Tarefa '+ tarefa + ' NÃO COMPILOU\n');
            log.close()

def testar():
    log = open('saida.log', 'a')
    log.write('=======================================================================\n');
    log.write('            Testar executáveis conforme entradas e saídas esperadas  \n');
    log.write('=======================================================================\n');
    log.close()

    tarefasAcorrigir = os.popen('ls executavel/*.exe').readlines()

    for indice, valor in enumerate(tarefasAcorrigir):
    	tarefasAcorrigir[indice] = tarefasAcorrigir[indice].replace('.exe','')
    	tarefasAcorrigir[indice] = tarefasAcorrigir[indice].replace('executavel/','')
    	tarefasAcorrigir[indice] = tarefasAcorrigir[indice].replace('\n','')


    for tarefa in tarefasAcorrigir:
        comando = './executavel/'+tarefa + '.exe'
            
        try:
            time.sleep(limite_segundos)

            print('CORREÇÃO DA TAREFA: ' + tarefa + '\n')
    
            p = Popen([comando, ''], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
            saidaComando = p.communicate(input=entradaDados, timeout=limite_segundos)[0]
            saida = saidaComando.decode()
    
            if saidaDadosEsperada in saida:
                log = open('saida.log', 'a')
                log.write('Tarefa '+ tarefa + ' rodou conforme esperado. \n');
                log.close()
            else:          
                log = open('saida.log', 'a')
                log.write('Tarefa '+ tarefa + ' NÃO RODOU CONFORME ESPERADO. \n');
                log.close()
        except subprocess.CalledProcessError:
            log = open('saida.log', 'a')
            log.write('Tarefa '+ tarefa + ' NÃO RODOU CONFORME ESPERADO, ERRO CAUSADO POR subprocess.CalledProcessError. \n');
            log.close()
        except subprocess.TimeoutExpired:
            log = open('saida.log', 'a')
            log.write('Tarefa '+ tarefa + ' NÃO RODOU CONFORME ESPERADO, ERRO CAUSADO POR subprocess.TimeoutExpired. \n');
            log.close()

def totalLinhas():
    log = open('saida.log', 'a')
    log.write('=======================================================================\n');
    log.write('            Número de linhas em cada arquivo ' + '\n');
    log.write('=======================================================================\n');
    log.close()
    tarefasAcorrigir = os.popen('ls code/*.cpp').readlines()

    for indice, valor in enumerate(tarefasAcorrigir):
        tarefasAcorrigir[indice] = tarefasAcorrigir[indice].replace('\n','')

    for tarefa in tarefasAcorrigir:
        arq = open(tarefa, 'r')
        texto = arq.readlines() 
        totalLinhas = str(len(texto))
        arq.close()
        tarefa = tarefa.replace('code/','')
        tarefa = tarefa.replace('.cpp','')

        log = open('saida.log', 'a')
        log.write('Tarefa ' + tarefa + ' : ' + totalLinhas + ' linhas. \n');
        log.close()

def possui_instrucao(procurarTexto):
    log = open('saida.log', 'a')
    log.write('=======================================================================\n');
    log.write('            Encontrar nos códigos-fonte a instrução ' + procurarTexto + '\n');
    log.write('=======================================================================\n');
    log.close()
    tarefasAcorrigir = os.popen('ls code/*.cpp').readlines()

    for indice, valor in enumerate(tarefasAcorrigir):
        tarefasAcorrigir[indice] = tarefasAcorrigir[indice].replace('\n','')

    print('Procurar nos códigos a instrução ' + procurarTexto)
    for tarefa in tarefasAcorrigir:
        arq = open(tarefa, 'r')
        texto = arq.readlines() 
        totalTermos = 0
        for linha in texto: 
            encontrado = linha.count(procurarTexto)
            if encontrado > 0:
                totalTermos = totalTermos + encontrado
        arq.close()
        tarefa = tarefa.replace('code/','')
        tarefa = tarefa.replace('.cpp','')
        log = open('saida.log', 'a')
        log.write('Tarefa ' + tarefa + ' possui  ' + str(totalTermos) + ' vezes o termo ' + procurarTexto + '\n');
        log.close()

if __name__ == "__main__":
    compilar()
    testar()
    totalLinhas()
    possui_instrucao('cout >>')
    possui_instrucao('cout <<')
    possui_instrucao('cin <<')
    possui_instrucao('cin >>')
    possui_instrucao('scanf')

