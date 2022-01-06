//TITLE: Deserts & Grasslands
//LAST MODIFIED: 03/08/2021
//DESCRIPTION: A simulation of the process of desertification in grassland ecosystems.
//              Try holding and dragging mouse across screen to plant Stage 1 Grasslands!

//CHANGEABLE VALUES (Current values will result in the entire grid desertified)
//Amount of Influence by each state
float s1Desert = 2;        //Below 2 & 3, severe desertification will not happen (with no other changes)
float s2Desert = 3;
float s2Grassland = 1;
float s1Grassland = 2;
float waterSource = 2.5;

//Turning points for deserts and grasslands to become Stage 2
float desertTurningPoint = 12;
float grasslandTurningPoint = 13;

//Colours of each state
color s1DesertFill = color(162, 157, 3);
color s2DesertFill = color(211, 204, 4);
color s2GrasslandFill = color(82, 122, 2);
color s1GrasslandFill = color(125, 186, 2);
color waterSourceFill = color(3, 180, 231);

//Initial setup ratios (Out of 100, adds to 100)
int s1DesertRatio = 20;
int s2GrasslandRatio = 40;
int s1GrasslandRatio = 30;
int waterSourceRatio = 10;

//Screen settings
int numColumns = 100;
float blinksPerSecond = 2;

//STANDARD VALUES (DON'T CHANGE)
int numRows = numColumns;
float cellSize;
float padding = 50;
String[][] cellsNow = new String[numRows][numColumns];
String[][] cellsNext = new String[numRows][numColumns];
color[][] coloursNow = new color[numRows][numColumns];
color[][] coloursNext = new color[numRows][numColumns];

//MAIN PROCEDURE
void setup(){
  size(1000, 1000);
  cellSize = (width - 2*padding)/numColumns;
  frameRate(blinksPerSecond);
  
  setInitialValues();
}

//DRAWING & ANIMATIONS
void draw(){
  background(0);
  stroke(0);
  
  drawState();
  getNextGeneration();
  update();
  showStats();
}

//SET INITIAL CELL VALUES
void setInitialValues(){
  for(int i = 0; i < numRows; i++){
    
    for(int j = 0; j < numColumns; j++){
      if(0 <= i && i <= 1 && 0 <= j && j <= 1)
        cellsNow[i][j] = "s2Desert";
      
      else if((2 == i && (j >= 0 && j <= 2)) || (2 == j && (i >=0 && i <= 2)))
        cellsNow[i][j] = "s1Desert";
      
      else if(i == 4 && j == 3)
        cellsNow[i][j] = "s1Grassland";
      
      else if(j == 4 && (i >=2 & i <=4))
        cellsNow[i][j] = "waterSource";
      
      else{
        int randint = round(random(0, 100));
        if(randint >= 0 && randint < s1DesertRatio)
          cellsNow[i][j] = "s1Desert";
        
        else if(randint >= s1DesertRatio && randint < s1DesertRatio + s2GrasslandRatio)
          cellsNow[i][j] = "s2Grassland";
        
        else if(randint >= s1DesertRatio + s2GrasslandRatio && randint < s1DesertRatio + s2GrasslandRatio + s1GrasslandRatio)
          cellsNow[i][j] = "s1Grassland";
        
        else
          cellsNow[i][j] = "waterSource";
      }
    }
  }
}

//DRAWING EACH CELL
void drawState(){
  for(int i = 0; i < numRows; i++){
    float x = padding + i*cellSize;
    
    for(int j = 0; j < numColumns; j++){
      float y = padding + j*cellSize;
      
      if(cellsNow[i][j].equals("s2Desert")){
        fill(s2DesertFill);
        stroke(s2DesertFill);
      }
      
      else if(cellsNow[i][j].equals("s1Desert")){
        fill(s1DesertFill);
        stroke(s1DesertFill);
      }
      
      else if(cellsNow[i][j].equals("s2Grassland")){
        fill(s2GrasslandFill);
        stroke(s2GrasslandFill);
      }
      
      else if(cellsNow[i][j].equals("s1Grassland")){
        fill(s1GrasslandFill);
        stroke(s1GrasslandFill);
      }
      
      else if(cellsNow[i][j].equals("waterSource")){
        fill(waterSourceFill);
        stroke(waterSourceFill);
      }
      
      rect(x, y, cellSize, cellSize);
    }
  }
}

