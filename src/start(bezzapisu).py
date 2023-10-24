import numpy as np
import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 1000)  # Ustawienie szerokości obrazu


# Inicjalizacja pierwszej klatki (referencyjnej)
ret, frame1 = cap.read()
frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

while True:
    ret, frame2 = cap.read()
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Obliczenie różnicy między klatkami
    frame_diff = cv2.absdiff(frame1_gray, frame2_gray)

    # Progowanie różnicy, aby uzyskać binaryzowany obraz
    _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)

    # Wyszukanie konturów w obrazie binaryzowanym
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Narysowanie prostokątów wokół zaznaczonych obiektów
    for contour in contours:
        if cv2.contourArea(contour) > 50:  # Minimalna powierzchnia obiektu do zaznaczenia
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)
            


    # Obsługa servo motora by śledzić obiekt
            if x < 200:
                print("lewo")
            elif x > 800:
                print("prawo")

            if y < 200:
                print("gora")
            elif y > 500:
                print("dol")


    # Wyświetlenie klatki z zaznaczonymi obiektami
    cv2.imshow('frame', frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Aktualizacja referencyjnej klatki
    frame1_gray = frame2_gray

cap.release()
cv2.destroyAllWindows()