class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        self.ligada = not self.ligada

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1
        else:
            print('A Televisão está deslida')

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1
        else:
            print('A Televisão está deslida')

if __name__ == '__main__':   
    televisao = Televisao()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    print('Canal: {}'.format(televisao.canal))
    televisao.aumenta_canal()
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))
