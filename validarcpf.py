# validador de cpf simples em python
cpf = input('Digite um cpf: ').replace('.', '').replace('-', '')

#filtro criado caso o usuario coloque numeros sequenciais
repetido = cpf.count(cpf[0])
if repetido > 10 :
    print('CPF inválido!')
else:
    cpf_convertido = 0
    contador = 0
    multi_cpf = 0
    multi_um = 10
    cpf_convertido_dois = 0
    contador_dois = 0
    multi_cpf_dois = 0
    multi_dois = 11
# contador criado para verificar o primeiro digito do cpf e auxiliar na verificação do segundo digito
    for i in cpf:
        if contador < 9:
            cpf_convertido = int(i)
            multi = cpf_convertido * multi_um
            multi_cpf += cpf_convertido * multi_um
            contador += 1
            multi_um -= 1
    digito_um = (multi_cpf * 10) % 11
# filtro criado caso o resto do calculo fique acima de 9
    if digito_um > 9:
        digito_um = 0
# contador para verificar o segundo digito
    for x in cpf:
        if contador_dois < 10:
            cpf_convertido_dois = int(x)
            multi_cpf_dois += cpf_convertido_dois * multi_dois
            contador_dois += 1
            multi_dois -= 1
    digito_dois = (multi_cpf_dois * 10) % 11
#filtro criado caso o resto do calculo fique acima de 9
    if digito_dois > 9:
        digito_dois = 0
# verificação dos numeros digitados pelo usuario, caso sejam iguais conforme o calculo, o cpf esta valido
    if digito_um == int(cpf[9]) and digito_dois == int(cpf[10]):
        print('CPF válido!')
    else:
        print('CPF inválido!')