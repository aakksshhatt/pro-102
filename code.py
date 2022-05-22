from asyncore import file_dispatcher
import cv2
import dropboximport 
import time 
import random

start_time = time.time()

def take_snapshot():
 number = random.randint(0,100)

 videoCaptureObject = cv2.VideoCapture(0)
 result = True
 while(result):
     ret, frame = videoCaptureObjec.read()
     image_name = 'ing' +str(number) +".png"
     cv2.imwrite(image_name, frame)
     start_time = time.time
     return image_name
     print("snapshot taken")

     videoCoptureObject.release()
     cv2.destryAllWindow()

     take.snapshot()

     def upload_file(image_name):
         access_token = "sl.BIG3oSSntnmophVzoI_DjSXd5_7oPMQfvcnzPi_H4E1lS9rQ_sjRxe7QmiOQSpeK9rVETC9qDQwoUrZL1iTwSOdIdcZlUiBWFhr-dr3_qxUFDh2Hog-wyWVy__KkDqD7HwbFTt0"
         file = image_name
         file_from = file
         file_to = ""+(image_name)
         dbx = drop.Dropbox(access_token)
         with open(file_from,'rb') as f:
             dbx.file_upload(f.read(), file_to,mode = dropbox.files.WriteMode.overWrite)
             print ("file uploaded")

             def main():
                 while(true):
                     if ((time.time()-start_time) ) = 3):
                          name = take_snapshot()
                          upload_file(name)
                    
     main()
     
     


