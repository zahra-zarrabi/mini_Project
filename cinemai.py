from media import My_media

class Cinemai(My_media):
    def __init__(self,id,Type,Name,Director,Casts,Score,URL,Duration,y):
        My_media.__init__(self, id,Type,Name,Director,Casts,Score,URL,Duration)
        self.year = y


    def my_editcinemai(self):
        self.id = int(input('Enter id:'))
        # self.type = input('type')
        self.name = input('Enter name: ')
        self.director = input('Enter director:')
        self.score = input("enter score: ")
        self.url = input("enter url: ")
        self.duration = input('Enter duration: ')
        number = int(input('Enter the number of actors:'))
        print("enter casts after enter: ")
        self.casts = []
        for cast in range(number):
            person = input('casts' + str(cast))
            self.casts.append(person)
        self.year = input('Enter year:')
        print('information editing was done.')