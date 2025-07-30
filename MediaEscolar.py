def media_escolar():

    print('Programa de cálculo de média escolar\n')

    nota1 = float(input('Digite sua primeira nota: '))
    nota2 = float(input('Digite sua segunda nota: '))
    nota3 = float(input('Digite sua terceira nota: '))

    media = (nota1 + nota2 + nota3)/3

    print(f'\nSua média escolar é de: {media:.2f} no entanto...')

    if media >= 7:
        print('Você está aprovado, parabéns!')
    else:
        print('Você está reprovado, que pena.')

media_escolar()