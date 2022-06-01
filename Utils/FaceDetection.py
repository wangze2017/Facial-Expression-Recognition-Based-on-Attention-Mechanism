import cv2
import mediapipe as mp


def get_face_image(image):
    mp_face_detection = mp.solutions.face_detection
    # For static images:
    with mp_face_detection.FaceDetection(
            model_selection=1, min_detection_confidence=0.5) as face_detection:

        # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        location = []
        if not results.detections:
            return image
        for detection in results.detections:
            for _, point in enumerate(mp_face_detection.FaceKeyPoint):
                location.append(mp_face_detection.get_key_point(detection, point))

        rows, cols, _ = image.shape
        x = int(location[2].x * cols)
        y = int(location[2].y * rows)
        width = int((location[5].x - location[4].x) * cols)
        if width * 2 > cols or width * 2 > rows:
            face_image = image
        else:
            face_image = image[y - width:y + width, x - width:x + width]

        return face_image


