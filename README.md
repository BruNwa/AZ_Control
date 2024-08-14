# AZ_Control

AZ Control: Face and Hand Gesture Computer Control

AZ Control is a Python-based computer vision project that allows users to control their computer using face and hand gestures. This application offers two main modes of operation: controlling specific actions using blinks, mouth movements, and hand gestures, or controlling the mouse using hand movements.

## Features

- Face and hand gesture recognition
- Two control modes:
  1. Blink, mouth, and hand gesture control
  2. Mouse control using hand gestures
- Customizable keyboard mappings for gestures
- Optional camera feed display

## Requirements

- Python 3.x
- OpenCV (cv2)
- MediaPipe
- PyAutoGUI
- Pynput
- NumPy

## Installation

1. Clone this repository:
git clone https://github.com/BruNwa/AZ_Control.git
cd AZ_Control
Copy
2. Install the required libraries:
pip install opencv-python mediapipe pyautogui pynput numpy
Copy
## Usage

Run the main script:
python main.py
Copy
Follow the on-screen prompts to choose your desired control mode and configure settings.

### Mode 1: Blink, Mouth, and Hand Gesture Control

- Choose keyboard mappings for blink, mouth open, and hand gesture actions
- Perform the corresponding gestures to trigger the mapped keys

### Mode 2: Mouse Control

- Move your hand to control the mouse cursor
- Perform specific gestures for left-click, right-click, and drag operations

## Modules

### handModule

This module uses MediaPipe to detect and track hand landmarks. It provides functionality to find hands in a frame and get their positions.

### faceModule

This module uses MediaPipe's face mesh to detect and track facial landmarks. It can detect face positions and draw specific landmark points.

## Customization

You can customize various aspects of the application, including:

- Gesture detection thresholds
- Keyboard mappings for gestures
- Mouse sensitivity and smoothing

Refer to the main script for customizable parameters.

## Exiting the Program

Press the 'End' key while the terminal is in focus to exit the program.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- MediaPipe for providing the hand and face detection models
- OpenCV community for computer vision tools
You can now copy this entire block and paste it directly into your README.md file on GitHub
