import lib.fileHelper
import smbus

#SMBus(0) - Model B

bus = smbus.SMBus(1)

#I2C address of sensor
address1 = 0x48
address2 = 0x4A

def temperature(address):
    rvalue0 = bus.read_word_data(address,0)
    rvalue1 = (rvalue0 & 0xff00) >> 8
    rvalue2 = rvalue0 & 0x00ff
    rvalue = (((rvalue2 * 256) + rvalue1) >> 4) *0.0625
    return rvalue

def celciusToFahrenheit(celTemp):
    return (celTemp*1.8+32)

def get_current_temps():
    #this is where you would return the current temperatures.
    #need sensors hooked up for this to work.
    #Currently returning array of temperatures
    outTemp = celciusToFahrenheit(temperature(address1))
    inTemp = celciusToFahrenheit(temperature(address2))
    return [outTemp,inTemp]

lib.fileHelper.log_temps(get_current_temps())
