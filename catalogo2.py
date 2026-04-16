while True:
    nome=input('Digite o nome do filme:')
    ano=int(input('Qual ano de lançamento?'))
    nota=float(input('Digite a nota: (ex:7.8)'))
    assistiu=input('Você já assistiiu?').lower()

    print('\033[0;36mTitulo:\033[0m',nome,'-tipo:',type(nome))
    print('\033[0;33mAno:\033[0m',ano,'-tipo:',type(ano))
    print('\033[0;32mNota:\033[0m',nota,'-tipo:',type(nota))
    print('\033[0;35mAssistiu?\033[0m',assistiu,'-tipo:',type(assistiu))

    if nota>=8.0:
        print('\033[36mImperdível\033[0m')
    elif 5.0<=nota<8.0:
        print('\033[36mVale a pena\033[0m')
    else:
        print('\033[31mPode pular\033[0m')

    if assistiu=='sim':
        print('\033[32mVocé já assistiu!\033[0m')
    else:
        print('\033[31mNão assistiu ainda!\033[0m')