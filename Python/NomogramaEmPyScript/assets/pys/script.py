nomograma = {
    -0.25: -0.75,
    -0.50: -1.00,
    -0.75: -1.25,
    -1.00: -1.50,
    -1.25: -1.75,
    -1.50: -2.00,
    -1.75: -2.25,
    -2.00: -2.50,
    -2.25: -2.50,
    -2.50: -2.75,
    -2.75: -3.00,
    -3.00: -3.25,
    -3.25: -3.50,
    -3.50: -3.75,
    -3.75: -4.00,
    -4.00: -4.00,
    -4.25: -4.25,
    -4.50: -4.50,
    -4.75: -4.75,
    -5.00: -4.75,
    -5.25: -5.00,
    -5.50: -5.25,
    -5.75: -5.50,
    -6.00: -5.75,
    -6.25: -6.00,
    -6.50: -6.25,
    -6.75: -6.25,
    -7.00: -6.50,
    -7.25: -6.75,
    -7.50: -7.00,
    -7.75: -7.25,
    -8.00: -7.25,
    -8.25: -7.50,
    -8.50: -7.75,
    -8.75: -8.00,
    -9.00: -8.25,
    -9.25: -8.50,
    -9.50: -8.75,
    -9.75: -9.00,
    -10.00: -9.00,
    -11.00: -9.50
}

def mostrar_tabela():
    tabela = Element('tabela-resultado')
    tabela.element.style.display = 'block'

def calcula_nomograma(*args, **kwargs):
    elemento_esferico = Element('esferico')
    esferico = float(elemento_esferico.value)
    elemento_cilindro = Element('cilindro')
    cilindro = float(elemento_cilindro.value)
    elemento_eixo = Element('eixo')
    eixo = int(elemento_eixo.value)

    if esferico < 0:
        if esferico < -8:
            esferico = round(esferico * 0.9, 3)
            dict = {
                -7.425 : -7.5,
                -7.65 : -7.75,
                -7.875 : -8.0,
                -8.1 : -8.0,
                -8.325 : -8.25,
                -8.55 : -8.5,
                -8.775 : -8.75,
                -9.0 : -9.0,
                -9.225 : -9.25,
                -9.45 : -9.50,
                -9.675 : -9.75,
                -9.9 : -10.0
            }
            esferico = dict[esferico]

        pyscript.write('esferico_calculado', nomograma[esferico])
    
    else:
        pyscript.write('esferico_calculado', esferico)
    
    
    if cilindro == -2:
        cilindro *= 0.9

    elif cilindro < -2:
        cilindro = round(cilindro * 0.8, 2)
        diferenca = cilindro - int()

    pyscript.write('cilindro_calculado', cilindro)
    pyscript.write('eixo_calculado', eixo)
    mostrar_tabela()