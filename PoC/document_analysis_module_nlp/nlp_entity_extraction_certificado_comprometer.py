import re

def extract_amount_and_person(text: str):
    # Regular expression to find the amount in both numerical and text format
    amount_pattern = re.compile(r'\b(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\b')
    
    # Regular expression to find the person's name (Beneficiary)
    person_pattern = re.compile(r'\b\d{11}\s+([\w\s]+)')
    
    # Search for the amount in the text
    amount_match = amount_pattern.findall(text)
    # Assuming the largest number found is the amount
    if amount_match:
        amount = max(amount_match, key=lambda x: float(x.replace(',', '')))
    else:
        amount = None

    # Search for the person's name in the text
    person_match = person_pattern.search(text)
    person = person_match.group(1).strip() if person_match else None

    return amount, person

# Example usage:
text = """
GOBIERNO DE LA
REPÚBLICA DOMINICANA Página 1 de 1
HACIENDA
CERTIFICADO DE DISPONIBILIDAD DE CUOTA PARA COMPROMETER

Sistema de Información de la Gestión Financiera.

Período Fiscal : 2022 No. Expediente :

Fecha: | No. Documento : EG1671129653591L5Aer

Fech

Capítulo : 0210-MINISTERIO DE AGRICULTURA

SubCapítulo: 01-MINISTERIO DE AGRICULTURA

Unidad Ejecutora : 0001-MINISTERIO DE AGRICULTURA

PARA CUBRIR PROCESO DE COMPRAS, SERVICIO DE ROTULACION DE 5,000 TAREAS
DE TERRENOS EN LABORES DE CORTE Y CRUCE, PARA LA SIEMBRA DE DIFERENTES
RUBROS CON TRACTORES PRIVADOS, EN LAS DISTINTAS PROVINCIAS AFECTADAS
POR EL HURACAN FIONA. SEGUN DOC. ANEXOS

Proceso :

No. Referencia :
Monto Total Proceso :
Moneda: PESOS DOMINICANOS

Se CERTIFICA la Disponibilidad de Cuota para Comprometer en base al Presupuesto General del Estado para el
año 2022, aprobado por Ley No. 345-21 que permite suscribir contratos de compra de bienes, obras y servicios o
firmar órdenes de compras por el monto indicado en este documento, en cumplimiento a lo establecido en el
Decreto 15-17 del 08 febrero de 2017. De acuerdo al siguiente detalle :

Cuenta s de pz ,
Nombre de la Cuenta Presupuestaria | Apropiación Presupuestaria 2022

2.7.2.6.01 Infraestructura y plantaciones agrícolas | 3,117,000.00
[Total | 3,117,000.00
El monto de : *Tres millones ciento diecisiete mil con 00/100 (3,117,000.00)

Número de Compromiso Fecha de Compromiso Monto de Compromiso
2022.0210.01.0001.10404-Versión 1 15/12/2022 3,117,000.00
Beneficiario

Moneda Original

3,117,000.00
3,117,000.00

04100164179 Seneyda Eulalia Abreu De Sanchez
Total
"""

amount, person = extract_amount_and_person(text)

print(f"Amount: {amount}")
print(f"Person: {person}")
