"""

Source code By: @LcfherShell (2023)

email: LcfherShell@tutanota.com

"""

import numpy as np
import random, string, psutil, datetime, statistics
import os, sys, re, itertools, time, timeit

try:

    from threading import Thread  # _thread import Thread

    lcs = "thread"

except:

    from concurrent.futures import ThreadPoolExecutor as Thread

    lcs = "concurrent"


def rename(newname):

    def decorator(f):

        f.__name__ = newname

        return f

    return decorator


class Threadser(Thread):

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):

        if lcs == "thread":

            Thread.__init__(self, group, target, name,
                            args, kwargs, daemon=daemon)

        else:

            self.target, self.args, self.kwargs = target, args, kwargs

            self.conss = True

            self.start = self.run

            try:

                del Threadser.run

            except:

                del self.run

        self._return = None

    def run(self):

        if self._target is not None:

            if "conss" in dir(self):

                with Thread() as executor:

                    future = executor.submit(
                        self.target, *self.args, **self.kwargs)

                    self._return = future.result()

            self._return = self._target(*self._args, **self._kwargs)

        if "conss" in dir(self):

            with Thread() as executor:

                future = executor.submit(
                    self.target, *self.args, **self.kwargs)

                self._return = future.result()

    def join(self):

        if "conss" in dir(self):

            pass

        else:

            Thread.join(self)

        return self._return


try:

    import httpx as requests

except:

    import requests


def notlive(lives=False, rect=int):

    if lives == True:

        return psutil.cpu_percent(rect)

    else:

        if "passcli" in os.environ.keys():

            return int(os.environ.get("passcli"))

        else:

            os.environ['passcli'] = str(round(psutil.cpu_percent(rect)))

            return int(os.environ.get("passcli"))


