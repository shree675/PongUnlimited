# PongUnlimited

## About
<p>
PongUnlimited is a simple and a slightly different version of the well-known arcade game Pong. This is a single player game where the opponent is a never-losing computer. This is more like a practice game for the real Pong.</p>
<p>There are two modes, normal and neon. Additionally, the scores of the players are stored in a database and is retrieved and displayed on tapping the DISPLAY SCORES button.</p>
<p>In theses two modes, the player can control the sliding bar using the mouse or a green pen (or a pointy green object of hsv values in the range (31,107,135) to (59,2208,255)).</p>
<p>To control the sliding bar using a green pen, all you need to do is point it to your webcam and move it left or right in mid-air. You must bring the cursor to the display area initially by moving the pen left,right,up or down.</p>

## Database
The game scores and player names are stored in a MySQL database. The scores are retrieved when DISPLAY SCORES button is called. The game initially creates a database and an appropriate table if not already created, to store the information.

<p>
  <img src="screenshots/Screenshot (123).png", height="100", width="100">
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

## Version
v2020
