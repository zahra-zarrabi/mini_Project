
from clip import Clip
from documentary import Documentary
from serial import Serial
from cinemai import Cinemai
from data import read_from_database



def show_menu():
    print('-------MENU: \n1 Add media \n2 Edit media \n3 Delete media \n4 Media search \n5 Show all media \n6 Media download\n7 Show casts \n8 Advanced Search \n9 exit')

def my_add(data):
    id = input('Enter id: ')
    type=input('Enter type:')
    name=input('Enter name: ')
    director=input('Enter director:')
    score = input("Enter score: ")
    url = input("Enter url: ")
    duration=input('Enter duration:')
    number=input('Enter the number of actors: ')
    print("Please press Enter after each actor. ")
    casts=[]
    for cast in range(int(number)):
        person=input('casts'+str(cast))
        casts.append(person)
    for obj in data:
        if obj.id == id or obj.name == name:
            print('This information has already been added to the database.')
            break

    else:
        if type =="serial":
            section=input('Enter Section:')
            obj=Serial(id,type,name,director,str(casts), score,url,duration,section)
            data.append(obj)
            print('This information was added to the database.')

        elif type=="cinemai":
            year=input('Enter year: ')
            obj = Cinemai(id, type,name, director, str(casts),score, url,duration,year)
            data.append(obj)
            print('This information was added to the database.')

        elif type =='documentary':
            context= input('Enter context: ')
            obj = Documentary(id, type, name, director, str(casts), score,  url,duration,context)
            data.append(obj)
            print('This information was added to the database.')

        elif type == 'clip':
            context = input('Enter context: ')
            obj=Clip(id, type, name, director, str(casts), score, url, duration, context)
            data.append(obj)
            print('This information was added to the database.')
        else:
            print('invalid type ...')
    return data

def my_search(data):
    user_input=input('enter name or id to search:')
    for obj in data:
        if obj.name==user_input or obj.id==user_input or obj.type==user_input or obj.director==user_input:
            if obj.type=='serial':
                print('id:',obj.id,'type:',obj.type,'name:',obj.name,'director:',obj.director,'casts:',obj.casts, 'score:',obj.score,'url:',obj.url,'duration:',obj.duration,'section:',obj.section)

            elif obj.type=='cinemai':
                print('id:',obj.id,'type:',obj.type,'name:',obj.name,'director:',obj.director,'casts:',obj.casts, 'score:',obj.score,'url:',obj.url,'duration:',obj.duration,'year:',obj.year)

            elif obj.type=='documentary':
                print('id:',obj.id,'type:',obj.type,'name:',obj.name,'director:',obj.director,'casts:',obj.casts, 'score:',obj.score,'url:',obj.url,'duration:',obj.duration,'context:',obj.doc_context)

            elif obj.type=='clip':
                print('id:',obj.id,'type:',obj.type,'name:',obj.name,'director:',obj.director,'casts:',obj.casts, 'score:',obj.score,'url:',obj.url,'duration:',obj.duration,'context:',obj.clip_context)
            break
    else:
        print('not found')

def show_all(data):
    for obj in data:
        obj.showInfo()

def my_edit(data):
    user_input=input('enter a name or id to edit: ')
    for obj in data:
        if obj.id==user_input or obj.name==user_input:
            if obj.type=='serial':
                print(obj.id,  obj.type, obj.name, obj.director,  obj.casts,  obj.score,  obj.url,  obj.duration, obj.section)
                obj.my_editserial()
            elif obj.type=='cinemai':
                print('id:', obj.id, 'type:', obj.type, 'name:', obj.name, 'director:', obj.director, 'casts:', obj.casts, 'score:', obj.score, 'url:', obj.url, 'duration:', obj.duration, 'year:',obj.year)
                obj.my_editcinemai()
            elif obj.type=='documentary':
                print('id:', obj.id, 'type:', obj.type, 'name:', obj.name, 'director:', obj.director, 'casts:', obj.casts, 'score:', obj.score, 'url:', obj.url, 'duration:', obj.duration, 'context:',obj.doc_context)
                obj.my_editdocumentary()
            elif obj.type=='clip':
                print('id:', obj.id, 'type:', obj.type, 'name:', obj.name, 'director:', obj.director, 'casts:', obj.casts, 'score:', obj.score, 'url:', obj.url, 'duration:', obj.duration, 'context:',obj.clip_context)
                obj.my_editclip()
            return data

    else:
        print('This information is not available in the database.')

def my_remove(data):
    user_input=input('enter a id or name to remove: ')
    for obj in data:
        if obj.id==user_input or obj.name==user_input:
            obj.showInfo()
            # print('id:',obj.id,'type:',obj.type,'name:',obj.name,'director:',obj.director,'casts:',obj.casts, 'score:',obj.score,'url:',obj.url,'duration:',obj.duration)
            informations.remove(obj)
            print('Deleted.')
            return data

def my_download(data):
    user=input('Enter a name or id to download.')
    for obj in data:
        if obj.name==user or obj.id==user:
            obj.download()
    else:
        print('not existing ...')

def show_cast(data):
    user_input=input('enter a name or id: ')
    for obj in data:
        if obj.id==user_input or obj.name==user_input:
            obj.show_casts()
            break
    else:
        print('not existing...')

def advanc_search(data):
    user_input = input('time1: ')
    user_input2 = input('time2: ')
    for obj in data:
        if obj.type != 'serial':
            dura = user_input <= obj.duration<= user_input2
            if dura:
                obj.showInfo()


def my_exit(data):
    f = open('database.CSV', 'w')
    for index, obj in enumerate(data):
        if obj.type == "serial":
            f.write(obj.id + ',' + obj.type+ ',' + obj.name + ','+obj.director + ',' + str(obj.casts) + ',' + obj.score+ ',' + obj.url+ ',' + obj.duration+',' + obj.section )
        elif obj.type == "cinemai":
            f.write(obj.id + ',' + obj.type+ ',' + obj.name + ','+obj.director + ',' + str(obj.casts) + ',' + obj.score+ ',' + obj.url+ ',' + obj.duration+',' + obj.year )
        elif obj.type == "clip":
            f.write(obj.id + ',' + obj.type + ',' + obj.name + ',' + obj.director + ',' + str(obj.casts) + ',' + obj.score + ',' + obj.url + ',' + obj.duration + ',' + obj.clip_context)
        elif obj.type == "documentary":
            f.write(obj.id + ',' + obj.type + ',' + obj.name + ',' + obj.director + ',' + str(obj.casts) + ',' + obj.score + ',' + obj.url + ',' + obj.duration + ',' + obj.doc_context)
        if index !=len(data)-1:
            f.write('\n')

    f.close()
    exit()


informations = read_from_database()
while True:
    show_menu()
    choice = input('enter your choice: ')

    if choice == '1':
        informations = my_add(informations)
    elif choice =='2':
        informations=my_edit(informations)
    elif choice=='3':
        informations=my_remove(informations)
    elif choice=='4':
        my_search(informations)
    elif choice=='5':
        show_all(informations)
    elif choice == '6':
        my_download(informations)
    elif choice == '7':
        show_cast(informations)
    elif choice == '8':
        advanc_search(informations)
    elif choice=='9':
        my_exit(informations)