class PasswordTest:

    def __init__(self, active=False, sites=False):

        # create a inner class object

        super(PasswordTest, self).__init__()

        # call sup class

        # self.inner = self.Inner()

        self.active = active

        self.active_sites = sites, re.compile("(http|https)://")

        if self.__main() == False or sys.version_info < (2, 6):

            sys.stderr.write(
                "You need python 2.7 or later to run this script\n")

            exit()

        self.text = 'Hello'

        self.stringlist = {

            'upper': string.ascii_uppercase,

            'lower': string.ascii_lowercase,

            'letther': string.ascii_letters,

            'digits': string.digits,

            'speciall': string.punctuation

        }

        self.choice_langth = [0x8, 0xc, 0x1e, 0x32]  # 8, 12, 50

        self.hightsec = 0

    def __dir__(self):

        try:

            def switchase(data):

                sxx = {

                    "__str__": True,

                    "text": True,

                    "__repr__": True,

                    "sites": True,

                    "calcul_online": True,

                    "Convert_Date": True,

                    "generate_password": True,

                    "__time__": True,

                    "Sort_Pw": True,

                    "_Score_Point": True,

                    "Precent_Safe": True,

                    "_get_long_shifts_percharacter": True,

                    "password_map": True

                }

                return sxx.get(data, False)

            _x = dir(self.__class__)

            for x in _x:

                if switchase(x) == True:

                    yield x

        except:
            return ['text', '__str__', '__repr__', 'sites', 'calcul_online', 'Convert_Date', 'generate_password',
                    '__time__', 'Sort_Pw', '_Score_Point', 'Precent_Safe', '_get_long_shifts_percharacter', 'password_map']

    def __str__(self) -> str:

        pass

    def __repr__(self) -> str:

        return self.text

    def sites(self, sitename="http://example.com", proxy="default", **kwargs):

        security_level, headers = [0, "passwordtest/0.0.1"]

        if kwargs.__len__() != 0:

            kwarg_keys = kwargs.keys()

            if "useragent" in kwarg_keys or "header" in kwarg_keys or \
                    "useragents" in kwarg_keys or "headers" in kwarg_keys:

                headers = kwargs.get("useragent") or kwargs.get("useragents") or \
                    kwargs.get("header") or kwargs.get("headers")

            if "security" in kwarg_keys:

                if isinstance(kwargs.get("security"), int) or isinstance(kwargs.get("security"), str):

                    security_level = int(kwargs.get("security"))

                else:

                    TypeError("Str or Int only")

        if sitename and bool(self.active_sites[1].search(sitename)) == True or sitename and \
                bool(self.active_sites[1].search(sitename.split("//")[0])) == True:

            chunck, rowdata, start, endstart = [0, 0, 0, 0]

            try:

                with requests.Client() as client:

                    start = time.perf_counter()

                    client.get(sitename)

                    endstart = time.perf_counter()

            except:

                start = time.perf_counter()

                with requests.get(sitename) as r:

                    endstart = time.perf_counter()

            return (start, endstart)

        return (0, 0)

    def calcul_online(self, y, x):

        checkpoint = []

        if self.active_sites[0] == False:

            Exception("")

        if isinstance(x, tuple) or isinstance(x, list):

            if x.__len__() > 2:

                return int(statistics.median(x) * y)

            endstart, start = x

        machst = ((endstart - start)/1.3)

        checkpoint.append(machst)

        if machst < 1.3:

            machst = machst + ((endstart/1.3))

            checkpoint.append(machst)

        if machst > 10:

            machst = machst % 2

            checkpoint.append(machst)

        if machst <= 0:

            machst = statistics.median_high(checkpoint)

        result = machst*y

        if result <= y:

            resultx = round((machst % 60)+result)*1.6

            if resultx <= y:

                # print(1) closed session 1

                resultx = round((machst*notlive(False, 2)+y)/.2)/6

            if resultx <= y:
                # print(1, 33)
                resultx = resultx*1.45

            if resultx <= y:
                # print(2, 33)
                resultx = resultx*resultx

            return resultx

        # print(3)# closed session 3
        if round(result, 2)/1.8 <= y:
            # print(3.1)
            result = result*(result/6)

        return round(result, 2)/1.8

    def generate_password(self, text='', Length=0, options=None):

        self.text = text

        self.textlist = self.stringlist['lower']+self.stringlist['digits']

        if not self.text:

            self.textlist = self.textlist+self.stringlist['speciall']

        if self.text in self.stringlist['speciall']:

            self.textlist = self.textlist+self.stringlist['speciall']

        if options == 'upper':

            self.textlist = self.textlist+self.stringlist['upper']

        try:

            if int(Length) > 0x4:

                Lengths = Length

            elif Lengths < 1:

                raise Exception("Sorry, no numbers below zero")

            else:

                raise TypeError("Only integers are allowed")

        except:

            Length = self.choice_langth[:2]

            Lengths = int((random.choice(Length)/2)+0x4)

        return ''.join(random.choice(self.textlist) for _ in range(Lengths))

    def password_map(self, text, lths=False):

        self.text = str(text)

        self.second_text = [char for char in self.text.upper()]

        self.Length = self.choice_langth[0x0]  # 8bit

        if type(lths) == int:

            if lths > 7:

                self.Length = lths

        # =================================================

        get_Length_fisrt = len(self.second_text)

        get_Length_fisrt = int(get_Length_fisrt)

        self.Lengths = self.Length-get_Length_fisrt

        if self.text in self.stringlist['speciall']:

            maps_text = self.text

            self.two_text = self.generate_password(
                text=maps_text, Length=self.Lengths)

        else:

            self.two_text = self.generate_password(Length=self.Lengths)

        self.two_text = self.two_text[-self.Lengths:]

        for data in self.two_text:

            self.second_text.append(data)

        reall_dat = random.sample(self.second_text, len(self.second_text))

        return ''.join(data for data in reall_dat)

    def __time__(self, text):

        self.text = text

        self.medium_chuck = 0

        self.specll_chuck = 0

        self.smail_chuck = 0.12

        if len(text) > self.choice_langth[0x0] or len(text) == self.choice_langth[0x0]:

            self.smail_chuck = 0.25

        self.class_text = self.Text_Get_Position(text=text)

        if self.class_text[0][0] > 0x0 or self.class_text[0][1] > 0x5:

            self.medium_chuck += 6

        if self.class_text[0][1] > 0x0 or self.class_text[0][1] > 0x5:

            self.medium_chuck += 4

        if self.class_text[0][2] > 0x1 or self.class_text[0][2] > 0x5:

            self.medium_chuck += 24

        if self.class_text[0][3] > 0x1 or self.class_text[0][3] > 0x5:

            self.medium_chuck += 145

        def Get_By_Time(self, text):

            self.sums_up = 0

            self.sums_low = 0

            self.sums_digit = 0

            self.sums_special = 0

            numb = 0

            for character in text:

                if character.islower() or character in self.stringlist['lower']:

                    if numb > 5:

                        self.sums_low += len(text)+4*numb

                    else:

                        self.sums_low += 4*numb

                if character.isupper() or character in self.stringlist['upper']:

                    if numb > 5:

                        self.sums_up += len(text)+25*numb

                    else:

                        self.sums_up += 25*numb

                if character.isdigit() or character in self.stringlist['digits']:

                    if numb > 5:

                        self.sums_digit += len(text)+45*numb

                    else:

                        self.sums_digit += 45*numb

                if character in self.stringlist['speciall']:

                    if numb > 4:

                        self.sums_special += len(text)+120*numb

                    else:

                        self.sums_special += 120*numb

                numb += 1

            total = self.sums_low+self.sums_up+self.sums_digit+self.sums_special

            return total/2

        def textsx_(self):

            textsx_buff = []

            y = 2

            x = 5

            try:

                for data in self.class_text[1][0]:

                    if data > 0:

                        data **= data

                    y += 1

                textsx_buff.append(y)

                y = data**2/y

                for data in self.class_text[1][2]:

                    if data > 1:

                        data **= data

                    x += 2

                textsx_buff.append(x)

                x = data**4/x

            except:

                pass

            if psutil.cpu_percent(2) > 12:

                chunck = int(psutil.cpu_percent(2)/2)

            else:

                chunck = int(psutil.cpu_percent(2))

            if chunck < 1:
                chunck = random.choice([1, 1.2, 1.5])

            fake_chunck = int(4*((60/chunck)+y+x))

            if len(str(fake_chunck)) < 3:

                x = 0

                y = 0

                for data in range(len(textsx_buff)):

                    x += textsx_buff[data]+textsx_buff[data]

                    y += textsx_buff[data]+textsx_buff[0]

                data = 2+(x*y**2)

            else:

                data = int(fake_chunck)

            return data/self.medium_chuck

        def digits_(self):

            digits_buff = 0

            for data in self.class_text[1][2]:

                if data > 1:

                    digits_buff += data*(0x3c+(self.choice_langth[0x0]**.12))

            return digits_buff

        def specials_(self):

            # special char

            speciall_buff = 0

            for data in self.class_text[1][3]:

                if data > 2:

                    speciall_buff += data * \
                        ((0x3c/2)+(self.choice_langth[0x0]**7))

            return speciall_buff

        # if not text:

        #  return (0, 0)

        # if len(text)==8:

         # self.times = 45

        # elif 8*.25 = 2

        specials_sums = Get_By_Time(self, text=text)

        chuck_times_x = self.medium_chuck

        chuck_times_y = self.smail_chuck

        text_chunck_time_ = textsx_(self)

        if isinstance(text_chunck_time_, float):

            if str(text_chunck_time_).split(".")[1].__len__() > 5 == True:

                text_chunck_time_ = float(round(text_chunck_time_))

        text_chunck_time_ = str(text_chunck_time_)

        text_chunck_time_ = str(text_chunck_time_[0:8])

        text_chunck_time_ = text_chunck_time_.replace('.', '')

        digits_chunck_time_ = digits_(self)

        specials_chunck_time_ = specials_(self)

        # if not text.islower() and not text.isupper() and  self.class_text[0][3]>3:

        # specll_chuck = chuck_times_y*len(str(text))+((text_chunck_time_+digits_chunck_time_)*2.2)+(specials_chunck_time_+len(str(text)))/2

        # elif text.islower() and not text.isupper() or text.isupper() and not text.islower():

        #    print(1)

        #    specll_chuck = chuck_times_y*len(str(text))+(self.medium_chuck+len(str(text))**8)

        # else:

        #    print(2)

        #    specll_chuck = chuck_times_y*len(str(text))+((text_chunck_time_+digits_chunck_time_)*1.3)+(specials_chunck_time_+len(str(text)))/2

        #

        # Ambil list, extract, lalu cocokan sesuai book > convert ke hex dan juamlahkan semua listnya Mean

        if text.islower() == True and not text.isupper() and self.class_text[0][3] < 1 \
                or text.isupper() == True and not text.islower() and self.class_text[0][3] < 1:

            if len(text) < 7:

                self.specll_chuck = chuck_times_y * \
                    len(str(text))+(chuck_times_x+(int(text_chunck_time_) %
                                                   4)+len(str(text))**2)-chuck_times_y/4

                if len(text) == 1:

                    self.specll_chuck = int(self.specll_chuck)-len(text)+2

                else:

                    self.specll_chuck = self.mp__operations(
                        i=text[-1:])+int(self.specll_chuck)-len(text)

            else:

                self.specll_chuck = chuck_times_y * \
                    len(str(text))+(chuck_times_x+(int(text_chunck_time_) %
                                                   2)+len(str(text))**2)-chuck_times_y/4

                self.specll_chuck = int(self.specll_chuck)-len(text)

        elif text.isdigit() == True:

            self.specll_chuck = chuck_times_y**len(str(text))+(self.medium_chuck+(
                self.per_to_per(text[-1:])*len(str(text))))-chuck_times_x/4

            self.specll_chuck = self.specll_chuck - \
                (self.per_to_per(text[0:1])/4)

            if len(text) < 5:

                self.specll_chuck = self.specll_chuck-(self.specll_chuck/3.5)

                self.specll_chuck = self.specll_chuck - \
                    (self.per_to_per(text[-1:])*2)

            else:

                self.specll_chuck = (
                    self.specll_chuck*(len(text)/3)+chuck_times_x)-(self.specll_chuck-(len(text)/2))

                self.specll_chuck = int(self.specll_chuck)*len(text)

        else:

            self.specll_chuck = len(str(text))**chuck_times_y+(
                chuck_times_x+chuck_times_y+digits_chunck_time_+specials_chunck_time_)/2

            if specials_chunck_time_ > 1 or specials_chunck_time_ == 1:

                self.specll_chuck = self.specll_chuck

            else:

                self.specll_chuck = self.specll_chuck + \
                    (self.smail_chuck*len(text))

        if len(text) > 9:

            self.specll_chuck = self.specll_chuck+specials_sums+len(text)

        # print(self.per_to_per(text[-1:]))

        return int(self.specll_chuck*2), int(Get_By_Time(self, text=text))

    def per_to_per(self, word):

        char = self.stringlist['lower']+self.stringlist['digits']

        output = ''

        for data in char:

            if word == data:

                output = self.mp__operations(i=word)

                break

        return output

    def mp__operations(self, i):

        switcher = {

            '0': 0xc,  # 12

            '1': 0xd,  # 13

            '2': 0xe,  # 14

            '3': 0xf,  # 15

            '4': 0x10,  # 16

            '5': 0x11,  # 17

            '6': 0x12,  # 18

            '7': 0x13,  # 19

            '8': 0x14,  # 20

            '9': 0x15,  # 21

            'a': 0x6,  # 2, 1

            'b': 0x7,

            'c': 0x8,

            'd': 0x9,

            'e': 0x2,

            'f': 0x7,  # 2, 1

            'g': 0x9,

            'h': 0x8,

            'i': 0x9,

            'j': 0x7,

            'A': 0x12,

            'B': 0xc,  # 18

            'C': 0x15,  # 19

            'D': 0x14,  # 20

            'E': 0x15,  # 18

            'F': 0x13,  # 19

            'G': 0x14,  # 20

        }

        def argsp(s):

            map_x = int(ord(s)/2)

            if map_x > 56:

                return int(ord(i)/3)

            return map_x

        # last version or switcher.get(i, 0x1e)
        return switcher.get(i, argsp(i))

    def Convert_Date(self, seconds):

        return str(datetime.timedelta(seconds=seconds))

    def _Score_Point(self, password):

        password_scores = {0: 'not password type',
                           1: 'Horrible', 2: 'Weak', 3: 'Medium', 4: 'Strong'}

        password_strength = dict.fromkeys(
            ['has_upper', 'has_lower', 'has_num', 'has_speciall'], False)

        if re.search(r'[A-Z]', password):

            password_strength['has_upper'] = True

        if re.search(r'[a-z]', password):

            password_strength['has_lower'] = True

        if re.search(r'[0-9]', password):

            password_strength['has_num'] = True

        if re.compile('[@_!#$%^&*()<>?/\|}{~:\'"]').search(password):

            password_strength['has_speciall'] = True

        score = len([b for b in password_strength.values() if b])

        try:

            if len(password) < 8:

                score -= 1

        except:

            pass

        return password_scores[score]

    def Precent_Safe(self, optionsz=None, optionsy=None, optionsx=None):

        score = 0

        if optionsz == 'Horrible' or optionsz == 'not password type':  # score point

            score += 0

        elif optionsz == 'Weak':

            score += 2

        elif optionsz == 'Medium':

            score += 4

        else:

            score += 5

        if optionsy < 0x960:  # time by time

            score += 3

        else:

            if optionsy > 0x36ce:

                score += 6

            else:

                score += 5

        if len(optionsx) > 7:

            score += 4

        if re.compile('[^0-9a-zA-Z]+').search(optionsx):  # check char

            score += 10

        else:

            score += 6

        score = score*4

        return score

    def Text_Get_Position(self, text):

        self.sums_up = 0

        self.postion_up = []

        self.sums_low = 0

        self.postion_low = []

        self.sums_digit = 0

        self.postion_digit = []

        self.sums_special = 0

        self.postion_sepcial = []

        ###

        numb = 0

        ##

        for character in text:

            if character.islower() or character in self.stringlist['lower']:

                self.postion_low.append(numb)

                self.sums_low += 1

            if character.isupper() or character in self.stringlist['upper']:

                self.postion_up.append(numb)

                self.sums_up += 1

            if character.isdigit() or character in self.stringlist['digits']:

                self.postion_digit.append(numb)

                self.sums_digit += 1

            if character in self.stringlist['speciall']:

                self.postion_sepcial.append(numb)

                self.sums_special += 1

            numb += 1

        return ((self.sums_up, self.sums_low, self.sums_digit, self.sums_special),

                (self.postion_low, self.postion_up, self.postion_digit, self.postion_sepcial))

    def _get_long_shifts_percharacter(self, x, y):

        x = int(x)

        y = int(y)

        tumple = [x, y]

        means = statistics.mean(tumple)

        sortword = self.Sort_Pw(tumple)

        sortword = sortword[1]/2

        if means > sortword and sortword < means:

            maximum = (means*30)/2

            minimum = sortword

            # print(1, sortword)

        else:

            quests = self.Sort_Pw([means, sortword])

            maximum = quests[1]

            minimum = quests[0]

            # print(2)

        if minimum > 0x4b0:

            minimum_X = minimum/364

            minimum_X = minimum_X*.25

            if self.text.isdigit() == True:

                # print(0.1)

                minimum = minimum/1.2

            else:

                # print(0.2)

                minimum = minimum_X

            # print(1.1)

        if maximum > 0x2b373d:

            maximum = maximum+(12*364)

            # print(1.2)

        return int(minimum), int(maximum)

    def Sort_Pw(self, text):

        maximum = max(text)

        minimum = min(text)

        return minimum, maximum

    def __main(self):

        if sys.version_info < (2, 6):

            self.active = False

            return self.active

        return self.active

        # if options == 'binary-to-text':

        #  "".join([chr(int(binary, 2)) for binary in text.split(" ")]) #binary 2 text

        # elif options == 'text-to-binary':

        #  " ".join(f"{ord(i):08b}" for i in text) #text 2 binary


