from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'),sg.Input(key='usuario',size=(30,1))],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*',size=(30,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#Janela
janela = sg.Window('Tela de login',layout)
#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Thenilson' and valores['senha']  == '123456':
            print('Bem Vindo ao meu site!')