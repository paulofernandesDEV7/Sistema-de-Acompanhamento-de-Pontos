
from datetime import datetime

from banco import(
    cadastrar_usuario,
    listar_usuario,
    excluir_usuario,
    registrar_servico,
    listar_servico,
    obter_total_pontos,
    obter_total_comissao,
    obter_total_servico,
    obter_total_comissao_usuario,
    obter_total_pontos_usuario,
    obter_total_servico_usuario
)

print("""
=====================================
        SELECIONE UMA OPÇÃO
=====================================

1 - Cadastrar usuário
2 - Listar usuários
3 - Excluir usuário
0 - Sair

======================================
""")
opcao = input('Escolha uma opção! ')

if opcao == '1':
   nome = input('Digite seu nome: ')
   id_usuario = cadastrar_usuario(nome)
   print('iD do usuário:', id_usuario)

if opcao == '2':
    usuarios = listar_usuario()
    print(usuarios)
    id_usuario = int(input(
        'Digite o ID do usuário que irá registrar os serviços: '
    ))

if opcao == '3':
    id_excluir = input('Digite o ID do usuário que deseja excluir: ')
    excluir_usuario(id_excluir)
    print('Usuario excluído!')


saldo_pontos = 0
comissao_reativados = 0
meta_mensal = 176

pontos_servicos = {
    1: 1,
    2: 0.84,
    3: 0.71,
    4: 0.81,
    5: 1,
    6: 1.09,
    7: 1,
    8: 1

}
comissao_servico = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 10,
    8: 0
}

print('Digite 1 para ativação de chip 5G\n')
print('Digite 2 para ativação de chip combo\n')
print('Digite 3 para ativação de chip madacaru\n')
print('Digite 4 para reativação de FWA\n')
print('Digite 5 para recolhimento\n')
print('Digite 6 para instalação de FWA\n')
print('Digite 7 para reativação na hora\n')
print('Digite 8 para chip avulso\n')
print('Digite 0 para sair\n')

servico = int(input('Digite o número do serviço: '))

def registrar_servico_pontos(servico):
    if servico >= 1 and servico <= 8:
        return pontos_servicos[servico], comissao_servico[servico]
    else:
        opcao_invalida(servico)

def opcao_invalida(servico):
    if servico < 0 or servico > 8:
        print('Opss... Opção Inválida!')

while servico != 0:
    if servico >= 1 and servico <= 8:
        pontos, comissao = registrar_servico_pontos(servico)
        data_hora = datetime.now().strftime(
            '%d / %m / %Y  %H : %M : %S'
        )
        registrar_servico(id_usuario, servico,comissao,data_hora,pontos)

        comissao_reativados += comissao
        saldo_pontos += pontos
        print('Seu saldo de pontos é de: {:.2f},'
              ' e sua comissão de reativados é de: {:.2f} R$'
              .format(saldo_pontos, comissao_reativados)
        )
    else:
        opcao_invalida(servico)
    servico = int(input('Digite o número do próximo serviço (0 para sair): '))


registros = listar_servico()
for registro in registros:
    id, nome, servico, comissao, data_hora, pontos = registro
print('╔══════════════════════════════════════╗')
print('║         Histórico de Serviço         ║')
print('╠══════════════════════════════════════╣')
print('║ ID: {}                               ║'
      .format(id))
print('║ Usuário: {}             ║'
      .format(nome))
print('║ Serviço: {}                           ║'
      .format(servico))
print('║ Pontos: R$ {}                      ║'
      .format(pontos))
print('║ Comissão: {:.0f}                          ║'
      .format(comissao))
print('║ Data: {}   ║'
      .format(data_hora))
print('╚══════════════════════════════════════╝')


total_pontos = obter_total_pontos()
total_comissao = obter_total_comissao()
total_servico = obter_total_servico()
total_pontos_usuario = obter_total_pontos_usuario(id_usuario)
total_comissao_usuario = obter_total_comissao_usuario(id_usuario)
total_servico_usuario = obter_total_servico_usuario(id_usuario)
percentual_meta = (total_pontos_usuario / meta_mensal) * 100
data_hora = datetime.now().strftime(
            '%d / %m / %Y  %H : %M : %S'
        )


print('╔══════════════════════════════════════╗')
print('║                RESUMO                ║')
print('╠══════════════════════════════════════╣')
print('║ Total de serviços: {}                ║'
      .format(total_servico))
print('║ Total de pontos: {:.2f}               ║'
      .format(total_pontos))
print('║ Total de comissão: R$ {}          ║'
      .format(total_comissao))
print('║ Data: {}   ║'
      .format(data_hora))
print('╚══════════════════════════════════════╝')

print('╔══════════════════════════════════════╗')
print('║         PAINEL DE PRODUÇÃO           ║')
print('╠══════════════════════════════════════╣')
print('║ Usuário: {}                          ║'
      .format(id_usuario))
print('║ Serviços realizados: {}              ║'
      .format(total_servico_usuario))
print('║ Pontos acumulados: {:.2f}             ║'
      .format(total_pontos_usuario))
print('║ Comissão: R$ {:.2f}                   ║'
      .format(total_comissao_usuario))
print('║ Meta: {:.0f} pontos                     ║'
      .format(meta_mensal))
print('║ Progresso da meta: {:.2f}%             ║'
      .format(percentual_meta))
print('╚══════════════════════════════════════╝')