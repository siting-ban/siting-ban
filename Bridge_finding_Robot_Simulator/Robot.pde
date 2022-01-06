class Robot{
  //FIELDS
  int x, y, size;              //Position & size
  int speed;                   //Robot speed (pixels/frame)
  int dist;                    //Distance travelled within one step
  int currentStep;             //Current step size
  String algo;                 //Algorithm used
  PImage image;                //Image used
  boolean foundBridge;         //Has robot found bridge
  ArrayList<Integer> markers;  //X positions for where markers should be drawn
  
  //CONSTRUCTOR (Sets values to fields)
  Robot(int xPos, int yPos, int s, String a, PImage i){
    this.x = xPos;
    this.y = yPos;
    this.size = 100;
    this.speed = s;
    this.algo = a;
    this.image = i;
    this.foundBridge = false;
    this.dist = 0;
    this.currentStep = stepSize;
    this.markers = new ArrayList<Integer>();
  }
  
  //METHODS
  void race(PVector bridge){
    if(foundBridge == false){                      //If robot has not found bridge yet:
      if(this.dist <= this.currentStep){           //If the distance travelled is less than/equal to the current step size:
         this.x += this.speed;                     //Update x position by speed
         this.dist += abs(this.speed);             //Update distance travelled by absolute value of speed
      }
          
      else{                                        //If distance travelled is greater than current step size:
        this.speed = -this.speed;                  //Change direction
          
        if(this.algo.equals("cg"))                 //If the robot is using a cg algorithm:
          this.currentStep += stepSize;            //Add the original step size to the current step size
          
        else                                       //If the robot is using da:
          this.currentStep = 2*this.currentStep;   //Double the current step size
          
        this.dist = 0;                             //Clear the distance travelled
        this.markers.add(this.x + (this.size/2));  //Add this x position to the markers ArrayList
      }
        
      if(this.x <= bridge.x)                       //If robot's position is smaller than/equal to the bridge's x position:
        foundBridge = true;                        //It has found the bridge
    }
  }
     
  void display(){
     image(this.image, this.x, this.y, this.size, this.size);    //Draws the image of the robot on the screen
  }
  
}
