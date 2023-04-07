import random
import pandas
import smtplib
import datetime

class Mail:

    def __init__(self):
        self.friends = pandas.read_csv("birthdays.csv").iterrows()
        self.day = datetime.datetime.now().day
        self.month = datetime.datetime.now().month
        self.year = datetime.datetime.now().year
        

    
    def check_birthday(self):
        for a in self.friends:
            if a[1][3] == self.month and a[1][4] == self.day:
                self.name = a[1][0]
                self.email = a[1][1]
                if (self.year - a[1][2]) % 10 == 1:
                    self.age = f"{self.year - a[1][2]}st birthday!"
                elif (self.year - a[1][2]) % 10 == 2:
                    self.age = f"{self.year - a[1][2]}nd birthday!"
                if (self.year - a[1][2]) % 10 == 3:
                    self.age = f"{self.year - a[1][2]}rd birthday!"
                else:
                    self.age = f"{self.year - a[1][2]}th birthday!"
                return True


    def edit_msg(self):
        self.dice = random.randint(1,3)
        self.letter = open(f"letter_{self.dice}.txt").readlines()
        self.letter[0] = self.letter[0].replace("[NAME]", self.name)
        self.letter[2] = self.letter[2].replace("birthday!", self.age)
        self.letters = ""
        for a in self.letter:
            self.letters += a

    
    def send_wish(self):
        self.mail = smtplib.SMTP("smtp.gmail.com", 587)
        self.mail.starttls()
        self.mail.login("obadah2109@gmail.com", "qpcmmnrjkhrcayce")
        self.mail.sendmail("obadah2109@gmail.com", self.email, f"Subject: Birthday\n\n{self.letters}")
        self.mail.close()


