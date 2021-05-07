from media import My_media

class Clip(My_media):
    def __init__(self,id,Type,Name,Director,Casts,Score,URL,Duration,context):
        My_media.__init__(self,id,Type,Name,Director,Casts,Score,URL,Duration)
        self.clip_context=context


    def my_editclip(self):
        self.id = input('Enter id: ')
        # self.type = input('type')
        self.name = input('Enter name: ')
        self.director = input('Enter director: ')
        self.score = input("enter score: ")
        self.url = input("enter url: ")
        self.duration = input('Enter duration: ')
        number = int(input('Enter the number of actors: '))
        print("Please press Enter after each actor. ")
        self.casts = []
        for cast in range(number):
            person = input('casts' + str(cast))
            self.casts.append(person)
        self.clip_context = input('Enter context: ')
        print('information editing was done')

