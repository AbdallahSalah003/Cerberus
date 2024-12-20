import cv2 as cv
import matplotlib.pyplot as plt

from core.pipeline import process_image

arabic_translation_map = {
    "1": "١",
    "2": "٢",
    "3": "٣",
    "4": "٤",
    "5": "٥",
    "6": "٦",
    "7": "٧",
    "8": "٨",
    "9": "٩",
    "Mem": "م",
    "aen": "ع",
    "alf": "ا",
    "ba'": "ب",
    "dal": "د",
    "fa'": "ف",
    "gem": "ج",
    "ha'": "هـ",
    "lam": "ل",
    "noon": "ن",
    "qaf": "ق",
    "ra'": "ر",
    "sad": "ص",
    "seen": "س",
    "ta'": "ط",
    "waw": "و",
    "ya'": "ي",
}


def test_license_plate(image_path):
    image = cv.imread(image_path)

    plate_image, recognized_text = process_image(image)

    arabic_plate = [arabic_translation_map.get(value, "") for value in recognized_text]
    arabic_plate.reverse()

    if len(recognized_text) > 0:
        print(f"Recognized Text: {' '.join(recognized_text)}")
        print(f"Arabic Text: {' '.join(arabic_plate)}")

    else:
        print("License plate text could not be recognized.")

    plate_image = cv.cvtColor(plate_image, cv.COLOR_BGR2RGB)
    plt.imshow(plate_image)
    plt.axis("off")
    plt.show()


image_path = "tests/test_images/test.jpeg"

test_license_plate(image_path)

