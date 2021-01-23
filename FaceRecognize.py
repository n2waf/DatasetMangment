import face_recognition
import os
from FilesHandle import FilesHandle


class FaceRecognize:

    def faceDetect(self,imagePath):
        image = face_recognition.load_image_file(imagePath)
        face_locations = face_recognition.face_locations(image)
        #print("I found {} face(s) in this photograph.".format(len(face_locations)))
        return face_locations
        
