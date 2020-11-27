
hora = input('Entre com o horário no seguinte formato: 11 (corresponde a 11 horas) >>> ')

if hora.isdigit():
    hora = int(hora)
    if hora >= 0 and hora < 12:
        print('Bom dia !!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde !!')
    elif hora > 17 and hora <= 23:
        print('Boa noite !!')
    else:
        print('Horário incoerente !!')
else:
    print('Erro: o horário digitado não corresponde ao formato correto !!')