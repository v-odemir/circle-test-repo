#Importing Libraries
#Importing Google Text to Speech library
from gtts import gTTS

#Importing PDF reader PyPDF2
import PyPDF2

#Open file Path
pdf_File = open('name.pdf', 'rb') 

#Create PDF Reader Object
pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
count = pdf_Reader.numPages # counts number of pages in pdf
textList = []

#Extracting text data from each page of the pdf file
for i in range(count):
   try:
    page = pdf_Reader.getPage(i)    
    textList.append(page.extractText())
   except:
       pass

#Converting multiline text to single line text
textString = " ".join(textList)

print(textString)

#Set language to english (en)
language = 'en'

#Call GTTS
myAudio = gTTS(text=textString, lang=language, slow=False)

#Save as mp3 file
myAudio.save("Audio.mp3")

import requests
import json
import time
    
    
# call API
def get_baidu_poi(roi_key, city_str, baidu_ak, output):
    """
    inputs:
        roi_key: poi name
        city_str: city name
        baidu_ak: baidu web API AK
        output: file save path
    """
    now_time = time.strftime("%Y-%m-%d")
    page_num = 0
    logfile = open(output + "/" + now_time + ".log", "a+", encoding="utf-8")
    file = open(output + "/" + now_time + ".txt", "a+", encoding="utf-8")
    while True:
        try:
            URL = "http://api.map.baidu.com/place/v2/search?query=" + roi_key + \
                "&region=" + city_str + \
                "&output=json" +  \
                "&ak=" + baidu_ak + \
                "&scope=2" + \
                "&page_size=20" + \
                "&page_num=" + str(page_num)
            resp = requests.get(URL)
            res = json.loads(resp.text)
            if len(res["results"]) == 0:
                logfile.writelines(time.strftime("%Y-%m-%d-%H-%M-%S") + " " + city_str + " " + str(page_num) + "\n")
                break
            else:
                for r in res["results"]:
                    j_name = r["name"]
                    j_lat = r["location"]["lat"]
                    j_lon = r["location"]["lng"]
                    j_area = r["area"]
                    j_add = r["address"]
                    j_str = str(j_name) + "," + str(j_lon) + "," + str(j_lat) + "," + str(j_area) + "," + str(j_add) + "\n"
                    file.writelines(j_str)
            page_num += 1
            time.sleep(1)
        except:
            print("except")
            logfile.writelines(time.strftime("%Y-%m-%d-%H-%M-%S") + " " + city_str + " " + str(page_num) + "\n")
            break


#This program shows the simulation of 5 balls bouncing under gravitational acceleration.
#It is also accompanied by eleastic collission with walls of the container.
#It is fun to watch.
import pygame,time,random

pygame.init()

#setting screen size of pygame window to 800 by 600 pixels
screen=pygame.display.set_mode((800,600))
background=pygame.image.load('background-img.jpg')

#Adding title
pygame.display.set_caption('Ball Bounce Simulation')

class ball:
    ball_image=pygame.image.load('ball.png')
    g=1
    def __init__(self):
        self.velocityX=4
        self.velocityY=4
        self.X=random.randint(0,768)
        self.Y=random.randint(0,350)

    def render_ball(self):
        screen.blit(ball.ball_image, (self.X,self.Y))
    def move_ball(self):
        #changing y component of velocity due to downward acceleration
        self.velocityY+=ball.g
        #changing position based on velocity
        self.X+=self.velocityX
        self.Y+=self.velocityY
        #collission with the walls lead to change in velocity
        if self.X<0 or self.X>768:
            self.velocityX*=-1
        if self.Y<0 and self.velocityY<0:
            self.velocityY*=-1
            self.Y=0
        if self.Y>568 and self.velocityY>0:
            self.velocityY*=-1
            self.Y=568
#list of balls created as objects
Ball_List=[ball(),ball(), ball(), ball(), ball()]

#The main program loop
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    time.sleep(0.02)
    screen.blit(background, (0,0))
    for ball_item in Ball_List:
        ball_item.render_ball()
        ball_item.move_ball()
    pygame.display.update()

  # -*- coding: utf-8 -*-
import time
from calendar import isleap

# judge the leap year
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False


# returns the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28


name = input("input your name: ")
age = input("input your age: ")
localtime = time.localtime(time.time())

year = int(age)
month = year * 12 + localtime.tm_mon
day = 0

begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

# calculate the days
for y in range(begin_year, end_year):
    if (judge_leap_year(y)):
        day = day + 366
    else:
        day = day + 365

leap_year = judge_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)

day = day + localtime.tm_mday
print("%s's age is %d years or " % (name, year), end="")
print("%d months or %d days" % (month, day))  


"""
Instructions
1. Install captcha: pip install captcha
2. download fonts and update the path in code
3. run the code
"""

from io import BytesIO
from tkinter import *
from random import *
from tkinter import messagebox
import string
from captcha.image import ImageCaptcha

image = ImageCaptcha(fonts=['C:/Users/Administrator/Downloads/ChelseaMarketsr.ttf', 'C:/Users/Administrator/Downloads/DejaVuSanssr.ttf'])

random=str(randint(100000,999999))
data = image.generate(random)
assert isinstance(data, BytesIO)
image.write(random,'out.png')

