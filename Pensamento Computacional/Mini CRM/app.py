from model import model_lead
import control

def add_lead():

    name = input("\nNome: ")
    email = input("E-mail: ")
    status = input("Situação: ")

    # validar os dados
    # depois de validar
    # precisamos modelar os dados como um dict

    # com o lead modelado como dict
    # precisa enviar para leads.json
    # usando control/controller

    control.create(model_lead(name, email, status))

    print("\nLead adicionado")

def list_leads():

    leads = control.read()
    # problema/desafio imprimir como tabela

    print(f"\n## | {"Nome":<10} | E-mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]}")

def search_leads():
    query = input("Buscar por: ").strip().lower()
    if not query:
        print("Consulta Vazia")
        return
    
    search_results = control.search(query)

    print(f"\n## | {"Nome":<10} | E-mail")

    for i, lead in search_results:
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]}")

def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possível exportar para CSV")
    else:
        print("Exportado para: ", path_csv)

def main():
    while True:
        print("\nMini CRM de leads\n")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar (nome/e-mail)")
        print("[4] Exportar para CSV")
        print("[0] Sair do programa")

        control.open()

        option = input("\nEscolha uma opção: ")

        match option:

            case '1':
                add_lead()

            case '2':
                list_leads()

            case '3':
                search_leads()

            case '4':
                export_leads()

            case '0':
                print("Até mais...")
                control.close()
                break

            case _:
                print("\nOpção inválida, tente novamente")


if __name__ == "__main__":
    main()