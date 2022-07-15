#include <wiringPi.h>
#include <stdio.h>

#define BtnPin		24
#define Gpin		21
#define Rpin	    22

void LED(char* color)
{
	pinMode(Gpin, OUTPUT);
	pinMode(Rpin, OUTPUT);
	if (color == "RED")
	{
		digitalWrite(Rpin, HIGH);
		digitalWrite(Gpin, LOW);
	}
	else if (color == "GREEN")
	{
		digitalWrite(Rpin, LOW);
		digitalWrite(Gpin, HIGH);
	}
	else
		printf("LED Error");
}

int main(void)
{
	if(wiringPiSetup() == -1){ //when initialize wiring failed,print messageto screen
		printf("setup wiringPi failed !");
		return 1; 
	}

	pinMode(BtnPin, INPUT);
	LED("GREEN");
	
	while(1){
		if(0 == digitalRead(BtnPin)){
			delay(10);
			if(0 == digitalRead(BtnPin)){
				LED("RED");	
			}
		}
		else if(1 == digitalRead(BtnPin)){
			delay(10);
			if(1 == digitalRead(BtnPin)){
				while(!digitalRead(BtnPin));
				LED("GREEN");
                printf("Button is pressed\n");	
			}
		}
	}
	return 0;
}
