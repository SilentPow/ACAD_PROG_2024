
const int HAUT_GAUCHE = D0;
const int HAUT_DROIT = D1;
const int MID_DROIT = D2;
const int LOW_DROIT = D3;
const int LOW_GAUCHE = D4;
const int MID_GAUCHE = D5;

const int PIN_A = D6;
const int PIN_E = D7;
const int PIN_I = 3;
const int PIN_O = 1;
const int PIN_U = 10;
void setup() {
  pinMode(HAUT_GAUCHE, INPUT_PULLUP);
  pinMode(HAUT_DROIT, INPUT_PULLUP);
  pinMode(MID_DROIT, INPUT_PULLUP);
  pinMode(LOW_DROIT, INPUT_PULLUP);
  pinMode(LOW_GAUCHE, INPUT_PULLUP);
  pinMode(MID_GAUCHE, INPUT_PULLUP);

  pinMode(PIN_A, OUTPUT);
  pinMode(PIN_E, OUTPUT);
  pinMode(PIN_I, OUTPUT);
  pinMode(PIN_O, OUTPUT);
  pinMode(PIN_U, OUTPUT);

}

void loop() {
  if(digitalRead(HAUT_GAUCHE) && !digitalRead(HAUT_DROIT) && !digitalRead(MID_DROIT) && !digitalRead(LOW_DROIT) && !digitalRead(LOW_GAUCHE) && !digitalRead(MID_GAUCHE)) {
    digitalWrite(PIN_A, HIGH);
  } else {
    digitalWrite(PIN_A, LOW)
  }

  if(!digitalRead(HAUT_GAUCHE) && !digitalRead(HAUT_DROIT) && digitalRead(MID_DROIT) && !digitalRead(LOW_DROIT) && !digitalRead(LOW_GAUCHE) && !digitalRead(MID_GAUCHE)) {
    digitalWrite(PIN_E, HIGH);
  } else {
    digitalWrite(PIN_E, LOW)
  }

  if(!digitalRead(HAUT_GAUCHE) && digitalRead(HAUT_DROIT) && !digitalRead(MID_DROIT) && !digitalRead(LOW_DROIT) && !digitalRead(LOW_GAUCHE) && digitalRead(MID_GAUCHE)) {
    digitalWrite(PIN_I, HIGH);
  } else {
    digitalWrite(PIN_I, LOW)
  }

  if(digitalRead(HAUT_GAUCHE) && !digitalRead(HAUT_DROIT) && digitalRead(MID_DROIT) && !digitalRead(LOW_DROIT) && digitalRead(LOW_GAUCHE) && !digitalRead(MID_GAUCHE)) {
    digitalWrite(PIN_O, HIGH);
  }  else {
    digitalWrite(PIN_O, LOW)
  }

  if(digitalRead(HAUT_GAUCHE) && !digitalRead(HAUT_DROIT) && !digitalRead(MID_DROIT) && digitalRead(LOW_DROIT) && digitalRead(LOW_GAUCHE) && !digitalRead(MID_GAUCHE)) {
    digitalWrite(PIN_U, HIGH);
  }  else {
    digitalWrite(PIN_U, LOW)
  }
}