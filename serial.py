from media import My_media

class Serial(My_media):
    def __init__(self,id,Type,Name,Director,Casts,Score,URL,Duration,Section):
        My_media.__init__(self, id,Type,Name,Director,Casts,Score,URL,Duration)
        self.section = Section

    def my_editserial(self):
        self.id = input('Enter id:')
        # self.type = input('type')
        self.name = input('Enter name:')
        self.director = input('Enter director:')
        self.score = input("enter score: ")
        self.url = input("enter url: ")
        self.duration = input('Enter duration')
        number = input('Enter the number of actors: ')
        print("Please press Enter after each actor. ")
        self.casts = []
        for cast in range(int(number)):
            person = input('casts' + str(cast))
            self.casts.append(person)
        self.section = input('Enter section:')
        print('Product information editing was done')


