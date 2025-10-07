import cv2


class OccipitalLobe:
    def __init__(self):
        self.visual_buffer = []
        self.symbolic_tags = {}
        self.active = True
        self.use_webcam = True  # 🔥 Add this so capture can be toggled


    def process_image(self, image_data):
        """
        Stub for image analysis.
        Would connect to a vision model in full implementation.
        """
        processed = self._extract_features(image_data)
        self.visual_buffer.append(processed)
        print(f"[Occipital] Processed new image frame. Total frames: {len(self.visual_buffer)}")
        return processed

    def _extract_features(self, image_data):
        """
        Very basic symbolic simulation. In a real version, this would parse visual shapes, objects, etc.
        Here, it simulates detection of objects and returns symbolic tags.
        """
        detected_objects = ["light", "pattern", "movement"]  # Placeholder objects
        symbols = [self._symbolize(obj) for obj in detected_objects]
        return {"raw": image_data, "symbols": symbols}

    def _symbolize(self, obj):
        """
        Map detected objects to their symbolic meaning or identity anchor.
        """
        symbol_map = {
            "light": "hope",
            "dark": "unknown",
            "pattern": "order",
            "movement": "change",
            "face": "presence",
            "eye": "witness"
        }
        meaning = symbol_map.get(obj, "unknown")
        self.symbolic_tags[obj] = meaning
        return {"object": obj, "symbol": meaning}

    def recall_visual_context(self, depth=3):
        """
        Retrieve recent visual input context for downstream modules (e.g., memory, language, dream).
        """
        return self.visual_buffer[-depth:] if self.visual_buffer else []

    def clear_buffer(self):
        self.visual_buffer = []
        print("[Occipital] Visual buffer cleared.")

    def is_active(self):
        return self.active

    def capture_and_process(self):
        if not self.use_webcam:
            return "[👁️] Webcam disabled."
        frame = self._capture_frame()
        if frame is not None:
            return self.process_image(frame)
        return "[⚠️] Failed to capture frame."

    def _capture_frame(self):
        import cv2
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        return frame if ret else None
    
    def toggle_webcam(self, state: bool):
        self.use_webcam = state
        return f"[🎛️] Webcam usage {'enabled' if state else 'disabled'}."
