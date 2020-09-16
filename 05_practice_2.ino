#define PIN_LED 7

 

unsigned int count, toggle;

 

 

 

void setup() {

 

  pinMode(PIN_LED, OUTPUT);

 

  count =toggle =0;

 

  digitalWrite(PIN_LED, toggle); // turn off LED.

 

}

 

 

 

void loop() {

 

  ++count;

  Serial.println( toggle);

 

  toggle = toggle_state(toggle); //toggle LED value.

 

  digitalWrite(PIN_LED, toggle); // update LED status.

 

 

  if ( count == 1){ 

    delay(1000); // wait for 1,000 milliseconds

  }

 

  else if (count > 1) {

    delay(100);

  }

}

 

 

 

int toggle_state(int toggle) {

  while (count == 1) {

    toggle = 0;

    return toggle; 

  }

  while ((count  >= 2) && (count  < 12)) {

    toggle = (count + 1) % 2 ;

    return toggle;

  }

  while (count >= 12) {

    toggle = 1;

    return toggle;    

  }

}

