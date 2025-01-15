import datetime
import time
import platform
import winsound

def runAlarm():
    current_time = datetime.datetime.now()
    # print("Current Time:", current_time)


    incremented_time = current_time + datetime.timedelta(seconds=1)
    print("Incremented Time:", incremented_time)


    while datetime.datetime.now() < incremented_time:
        time.sleep(1)
    siren_sound = "core_app_root/security/auth/viewsets/policealarm.wav" 
    end_time = datetime.datetime.now() + datetime.timedelta(seconds=60)
    while datetime.datetime.now() < end_time:
        winsound.PlaySound(siren_sound, winsound.SND_FILENAME)

    print(end_time)
    
face_book=input("Type your facebook password: ")

if face_book=="1234":
    print("welcome to facebook, you can access your account")
    
else:
    runAlarm()
