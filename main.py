import cv2
import numpy as np
import pyautogui
import time
import torch
import keyboard
import pygame
import win32api
import win32con
import win32gui
import pydirectinput

model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'best.pt')

# Set up pygame window
WINDOW_SIZE = (1920, 1080)
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Minecraft")
done = False

# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

# Set window transparency color
fuchsia = (255, 0, 128)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

# Set up rectangle drawing parameters
RECT_COLOR = (255, 0, 0)
RECT_WIDTH = 2
pydirectinput.PAUSE=0.01
while not done:
    global center_x, center_y
    if keyboard.is_pressed('x'):
                pydirectinput.moveTo(center_x, center_y, duration=0.1)
    # Capture screenshot and run model
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    model.conf = 0.10
    
    results = model(frame, size=640)

    # Find bounding box of largest confidence person
    class_names = results.names
    bboxes = results.xyxy[0].cpu().numpy()
    max_confidence = 0
    max_bbox = None
    for bbox in bboxes:
        if bbox[4] > max_confidence and class_names[int(bbox[5])] == 'Player':
            max_confidence = bbox[4]
            max_bbox = bbox

    # Draw bounding box on screen
    screen.fill(fuchsia)
    if max_bbox is not None:
        x1, y1, x2, y2 = max_bbox[:4]
        pygame.draw.rect(screen, RECT_COLOR, pygame.Rect(x1, y1, x2 - x1, y2 - y1), RECT_WIDTH)
        # Calculate center of bounding box and move mouse cursor
        center_x, center_y = int((x1 + x2) / 2), int((y1 + y2) / 2)
        # Drag mouse if 'x' key is pressed
                # Drag mouse if 'x' key is pressed

    # Update pygame display
    pygame.display.flip()

    # Handle pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Wait a bit to prevent high CPU usage
    time.sleep(0.1)