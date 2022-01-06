class Host{
  //FIELDS
  String name;
  String hobbies;
  int age;
  Museum museum;
  ArrayList<Kid> kids;
  
  //CONSTRUCTOR
  Host(String n, String h, int a, Museum m){
    this.name = n;
    this.hobbies = h;
    this.age = a;
    this.museum = m;
    kids = new ArrayList<Kid>();
  }
  
  //METHODS
  void describe(){
    println("=====================================================================================================================================");
    println("Good day everyone, and welcome to the", this.museum.name + "! This museum was established in the year", this.museum.yearEstablished + ".");
    println("My name is", this.name, "and I am", this.age, "years old. I enjoy", this.hobbies + "!");
    println("I will be your host for today and take you on a fantastic tour of this museum. I hope you all are very excited!");
    println();
    println("Before we begin, let us familiarize with each other with introductions. :)");
    println("=====================================================================================================================================");
    println();
  }
  
  void introduce(Kid k){
    kids.add(k);
    k.describe();
  }
  
  void startTour(){
    println("=====================================================================================================================================");
    println("Alright! Let us start our journey! Remember to follow me and beware of any traps!");
    println("=====================================================================================================================================");
    println();
  }
  
  void tour(Exhibit e){
    println("=====================================================================================================================================");
    println("This is the", e.name + "! Here, you will find", e.display + ".");
    println("Feel free to look around, but be careful!");
    println("=====================================================================================================================================");
    println();
  }
  
  
  void endTour(){
    println("=====================================================================================================================================");
    println("Thank you for joining me on this tour of the", museum.name + "! We have now reached the end of this tour.");
    println("Let's first check how many children are still here with me:");
    
    int numHere = 0;
    for(int i = 0; i < kids.size(); i++){
      if(kids.get(i).inTrap == false){
        println("   -", kids.get(i).name);
        numHere ++;
      }
    }
    
    if(numHere < kids.size()){
      println("Oh no! Some kids have activated the traps here in the museum. Let's get them back with us.");
      println("***************************************RELEASE KIDS FROM TRAPS*******************************************");
      for(int i = 0; i < kids.size(); i++){
        if(kids.get(i).inTrap){
          kids.get(i).inTrap = false;
          kids.get(i).wasTrapped = true;
        }
      }
    }
    println("Now, one final question: how did you enjoy this experience?");
    println("=====================================================================================================================================");
    println();
  }
  
  void printTrappedHistory(){
    
  }
}
