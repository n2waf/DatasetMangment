import os
import importlib

class FilesHandle():


    def create_folder(self,folder_path):
        try:
            os.mkdir(folder_path)
        except OSError:
            print ("Creation of the directory %s failed" % folder_path)
        else:
            print ("Successfully created the directory %s " % folder_path)

    def delete_file(self,del_file_path):
        if os.path.exists(del_file_path):
            os.remove(del_file_path)             
        else:
            print('file not exist')

    def delete_folder(self,del_folder_path):
         os.rmdir(del_folder_path)

    def listFolders(self,folders_path): 
        folders = next(os.walk(folders_path))[1]
        return folders
    
    def listFiles(self,folder_path):
        sortlist = sorted(os.listdir(folder_path))   
        return sortlist

    def removeWhiteSpaces(self,path,fName):
        if ' ' in fName:
            newName = fName.replace(' ','_')
            newPath = os.path.join(path,newName)
            oldPath = os.path.join(path,fName)
            if os.path.exists(newPath) == False:
                print('new path its not exist so the operation will be sucess')
                os.rename(oldPath,newPath)
                print('{} renamed'.format(fName))
            else:
                print('This PATH = {} IS EXIST '.format(newPath))
                print('I will move all files to the same folder Name')
                filesList = self.listFiles(newPath)
                for i in filesList:
                    oldFilePath = os.path.join(newPath,i)
                    destPath = os.path.join(oldPath,i)
                    os.rename(oldFilePath,destPath)  
                self.delete_folder(newPath)
            
        
        

    def imagesCount(self,folderPath):
        count = 0
        i = 0
        sortlist = sorted(os.listdir(folderPath))
        while(i<len(sortlist)):
           folderDir = os.path.join(folderPath,sortlist[i])
           filesList = sorted(os.listdir(folderDir))
           for _ in filesList:
              count+=1
           i+=1
        return str(count)
    
