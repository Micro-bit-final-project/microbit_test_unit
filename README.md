
## Micro:bit Test Unit
This repository contains a python script used to check whether a working controller for 3M is connected or not.

### Set up
Make sure you are running python 3. This software has been tested on python 3.8.6.

### Repo structure
* [microbit_test_unit.py](https://github.com/Micro-bit-final-project/microbit_test_unit/blob/master/microbit_test_unit.py "microbit_test_unit.py"): Python script used to communicate with the controller and test its functionality.
*  [dpcomic](https://github.com/Micro-bit-final-project/microbit_test_unit/tree/master/dpcomic "dpcomic folder"): Folder containing the DPComic font and uts license.

### How to check if the Micro:bit is working
Before running this script make sure you also download our [Micro:bit serial](https://github.com/Micro-bit-final-project/microbit_serial) python module. Make sure you have this directories structure:
```
-- microbit_dev/
  |-- microbit_serial/
  |-- microbit_test_unit/
```

The root folder name does not matter, but please make sure you keep the two folders [microbit_serial](https://github.com/Micro-bit-final-project/microbit_serial) and [microbit_test_unit](https://github.com/Micro-bit-final-project/microbit_test_unit) under the same root.
Then to check a connection can be established, plug in your Micro:bit (make sure you first flash [this](https://github.com/Micro-bit-final-project/microbit) on it), then run [microbit_test_unit.py](https://github.com/Micro-bit-final-project/microbit_test_unit/blob/master/microbit_test_unit.py "microbit_test_unit.py") (better in a console window than in an IDE) and you should be prompted with a window containing information about what button is currently being pressed (either none or: U, L, D, R), what the value read on the potentiometer output is (between 5±5 and 1023) and what the value read from the DC motor is (between 70±10 and 1023) . Furthermore, the LEDs should gradually go from 8 on to 8 off and again in an inifinite loop. If you do not experience this behaviour, check you wired everything up properly.
