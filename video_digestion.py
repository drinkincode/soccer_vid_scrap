import numpy as np
import tensorflow as tf
import cv2

# Load pretraine model
model = tf.compat.v2.saved_model.load(r'C:/Users/jonny/.cache/kagglehub/models/google/faster-rcnn-inception-resnet-v2/tensorFlow1/faster-rcnn-openimages-v4-inception-resnet-v2/1')

# Open a video file
cap = cv2.VideoCapture(r'./tmp/soccer_match_clip.avi')

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Run the frame through the model
    inputs = tf.constant(frame[np.newaxis, ...])
    outputs = model.signatures["default"](inputs)

    # Get the object detect results
    boxes, scores, classes, num = outputs["detection_boxes"], outputs["detection_scores"], outputs["detection_classes"], \
    outputs["num_detections"]

    # Draw the detect boxes on the frame
    for i in range(num.numpy()[0]):
        if scores.numpy()[0, i] > 0.5:
            box = boxes.numpy()[0, i]
            x1, y1, x2, y2 = box[1] * frame.shape[1], box[0] * frame.shape[0], box[3] * frame.shape[1], box[2] * \
                             frame.shape[0]
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
            cv2.putText(frame, '{}'.format(classes.numpy()[0, i]), (int(x1), int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255, 0, 0), 2)

    # Show the frame
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video file and close the window
cap.release()
cv2.destroyAllWindows()