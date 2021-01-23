from tkinter import *
import shutil         
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb
import re
from FaceRecognize import FaceRecognize
from FilesHandle import FilesHandle


datasetDir = "C:/Users/NF/Documents/project1/DatasetMangment/dataset"
imagesFilePath = 'C:/Users/NF/Documents/project1/DatasetMangment/jpg/'
currentWorkingPath = datasetDir
file = FilesHandle()
faceHandle = FaceRecognize()
imagesCount = file.imagesCount(currentWorkingPath)

def open_window():
    read=easygui.fileopenbox()
    return read

def __main__():
    sortlist = sorted(os.listdir(currentWorkingPath))   
    print(sortlist)    
    i=0
    print("number of items inside folder = " , len(sortlist))
    while(i<len(sortlist)):
        deleteSingleImages(sortlist[i])
        deleteEmptyFolders(sortlist[i])
        i+=1

def deleteSingleImages(folderName):
    folderDir = os.path.join(currentWorkingPath,folderName)
    sortlist = sorted(os.listdir(folderDir))
    n = 1
    print('[*] folder name = {} '.format(folderName))
    if len(sortlist) == 1:
        for i in sortlist:
            fileDir = os.path.join(folderDir , i)
            file.delete_file(fileDir)
            n+=1
    

def deleteEmptyFolders(folderName):
    folderDir = os.path.join(currentWorkingPath,folderName)
    sortlist = file.listFiles(folderDir)
    if len(sortlist) == 0:
        file.delete_folder(folderDir)
    else:
        print('folder not empty ')


def deleteImagesWithMultipleFaces(imgPath):
    face_locations = faceHandle.faceDetect(imgPath)
    faceCount = len(face_locations)
    if faceCount > 1 or faceCount == 0: 
        file.delete_file(imgPath)
        print('image path : {} was removed succesfully !'.format(imgPath))


def create_folder_for_images(): 
    #persons = 0
    
    sortlist = sorted(os.listdir(currentWorkingPath))
    perons = []
    for n in sortlist: 
        nameOfPerson = n
        nameOfPerson = ''.join([i for i in nameOfPerson if not i.isdigit()])
        nameOfPerson = os.path.splitext(nameOfPerson)[0]
        nameOfPerson = nameOfPerson.replace('!','')
        nameOfPerson = str(re.findall('\d+', nameOfPerson))
        nameOfPerson = nameOfPerson.replace('[','').replace(']','').replace("'",'').replace(',','').replace(' ','')
        perons.append(nameOfPerson)
        #print(nameOfPerson)
    foldersNames = [] 
    [foldersNames.append(x) for x in perons if x not in foldersNames] 
    
    #Create Folders
    for i in foldersNames:
        folderPath = os.path.join(currentWorkingPath,i)
        print(i)
        file.create_folder(folderPath)

    

def image_classification():
    print('starting..')
    folders = next(os.walk(currentWorkingPath))[1]
    files = next(os.walk(currentWorkingPath))[2]
   
    for i in folders: 
        for n in files: 
            #print('i = {} \n n = {}'.format(i,n))
            if i in n:
                oldPath = os.path.join(currentWorkingPath,n)
                newPath = os.path.join(currentWorkingPath,i,n)
                os.rename(oldPath,newPath)
    

#__main__()

#image_classification()
#create_folder_for_images()
def removeWhiteSpacesFromFolderName():
    lists = file.listFiles(currentWorkingPath)
    for i in lists:
        file.removeWhiteSpaces(currentWorkingPath,i)


def removeWhiteSpaceFromFilesNames():
    listFolders = file.listFolders(currentWorkingPath)
    for n in listFolders:
        folderDir = os.path.join(currentWorkingPath,n)
        filesList = file.listFiles(folderDir)
        for i in filesList:
            newName = i.replace(' ','_')
            newNamePath = os.path.join(folderDir,newName)
            oldNmae = os.path.join(folderDir,i)
            os.rename(oldNmae,newNamePath)

def removeMultipleFaces():
    listFolders = file.listFolders(currentWorkingPath)
    for n in listFolders:
        folderDir = os.path.join(currentWorkingPath,n)
        filesList = file.listFiles(folderDir)
        for i in filesList:
            imgPath = os.path.join(folderDir,i)
            faces = faceHandle.faceDetect(imgPath)
            FacesCount = len(faces)
            if FacesCount > 1 or FacesCount == 0:
                file.delete_file(imgPath)
#images Count before remove multiple Faces = 81324
#removeMultipleFaces()
#removeWhiteSpacesFromFolderName()
#removeWhiteSpaceFromFilesNames()
print(imagesCount)