#!/home/pi/server
# coding=utf-8
#ʹÓó¬Éù²¨²â¾àģ¿éʱ,VCC½ÓÊ÷ݮÅɵÄ5V,GND½ÓÊ÷ݮÅÉGND¡£trig½ÓÊ÷ݮÅÉ38£¬echo½ÓÊ÷ݮÅÉ40.
#GPIO±àÂ뷽ʽΪBOARD£¡£¡
import  RPi.GPIO as GPIO
import time

PWMA = 18
AIN1   =  22
AIN2   =  27

PWMB = 23
BIN1   = 25
BIN2  =  24

def t_up(speed,t_time):
        L_Motor.ChangeDutyCycle(speed)
        GPIO.output(AIN2,False)#AIN2
        GPIO.output(AIN1,True) #AIN1

        R_Motor.ChangeDutyCycle(speed)
        GPIO.output(BIN2,False)#BIN2
        GPIO.output(BIN1,True) #BIN1
        time.sleep(t_time)
        
def t_stop(t_time):
        L_Motor.ChangeDutyCycle(0)
        GPIO.output(AIN2,False)#AIN2
        GPIO.output(AIN1,False) #AIN1

        R_Motor.ChangeDutyCycle(0)
        GPIO.output(BIN2,False)#BIN2
        GPIO.output(BIN1,False) #BIN1
        time.sleep(t_time)
        
def t_down(speed,t_time):
        L_Motor.ChangeDutyCycle(speed)
        GPIO.output(AIN2,True)#AIN2
        GPIO.output(AIN1,False) #AIN1

        R_Motor.ChangeDutyCycle(speed)
        GPIO.output(BIN2,True)#BIN2
        GPIO.output(BIN1,False) #BIN1
        time.sleep(t_time)

def t_left(speed,t_time):
        L_Motor.ChangeDutyCycle(speed)
        GPIO.output(AIN2,True)#AIN2
        GPIO.output(AIN1,False) #AIN1

        R_Motor.ChangeDutyCycle(speed)
        GPIO.output(BIN2,False)#BIN2
        GPIO.output(BIN1,True) #BIN1
        time.sleep(t_time)

def t_right(speed,t_time):
        L_Motor.ChangeDutyCycle(speed)
        GPIO.output(AIN2,False)#AIN2
        GPIO.output(AIN1,True) #AIN1

        R_Motor.ChangeDutyCycle(speed)
        GPIO.output(BIN2,True)#BIN2
        GPIO.output(BIN1,False) #BIN1
        time.sleep(t_time)    
 # 如果RPi.GRIO检测到一个引脚已经被设置成了非默认值，那么你将看到一个警告信息。
GPIO.setwarnings(False)
# 针脚的编码方式是BCM
GPIO.setmode(GPIO.BCM)
# 将引脚设置为输出模式
GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(PWMA,GPIO.OUT)

GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)
GPIO.setup(PWMB,GPIO.OUT)

# 将PWMA引脚初始化为PWM实例 ，频率为100Hz
L_Motor= GPIO.PWM(PWMA,100)
# 开始脉宽调制，参数范围为： (0.0% <= dc <= 100.0%)
L_Motor.start(0)

R_Motor = GPIO.PWM(PWMB,100)
R_Motor.start(0)

try:
    while True:
        t_up(50,3)
        t_down(50,3)
        t_left(50,3)
        t_right(50,3)
        t_stop(3)
except KeyboardInterrupt:
    GPIO.cleanup()

