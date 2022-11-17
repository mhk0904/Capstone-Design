#include <ros.h>
#include <std_msgs/String.h>

ros::NodeHandle  nh;

std_msgs::String str_msg;
ros::Publisher chatter("chatter", &str_msg);

int sensorPin1 = A0;
int sensorPin2 = A1;
int sensorPin3 = A2;
int sensorPin4 = A3;
int sensorPin5 = A4;

int sensorValue1 = 0;
int sensorValue2 = 0;
int sensorValue3 = 0;
int sensorValue4 = 0;
int sensorValue5 = 0;

int flex_1_val = 0;
int flex_2_val = 0;
int flex_3_val = 0;
int flex_4_val = 0;
int flex_5_val = 0;

char array[100];
String flex_total;

void setup()
{
  nh.initNode();
  nh.advertise(chatter);
//  Serial.begin(9600);
}

void loop()
{

  sensorValue1 = analogRead(sensorPin1);
  sensorValue2 = analogRead(sensorPin2);
  sensorValue3 = analogRead(sensorPin3);
  sensorValue4 = analogRead(sensorPin4);
  sensorValue5 = analogRead(sensorPin5);

  flex_1_val = map(sensorValue1, 240, 470, 0, 180);
  flex_2_val = map(sensorValue2, 470, 770, 0, 180);
  flex_3_val = map(sensorValue3, 470, 770, 0, 180);
  flex_4_val = map(sensorValue4, 470, 770, 0, 180);
  flex_5_val = map(sensorValue5, 470, 770, 0, 180);
  //Serial.print("Thumb Finger : ");
  //Serial.println(flex_5_val);
  
  flex_total = String(flex_1_val)+"," + String(flex_2_val)+","+String(flex_3_val)+","+String(flex_4_val)+","+ String(flex_5_val);
  flex_total.toCharArray(array,100);
  
  str_msg.data = array;
  chatter.publish( &str_msg );
  nh.spinOnce();  
  delay(1000);
}
