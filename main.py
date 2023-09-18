from tkinter import *

root = Tk()
root.title('Calculadora')
root.geometry('340x410')
root.maxsize(340,410)
root.minsize(340,410)
root.configure(background='#181818')

op = ''
num1 = ''
num2 = ''

divisao = False
multiplicacao = False
adicao = False
subtracao = False
resultado = False

def btnFormatado(root,txt,comando=''):
    btn = Button(root,
                text=txt,
                command=comando,
                fg='#FFFFFF',
                activebackground='#3C3C3C',
                bg='#323232',
                width = 8,
                height = 2,
                activeforeground='#FFFFFF',
                relief=FLAT,
                font=('Segoe UI',12),
                borderwidth=1,
                )
    return btn

def operador(op=''):
    global num1, num2
    global adicao
    global multiplicacao
    global divisao
    global subtracao

    if num1 == '':
        num1 = e.get().replace(',','.')
        num1 = float(num1)
    else:
        num2 = e.get().replace(',','.')
        num2 = float(num2)
        if op == '+':
            print(f'adição executada: {num1} + {num2} = ',end='')
            num1 = float(num1)+float(num2)
            adicao = True
            print(f'{num1} - {adicao}')

        if op == '-':
            print(f'subtração executada: {num1} - {num2} = ',end='')
            num1 = float(num1)-float(num2)
            subtracao = True
            print(f'{num1} - {subtracao}')

        if op == '/':
            print(f'divisão executada: {num1} / {num2} = ',end='')
            num1 = float(num1)/float(num2)
            divisao = True
            print(f'{num1} - {divisao}')

        if op == 'x':
            print(f'multiplicacao executada: {num1} * {num2} = ',end='')
            num1 = float(num1)*float(num2)
            multiplicacao = True
            print(f'{num1} - {multiplicacao}')

        if op =='%':
            num1 = num1 + (num2/100)
            return num2
    btnClear()
    return num1

def btnDivisao():
    btnEquals()
    global op 
    op = '/'
    operador(op)
    print(num1)

def btnMultiplicacao():
    btnEquals()
    global op 
    op = 'x'
    operador(op)
    print(num1)

def btnAdicao():
    btnEquals()
    global op 
    op = '+'
    operador(op)
    print(num1)

def btnSubtracao():
    btnEquals()
    global op 
    op = '-'
    operador(op)
    print(num1)

def btnPorcentagem():
    operador(op)
    print(num1)

def btnQuadrado():
    num = e.get()
    btnClear()
    e.insert(0, float(num)*float(num))

def btnEquals():
    global num1
    valor = str(operador(op)).replace('.',',')
    e.insert(0, valor)
    print(valor)
    num1 = ''

def btnClear():
    e.delete(0, END)

def btnClearAll():
    global num1
    global num2
    num1 = num2 = ''
    btnClear()

def clique(num):
    if resultado:
        btnClear()
    e.insert(END, num)

# --------- JANELA
titulo = Label(root, 
                 text='Padrão', 
                 fg='#FFFFFF', 
                 bg='#181818', 
                 font=('Segoe UI', 15, 'bold')
               ).place(x=5,y=10)

e = Entry(root, 
            width=14, 
            bd=5, 
            relief=FLAT, 
            fg='#FFFFFF', 
            bg='#181818', 
            font=('Segoe UI', 30, 'bold'), 
            justify=RIGHT)
e.place(x = 326, y = 70, anchor=E)


# --------- OPERADORES
porcento = btnFormatado(root,'%',btnPorcentagem)
porcento.place(x=6,y=110)

quadrado = btnFormatado(root,'x²',btnQuadrado) 
quadrado.place(x=89,y=110)

raiz = btnFormatado(root,'C',btnClearAll)
raiz.place(x=172,y=110)

limpar = btnFormatado(root,'CE',btnClear)
limpar.place(x=255,y=110)

divide = btnFormatado(root,'÷',btnDivisao)
divide.place(x=255,y=169)

multiplica = btnFormatado(root,'×',btnMultiplicacao)
multiplica.place(x=255,y=228)

subtrai = btnFormatado(root,'-',btnSubtracao)
subtrai.place(x=255,y=287)

igual = btnFormatado(root,'=',btnEquals)
igual.place(x=255,y=346)

soma = btnFormatado(root,'+',btnAdicao)
soma.place(x=172,y=346)


# --------- primeira fileira
sete = btnFormatado(root,'7',lambda:clique(7))
sete.place(x=6,y=169)

oito = btnFormatado(root,'8',lambda:clique(8))
oito.place(x=89,y=169)

nove = btnFormatado(root,'9',lambda:clique(9))
nove.place(x=172,y=169)


# --------- segunda fileira
quatro = btnFormatado(root,'4',lambda:clique(4))
quatro.place(x=6,y=228)

cinco = btnFormatado(root,'5',lambda:clique(5))
cinco.place(x=89,y=228)

seis = btnFormatado(root,'6',lambda:clique(6))
seis.place(x=172,y=228)


# --------- terceira fileira
um = btnFormatado(root,'1',lambda:clique(1))
um.place(x=6,y=287)

dois = btnFormatado(root,'2',lambda:clique(2))
dois.place(x=89,y=287)

tres = btnFormatado(root,'3',lambda:clique(3))
tres.place(x=172,y=287)


# --------- ultima fileira
ponto = btnFormatado(root,'·',lambda:clique(','))
ponto.place(x=6,y=346)

zero = btnFormatado(root,'0',lambda:clique(0))
zero.place(x=89,y=346)


root.mainloop()