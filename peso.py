def kilogramo_gramo(kilos):
    formula = kilos * 1000
    return f"Resultado: {formula} gr"
def gramo_kilogramos(gramos):
    formula = gramos * 0.001
    return f"Resultado: {formula} kg"

if __name__ == '__main__':
    kilos = 2
    gramos = 1000
    print(kilogramo_gramo(kilos))
    print(gramo_kilogramos(gramos))