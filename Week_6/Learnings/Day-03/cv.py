import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options = python.BaseOptions(model_asset_path="efficientdet_lite0.tflite")

options = vision.ObjectDetectorOptions(
    base_options=base_options,
    score_threshold=0.5,
    running_mode=vision.RunningMode.VIDEO
)

detector = vision.ObjectDetector.create_from_options(options)

cap = cv2.VideoCapture("traffic.mp4")

timestamp = 0
vehicle_classes = ["car", "truck", "bus", "motorcycle"]

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    results = detector.detect_for_video(mp_image, timestamp)

    vehicle_count = 0

    for detection in results.detections:
        category = detection.categories[0]
        label = category.category_name.lower()

        if label in vehicle_classes:
            vehicle_count += 1

            bbox = detection.bounding_box
            x1 = bbox.origin_x
            y1 = bbox.origin_y
            x2 = x1 + bbox.width
            y2 = y1 + bbox.height

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.putText(frame, f"Vehicles: {vehicle_count}",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)

    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    timestamp += 33

cap.release()
cv2.destroyAllWindows()

# import cv2
# import mediapipe as mp
# from mediapipe.tasks import python
# from mediapipe.tasks.python import vision

# # Load model
# base_options = python.BaseOptions(model_asset_path="efficientdet_lite0.tflite")
# options = vision.ObjectDetectorOptions(
#     base_options=base_options,
#     score_threshold=0.5,
#     running_mode=vision.RunningMode.VIDEO
# )
# detector = vision.ObjectDetector.create_from_options(options)

# # Open webcam
# cap = cv2.VideoCapture(0)

# frame_timestamp_ms = 0

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Convert BGR to RGB
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

#     # Perform detection
#     results = detector.detect_for_video(mp_image, frame_timestamp_ms)

#     # Draw detections
#     for detection in results.detections:
#         bbox = detection.bounding_box
#         start_point = (bbox.origin_x, bbox.origin_y)
#         end_point = (bbox.origin_x + bbox.width, bbox.origin_y + bbox.height)

#         cv2.rectangle(frame, start_point, end_point, (0, 255, 0), 2)

#         category = detection.categories[0]
#         label = f"{category.category_name} ({round(category.score, 2)})"
#         cv2.putText(frame, label,
#                     (bbox.origin_x, bbox.origin_y - 10),
#                     cv2.FONT_HERSHEY_SIMPLEX,
#                     0.5, (0, 255, 0), 2)

#     cv2.imshow("Object Detection", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#     frame_timestamp_ms += 33  

# cap.release()
# cv2.destroyAllWindows()


# import cv2
# import mediapipe as mp
# from mediapipe.tasks import python
# from mediapipe.tasks.python import vision

# # Load model
# base_options = python.BaseOptions(model_asset_path="face_landmarker.task")
# options = vision.FaceLandmarkerOptions(
#     base_options=base_options,
#     running_mode=vision.RunningMode.VIDEO,
#     num_faces=1
# )

# detector = vision.FaceLandmarker.create_from_options(options)

# cap = cv2.VideoCapture(0)
# timestamp = 0

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break

#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

#     result = detector.detect_for_video(mp_image, timestamp)

#     if result.face_landmarks:
#         for face_landmarks in result.face_landmarks:
#             for landmark in face_landmarks:
#                 h, w, _ = frame.shape
#                 x = int(landmark.x * w)
#                 y = int(landmark.y * h)
#                 cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

#     cv2.imshow("Face Mesh", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#     timestamp += 33

# cap.release()
# cv2.destroyAllWindows()

# import cv2
# import mediapipe as mp
# from mediapipe.tasks import python
# from mediapipe.tasks.python import vision

# # Load gesture recognizer model
# base_options = python.BaseOptions(model_asset_path="gesture_recognizer.task")

# options = vision.GestureRecognizerOptions(
#     base_options=base_options,
#     running_mode=vision.RunningMode.VIDEO,
#     num_hands=1
# )

# recognizer = vision.GestureRecognizer.create_from_options(options)

# cap = cv2.VideoCapture(0)
# timestamp = 0

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break

#     frame = cv2.flip(frame, 1)

#     # Convert BGR to RGB
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     mp_image = mp.Image(
#         image_format=mp.ImageFormat.SRGB,
#         data=rgb_frame
#     )

#     # Run recognition
#     result = recognizer.recognize_for_video(mp_image, timestamp)

#     gesture_text = ""

#     if result.gestures:
#         top_gesture = result.gestures[0][0]
#         gesture_text = f"{top_gesture.category_name} ({top_gesture.score:.2f})"

#     cv2.putText(frame, gesture_text, (10, 50),
#                 cv2.FONT_HERSHEY_SIMPLEX, 1,
#                 (0, 255, 0), 2)

#     cv2.imshow("Gesture Recognizer", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#     timestamp += 33  # ~30 FPS

# cap.release()
# cv2.destroyAllWindows()
