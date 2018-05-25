int time = 0;
int potpin = A0;
int potval;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  potval = analogRead(potpin);
  Serial.println(String(time) + ": " + String(potval));
  time += 1;
  delay(500);
  Serial.flush();
}
