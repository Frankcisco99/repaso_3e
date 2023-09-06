def metro_pulgada(metros):
    formula = metros * 39.37
    return f"Resultado: {formula} pulgadas"

def pulgada_metro(pulgadas):
    formula = pulgadas * 0.0254
    return f"Resultado: {formula} metros"

if __name__ == '__main__':
    metros = 2
    pulgadas = 10
    print(metro_pulgada(metros))
    print(pulgada_metro(pulgadas))
