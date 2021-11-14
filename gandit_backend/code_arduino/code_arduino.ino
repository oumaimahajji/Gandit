void setup(){
  //pinMode(A0, INPUT);
  pinMode(A0, INPUT);
  pinMode(A5, INPUT);
  Serial.begin(9600);
}

void measurePressure(){

  //pour imprimer les donnees du capteur du pression -> doigt 1
  // id du capteur espace valeur
  Serial.print("P1 ");
  Serial.print(analogRead(A0));
  //pour imprimer les donnees du capteur du flexion -> doigt 2 
  // id du capteur espace valeur
   Serial.print(" F2 ");
  Serial.println(analogRead(A5));
  

}

void loop() {
  measurePressure();
  delay(100);
}
