int led = 13;
 
void setup(){
    pinMode(led, OUTPUT);
    Serial.begin(9600);
}
 
void serialEvent(){
    byte in = Serial.read();
    if(in == 0){
        digitalWrite(led, LOW);
    }else if(in == 1){
        digitalWrite(led, HIGH);
    }
}
 
void loop(){
    delay(1000);
}


