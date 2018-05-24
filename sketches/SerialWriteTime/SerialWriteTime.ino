int time = 0;

void setup() 
{
  Serial.begin(9600);
}

void loop() 
{
 Serial.println(time);
 time += 1;
 delay(1000);
 Serial.flush();

 if(time > 50) {
  time = 0;
 }
}
