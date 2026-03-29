"""
#### Exercício 2

Uma fórmula recomenda 2mg de medicamento por kg de peso do paciente.

Peça o peso de uma pessoa e calcule a dose recomendada.

Exemplo:

Digite o peso do paciente (em kg):
70

Resposta:
Média: 140 mg
"""


def calcular_dose():
    peso = float(input("Digite o peso do paciente (em kg): "))
    dose = peso * 2
    
    return dose
    

print(f"Dose: {calcular_dose():.2f} mg")
