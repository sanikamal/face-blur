


def do_face_blur(input_path, output_path):
    """
    1. read image from the input_path
    2. use mediapipe to detect face
    3. use cv2 to heavily blur two Rectangle areas, which covers eyes, nose and mouth. See areas.png.
    As long as eyes, nose, mouth are blurred, that's OK.
    The purpose is to de-identify people.
    4. write the result to output_path

    """

if __name__ == '__main__':
    do_face_blur('test.jpg', 'output.jpg')