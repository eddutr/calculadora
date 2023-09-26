from tkinter import *
from math import sqrt

root = Tk()
root.title('')
root.geometry('340x470')
root.maxsize(340,470)
root.minsize(340,470)
root.configure(background='#181818')

op = ''
num1 = 0
num2 = 0

def btnFormatado(txt,comando='',cor='#323232',corfg='#FFFFFF',w=8,h=2,padx=0):
    btn = Button(root,
                text=txt,
                command=comando,
                fg=corfg,
                activebackground='#3C3C3C',
                bg=cor,
                padx=padx,
                width = w,
                height = h,
                activeforeground='#FFFFFF',
                relief=FLAT,
                font=('Segoe UI',12),
                borderwidth=1,
                )
    return btn

def operador(op):
    global num1, num2
    if num1 == 0:
        num1 = float(e.get())
    else:
        num2 = float(e.get())
        if op == '+':
            num1 += num2
        if op == '-':
            num1 -= num2
        if op == 'x':
            num1 *= num2
        if op == '/':
            if num2 == 0:
                num1 = 'ERROR'
            else:
                num1 /= num2      
    btnClear()
    return num1

def btnDivisao():
    btnEquals()
    global op 
    op = '/'
    operador(op)
    showResult()

def btnMultiplicacao():
    btnEquals()
    global op 
    op = 'x'
    operador(op)
    showResult()

def btnAdicao():
    btnEquals()
    global op 
    op = '+'
    operador(op)
    showResult()

def btnSubtracao():
    btnEquals()
    global op 
    op = '-'
    operador(op)
    showResult()

def btnPorcentagem():
    global num2, num1
    if num1 == 0:
        num = float(e.get())
        num = num/100
    else:
        num2 = float(e.get())
        print('pegou num2')
        num = num1/100*num2
    btnClear()
    e.insert(0, num)

def btnTroca():
    num = float(e.get())
    num = num*(-1)
    btnClear()
    e.insert(0, num)

def btnFracional():
    num = float(e.get())
    if num == 0:
        num = 'ERROR'
    else:
        num = 1/num
    btnClear()
    e.insert(0, num)

def btnQuadrado():
    num = float(e.get())
    btnClear()
    e.insert(0, num*num)

def raizQuadrada():
    num = float(e.get())
    if num < 0:
        num = 'ERROR'
    else:
        num = sqrt(num)
    btnClear()
    e.insert(0, num)

def btnEquals():
    global num1
    valor = str(operador(op))
    e.insert(0, valor)
    showResult()
    num1 = 0

def btnClear(): 
    e.delete(0, END)

def btnClearAll():
    global num1, num2
    num1 = num2 = 0
    showResult()
    btnClear()

def clique(num):
    e.insert(END, num)

def showResult():
    global num1
    s.delete(0, END)
    s.insert(0, num1)

# --------- JANELA
titulo = Label(root, 
                 text='Calculadora', 
                 fg='#FFFFFF', 
                 bg='#181818', 
                 font=('Segoe UI', 15, 'bold')
               ).place(x=5,y=10)

s = Entry(root,
          width=7,
          bd=5,
          relief=FLAT, 
          fg='#3D3D3D', 
          bg='#181818', 
          font=('Segoe UI', 10, 'bold'), 
          justify=RIGHT)
s.place(x=326, y=31, anchor=E)

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

porcento = btnFormatado('%',btnPorcentagem)
porcento.place(x=6,y=110)

sinal = btnFormatado(r'+/-',btnTroca) 
sinal.place(x=89,y=110)

limpar = btnFormatado('CE',btnClear)
limpar.place(x=172,y=110)

reset = btnFormatado('C',btnClearAll)
reset.place(x=255,y=110)

# ---------

decimos = btnFormatado('¹/x', btnFracional)
decimos.place(x=6,y=169)

quadrado = btnFormatado('x²',btnQuadrado) 
quadrado.place(x=89,y=169)

raiz = btnFormatado('²√', raizQuadrada)
raiz.place(x=172,y=169)

divide = btnFormatado('÷',btnDivisao)
divide.place(x=255,y=169)

# ---------

multiplica = btnFormatado('×',btnMultiplicacao)
multiplica.place(x=255,y=228)

subtrai = btnFormatado('-',btnSubtracao)
subtrai.place(x=255,y=287)

soma = btnFormatado('+',btnAdicao)
soma.place(x=255,y=346)

igual = btnFormatado('=',btnEquals,'#98E1BE','#181818')
igual.place(x=255,y=405)


# --------- primeira fileira
sete = btnFormatado('7',lambda:clique(7),'#3D3D3D')
sete.place(x=6,y=228)

oito = btnFormatado('8',lambda:clique(8),'#3D3D3D')
oito.place(x=89,y=228)

nove = btnFormatado('9',lambda:clique(9),'#3D3D3D')
nove.place(x=172,y=228)


# --------- segunda fileira
quatro = btnFormatado('4',lambda:clique(4),'#3D3D3D')
quatro.place(x=6,y=287)

cinco = btnFormatado('5',lambda:clique(5),'#3D3D3D')
cinco.place(x=89,y=287)

seis = btnFormatado('6',lambda:clique(6),'#3D3D3D')
seis.place(x=172,y=287)


# --------- terceira fileira
um = btnFormatado('1',lambda:clique(1),'#3D3D3D')
um.place(x=6,y=346)

dois = btnFormatado('2',lambda:clique(2),'#3D3D3D')
dois.place(x=89,y=346)

tres = btnFormatado('3',lambda:clique(3),'#3D3D3D')
tres.place(x=172,y=346)


# --------- ultima fileira
zero = btnFormatado('0',lambda:clique(0),'#3D3D3D',w=17,h=2,padx=1)
zero.place(x=6,y=405)

ponto = btnFormatado(',',lambda:clique('.'),'#3D3D3D')
ponto.place(x=172,y=405)


root.mainloop()