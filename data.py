from serial import Serial
from cinemai import Cinemai
from documentary import Documentary
from clip import Clip

def read_from_database():
    try:
        informations = []
        f = open('database.CSV', 'r')
        big_text = f.read()
        information_row = big_text.split('\n')
        for i in range(len(information_row)):
            line_text = information_row[i].split(',')

            join_line_text=','.join(line_text)
            part_line_text=join_line_text.split(',[')
            before_cast = part_line_text[0].split(',')
            part1_line_text=part_line_text[1].split('],')
            after_cast = part1_line_text[1].split(',')

            if before_cast[1]=='serial':
                obj=Serial(before_cast[0],before_cast[1],before_cast[2],before_cast[3],[part1_line_text[0][1:-1]],after_cast[0],after_cast[1],after_cast[2],after_cast[3])
            if before_cast[1] == 'cinemai':
                obj= Cinemai(before_cast[0], before_cast[1], before_cast[2], before_cast[3],[part1_line_text[0][1:-1]], after_cast[0], after_cast[1], after_cast[2],after_cast[3])
            if before_cast[1] == 'documentary':
                obj = Documentary(before_cast[0], before_cast[1], before_cast[2], before_cast[3],[part1_line_text[0][1:-1]],after_cast[0], after_cast[1], after_cast[2], after_cast[3])
            if before_cast[1] == 'clip':
                obj = Clip(before_cast[0], before_cast[1], before_cast[2], before_cast[3], [part1_line_text[0][1:-1]],after_cast[0], after_cast[1], after_cast[2], after_cast[3])

            informations.append(obj)
    except Exception as e:
        informations = []
        print(e)
    return informations