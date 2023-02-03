"""
Source code By: @LcfherShell (2023)
email: LcfherShell@tutanota.com
"""
import os, sys, time
try:
    from passwordtest.main import PasswordTest, Version
except:
    from main import PasswordTest, Version


class PasswordTest_CLi():
    """docstring for CLi"""

    def __init__(self):
        super(PasswordTest_CLi, self).__init__()
        self.PasswordTest = PasswordTest(active=True)
        self.timeout = 0.2

    def Banner(self):
        print(f"""

     ==============PASSWORD TEST==============          ********                        
     Menu: 1.Generated PW | press a or 1             ****      ***                
           2.Create by key| press b or 2            ***         ***                     
           3.Test PW      | press t or 12           ***  V.{Version}  ***                     
           4.Helper       | press h or 0            ***         ****** *****            
           5.exit program | press e or control+z  ****************************          
     Info:                                        ****** ***   **********  ***         
     Each character has its own value, this       ****** *** ********   *****
     tool only predicts password security risk    ****** *** ********      *****        
     from bruteforce/cracking. The length of      ******   *   ******       ****     
     the password depends on the characters,      *******************         ****       
     used, GPU, and Program used for cracking     Create: LcfherShell          **


     X = Time required in Dictionary attack technique
     Y = Time required in bruteforce attack technique
        """)

    def Exec(self):
        self.Banner()
        session_test = 0

        def Validation(self, text, length, session_test=session_test):
            check_point = 0
            text = str(text)
            if not text:
                check_point += 1
            if len(text) < length:
                check_point += 1

            if check_point == 0:
                session_test = 1
            else:
                print(
                    f"Not a password type, input data length of at least {length}")
                pass
            return session_test

        tests = 0
        creath = 0
        autox = 0
        session = ''
        self.sessions = []
        memory, sccc = {}, ""
        while True:
            choice_command = input('Key Menu :>')
            if str(choice_command) == '1' or choice_command.lower() == 'a':

                session = f'createpw_{autox}'
                autox += 1
                self.sessions.append(session)
                memory[session] = []
                for Length_later in self.PasswordTest.choice_langth:
                    data = self.PasswordTest.generate_password(
                        Length=Length_later, options='upper')
                    output = self.PasswordTest.__time__(text=data)

                    getvaluess = self.PasswordTest.Sort_Pw(text=output)
                    goodtime = self.PasswordTest.Convert_Date(getvaluess[0])
                    badtime = self.PasswordTest.Convert_Date(getvaluess[1])
                    security = self.PasswordTest._Score_Point(data)

                    sccc = f"""
                    -----------------------------------------------------------------------
                    Password : {data} | Length: {Length_later}
                    X Time : {goodtime} |Total Test Char: {self.PasswordTest._get_long_shifts_percharacter(output[0], output[1])[0]}
                    Y Time : {badtime} |Total Test Char: {self.PasswordTest._get_long_shifts_percharacter(output[0], output[1])[1]}
                    Security Level: {security}
                    Percentate: {self.PasswordTest.Precent_Safe(security, output[0], data)}%
                    ---------------------------------END-----------------------------------
                    """
                    print(sccc)
                    memory[session].append(sccc)
                    # print(
                    #    "-----------------------------------------------------------------------")
                    # print("Password : ", data, "     | Length: ", Length_later)
                    # print("X Time : ", goodtime, " |Total Test Char:",
                    #      self.PasswordTest._get_long_shifts_percharacter(output[0], output[1])[0])
                    # print("Y Time : ", badtime, " |Total Test Char:",
                    #      self.PasswordTest._get_long_shifts_percharacter(output[0], output[1])[1])
                    # print('Security Level: ', security)
                    # print('Percentate: ', self.PasswordTest.Precent_Safe(
                    #    security, output[0], data), '%')
                    # print(
                    #    "---------------------------------END-----------------------------------")

            elif str(choice_command) == '2' or choice_command.lower() == 'b':
                data = input('Create Password :>')
                data = str(data)
                if Validation(self, data, 3):

                    session = f'createpw_{creath}'
                    creath += 1
                    self.sessions.append(session)
                    memory[session] = []
                    for Length_later in self.PasswordTest.choice_langth:
                        if len(data) < Length_later:
                            data = self.PasswordTest.password_map(
                                text=data, lths=Length_later)
                        else:
                            Length_later = len(data)
                        output = self.PasswordTest.__time__(text=data)

                        getvaluess = self.PasswordTest.Sort_Pw(text=output)
                        goodtime = self.PasswordTest.Convert_Date(
                            getvaluess[0])
                        badtime = self.PasswordTest.Convert_Date(getvaluess[1])
                        security = self.PasswordTest._Score_Point(data)
                        sccc = f"""
                    -----------------------------------------------------------------------
                    Password : {data} | Length: {Length_later}
                    X Time : {goodtime} |Total Test Char: {self.PasswordTest._get_long_shifts_percharacter(output[0], output[1])[0]}
                    Y Time : {badtime} |Total Test Char: {self.PasswordTest._get_long_shifts_percharacter(output[0], output[1])[1]}
                    Security Level: {security}
                    Percentate: {self.PasswordTest.Precent_Safe(security, output[0], data)}%
                    ---------------------------------END-----------------------------------
                    """
                        print(sccc)
                        memory[session].append(sccc)

            elif str(choice_command) == '12' or choice_command.lower() == 't':
                online = input('Choice [Online/Offline | o/f]:>')
                data = input('Password Test :>')
                data = str(data)
                if online:
                    if online.lower() == "online" or online.lower() == "onlines"\
                            or online.lower() == "o":
                        lcall = False
                    else:
                        lcall = True
                else:
                    lcall = True

                if Validation(self, data, 5):

                    session = f'testpw_{tests}'
                    tests += 1
                    self.sessions.append(session)
                    memory[session] = []

                    output = self.PasswordTest.__time__(text=data)

                    getvaluess = self.PasswordTest.Sort_Pw(text=output)
                    goodtime = self.PasswordTest.Convert_Date(getvaluess[0])
                    badtime = self.PasswordTest.Convert_Date(getvaluess[1])
                    security = self.PasswordTest._Score_Point(data)
                    if lcall == True:
                        sccc = f"""
                        status: Offline
                        -----------------------------------------------------------------------
                        Password : {data} | Length: {len(data)}
                        X Time : {goodtime} |Total Test Char: {self.PasswordTest._get_long_shifts_percharacter(output[0], output[1])[0]}
                        Y Time : {badtime} |Total Test Char: {self.PasswordTest._get_long_shifts_percharacter(output[0], output[1])[1]}
                        Security Level: {security}
                        Percentate: {self.PasswordTest.Precent_Safe(security, output[0], data)}%
                        ---------------------------------END-----------------------------------
                        """
                    else:
                        try:
                            on_output = self.PasswordTest.calcul_online(
                                int(getvaluess[0]), self.PasswordTest.sites(sitename="http://example.com"))
                            on_output = self.PasswordTest.Convert_Date(
                                round(on_output, 2))
                            status = "Online"
                        except:
                            status = "Offline (Trouble Connection)"
                            on_output = None
                        sccc = f"""
                        status:{status}
                        -----------------------------------------------------------------------
                        Password : {data} | Length: {len(data)}
                        X Time : {goodtime} |Total Test Char: {self.PasswordTest._get_long_shifts_percharacter(output[0], output[1])[0]}
                        Y Time : {badtime} |Total Test Char: {self.PasswordTest._get_long_shifts_percharacter(output[0], output[1])[1]}
                        Online Test : { on_output } 
                        Security Level: {security}
                        Percentate: {self.PasswordTest.Precent_Safe(security, output[0], data)}%
                        ---------------------------------END-----------------------------------
                        """
                    print(sccc)
                    memory[session].append(sccc)

            elif str(choice_command) == '0' or choice_command.lower() == 'h':
                print("Usage: H to show help command")
                print(
                    "            Menu: 1.Generated PW | press a or 1                    ")
                print(
                    "                  2.Create by key| press b or 2                    ")
                print(
                    "                  3.Test PW      | press t or 12                    ")
                print(
                    "                  4.Helper       | press h or 0                   ")
                print(
                    "                  5.exit program | press e or control+z            ")
            elif choice_command.lower() == 'e':
                exit()

            elif choice_command.lower() == 'clear' or choice_command.lower() == 'cls':
                os.system("cls||clear")
                self.Banner()

            elif choice_command.lower() == 'riset':
                self.timeout = 0.2
                self.sessions.clear()

            elif choice_command.lower() == 'show':
                print(self.sessions)

            elif choice_command.lower().split(" ")[0] == 'select':
                xccs = choice_command.lower().split(" ")[1]
                if self.sessions.__len__() > 0:
                    if xccs.isdigit():
                        selct = self.sessions[int(xccs)]
                    elif xccs in self.sessions:
                        selct = xccs

                    print("session:", selct)
                    for result in memory[selct]:
                        print(result)

            time.sleep(self.timeout)


def Mainprogram():
    """
    Source code By: @LcfherShell (2023)
    email: LcfherShell@tutanota.com
    """
    try:
        PasswordTest_CLi().Exec()
    except:
        pass
    print("Thanks Friends :V")
# data = outh.generate_text()
# data = outh.__time__(text='abcdfga')
# print(data)
# print(outh.Get_Days_Finish(data))


if __name__ == "__main__":
    Mainprogram()
