import cv2

CONFIDENCE_THRESHOLD = 0.1
NMS_THRESHOLD = 0.4
COLORS = [(0, 255, 255), (255, 255, 0), (0, 0, 255)]
CLASS_NAMES = ["incorrect", "wearing", "not wearing"]

class MaskDetector:
    def __init__(self) -> None:
        self.net = cv2.dnn.readNetFromDarknet('mask.cfg', darknetModel='mask.weights')
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

        self.model = cv2.dnn_DetectionModel(self.net)
        self.model.setInputParams(size=(416, 416), scale=1/255)

        self.frame_callback = None
    
    def set_input_capture(self, callback):
        self.frame_callback = callback

    def loop(self):
        """Main loop of the detector, recives frame from frame callback and does the ML"""
        while True:
            frame = self.frame_callback()

            frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
            classes, scores, boxes = self.model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)

            for (class_id, score, box) in zip(classes, scores, boxes):
                color = COLORS[int(class_id) % len(COLORS)]
                label = "%s : %f" % (CLASS_NAMES[class_id[0]], score)
                cv2.rectangle(frame, box, color, 2)
                cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            cv2.imshow('Input', frame)

            c = cv2.waitKey(1)
            if c == 27:
                break

        cv2.destroyAllWindows()
