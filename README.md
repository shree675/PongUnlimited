# PongUnlimited

## About
<p>
PongUnlimited is a simple version of the well-known arcade game Pong. This is a single player game where the opponent is a never-losing computer. This is more like a practice game for the real Pong.
</p>
<p>
  This game can be played without touching the mouse or the keyboard. OpenCV has been used to detect green colored pen movements in front of the screen through a webcam. The slider then moves based on the pen movement.
</p>

<p>
  <img src="screenshots and videos/Screenshot (120).png", height="350", width="350">
 </p>

<p>There are two modes, normal and neon. Additionally, the scores of the players are stored in a database and is retrieved and displayed on tapping the DISPLAY SCORES button.</p>
<p>In theses two modes, the player can control the sliding bar using the mouse or a green pen (or a pointy green object of hsv values in the range (31,107,135) to (59,2208,255)).</p>

<p>
  <img src="screenshots and videos/Screenshot (121).png", height="350", width="350">
 </p>

<p>To control the sliding bar using a green pen, all you need to do is point it to your webcam and move it left or right in mid-air. You must bring the cursor to the display area initially by moving the pen left, right, up or down.</p>

## Database
The game scores and player names are stored in a MySQL database. The scores are retrieved when DISPLAY SCORES button is called. The game initially creates a database and an appropriate table if not already created, to store the information.


<p>
  <img src="screenshots and videos/Screenshot (123).png", height="350", width="350">
</p>


## Python Libraries Used
* opencv
* tkinter
* mysql
* mouse
* numpy
* sys
* datetime
* pygame
* time
* random

## Videos and Screenshots
Follow this link to view game screenshots and videos: [screenshots and videos](https://github.com/shree675/PongUnlimited/tree/main/screenshots%20and%20videos)

## Version
2020