//USE EVOLUTION RULES TO SET NEXT GENERATION
void getNextGeneration(){
  for(int i = 0; i < numRows; i++){
    for(int j = 0; j < numColumns; j++){
      float desertCount = countDesertNeighbours(i, j);
      float grasslandCount = countGrasslandNeighbours(i, j);
      
      if(desertCount >= desertTurningPoint && cellsNow[i][j].equals("s1Desert"))
        cellsNext[i][j] = "s2Desert";
      
      else if(grasslandCount >= grasslandTurningPoint && cellsNow[i][j].equals("s2Grassland"))
        cellsNext[i][j] = "s1Grassland";
      
      else if(grasslandCount <= desertCount){
        
        if(cellsNow[i][j].equals("s2Grassland"))
          cellsNext[i][j] = "s1Desert";
        
        else if(cellsNow[i][j].equals("s1Grassland"))
          cellsNext[i][j] = "s2Grassland";
        
        else if(cellsNow[i][j].equals("waterSource"))
          cellsNext[i][j] = "s2Grassland";
        
        else
          cellsNext[i][j] = cellsNow[i][j];
      }
      else
        cellsNext[i][j] = cellsNow[i][j];
    }
  }
}

//DESERT CELL INFLUENCE COUNT
float countDesertNeighbours(int i, int j){
  int count = 0;
  
    for(int a = -1; a < 2; a++){
      for(int b = -1; b < 2; b++){
        try{
        if(cellsNow[i+a][j+b].equals("s1Desert"))
          count += s1Desert;
        
        else if(cellsNow[i+a][j+b].equals("s2Desert"))
          count += s2Desert;
      }
      catch(Exception e){}
    }
  }
  return count;
}

//GRASSLAND CELL INFLUENCE COUNT
float countGrasslandNeighbours(int i, int j){
  int count = 0;
  
    for(int a = -1; a < 2; a++){
      for(int b = -1; b < 2; b++){
        try{
        if(cellsNow[i+a][j+b].equals("s2Grassland"))
          count += s2Grassland;
        
        else if(cellsNow[i+a][j+b].equals("s1Grassland"))
          count += s1Grassland;
        
        else if(cellsNow[i+a][j+b].equals("waterSource"))
          count += waterSource;
      }
      catch(Exception e){}
    }
  }
  return count;
}

//UPDATE CELLSNOW TO CELLSNEXT
void update(){
  for(int i = 0; i< numRows; i++){
    for(int j = 0; j < numColumns; j++){
      cellsNow[i][j] = cellsNext[i][j];
    }
  }
}

//SHOWING STATISTICS ON THE SCREEN
void showStats(){
  PFont statFont = createFont("Times New Roman", 32);
  String  stats = "Frames Passed: " + str(frameCount);
  fill(255);
  textFont(statFont);
  text(stats, 50, 30);
  
  float numDeserts = 0;
  float total = numRows*numColumns;
  for(int i = 0; i < numRows; i++){
    for(int j = 0; j < numColumns; j++){
      if(cellsNow[i][j].equals("s1Desert") || cellsNow[i][j].equals("s2Desert"))
        numDeserts += 1;
    }
  }
  float percent = roundAny(((numDeserts/total)*100), 2);
  String desertPercent = "Desert Percentage: " + percent + "%";
  textFont(statFont);
  text(desertPercent, 500, 30);
}

//ROUNDING FUNCTION
float roundAny(float x, int d){
  float powd = pow(10, d);
  float y = x * powd;
  float z = round(y);
  return z/powd;
}

//MOUSE DRAGS TO CHANGE SQUARES
void mouseDragged(){
  try{
  int row = int((mouseX - padding)/cellSize);
  int col = int((mouseY - padding)/cellSize);
  cellsNow[row][col] = "s1Grassland";
  redraw();
  }
  catch(Exception e){}
}
