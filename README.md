# Power Systems Project Lab
## Microcontroller Buck Converter Design
The project description given was to build an adjustable DC-DC buck converter with digital control from a microcontroller to be able to power a range of devices. 
It was decided the input voltage of the converter would be 8-14 V with an output range of 2.5-5.5 V at 2 A max.\
Originally, a basic buck converter was designed with an input capacitor, MOSFET, diode, and output LC filter commonly seen in most power electronics theory examples.

The next addition to the design was a MOSFET gate driver (First the Infineon IR2125, then the Onsemi NCP5901).

The next iteration included:\
  -Pi LC EMI filter between the power source and the high side MOSFET\
  -Input negative thermal coefficient (NTC) resistor to limit inrush current\
  -Input/output current sensing with Monolith Power Systems MCS1806 Linear Hall Effect Current Sensor\
  -Input/output voltage sensing with Analog Devices LT1112 Low Power Precision Amplifier\
  -Changed Onsemi NCP5901 MOSFET Gate Driver to Onsemi NCP3420 to better fit ESP32 logic level voltages
  
Finally, the design was changed to replace parts mentioned above:\
  -Texas Instruments INA219 for current sensing\
  -Texas Instruments INA157 for voltage sensing\
PCB was designed to be 2-layer to minimize cost, manufacturing difficulty, 

Future work includes:\
  -MOSFET gate driver redesign\
  -Change microcontroller from ESP32 to Arduino Nano (Preferably IoT version)\
  -Redesign PCB
    -Inductor component replacement and relocation\
    -Decrease EMI filter current loop area\
    -Add testpoints/vias/pads\
    -Use copper pours for input/output connectors to decrease resistance\
    -Add more documentation/notes to board sikscreen\
  -Finish automated test equipment (ATE) programs
