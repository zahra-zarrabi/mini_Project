import pytube
from actor import Actor


class My_media():
    def __init__(self,id,Type,Name,Director,Casts,Score,URL,Duration):
        self.id=id
        self.type=Type
        self.name=Name
        self.director=Director
        self.casts=Casts
        self.score=Score
        self.url=URL
        self.duration=Duration

    def showInfo(self):
        if self.type=='serial':
            print('id:', self.id, 'type:', self.type, 'name:', self.name, 'director:', self.director, 'casts:', self.casts,'score:', self.score, 'url:', self.url, 'duration:', self.duration, 'section:', self.section)
        elif self.type == 'cinemai':
            print('id:', self.id, 'type:', self.type, 'name:', self.name, 'director:', self.director, 'casts:', self.casts,'score:', self.score, 'url:', self.url, 'duration:', self.duration,'year:', self.year)

        elif self.type == 'documentary':
            print('id:', self.id, 'type:', self.type, 'name:', self.name, 'director:', self.director, 'casts:', self.casts,'score:', self.score, 'url:', self.url, 'duration:', self.duration, 'context:', self.doc_context)

        elif self.type == 'clip':
            print('id:', self.id, 'type:', self.type, 'name:', self.name, 'director:', self.director, 'casts:', self.casts,'score:', self.score, 'url:', self.url, 'duration:', self.duration, 'context:', self.clip_context)


    def download(self):
        pytube.YouTube(self.url).streams.first().download()
        print('download done')

    def show_casts(self):
        print(self.casts)

