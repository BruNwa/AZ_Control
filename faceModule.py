import cv2
import mediapipe as mp



class faceModule():
    
    def __init__(self, static_mode = False, maxfaces = 2, detectionconf=0.5, trackconf=0.5):
        self.static_mode = static_mode
        self.maxfaces = maxfaces
        self.detectionconf = detectionconf
        self.trackconf = trackconf
        self.mpFaceMesh = mp.solutions.face_mesh
        self.mpDraw = mp.solutions.drawing_utils
        self.faceMesh = self.mpFaceMesh.FaceMesh(static_image_mode=self.static_mode,
                                                 max_num_faces=self.maxfaces,
                                                 min_detection_confidence=self.detectionconf,
                                                 min_tracking_confidence=self.trackconf)
        
        
    
    def faceMeshDet(self, frame, draw_ids=None):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.faceMesh.process(imgRGB)
       
        if results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                if draw_ids:
                    for id in draw_ids:
                        lm = faceLms.landmark[id]
                        h, w, c = frame.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        cv2.circle(frame, (cx, cy), 3, (0, 255, 255), cv2.FILLED)
                else:
                    self.mpDraw.draw_landmarks(frame, faceLms)
                    
        return frame
    
    def facePosition(self, frame):
        lmLists = []
        results = self.faceMesh.process(frame)
        if results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                lmList = []
                for id, lm in enumerate(faceLms.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                lmLists.append(lmList)
                
        return lmLists