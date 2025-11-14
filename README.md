# Mr. Rubik

This is my project for my ECE 210 class at UW Madison (Intro to electrical engineering). My goal is to build a robot which can solve a rubik's cube.  I'm calling it Mr. Rubik. 

# Notes

The project will be powered using a custom-PCB (class requirement) and a Pi Zero 2W. There will be three servo motors and a 3D printed case to control the cube. The CV and Solver will run on the Pi. 

Right now, I'm just trying to get the camera setup on the Pi, and learn to use the school's 3D printer. One of the most interesting things I have learned about so far is gears. I'm not a mechanical engineering, but it does fascinate me, so I've been studying on how effective involute gears are designed. The way the robot will work attempts to minimize the number of servo motors needed. There will be one on the bottom which can turn the whole cube. Additionally, there will be a retractible arm on the right side. This will allow the middle layer to be held (and bottom face turned), the whole cube to be turned about vertical axis, or the (interchangeable) right face to be turned. I suspect that this is very unique design, but I am still releasing all code in case any tinkerers might hope to draw inspiration!
