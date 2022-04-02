from m5stack import *
from m5ui import *
from uiflow import *
from easyIO import *

setScreenColor(0x222222)


correctWord = ".-. .- -.. .- .-."
userWord = ""

userOutput = M5TextBox(149, 109, "morse code", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
status = M5TextBox(149, 109, "", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)

pin0 = machine.Pin(21, mode=machine.Pin.OUT, pull=0x00)
pin0.off()


wait_ms(5)

while True:

  if digitalRead(5):
    userWord = userWord + "-"
    userOutput.setText(userWord)
    time.sleep(0.3) # Sleep for 1 seconds
  elif digitalRead(17):
    userWord = userWord + "."
    userOutput.setText(userWord)
    time.sleep(0.3) # Sleep for 1 seconds
  elif digitalRead(16):
    userWord = ""
    userOutput.setText(userWord)
    status.setText("")
  elif digitalRead(22):
    userWord = ""
    userOutput.setText(userWord)
    status.setText("")
  elif digitalRead(23):
    status = M5TextBox(149, 109, "Correct!", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
    userWord = ""
    userOutput.setText(userWord)
  elif digitalRead(1):
    userWord = userWord + " "
    userOutput.setText(userWord)
    time.sleep(0.3) # Sleep for 1 seconds
    
  if (userWord == correctWord):
    pin0.on()
    status = M5TextBox(149, 109, "Correct!", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
    userWord = ""
    userOutput.setText(userWord)
  wait_ms(8)


