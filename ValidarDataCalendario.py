from datetime import datetime

def verificar_data_iso(data_iso):
    try:
        # Tenta converter a string para um objeto datetime
        data_valida = datetime.strptime(data_iso, "%Y-%m-%d")
        return f"A data {data_iso} é válida."
    except ValueError:
        return f"A data {data_iso} não é válida."

# Teste
data = "2024-10-09"
resultado = verificar_data_iso(data)
print(resultado)