# class_text[0][3]>3               abcdfga


# outh =  PasswordTest(active=True)

# print("===========================Password Generator===========================")

# while True:

#    data = input('Password Test:>')

#    for Length_later in outh.choice_langth:

#        data = outh.password_map(text=data, lths=Length_later)

#        output = outh.__time__(text=data)

#        print("-----------------------------------------------------------------------")

#        print("Password : ",data, "     | Length: ", Length_later)

#        print("X Time: ",outh.Convert_Date(outh.Get_By_Time(text=data)))

#        print("Y Time : ", outh.Convert_Date(output))

    # create a 1st inner class

     # class Inner:

     #

     #  def __init__(self):

     #    # create a inner class of inner class object

     #    self.innerclassofinner = self.Innerclassofinner()

     #    self.innerclassofinner.text = 'New Text'

     #  def show(self):

     #   print(self.innerclassofinner.text)

       # create a inner class of inner

     #  class Innerclassofinner:

     #     text = ''

     #     def show(self):

     #        print(self.text)

     #        self.text = 'KKK'


# create a outer class object

# i.e.Geeksforgeeks class object

# outer = Geeksforgeeks()

# outer.show()

# print()


# create a inner class object

# gfg1 = outer.inner

# gfg1.show()

# print()


# create a inner class of inner class object

