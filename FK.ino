/* Libraries */
#include "Servo.h"
#include "IRremote.h"


/* Create IRremote Object */
const int receiver = 15;
IRrecv irrecv(receiver);
decode_results results;


/* Create Servo Objects */

// Servo Objects
Servo servo_1;
Servo servo_2;
Servo servo_3;
Servo servo_4;
Servo servo_5;
Servo servo_6;

// Servo Positions
int serv1Pos, serv2Pos, serv3Pos, serv4Pos, serv5Pos, serv6Pos;   //current
int serv1Ppos, serv2Ppos, serv3Ppos, serv4Ppos, serv5Ppos, serv6Ppos;   //previous

void setup() {
  // Where servos attach
  servo_1.attach(3);
  servo_2.attach(5);
  servo_3.attach(7);
  servo_4.attach(9);
  servo_5.attach(11);
  servo_6.attach(13);

  // Servo initial positions
  serv1Pos = 90;
  servo_1.write(serv1Pos);
  serv2Pos = 10;
  servo_2.write(serv2Pos);
  serv3Pos = 30;
  servo_3.write(serv3Pos);
  serv4Pos = 135;
  servo_4.write(serv4Pos);
  serv5Pos = 75;
  servo_5.write(serv5Pos);
  serv6Pos = 60;
  servo_6.write(serv6Pos);

  // Start the receiver
  irrecv.enableIRIn();
}

void loop() {
  if (irrecv.decode(&results)) { // have we received an IR signal?
    
    switch (results.value) {
      
        /* Servo 1 positioning, Base */ 
        case 0xFF22DD: // "FAST BACK" button pressed, Servo 1 goes CCW
                    serv1Ppos = serv1Pos;
                    if (serv1Pos == 0) {
                      Serial.println("Turn back!");
                      break;                        
                    } 
                    for (int pos = serv1Pos; pos >= serv1Ppos - 30; pos -= 1) {
                      servo_1.write(pos);
                      serv1Pos = pos;
                      delay(10);
                    }                                      
                    Serial.print("Servo 1 is at position: "); 
                    Serial.println(serv1Pos);                     
                    break;
                    
    }
    irrecv.resume();
  }
}                    
