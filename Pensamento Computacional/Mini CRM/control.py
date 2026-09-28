from pathlib import Path
import json, csv, os

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

# famoso CRUD (create/read/update/delete)

def read():
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

def create(lead_dict):

    leads = read()

    leads.append(lead_dict)

    # problema para resolver = otimizacao, arquivo é carregado toda vez que e para ser escrito
    # e reescreve o arquivo inteiro toda vez
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

def search(query):
    """
        Função que recebe uma query(busca de nome ou email) no leads.json
        e RETORNA uma lsita com os resultados   
    """

    leads = read()
    results = []

    for i, lead in enumerate(leads):
        txt_lead = f"{lead["name"]} {lead["email"]}".lower()

        if query.lower() in txt_lead:
            results.append((i, lead))

    return results

def export_csv():
    """
        Função exporta todos os leads para uma arquivo csv e
        retorna o caminho deste arquivo
    """

    path_csv = DATA_DIR / "leads.csv"

    leads = read()
    
    try:
        with path_csv.open("w", newline="", encoding="utf-8") as file_csv:
            writer = csv.DictWriter(file_csv, leads[0].keys())
            writer.writeheader()
            for row_dict in leads:
                writer.writerow(row_dict)

        return path_csv
    except PermissionError:
        return None