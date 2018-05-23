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
  Serial.println(potval + ": " + time);
  time += 1;
  delay(1000);
  Serial.flush();

  if (time > 50) { time = 0; }
}
