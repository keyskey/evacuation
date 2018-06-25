# coding: utf-8
#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
from PIL import Image
import matplotlib.animation as animation
import re

def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

def plot(finish_time):
    # Plot all output files
    for i in range(finish_time+1):
        df = pd.read_csv('output{}.csv'.format(i))
        df_pivot = pd.pivot_table(df, 'People', 'Y','X')
        sns.heatmap(df_pivot, vmin = 0, vmax=10, cmap = 'binary', cbar=False)
        plt.title('t = {:.1f} s'.format(i/3.2))
        plt.xlabel('× 0.5 (m)')
        plt.ylabel('× 0.5 (m)')
        plt.gca().invert_yaxis()
        plt.gca().set_aspect('equal', adjustable='box')
        plt.savefig('output{}.png'.format(i))
        plt.close()

def anime():

    picList=sorted(glob.glob('*.png'), key=numericalSort)
    images = []
    # Read all images and make animation
    for i in range(len(picList)):  
        tmp = Image.open(picList[i])
        images.append(tmp)
    
    images[0].save('animation.gif', save_all=True, append_images=images[1:], optimize=False, duration=200)    # By adding loop=0, repeat endlessly

def main():
    finish_time = int(input("何タイムステップかかりましたか? :"))
    plot(finish_time)
    anime()

if __name__=="__main__":
    main()

