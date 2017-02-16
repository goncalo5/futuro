from Tkinter import *
import random
# from constantes import *


class Menu(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('futuro')

        # botoes
        self.b_resp = Button(text='sim/nao', command=self.responder)
        self.b_resp.grid(row=0, column=0)
        self.b_tarot = Button(text='Tarot', command=self.escolher_cartas)
        self.b_tarot.grid(row=1, column=0)

        # respostas
        self.resp = Label(self.root, text='')
        self.resp.grid(row=0, column=1)

        self.root.mainloop()

    def responder(self):
        self.resp['text'] = random.choice(['sim', 'nao', 'talvez'])

    def escolher_cartas(self):
        cartas = ['estupido', 'magico', 'papisa', 'imperatriz', 'imperador', 'papa',
                  'namorados', 'carro', 'justica', 'ermita', 'roda da fortuna', 'forca',
                  'enforcado', 'morte', 'temperanca', 'diabo', 'torre', 'estrela',
                  'lua', 'sol', 'julgamento', 'mundo']
        self.resp['text'] = random.choice(cartas)

if __name__ == '__main__':
    Menu()
