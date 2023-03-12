import cv2
import secret
from deepface import DeepFace

# Counters
neutral_counter = 0
sad_counter = 0
happy_counter = 0
angry_counter = 0
surprise_counter = 0
fear_counter = 0
disguist_counter = 0 
    

Vdo_cap = cv2.VideoCapture(0)

while True:
    ret, frame = Vdo_cap.read()
    result = DeepFace.analyze(frame, actions=['emotion'])

    faceCascade =  cv2.CascadeClassifier(secret.folder)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    # Rectecangle around the Face
    for(x1, y1, w1, h1) in faces:
        cv2.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (204, 0, 204), 4) # Face Box Color(BGR)
    

    text = ""

    if result["dominant_emotion"] == "neutral":
        text = "NEUTRAL"

    elif result["dominant_emotion"] == "sad": 
        text = "SAD"

    elif result["dominant_emotion"] == "happy":
        text = "HAPPY"

    elif result["dominant_emotion"] == "angry":
        text = "ANGRY"

    elif result["dominant_emotion"] == "surprise":
        text = "SURPRISE"  

    elif result["dominant_emotion"] == "fear":
        text = "FEAR"  

    elif result["dominant_emotion"] == "disguist":
        text = "DISGUIST"  

    # # Creating a black box in (o, o) to write text in that black box
    # start_point = (0, 0)
    # end_point = (130, 28)
    # color = (0 ,0, 0)
    # thickness = -1
    # black_box = cv2.rectangle(frame, start_point, end_point, color, thickness) 
    
    # # Putting Text in that black box
    # font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    # cv2.putText(
    #     black_box,
    #     text,
    #     (4, 20),
    #     font, 1,
    #     (252, 220, 11),
    #     2,
    #     cv2.LINE_4
    # )      

    # Showing Text above the head
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    scale = 1
    color = (4, 147, 255) # Text Color(BGR)
    thickness = 2

    # Text Box
    for(x, y, w, h) in faces:
        black_box = cv2.rectangle(frame, (x, y), (x+w, y-37), (64, 64, 64), -1) # Text Box Color(BGR)
        x_center = int(x + (w/2))
        y_center = int(y)
        (text_width, text_height) = cv2.getTextSize(text, font, scale, thickness)[0]
        text_x = int(x_center - (text_width/2))
        text_y = int(y_center - (text_height))
        cv2.putText(frame, text, (text_x, text_y), font, scale, color, thickness)

    if text == "NEUTRAL":
        neutral_counter += 1

    elif text == "SAD":
        sad_counter += 1

    elif text == "HAPPY":
        happy_counter += 1

    elif text == "ANGRY":
        angry_counter += 1

    elif text == "SURPRISE":
        surprise_counter += 1

    elif text == "FEAR":
        fear_counter += 1   

    elif text == "DISGUIST":
        disguist_counter += 1 


    cv2.imshow("Camera", frame)

    if cv2.waitKey(10) == ord('0'):
        break

    print(text)

def emotion_counter():
    max_emotion = max(neutral_counter, sad_counter, happy_counter, angry_counter, surprise_counter, fear_counter, disguist_counter)

    # Printing values of emotion by counting
    print("\n")
    print("Neutral->",neutral_counter)
    print("Sad->",sad_counter)
    print("Happy->",happy_counter)
    print("Angry->",angry_counter)
    print("Surprise->",surprise_counter)
    print("Fear->",fear_counter)
    print("Disguist->",disguist_counter)
    print("\n")

    # Printing maximum emotion by counting and the value of emotion counter
    if max_emotion == neutral_counter:
        print(f"Emotion Pediction: [Neutral]({max_emotion})")

    elif max_emotion == sad_counter:
        print(f"Emotion Pediction: [Sad]({max_emotion})")    

    elif max_emotion == happy_counter:
        print(f"Emotion Pediction: [Happy]({max_emotion})") 

    elif max_emotion == angry_counter:
        print(f"Emotion Pediction: [Angry]({max_emotion})") 

    elif max_emotion == surprise_counter:
        print(f"Emotion Pediction: [Surprise]({max_emotion})") 

    elif max_emotion == fear_counter:
        print(f"Emotion Pediction: [Fear]({max_emotion})") 

    elif max_emotion == disguist_counter:
        print(f"Emotion Pediction: [Disguist]({max_emotion})")  

Vdo_cap.release()
emotion_counter()           