def verify():
    global random
    x=t1.get("0.0",END)
    if (int(x)==int(random)):
        messagebox.showinfo("sucsess", "verified")
    else:
        messagebox.showinfo("Alert", "Not verified")
        refresh()

def refresh():
        random=str(randint(100000,999999))
        data = image.generate(random)
        assert isinstance(data, BytesIO)
        image.write(random,'out.png')
        photo = PhotoImage(file="out.png")
        l1.config(image=photo,height=100,width=200)
        l1.update()
        UpdateLabel()
    
root=Tk()
photo = PhotoImage(file="out.png")

l1=Label(root,image=photo,height=100,width=200)
t1=Text(root,height=5,width=50)
b1=Button(root,text="submit",command=verify)
b2=Button(root,text="refresh",command=refresh)

l1.pack()
t1.pack()
b1.pack()
b2.pack()
root.mainloop()

import os
import shutil
import sys
import cv2

class FrameCapture:
    '''
        Class definition to capture frames
    '''
    def __init__(self, file_path):
        '''
            initializing directory where the captured frames will be stored.
            Also truncating the directory where captured frames are stored, if exists.
        '''
        self.directory = "captured_frames"
        self.file_path = file_path
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.mkdir(self.directory)

    def capture_frames(self):
        '''
            This method captures the frames from the video file provided.
            This program makes use of openCV library
        '''
        cv2_object = cv2.VideoCapture(self.file_path)

        frame_number = 0
        frame_found = 1

        while frame_found:
            frame_found, image = cv2_object.read()
            capture = f'{self.directory}/frame{frame_number}.jpg'
            cv2.imwrite(capture, image)

            frame_number += 1

if __name__ == '__main__':
    file_path = sys.argv[1]
    fc = FrameCapture(file_path)
    fc.capture_frames()

import csv

import requests


status_dict = {"Website": "Status"}


def main():
    with open("websites.txt", "r") as fr:
        for line in fr:
            website = line.strip()
            status = requests.get(website).status_code
            status_dict[website] = "working" if status == 200 \
                else "not working"

    # print(status_dict)
    with open("website_status.csv", "w", newline="") as fw:
        csv_writers = csv.writer(fw)
        for key in status_dict.keys():
            csv_writers.writerow([key, status_dict[key]])


if __name__ == "__main__":
    main()

import click

@click.group()
@click.pass_context
def todo(ctx):
    '''Simple CLI Todo App'''
    ctx.ensure_object(dict)
    #Open todo.txt – first line contains latest ID, rest contain tasks and IDs
    with open('./todo.txt') as f:
        content = f.readlines()
    #Transfer data from todo.txt to the context
    ctx.obj['LATEST'] = int(content[:1][0])
    ctx.obj['TASKS'] = {en.split('```')[0]:en.split('```')[1][:-1] for en in content[1:]}

@todo.command()
@click.pass_context
def tasks(ctx):
    '''Display tasks'''
    if ctx.obj['TASKS']:
        click.echo('YOUR TASKS\n**********')
        #Iterate through all the tasks stored in the context
        for i, task in ctx.obj['TASKS'].items():
            click.echo('• ' + task + ' (ID: ' + i + ')')
        click.echo('')
    else:
        click.echo('No tasks yet! Use ADD to add one.\n')

@todo.command()
@click.pass_context
@click.option('-add', '--add_task', prompt='Enter task to add')
def add(ctx, add_task):
    '''Add a task'''
    if add_task:
        #Add task to list in context 
        ctx.obj['TASKS'][ctx.obj['LATEST']] = add_task
        click.echo('Added task "' + add_task + '" with ID ' + str(ctx.obj['LATEST']))
        #Open todo.txt and write current index and tasks with IDs (separated by " ``` ")
        curr_ind = [str(ctx.obj['LATEST'] + 1)] 
        tasks = [str(i) + '```' + t for (i, t) in ctx.obj['TASKS'].items()]
        with open('./todo.txt', 'w') as f:
            f.writelines(['%s\n' % en for en in curr_ind + tasks])

@todo.command()
@click.pass_context
@click.option('-fin', '--fin_taskid', prompt='Enter ID of task to finish', type=int)
def done(ctx, fin_taskid):
    '''Delete a task by ID'''
    #Find task with associated ID
    if str(fin_taskid) in ctx.obj['TASKS'].keys():
        task = ctx.obj['TASKS'][str(fin_taskid)]
        #Delete task from task list in context
        del ctx.obj['TASKS'][str(fin_taskid)]
        click.echo('Finished and removed task "' + task + '" with id ' + str(fin_taskid))
        #Open todo.txt and write current index and tasks with IDs (separated by " ``` ")
        if ctx.obj['TASKS']:
            curr_ind = [str(ctx.obj['LATEST'] + 1)] 
            tasks = [str(i) + '```' + t for (i, t) in ctx.obj['TASKS'].items()]
            with open('./todo.txt', 'w') as f:
                f.writelines(['%s\n' % en for en in curr_ind + tasks])
        else:
            #Resets ID tracker to 0 if list is empty
            with open('./todo.txt', 'w') as f:
                f.writelines([str(0) + '\n'])
    else:
        click.echo('Error: no task with id ' + str(fin_taskid))

if __name__ == '__main__':
    todo()       

