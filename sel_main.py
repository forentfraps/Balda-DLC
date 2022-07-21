from solver import Balda
from selenium import webdriver
import time 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.by import By
import threading
#from data import my_cookies -> i used data.py to store my cookies from the site

class Instance:
    def __init__(self):
        """
        Creates an instance with modified balda web client in chrome, using selenium
        """
        url = r"https://logic-games.spb.ru/balda/"
        options = webdriver.ChromeOptions()
        options.add_argument("--log-level=OFF")
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome('./chromedriver.exe', options=options)
        driver.get(url)
        time.sleep(1)
        driver.delete_all_cookies()
        if my_cookies:
            for cookie in my_cookies:
                driver.add_cookie(cookie)
            driver.get(url)
        with open('manipulate.js','r') as f:
            driver.execute_script(f.read())
        self.driver = driver
        t = threading.Thread(target = self.exec_cmd)
        t.start()
        self.turn = -1
        self.size = 7
    def wait(self):
        """
        Constantly updates games status in main thread\n
        self.turn == 0 -> game is over\n
        self.turn == 1 -> its your turn\n
        self.turn == 2 -> opponents turn\n
        """
        
        xpath = r'/html/body/div[1]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/div'
        while 1:
            
            try: 
                decider = self.driver.find_element(By.XPATH, xpath).text
                if decider:
                    turn = list(filter(bool, decider.split(' ')))
                    match turn[0]:
                        case 'Ход':
                            self.turn = 2
                        case 'Игра':
                            self.turn = 0
                        case 'Ваш':
                            self.turn = 1
                    time.sleep(1)
            except NoSuchElementException:
                time.sleep(1)
    def get_banwords(self):
        """
        Gets already used words to avoid repetition
        """
        rw = []
        words = self.driver.find_element(By.XPATH, r'/html/body/div[1]/div[1]/div[4]/div[3]/div[1]/div[2]/div').text.split('\n')
        for word in words:
            rw.append(word.lower())
        return rw
    def edit_label(self,id, value):
        """
        Edits given label, check manipulate.js for ids
        """
        xpath_status = r'/html/body/div[1]/div[1]/div[4]/div[1]/div[3]/label[1]'
        self.driver.execute_script(f'''var elem = document.getElementById("{id}");
elem.innerHTML = "{value}"''')
    def reset(self, size):
        """
        Resets green fields in the web client
        """
        for i in range(7):
            if i < size:
                self.edit_label(f'string{i}', str('- ' * size)[:-1])
            else:
                self.edit_label(f'string{i}', 'null')
    def get_strings(self):
        """
        Gets letters from strings\n
        Returns 2d array self.size * self.size
        """
        field = []
        for i in range(self.size):
            elem = self.driver.find_element(By.ID, f'string{i}').text.split(' ')
            field.append(elem)
        return field
    def exec_cmd(self):
        """
        Operates in the separate thread, checks command line field (red one) for commands
        """
        while True:
            time.sleep(0.2)
            xpath_cmd = r'/html/body/div[1]/div[1]/div[4]/div[1]/div[3]/div[2]'
            cmdln = self.driver.find_element(By.XPATH, xpath_cmd)
            validlist = ['reset7', 'reset5', 'reset3', '-']
            cmd = cmdln.text
            if cmd in validlist:
                self.edit_label('commandline', '')
                match cmd:
                    case 'reset7':
                        self.reset(7)
                        self.edit_label('cheeckyoutput', 'Empty for now :-)')
                        self.size = 7
                    case 'reset5':
                        self.reset(5)
                        self.edit_label('cheeckyoutput', 'Empty for now :-)')
                        self.size = 5
                    case 'reset3':
                        self.reset(3)
                        self.edit_label('cheeckyoutput', 'Empty for now :-)')
                        self.size = 3
                    case '-':
                        self.edit_label('commandline', '')
                        #if self.turn == 1: (Doesnt work as it is supposed, may be for the better, who knows)
                        if True:
                            self.edit_label('cheeckystatus','We are fetching words, please be patient')
                            b = Balda(f_array = self.get_strings(), bans = self.get_banwords())
                            res = b.solve()
                            self.edit_label('cheeckyoutput', str(res[:10]))
                            self.edit_label('cheeckystatus','We are IDLING')
                        else:
                            self.edit_label('cheeckystatus','You tried accessing the engine when its not your turn dont do that')
        
if __name__ == '__main__':
    w = Instance().wait()
    input()
