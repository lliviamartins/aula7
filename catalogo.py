#   titulo (texto)
#   ano_lancamento (número inteiro)
#   nota_avaliacao (número decimal, de 0.0 a 10.0)
# j a_assistido (verdadeiro ou falso)
#Título: Interestelar — tipo: <class 'str'>
   #Ano: 2014 — tipo: <class 'int'>

#Se a nota for maior ou igual a 8.0, exiba "Imperdível"
   #Se a nota for maior ou igual a 5.0 e menor que 8.0, exiba "Vale a pena"
   #Se a nota for menor que 5.0, exiba "Pode pular"

#Se for verdadeiro, exiba "Você já assistiu esse título"
#   Se for falso, exiba "Ainda está na sua lista"

nome='A Empregada'
ano=2026
nota=10.0
assistiu=True

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

if assistiu:
    print('\033[32mVocé já assistiu!\033[0m')
else:
    print('\033[31mNão assistiu ainda!\033[0m')


