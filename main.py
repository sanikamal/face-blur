import cv2
import mediapipe as mp

def do_face_blur(input_path, output_path):
    """
    1. read image from the input_path
    2. use mediapipe to detect face
    3. use cv2 to heavily blur two Rectangle areas, which covers eyes, nose and mouth. See areas.png.
    As long as eyes, nose, mouth are blurred, that's OK.
    The purpose is to de-identify people.
    4. write the result to output_path

    """
    image = cv2.imread(input_path)
    # Run MediaPipe Face Detection model
    with mp.solutions.face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        for detection in results.detections:
            # Extract key points
            landmarks = detection.location_data.relative_keypoints
            right_eye = (int(landmarks[0].x * image.shape[1]), int(landmarks[0].y * image.shape[0]))
            left_eye = (int(landmarks[1].x * image.shape[1]), int(landmarks[1].y * image.shape[0]))
            nose = (int(landmarks[2].x * image.shape[1]), int(landmarks[2].y * image.shape[0]))
            mouth = (int(landmarks[3].x * image.shape[1]), int(landmarks[3].y * image.shape[0]))
            # Draw rectangle for eyes
            cv2.rectangle(image, (left_eye[0]+30,left_eye[1]-15), (right_eye[0]-30, right_eye[1]+5), (120, 120, 120), thickness = -1)
            # Draw rectangle for nose and mouth
            cv2.rectangle(image, (nose[0]+40,nose[1]-80), (mouth[0]-40, mouth[1]+20), (120, 120, 120), thickness = -1)
            cv2.imwrite(output_path, image)

if __name__ == '__main__':
    do_face_blur('test.jpg', 'output2.jpg')