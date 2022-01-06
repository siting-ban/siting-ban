//TITLE: ACROSS THE VOID
//LAST DATE MODIFIED: 2021/04/08
//DESCRIPTION: Wall-e and Eve are trying to find each other across the rainbow bridge using different algorithms!
//             Wall-e is using constant growth algorithm, and Eve is using the doubling algorithm. Change the values to help them find each other faster or slower.

import g4p_controls.*;

//GLOBAL VARIABLES
PVector bridge;
PImage cgBot, daBot, rainbow;

//Sets initial values
int startX = 1000;
int stepSize = 60;
int cgSpeed = 5;
int daSpeed = 5;

//Background drawings (Uses up a lot of CPU, turn on at own risk)
boolean backgroundDrawings = false;
int numStars = 200;        //Stars of the void
int numBoxes = 100;        //Trash on earth
int numCircles = 100;      //Water bubbles/droplets on spaceship

float[][] stars = new float[numStars][3];
float[][] boxes = new float[numBoxes][3];
float[][] circles = new float[numCircles][3];

boolean paused = false;
Robot cg, da;

//MAIN PROCEDURE
void setup(){
  size(1500, 800);
  bridge = new PVector(20, height/3 - 20, 80);
  
  //Load Images
  cgBot = loadImage("wall-e.png");
  daBot = loadImage("eve.png");
  rainbow = loadImage("rainbow.png");
  
  reset();
  createGUI();
}

//DRAWING PROCEDURE
void draw(){
  if(!paused){
    background(22, 175, 21);
    
    if(backgroundDrawings){
      //Draws the boxes and circles
      for(int i = 0; i < numBoxes; i++){
        stroke(0);
        strokeWeight(2);
        fill(125, 95, 45);
        square(boxes[i][0], boxes[i][1], boxes[i][2]);
      }
      
      for(int i = 0; i < numCircles; i++){
        stroke(235, 230, 240);
        strokeWeight(2);
        fill(97, 202, 240);
        circle(circles[i][0], circles[i][1], circles[i][2]);
      }
    }
    
    //Draws the void & the stars
    noStroke();
    fill(0);
    rect(0, height/3, width, height/3);
    
    for(int i = 0; i < numStars; i++){
      fill(255);
      circle(stars[i][0], stars[i][1], stars[i][2]);
    }
    
    //Draws the rainbow bridge
    image(rainbow, bridge.x, bridge.y, bridge.z, height/3 + 40);
    
    //Draws the robots racing and updates according to their algorithm
    cg.display();
    cg.race(bridge);
    
    //Draws the markers for the cg bot
    if(cg.markers.size() > 0){
      for(int i = 0; i < cg.markers.size(); i++){
        stroke(255);
        strokeWeight(3);
        line(cg.markers.get(i), cg.y - 20, cg.markers.get(i), cg.y + cg.size + 20);
      }
    }
    
    da.display();
    da.race(bridge);
    
    //Draws the markers for the da bot
    if(da.markers.size() > 0){
      for(int i = 0; i < da.markers.size(); i++){
        stroke(255);
        strokeWeight(3);
        line(da.markers.get(i), da.y - 20, da.markers.get(i), da.y + da.size + 20);
      }
    }
    
    if(cg.foundBridge && da.foundBridge){    //Pause animation when both bots have found the bridge
      paused = true;
      println("Wall-e and Eve have found each other across the rainbow bridge! Thank you for your support on this journey! <3");
    }
  }
}

void reset(){
  //Set robot values (starting x position, starting y position, speed, algorithm, image)
  cg = new Robot(startX, 100, cgSpeed, "cg", cgBot);
  da = new Robot(startX, 600, daSpeed, "da", daBot);
  
  //Set random star values
  for(int i = 0; i < numStars; i++){
    float x = random(0, width);
    float y = random(height/3, 2*height/3);
    float size = random(1, 5);
    stars[i][0] = x;
    stars[i][1] = y;
    stars[i][2] = size;
  }
  
  //Set random box values
  for(int i = 0; i < numBoxes; i++){
    float x = random(-20, width);
    float y = random(-20, height/8);
    float size = random(20, 70);
    boxes[i][0] = x;
    boxes[i][1] = y;
    boxes[i][2] = size;
  }
  
  //Set random circle values
  for(int i = 0; i < numCircles; i++){
    float x = random(-20, width);
    float y = random(5*height/6, height);
    float size = random(20, 70);
    circles[i][0] = x;
    circles[i][1] = y;
    circles[i][2] = size;
  }
}