# gfg2 = outer.inner.innerclassofinner

# gfg2.show()


# gfg1 = outer.inner

# gfg1.show()


# data =  input('password> ')

# ob = Solution()

# print(ob.strongPasswordChecker(data))


# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")

# nr_letters = int(input("How many letters would you like in your password?\n"))

# nr_symbols = int(input(f"How many symbols would you like?\n"))

# nr_numbers = int(input(f"How many numbers would you like?\n"))

# password_list = []

# for char in range(1, nr_letters + 1):

#  password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):

#  password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):

#  password_list += random.choice(numbers)


# random.shuffle(password_list)

# password = ""

# for char in password_list:

#  password += char

# print(f"Your password is: {password}")

class PasswordStrength(PasswordTest):

    def __dir__(self):

        try:

            def switchase(data):

                sxx = {

                    "__str__": True,

                    "__repr__": True,

                    "sites": True,

                    "calcul_online": True,

                    "generate_password": True,

                    "password_map": True,

                    "inputs": True,

                    "get_longtime": True,

                    "long_testchar": True,

                    "score": True,

                    "precent": True





                }

                return sxx.get(data, False)

            _x = dir(self.__class__)

            for x in _x:

                if switchase(x) == True:

                    yield x

        except:
            return []

    def inputs(self, text):

        predict = self.__time__(str(text))

        try:

            x = predict.sort()

        except:

            x = sorted(predict)

        self.predict = x

    @property
    def get_longtime(self):

        if isinstance(self.predict, list) or isinstance(self.predict, tuple):

            try:

                Sort_Pw = self.Sort_Pw(self.predict)

                return {"goodtime": self.Convert_Date(Sort_Pw[0]), "badtime": self.Convert_Date(Sort_Pw[1])}

            except:

                return {"goodtime": self.Convert_Date(self.predict[0]), "badtime": self.Convert_Date(self.predict[1])}

        Exception("This Not tuples or List")

    @get_longtime.setter
    def get_longtime(self):

        Exception("Cannot Edit")

    @property
    def long_testchar(self):

        try:

            return self._get_long_shifts_percharacter(**self.predict)

        except:

            try:
                return self._get_long_shifts_percharacter(*self.predict)

            except:
                return self._get_long_shifts_percharacter(self.predict[0], self.predict[1])

    @long_testchar.setter
    def long_testchar(self):

        Exception("Cannot Edit")

    def score(self, data):

        return self._Score_Point(data)

    def precent(self, security=str, score=int, text=str):

        return self.Precent_Safe(optionsz=security, optionsy=score, optionsx=text)

    def callback(self, callback, args=[], **kwargs):

        if isinstance(callback, function):

            callbackx = callback

        else:

            TypeError()

        return callbackx


Version = 1.3

__all__ = ["PasswordTest", "PasswordStrength", "Threadser", "Version"]
