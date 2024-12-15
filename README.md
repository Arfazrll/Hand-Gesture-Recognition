# 🤖 Hand Gesture Recognition with Python

**Hand Gesture Recognition** is a real-time system that detects and recognizes hand gestures using **MediaPipe** and **OpenCV**. This project demonstrates the potential of computer vision for dynamic, interactive applications such as finger counting and gesture-based control.

---

## ✨ Key Features

- **🔍 Real-Time Hand Tracking**: Accurately detects and tracks hand landmarks in video streams.
- **✋ Gesture Recognition**: Counts the number of fingers raised dynamically.
- **🌐 Cross-Platform Compatibility**: Works on any system supporting Python, OpenCV, and MediaPipe.

---

## ⚙️ Requirements

- Python 3.7+
- OpenCV
- MediaPipe

---

## 🚀 Installation

### 1. Clone the Repository
   ```bash
   git clone https://github.com/Arfazrll/Hand-Gesture-Recognition.git
   cd your-repo-name
   ```

### 2. Create and Activate a Virtual Environment
   ```bash
   python -m venv HandTracking-env
   HandTracking-env\Scripts\Activate
   ```

### 3. Install Dependencies
   ```bash
   pip install opencv-python mediapipe
   ```

---

## 📊 Usage

### 1. Run the Application
   ```bash
   python HandsTrackingAI.py
   ```

### 2. Interact
   - Allow camera access to start hand tracking.
   - Observe the live feed with hand landmarks highlighted and the number of raised fingers printed in the console.

### 3. Exit
   - Press `q` to close the application.

---

## 🔑 Code Highlights

### **Hand Tracking with MediaPipe**
The system leverages the MediaPipe Hands solution for robust hand detection:
```python
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
```

---

## 🌟 Future Enhancements

- Add recognition for specific gestures (e.g., thumbs up, peace sign).
- Support multiple hand tracking simultaneously.
- Optimize for mobile deployment using TensorFlow Lite.

---

## 🛠️ Technologies Used

- **🐍 Python**: Core programming language.
- **📦 MediaPipe**: For hand landmark detection.
- **📊 OpenCV**: For video processing and visualization.

---

## 🤝 Contributions

Feel free to fork this repository, submit pull requests, or open issues for suggestions and improvements. <br>
Thank You :) 

---


## 🙏 Acknowledgments

- [MediaPipe by Google](https://mediapipe.dev/)
- [OpenCV Library](https://opencv.org/)
