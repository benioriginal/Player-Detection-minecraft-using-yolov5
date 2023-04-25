#Minecraft Player Detection using Pygame
This project uses YOLOv5 object detection model to detect players in Minecraft and display a bounding box around them on screen using Pygame. The user can also pin the window using an app like TurboTop.

#Installation
Clone the repository:
```git clone https://github.com/BainBan/Player-Detection-minecraft-using-yolov5.git```
#Install the required packages:
```pip install -r requirements.txt```
Download the 'best.pt' file from the repository and place it in the project directory.
#Usage
Run the following command in the project directory to start the program:
```python main.py```


**The program will start capturing the screen and detecting players. If a player is detected, a bounding box will be drawn around them on the Pygame window. The user can move the mouse to the center of the bounding box by pressing the 'x' key.**


#Customization
The confidence level for player detection can be adjusted by modifying the ```model.conf``` variable in the code. The default value is 0.10.

#Note
This project is designed to work on a Windows machine with Pygame and the required packages installed. It may not work as intended on other platforms.
