const int lSensor = A1;
int time = 0;
int lightVal;

void setup() {
  pinMode(lSensor, INPUT);
  Serial.begin(9600);
}

void loop() {
  lightVal = analogRead(lSensor);
  Serial.println(String(time) + ": " + String(lightVal));
  time += 1;
  delay(50);
  Serial.flush();
}
