class Trap{
  //FIELDS
  String activation;
  String description;
  int intelligence;
  int meanness;
  ArrayList<Kid> kidsTrapped;
  
  //CONSTRUCTOR
  Trap(String a, String d, int i, int m){
    this.activation = a;
    this.description = d;
    this.intelligence = i;
    this.meanness = m;
    kidsTrapped = new ArrayList<Kid>();
  }
  
  //METHODS
  void release(Kid k){
    println(k.name, "has miraculously been released from the trap they activated and now can continue their tour!");
    println();
    k.inTrap = false;
  }
  
  void printKidsTrapped(){
    println("================================================================");
    println("Kids that were", this.description);
    println("================================================================");
    
    if(kidsTrapped.size() > 0){
      for(int i = 0; i < kidsTrapped.size(); i++)
        println("   -", kidsTrapped.get(i).name);
    }
    else
      println("None");
    
    println();
  }
}
