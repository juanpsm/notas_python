#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
#~ from demo_opts import get_device
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT,TINY_FONT, LCD_FONT
from luma.core.virtual import viewport
from itertools import repeat
from luma.core import legacy
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
import RPi.GPIO as GPIO

class Sonido:
    
    def __init__(self, canal=22):
        self._canal = canal
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._canal, GPIO.IN)
        # Desactivo las warnings por tener más de un circuito en la GPIO
        GPIO.setwarnings(False)
        GPIO.add_event_detect(self._canal, GPIO.RISING)

    def evento_detectado(self, funcion):
        if GPIO.event_detected(self._canal):
            funcion()


def main():
    #~ eyes_open = [
        #~ [[
            #~ 0x00, 0x7e, 0x81, 0xb1, 0xb1, 0x81, 0x7e, 0x00
        #~ ]],
        #~ [[
            #~ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
        #~ ]],
        #~ [[
            #~ 0x00, 0x78, 0x84, 0xb4, 0xb4, 0x84, 0x78, 0x00
        #~ ]],
        #~ [[
            #~ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
        #~ ]],
        #~ [[
            #~ 0x00, 0x20, 0x50, 0x70, 0x70, 0x50, 0x20, 0x00
        #~ ]],
        #~ [[
            #~ 0x00, 0x20, 0x60, 0x60, 0x60, 0x60, 0x20, 0x00
        #~ ]]
    #~ ]
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=2,block_orientation=0)
    #~ device = get_device()
    
    
    
    
    while True:
        #aca habría que leer los pines del mic
        def test():
        print('Sonido detectado!')
    

    sonido = Sonido()
    while True:
        time.sleep(0.0001)
        sonido.evento_detectado(test)

    GPIO.cleanup()
        
        
        
        mic = True
        if mic:
            #leer temperatura y humedad del sensor
            temp, hum = 34, 89
            #realizar las conversiones necesarias
            temp = temp
            hum = hum
            
            msg = "Oficina 12"
            print(msg)
            show_message(device, msg, fill='white', font=proportional(LCD_FONT), scroll_delay=0.05)
            
            #~ with canvas(device) as draw:
                #~ frame_ = 1
                #for i in range(0,5):
                    #print("\\"+str(i))
                    #legacy.text(draw, (0, 0), "\\"+str(i), fill="white", font=eyes_open)
                    #time.sleep(frame_)
                #~ legacy.text(draw, (0, 0), "\0",font=eyes_open[0])
                #~ time.sleep(frame_) 
                #~ legacy.text(draw, (0, 0), "\0", font=eyes_open[1])
                #~ time.sleep(frame_)
                #~ legacy.text(draw, (0, 0), "\0", font=eyes_open[2])
                #~ time.sleep(frame_)
                #~ legacy.text(draw, (0, 0), "\0", font=eyes_open[3])
                #~ time.sleep(frame_)
                #~ legacy.text(draw, (0, 0), "\0", font=eyes_open[4])
                #~ time.sleep(frame_)
                #~ legacy.text(draw, (0, 0), "\0", font=eyes_open[5])
                #~ time.sleep(5)
                # draw.rectangle(device.bounding_box, outline="white", fill="black")
            msg = 'Temperatura'
            show_message(device, msg, fill='white', font=proportional(LCD_FONT), scroll_delay=0.05)
            msg = str(temp)+'º C'
            with canvas(device) as draw:
                text(draw, (1, 0), msg, fill="white")
            time.sleep(3)
            msg = 'Humedad'
            show_message(device, msg, fill='white', font=proportional(LCD_FONT), scroll_delay=0.05)
            msg = str(hum)+'%'
            with canvas(device) as draw:
                text(draw, (1, 0), msg, fill="white")
            time.sleep(5)
    
    
#            for _ in repeat(None):
#                time.sleep(1)
#                msg = time.asctime()
#                msg = time.strftime("%S")
#                
#                with canvas(device) as draw:
#                    draw.rectangle(device.bounding_box, outline="white", fill="black")
#                    text(draw, (1, 0), msg, fill="white")
#            time.sleep(5)
#    pass
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
