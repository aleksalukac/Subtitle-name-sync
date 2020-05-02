# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:38:33 2020

@author: Aleksa
"""
from os import listdir, rename
from os.path import isfile, join

def lcs(str1, str2): #longest common subsequence
    a = len(str1)
    b = len(str2)
    string_matrix = [[0 for i in range(b+1)] for i in range(a+1)]   
    for i in range(1, a+1):
        for j in range(1, b+1):
            if i == 0 or j == 0:
                string_matrix[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                string_matrix[i][j] = 1 + string_matrix[i-1][j-1]
            else:
                string_matrix[i][j] = max(string_matrix[i-1][j], string_matrix[i][j-1])
    index = string_matrix[a][b]
    res = [""] * index
    i = a
    j = b
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            res[index-1] = str1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif string_matrix[i-1][j] > string_matrix[i][j-1]:
            i -= 1
        else:
            j -= 1

    return res

if(__name__ == "__main__"):
        
    mypath = "F:\\torenti\\House MD Season 1, 2, 3, 4, 5, 6, 7 & 8 + Extras DVDRip TSV\\Season 3\\"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    subs = []
    movies = []
    for file in onlyfiles:
        if(file[-3:] == "srt"):
            subs.append(file)
        else:
            movies.append(file)
            
    suitable = []
    for sub in subs:
        maxSubs = 0
        index = 0
        for movie in movies:
            lcs_temp = lcs(sub,movie)
            if(len(lcs_temp) > maxSubs):
                index = movies.index(movie)
                maxSubs = len(lcs_temp)
        movieName, _ = movies[index].split('.')
        rename(mypath + sub, mypath + movieName + ".srt")
        suitable.append(index)
        
    
            
            
            