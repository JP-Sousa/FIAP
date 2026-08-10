"""DESAFIO: ANALISADOR DE E-MAILS DA FIAP
▪ Você foi contratado para criar um pequeno sistema que analisa uma lista de endereços de e-mail de
alunos da FIAP e gera um relatório.
▪ O programa deve:
▪ Receber uma lista de e-mails digitada pelo usuário (separados por vírgula).
▪ Exemplo: joao.silva@fiap.com.br, maria.souza@fiap.com.br, ana.paula@fiap.com.br
▪ Separar cada e-mail em:
▪ Nome de usuário (parte antes do @)
▪ Domínio (parte depois do @)
▪ Contar quantos e-mails pertencem a cada domínio usando um dicionário.

DESAFIO: ANALISADOR DE E-MAILS DA FIAP
▪ Você foi contratado para criar um pequeno sistema que analisa uma lista de endereços de e-mail de
alunos da FIAP e gera um relatório.
▪ O programa deve:
▪ Criar uma tupla com todos os nomes de usuário e exibir o primeiro e o último.
▪ Trocar a ordem do primeiro e último nome de usuário usando atribuição de tupla (sem variável temporária).
▪ Exibir o relatório final, por exemplo:
▪ Relatório:
▪ Quantidade de e-mails por domínio:
▪ fiap.com.br: 3
▪ Lista de usuários: ('ana.paula', 'joao.silva', 'maria.souza')
▪ Após troca de posições: ('maria.souza', 'joao.silva', 'ana.paula')

DESAFIO: ANALISADOR DE E-MAILS DA FIAP
Dicas:
▪ Use split('@') para separar nome de usuário e domínio.
▪ Use um dicionário para contar os domínios.
▪ Use tuple(lista) para converter uma lista em tupla.
▪ Use a, b = b, a para trocar valores."""

emails = [
    "gabriel.silva@fiap.com.br",
    "mariana.souza@alura.com.br",
    "lucas.oliveira@alun.com.br",
    "fernanda.costa@pm3.com.br",
    "rafael.pereira@statse.com.br",
    "juliana.rodrigues@fiap.com.br",
    "bruno.almeida@alura.com.br",
    "camila.martins@alun.com.br",
    "thiago.lima@pm3.com.br",
    "beatriz.carvalho@statse.com.br",
    "andre.ferreira@fiap.com.br",
    "larissa.gomes@alura.com.br",
    "mateus.barros@alun.com.br",
    "isabela.ribeiro@pm3.com.br",
    "eduardo.teixeira@statse.com.br",
    "aline.moura@fiap.com.br",
    "vinicius.castro@alura.com.br",
    "patricia.nunes@alun.com.br",
    "gustavo.mendes@pm3.com.br",
    "leticia.freitas@statse.com.br",
    "felipe.araujo@fiap.com.br",
    "carolina.correia@alura.com.br",
    "diego.cardoso@alun.com.br",
    "renata.machado@pm3.com.br",
    "leonardo.barbosa@statse.com.br",
    "amanda.dias@fiap.com.br",
    "ricardo.monteiro@alura.com.br",
    "natalia.morais@alun.com.br",
    "henrique.pinto@pm3.com.br",
    "sofia.melo@statse.com.br",
    "daniel.vieira@fiap.com.br",
    "isabela.santos@alura.com.br",
    "marcos.reis@alun.com.br",
    "vanessa.batista@pm3.com.br",
    "caio.azevedo@statse.com.br",
    "gabriela.duarte@fiap.com.br",
    "rodrigo.fonseca@alura.com.br",
    "laura.assis@alun.com.br",
    "joao.moraes@pm3.com.br",
    "manuela.tavares@statse.com.br",
    "arthur.cunha@fiap.com.br",
    "bianca.pires@alura.com.br",
    "sergio.peixoto@alun.com.br",
    "monique.leal@pm3.com.br",
    "murilo.siqueira@statse.com.br",
    "luana.borges@fiap.com.br",
    "fabio.neves@alura.com.br",
    "clara.queiroz@alun.com.br",
    "igor.vasconcelos@pm3.com.br",
    "alice.farias@statse.com.br",
    "pedro.silveira@fiap.com.br",
    "beatriz.magalhaes@fiap.com.br",
    "caio.nascimento@fiap.com.br",
    "luiza.ramos@fiap.com.br",
    "gabriel.coelho@fiap.com.br",
    "mariana.viana@fiap.com.br",
    "lucas.farias@fiap.com.br",
    "ana.clara@fiap.com.br",
    "thiago.brito@fiap.com.br",
    "bruna.macedo@fiap.com.br",
    "eduardo.xavier@fiap.com.br",
    "carolina.figueiredo@fiap.com.br",
    "henrique.salles@alura.com.br",
    "manuela.azevedo@alura.com.br",
    "joao.varela@alura.com.br",
    "isadora.prado@alura.com.br",
    "rafaela.campos@alura.com.br",
    "otavio.moraes@alura.com.br",
    "victoria.pacheco@alura.com.br",
    "bruno.sampaio@alura.com.br",
    "luana.martins@alura.com.br",
    "danilo.torres@alura.com.br",
    "marcelo.dantas@alun.com.br",
    "sofia.nogueira@alun.com.br",
    "vinicius.rezende@alun.com.br",
    "amanda.valente@alun.com.br",
    "felipe.garcia@alun.com.br",
    "isabel.teodoro@alun.com.br",
    "ricardo.farias@alun.com.br",
    "mateus.bernardo@pm3.com.br",
    "laura.miranda@pm3.com.br",
    "andre.lopes@pm3.com.br",
    "camila.magalhaes@pm3.com.br",
    "gustavo.assis@pm3.com.br",
    "nicolas.pontes@pm3.com.br",
    "marina.cabral@statse.com.br",
    "arthur.teles@statse.com.br",
    "julia.novaes@statse.com.br",
    "renan.medeiros@statse.com.br",
    "aline.prates@statse.com.br",
    "luciana.souza@fiap.com.br",
    "diego.machado@fiap.com.br",
    "rafael.nogueira@fiap.com.br",
    "paula.monteiro@fiap.com.br",
    "sergio.alves@fiap.com.br",
    "carla.vieira@fiap.com.br",
    "murilo.domingues@fiap.com.br",
    "elisa.rangel@fiap.com.br",
    "bruno.tavares@fiap.com.br",
    "natalia.paz@fiap.com.br"
]

emailCount = dict()
users = ()

for e in emails:
    user, domain = e.split("@")

    users = users + (user, )

    if domain not in emailCount:
        emailCount[domain] = 1
    else:
        emailCount[domain] += 1

print("Quantidade de e-mails por domínio:")
print(emailCount)
print(users)

users = users[-1], *users[1:-1], users[0]

print(users)