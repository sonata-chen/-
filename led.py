# 123
# 匯入函式庫
import time
import RPi.GPIO as GPIO

# 設定LED和按鈕的腳位
GPIO.setmode(GPIO.BOARD)

LED1 = 16
LED2 = 18
LED3 = 22

BUTTON = 24

# 將LED接腳的工作模式設為output
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

# 關閉所有的LED
GPIO.output(LED1, GPIO.LOW)
GPIO.output(LED2, GPIO.LOW)
GPIO.output(LED3, GPIO.LOW)

# 將按鈕接腳的工作模式設為input
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# 用來記錄已經過的時間
start = 0

# 按鈕被按下的次數
press = 0

# 定義函式
def reset():
    # 關閉所有的LED，並將按鈕被按下的次數歸零
    global press
    press = 0
    GPIO.output(LED1, GPIO.LOW)
    GPIO.output(LED2, GPIO.LOW)
    GPIO.output(LED3, GPIO.LOW)

# 當按紐被按下時，這個函式會被呼叫
def button_callback(channel):
    global press
    global start

    if (press == 0):
        # 按鈕第一次被按下時，呼叫monotonic函示，紀錄當下的時間
        start = time.monotonic_ns()
        # 點亮第一個LED
        GPIO.output(LED1, GPIO.HIGH)
        press = press + 1
    elif (press == 1):
        # 點亮第二個LED
        GPIO.output(LED2, GPIO.HIGH)
        press = press + 1
    elif (press == 2):
        # 點亮第三個LED
        GPIO.output(LED3, GPIO.HIGH)
        press = press + 1
    elif (press >= 3):
        # 按鈕被按下第四次，重設
        reset()


GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback=button_callback, bouncetime=200)

# 無窮迴圈
try:
    while (True):
        # 按鈕第一次被按下後，超過十秒，就重設
        if ((time.monotonic_ns() - start >  10 * 10**9) and press >= 1):
            reset()
except KeyboardInterrupt:
    print("\nstop")
finally:
    GPIO.cleanup()
 #do something by xunil-cloud
