import copy
from multiprocessing import Process
import time
from crp import crypter
import os

class TiBalda(Exception):
    pass

class Balda:
    def __init__(self, variant = 5):
        with open(str ("./prompt" + str(variant) + '.txt') , 'r', encoding='utf-8') as f:
            self.field = list(map(lambda x: x.split(' '), f.read().split('\n')))
        self.letters = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
       
        if not os.path.exists('./vutf8dec.txt'):
            print('Initializing wordlist, this happens only once :-)')
            c = crypter(f'{os.getcwd()}{os.sep}crypted.txt', '82965977d6efb15b73884fccbe6bdb8d7093f1acf12c25a2b25146545b424d3b')
            c.decrypt_file()
            
        with open('vutf8dec.txt','r', encoding = 'utf-8') as f:
            self.wordlist = f.read().split('\n')
        self.rezus = []
        with open('tmp.txt', 'w') as f:
            pass
    def write(self, word):
        with open('tmp.txt', 'a') as f:
            f.write(str(word + '\n'))
    def match(self, word):
        return [word.replace('-', letter) for letter in self.letters]
    def get_directions(self, x, y):
        #return up, right, down, left
        return list(map(lambda cords: self.field[cords[1]][cords[0]] if (cords[0] >= 0 and cords[0] <= 4 and cords[1] >= 0 and cords[1] <= 4) else False,[(x, y - 1),(x + 1, y),(x, y +1),(x - 1, y)]))
    def rotate(self, strg, n):
        return strg[n:] + strg[:n]
    def subString(self, s):
        sb = []
        for i in range(len(s)):
            for l in range(i + 1,len(s) + 1):
                sb.append(s[i: l])
                    
        return list(set(filter(bool, (map(lambda a: a if a.count('-') == 1 else False, sb)))))
    def find_patterns(self, x, y, prevstr, usedcords1):
        
        match '-' in prevstr:
            case True:
                if prevstr.count('-') > 1:
                    return
                self.write(prevstr)
                c = prevstr.split('-')
                if not any(c[0] in string and c[1] in string for string in self.wordlist):
                    return
            case False:
                if not any(prevstr in string for string in self.wordlist):
                    return
        usedcords = copy.deepcopy( usedcords1)
        usedcords.append((x, y))
        dirs = self.get_directions(x, y)
        for index, dir in enumerate(dirs):
            if dir:
                match index:
                    case 0:
                        x1, y1 = x, y - 1
                    case 1:
                        x1, y1 = x + 1, y 
                    case 2:
                        x1, y1 = x, y + 1
                    case 3:
                        x1, y1 = x - 1, y 
                    case _:
                        raise TiBalda('We got an out of bounds situation in Balda.find_patterns after get_directions')
                if (x1,y1) not in usedcords:
                    value = self.field[y1][x1]                  
                    if value in self.letters or value == '-':
                        self.find_patterns(x1, y1, prevstr + value, usedcords)   
                    else:
                        raise TiBalda(f'Unexpected letter {value}, cords on prompt x = {x1} y = {y1}')
    
    def find_all(self):
        pss = []
        for x in range(5):
            for y in range(5):
                pss.append(Process(target = self.find_patterns, args = (x, y,'', [])))
        for p in pss:
            p.start()
        for p in pss:
            p.join()
            
    def match_all(self):
        with open('tmp.txt', 'r') as f:
            strs = list(set(f.read().split('\n')))
        ps = []
        for s in strs:
            ps += self.match(s)
        ps = list(set(ps) & set(self.wordlist))
        ps.sort(key=len)
        self.rezus = ps
        with open('tmp.txt', 'w') as f:
            pass
    def solve(self):
        t1 = time.time()
        print('Fetching word masks...\n')
        self.find_all()
        print('Comparing to wordlist...\n')
        self.match_all()
        print(self.rezus)
        print(f'All it took was {int(time.time() - t1)}s')
        

        
if __name__ == "__main__":
    Balda().solve()
    input()

