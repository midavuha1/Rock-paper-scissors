import PySimpleGUI as sg
import random

def result(item):
    r = random.randint(0,2)
    objects = ['камень', 'ножницы', 'бумага']
    rand_answer = objects[r]
    
    text_elem_rand = window['-rand_text-']
    text_elem_player = window['-player_text-']
    text_elem_player.update(f"Твой ответ: {item}")
    text_elem_rand.update(f"Мой ответ: {rand_answer}")

layout = [[sg.Button('Камень', enable_events=True, key='камень', font='Helvetica 16'),
        sg.Button('бумага', enable_events=True, key='бумага', font='Helvetica 16'),
        sg.Button('Ножницы', enable_events=True, key='ножницы', font='Helvetica 16')],
        [sg.Text('Выбирай!)', size=(25, 1), key='-player_text-', font='Helvetica 16'), 
         sg.Text(' ', size=(25, 1), key='-rand_text-', font='Helvetica 16')],
         [sg.Button('Exit', enable_events=True, key='Exit', font='Helvetica 16')]]

window = sg.Window('Камень, ножницы, бумага!', layout, size=(560, 360))

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break 

    if event == 'камень' or event == 'бумага' or event == 'ножницы':
        object = str(event)
        result(f'{event}')

window.close()