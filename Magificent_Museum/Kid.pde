class Kid{
  //FIELDS
  String name;
  String hobbies;
  int age;
  int intelligence;
  int happiness;
  boolean inTrap;
  boolean wasTrapped;
  ArrayList<Craft> craftsMade;
  
  //CONSTRUCTOR
  Kid(String n, String h, int a, int i, int hap){
    this.name = n;
    this.hobbies = h;
    this.age = a;
    this.intelligence = i;
    this.happiness = hap;
    this.inTrap = false;
    this.wasTrapped = false;
    craftsMade = new ArrayList<Craft>();
  }
  
  //METHODS
  void describe(){
    if(this.happiness >= 5)
      println("Hello! My name is", this.name, "and I'm", this.age, "years old. I like", this.hobbies + "! I'm very excited to explore this factory!!");
    
    else
      println("My name is", this.name, "and I'm", this.age, "years old. I like", this.hobbies + ". Today is gonna be sooo boring.");
    
    println();
  }
  
  void activateTrap(Trap t){
    if(this.intelligence < t.intelligence){
      println(this.name, "has activated a trap by", t.activation + ". They are now", t.description + ", and cannot continue exploring the museum.");
      println("Don't worry, they'll automatically be released when the tour ends!");
      t.kidsTrapped.add(this);
      this.happiness -= t.meanness;
      this.inTrap = true;
    }
    else{
      println(this.name, "has avoided a trap by not", t.activation + ". They are too smart to fall for these things!");
    }
    println();
  }
  
  void explore(Exhibit e){
    if(this.inTrap == false){
      if(e.name.equals("toy exhibit")){
        if(this.happiness >= 5){
          println(this.name, "happily wanders off to go look at the displays of all the toys from when their grandparents were their age.");
          println(this.name, "also wants to play with those toys, but sadly isn't allowed.");
          this.happiness += round(random(-5, e.rating));
        }
        else{
          println(this.name, "is drowning in disappointment from the moment they step into the toy exhibit.");
          println(this.name, "says: 'This exhibit isn't even as interesting as", this.hobbies +".', which is what they start doing.");
          this.happiness += round(random(-7, e.rating));
        }
      }
      else if(e.name.equals("dinosaur exhibit")){
        if(this.happiness >= 5){
          println(this.name, "heads straight for the giant tryannosaurus rex skeleton, and marvels at the skeleton's tiny little 'hands'.");
          println("They also take a selfie with this dinosaur, but can't get the tail in the picture, so they leave the poor tail out.");
          this.happiness += round(random(-5, e.rating));
        }
        else{
          println(this.name, "starts to yawn from walking around. They've seen 'Jurassic Park', which they think is way more enjoyable than this exhibit.");
          println(this.name, "then begins to rewatch the movie on their phone, even if there's no time to finish it.");
          this.happiness += round(random(-7, e.rating));
        }
      }
      else if(e.name.equals("space exhibit")){
        if(this.happiness >= 5){
          println(this.name, "is mesmerized by the interactive Earth model, and hurries to go push its buttons, lighting up different parts of the Earth.");
          println(this.name + "'s attention soon gets drawn by a model of the moon orbiting the Earth, and gleefully chases after it.");
          this.happiness += round(random(-5, e.rating));
        }
        else{
          println(this.name, "gets dizzy just by looking at all the orbiting spheres so decides to distract themselves by", this.hobbies + ".");
          println(this.name, "attempts to leave the museum, but gets caught by the host to finish the tour.");
          this.happiness += round(random(-7, e.rating));
        }
      }
      else{
        if(this.happiness >= 5){
          println(this.name, "magically travels into LaLaland, a place unknown to the museum. They are lost forever.");
          this.inTrap = true;
        }
        else{
          println(this.name, "is lured into a dark void of nothingness, where nothing exists. They are lost forever.");
          this.inTrap = true;
        }
      }
    }
    else{
      println(this.name, "is stuck in a trap! They won't be able to explore this exhibit :(");
    }
    println();
  }
  
  void talk(Kid k, String msg){
    println(this.name, "says to", k.name + ": '" + msg + "'");
    println();
  }
  
  void takePhoto(String object){
    float quality = random(0, 3);
    
    if(quality < 1)
      println(this.name, "took a really blurry photo of... what is it? The", object + "?");
    
    else if(quality < 2)
      println(this.name, "took an alright picture of a", object, "given that they are only", this.age, "years old.");
    
    else
      println(this.name, "took the most wonderful picture of a", object, "that there could ever be! They must be an aspiring photographer!");
    
    println();
  }
  
  void craft(Craft c){
    println(this.name, "discovered a crafting area and wanted to make a", c.name, "to take home with them.");
    println("*******************************LOTS OF WORK LATER*********************************************");
    
    if(this.intelligence > c.difficulty){
      println(this.name, "has successfully made a", c.name + "! Good job!");
      craftsMade.add(c);
      this.happiness += c.happiness;
    }
    else{
      println(this.name, "has failed in making a", c.name, "and now wasted a bunch of materials. Well, maybe next time...");
      this.happiness -= c.happiness;
    }
    println();
  }
  
  void expressThoughts(){
    if(this.wasTrapped){
      if(this.happiness >= 5){
        println(this.name, "says: 'I think it was alright. I liked the exhibit that I got to explore before I was trapped and couldn't explore further.'");
        println("\t 'Hopefully next time I'll get to see all the exhibits... but I probably won't come back.'");
      }
      else{
        println(this.name, "says: 'This place is terrible! What kind of a museum sets traps for their visitors?? I want my money back!'");
        println("\t 'I will never ever ever ever EVER come back to this place, I wanna get out of here now!'");
      }
    }
    else{
      if(this.happiness >=5){
        println(this.name, "says: 'I loved all the exhibits here! It was so fun and I had an amazing day, the interactives was especially cool!'");
        println("\t 'I will definitely come back again and also bring all my friends with me, I can't wait for next time!'");
      }
      else if(this.happiness >= 0){
        println(this.name, "says: 'Eh, I guess this museum is ok. There were some exhibits that weren't too bad, but there were ones that I didn't like.'");
        println("\t 'I could've spent my day", this.hobbies + ", which would've been better than this, but whatever.'");
      }
      else{
        println(this.name, "says: 'There wasn't anything interesting in this place. I didn't enjoy anything from this tour, it was such a waste of time!'");
        println("\t 'I definitely won't come back again, even if you pay me to. Unless if you pay me a million dollars... now that would be nice.");
      }
    }
    
    if(this.craftsMade.size() > 0){
      println();
      println("While on this tour,", this.name, "has proudly crafted:");
      for(int i = 0; i < this.craftsMade.size(); i++)
        println("   -", this.craftsMade.get(i).name);
    }
    
    println();
  }
    
}
