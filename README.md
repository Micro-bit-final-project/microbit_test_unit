## Micro:bit Test Unit
This repository contains a python script used to check whether an UART communication can be established between a Micro:bit and a computer.

### Set up
Make sure you are running python 3. This software has been tested on python 3.8.6.

### Repo structure
* [microbit_test_unit.py](https://github.com/Micro-bit-final-project/microbit_test_unit/blob/master/microbit_test_unit.py "microbit_test_unit.py"): Python script used to communicate via UART with a Micro:bit.
* [microbit.png](https://github.com/Micro-bit-final-project/microbit_test_unit/blob/master/microbit.png "microbit.png"): Image used by the python script to provide an easy to understand output to the user.

### How to check if the Micro:bit is working
Before running this script make sure you also download our [Micro:bit serial](https://github.com/Micro-bit-final-project/microbit_serial) python module. Make sure you have this directories structure:
```
-- microbit_dev/
  |-- microbit_serial/
  |-- microbit_test_unit/
```

The root folder name does not matter, but please make sure you keep the two folders [microbit_serial](https://github.com/Micro-bit-final-project/microbit_serial) and [microbit_test_unit](https://github.com/Micro-bit-final-project/microbit_test_unit) under the same root.
Then to check a connection can be established, plug in your Micro:bit (make sure you first flash [this](https://github.com/Micro-bit-final-project/microbit) on it first), then run [microbit_test_unit.py](https://github.com/Micro-bit-final-project/microbit_test_unit/blob/master/microbit_test_unit.py "microbit_test_unit.py") (better in a console window than in an IDE) and you should be prompted with a window containing a Micro:bit image that rotates based on how you hold your Micro:bit. Furthermore, whenever the `S` key is pressed, you should be able to see what data the computer sent and what data the Micro:bit sent back. If you don't see a Micro:bit image on your screen the reason is that your computer is not receiving complete (or any at all) information from the Micro:bit. If when your press `S` the data sent differs from the data received then something is probably wrong with the Micro:bit's serial buffer.
