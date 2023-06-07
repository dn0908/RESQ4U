import sys
sys.path.append('/home/roboin/ResQ4U/RaspberryPi_src/common')
from imports import *

from pan_tilt.pan_tilt import PanTilt
from serial_communication.arduino_serial import SerialWrapper
from camera_detection.detect_person_v2 import PersonDetector
from pan_tilt.stepmotor_control import StepMotorController
from alert.relay_control import Relay
# from alert.emergency_call import EmergencyCaller



if __name__ == "__main__":
    print('Hello ResQ4U')

    # inits
    pan_tilt = PanTilt(config)
    arduino = SerialWrapper(device=config.arduino_uno)
    detector = PersonDetector(pan_tilt, show_image=True, record_vid=False)
    searchLight = Relay(pin = config.searchlight)
    alertLight = Relay(pin = config.alert)
    # caller = EmergencyCaller()

    # Turn Search Light OFF
    searchLight.off()
    print('Searchlight OFF ...')

    # Turn Alert Siren OFF
    alertLight.on()
    print('Alert OFF ...')
    # alertLight.toggle()
    # print('Alert TOGGLE ed')

    # DETECT
    while True:
        mode = detector.detect()
        print("mode", mode)
        if (mode == 0): 
            print("inside mode 0")
            # arduino.send_flag("d")
            time.sleep(0.5)
        elif (mode == 1):
            print("inside mode 1")
            break
    
    time.sleep(1)
    arduino.send_flag("f")
    
    ###################### WHEN DETECTED LAUNCH! #######################
    # # Call for HELP
    # caller.callHELP()

    # Turn Search Light ON
    searchLight.on()
    print('Searchlight ON ...')
    
    # Turn Alert Siren ON
    alertLight.off()
    print('Alert ON ...')

    # Read Arduino
    while(arduino.end_flag == False):
        arduino.check_end_flag()
    
    # #################### AFTER LAUNHCH RETURsN INIT ####################
    
    print("END ... Returning to initial state ...")
    
    # PanTilt to initial State
    pan_tilt.return_to_init()
    
    # Turn Search Light OFF
    searchLight.off()
    print('Searchlight OFF ...')

    # Turn Alert Siren OFF
    alertLight.on()
    print('Alert OFF ...')
    
    print('ResQ4U Bye')