int in1 = 7;    // Pin IN1 del L298N
int in2 = 8;    // Pin IN2 del L298N
int ena = 9;    // Pin ENA (PWM) del L298N

void setup() {
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(ena, OUTPUT);
  Serial.begin(9600);  // Comunicación serial a 9600 baudios
}

void loop() {
  if (Serial.available() > 0) {
    int speed = Serial.parseInt();  // Leer la velocidad (0-255)
    int direction = Serial.parseInt();  // Leer la dirección (0 o 1)
    
    if (direction == 1) {  // Girar hacia adelante
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
    } else if (direction == 0) {  // Girar hacia atrás
      digitalWrite(in1, LOW);
      digitalWrite(in2, HIGH);
    }

    analogWrite(ena, speed);  // Control de velocidad con PWM (0-255)
    Serial.println("Motor controlado");
  }
}
