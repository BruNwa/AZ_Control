# AZ Control: Face and Hand Gesture Computer Control

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
> cd AZ_Control

3. Install the required libraries:
> pip install opencv-python mediapipe pyautogui pynput numpy

## Usage

### Option 1: Run the Python script

To use this option, ensure you have installed all the required libraries listed in the Requirements section.

Run the main script:
> python3 controlAZ.py

### Option 2: Run the executable version

For quick and easy use, an executable version is available. Simply click on <a href="https://drive.google.com/drive/folders/1ztA_Wa3PFQ_II1XcXvuw4jvumBHwCRJL?usp=sharing" target="_blank"> <b>AZ Control-Executable</b></a> to download it. This option does not require Python or any additional libraries to be installed on your system.

Follow the on-screen prompts to choose your desired control mode and configure settings.

### Important Instructions

- Ensure you are in front of a fixed camera.
- For Mode 1 (Blink, Mouth, and Hand Gesture Control):
  - Position yourself closer to the camera for clear face detection.
  - Maximum distance: 1 meter from the camera.
- For Mode 2 (Mouse Control):
  - Ensure you have enough space to move your hand freely without going out of the camera frame.

### Mode 1: Blink, Mouth, and Hand Gesture Control

- Choose keyboard mappings for blink, mouth open, and hand gesture actions
- Perform the corresponding gestures to trigger the mapped keys

### Mode 2: Mouse Control

- Move your hand to control the mouse cursor
- Perform specific gestures for left-click, right-click, and drag operations

#### Left Click Gesture
![leftClick](https://github.com/user-attachments/assets/9a92df80-4758-41b1-a1f4-133f1493775c)
#### Right Click Gesture
![rightClick](https://github.com/user-attachments/assets/f08a28ff-97f5-47ce-bc9d-6471da8783a2)

## Modules

### handModule


This module uses MediaPipe to detect and track hand landmarks. It provides functionality to find hands in a frame and get their positions.

![hand_landmarks](https://github.com/user-attachments/assets/43d0a973-afd3-461a-bd9b-0cf261cf85f8)

The image above shows the 21 hand landmarks used by the handModule. Each point is numbered and corresponds to a specific part of the hand, as detailed in the legend.

### faceModule

This module uses MediaPipe's face mesh to detect and track facial landmarks. It can detect face positions and draw specific landmark points.
![face_mesh](https://github.com/user-attachments/assets/2799a40a-0151-43dd-babd-ad83a81f3a25)
The image above displays the face mesh with 468 landmarks. Each point is numbered, allowing for precise facial feature tracking.

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
