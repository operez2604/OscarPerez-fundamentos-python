import time 
import os

def load_file():
    filepath = input("enter the path of the file to load: ")

    file=open(filepath,'r',encoding="utf-8")
    lines = file.readlines()
    file.close()

    return lines

def set_enviroment(raw_file):
    env = []
    for line in raw_file:
        line = line.strip()
        env.append([int(c)for c in line])
    return env

def print_env(env):
    for row in env:
        for cell in row:
            if cell==1:
                print('▬',end="")
            else:
                print(' ',end="")
        print()

def count_neighbors(env, x, y):
    count = 0
    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            if i == x and j == y:
                continue
            if env [i][j] == 1:
                count += 1
    return count
                

my_files=load_file()
print(my_files)
env=set_enviroment(my_files)
print_env(env)

#Simulación
for generation in range(25):
    for i in range(1,len(env)-1):
        for j in range(1,len(env[0])-1):
            count = count_neighbors(env,i,j)
            if env[i][j]==1:
                if count <2 or count >3:
                    env [i][j] == 0
                if count == 2 or count == 3:
                    env[i][j]=1
            else:
                if count == 3:
                    env[i][j]=1
                else:
                    env[i][j]=0