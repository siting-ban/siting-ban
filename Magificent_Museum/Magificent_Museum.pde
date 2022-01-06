//TITLE: Magnificent Museum
//DATE LAST MODIFIED: 03/26/2021

void setup(){
  
  //Trap (activation, description, intelligence, meanness)
  Trap dangerSign = new Trap("touching the danger sign", "stuck to that sign", 5, 2);
  Trap artifact = new Trap("grabbing the artifact on a pedestal", "trapped in a cage", 8, 7);
  Trap rope = new Trap("tugging the end of a rope hanging off the ceiling", "caught in a net", 6, 5);
  
  //Place (name, display, rating) **NOTE: Please do not change the names of the exhibits as this museum only offers these current exhibits.
  Exhibit toyExhibit = new Exhibit("toy exhibit", "toys from all around the world during different time periods", 6);
  Exhibit dinosaurExhibit = new Exhibit("dinosaur exhibit", "skeletons and models of many types of dinosaurs, including the tyrannosaurus rex", 7);
  Exhibit spaceExhibit = new Exhibit("space exhibit", "a model of the solar system highlighting planet Earth", 6);
  
  //Kid (name, hobby, age, intelligence, happiness)
  Kid liam = new Kid("Liam", "running around screaming", 7, 3, 10);
  Kid emma = new Kid("Emma", "lying in bed", 10, 6, 5);
  Kid helen = new Kid("Helen", "going on the phone", 13, 8, 4);
  Kid ava = new Kid("Ava", "pondering the meaning of life", 16, 10, 3);
  Kid oliver = new Kid("Oliver", "playing video games on a tree", 9, 4, 8);

  //Craft (name, difficulty, happiness)
  Craft yoyo = new Craft("yoyo", 7, 4);
  Craft dinosaurEgg = new Craft("dinosaur egg", 2, 2);
  Craft kaleidoscope = new Craft("kaleidoscope", 8, 3);
  
  //Museum (name, year established)
  Museum magnificentMuseum = new Museum("Magificent Museum", 2000);
  
  //Host (name, hobby, age, museum)
  Host maria = new Host("Maria", "pretending to do nothing", 28, magnificentMuseum);
  
  //INTRODUCTIONS
  maria.describe();
  maria.introduce(liam);
  maria.introduce(emma);
  maria.introduce(helen);
  maria.introduce(ava);
  maria.introduce(oliver);

  //FIRST EXHIBIT: TOYS
  maria.startTour();
  maria.tour(toyExhibit);
  
  //Children explore the exhibit
  liam.explore(toyExhibit);
  emma.explore(toyExhibit);
  helen.explore(toyExhibit);
  ava.explore(toyExhibit);
  oliver.explore(toyExhibit);

  liam.activateTrap(dangerSign);
  liam.talk(oliver, "Help me! I'm stuck to a danger sign!");
  oliver.talk(emma, "Did you hear something?");
  emma.talk(oliver, "No, let's go and look at something else!");
  helen.activateTrap(dangerSign);
  
  ava.takePhoto("nutcracker");
  
  //Children making crafts
  emma.craft(yoyo);
  helen.craft(yoyo);
  oliver.craft(yoyo);
  
  //SECOND EXHIBIT: DINOSAURS
  maria.tour(dinosaurExhibit);
  
  //Children explore the exhibit
  liam.explore(dinosaurExhibit);
  emma.explore(dinosaurExhibit);
  helen.explore(dinosaurExhibit);
  ava.explore(dinosaurExhibit);
  oliver.explore(dinosaurExhibit);
  
  emma.activateTrap(artifact);
  helen.activateTrap(artifact);
  
  oliver.takePhoto("velociraptor model");
  dangerSign.release(liam);
  liam.talk(oliver, "I was stuck in a trap and called for help and you just ignored me! I'm mad at you now. Hmph.");
  oliver.talk(liam, "Oops... sorry, I didn't hear. Well, we can run around in circles now!");
  
  //Children making crafts
  liam.craft(dinosaurEgg);
  oliver.craft(dinosaurEgg);
  ava.craft(dinosaurEgg);
  helen.craft(dinosaurEgg);
  
  //THIRD EXHIBIT: SPACE
  maria.tour(spaceExhibit);
  
  //Children explore the exhibit
  liam.explore(spaceExhibit);
  emma.explore(spaceExhibit);
  helen.explore(spaceExhibit);
  ava.explore(spaceExhibit);
  oliver.explore(spaceExhibit);

  ava.activateTrap(rope);
  oliver.activateTrap(rope);
  
  helen.takePhoto("space suit");
  
  //Children making crafts
  helen.craft(kaleidoscope);
  ava.craft(kaleidoscope);
  
  //END TOUR & THOUGHTS
  maria.endTour();
  liam.expressThoughts();
  emma.expressThoughts();
  helen.expressThoughts();
  ava.expressThoughts();
  oliver.expressThoughts();

  //TO SEE WHO WAS TRAPPED
  //dangerSign.printKidsTrapped();
  //artifact.printKidsTrapped();
  //rope.printKidsTrapped();
}
