# RpiKeyboard
This is a project to make a five-buttons keyboard for Raspberry Pi (I used Raspberry Pi 4 Model B 8GB ram).

## Circuit

First of all we must to make the phisical keyboard, and there is the circuit (I used Fritzing to draw it), and we can already cover it with a box, or customize it

[![Keyboard](https://raw.githubusercontent.com/Nicrom098195/RpiKeyboard/main/Keyboard.png)]()

## Software

After we have to install the keyboard software, that's easy than how it looks, we must only to downoad it:

### Downloading code

To download the code we need to have installed *git*, to install git run
```sh
sudo apt install git
```
After we can download the code typing
```sh
cd ~
git clone https://github.com/Nicrom098195/RpiKeyboard.git
```
### Installing dependencies

To make working the keyboard we need to have installed the right dependencies:

```sh
pip3 install pynput
```

### Running the code

If we don't see an error installing the dependencies, we can run the code by typing
```sh
cd ~/RpiKeyboard
python3 keyboard.py
```

## Run the keyboard automatically booting the Pi

We can run automatically the keyboard when we turn on our Raspberry Pi, but this will work only if we are logged in to the profile

To autostart the keyboard, let's make an autostart script
```sh
mv ~/RpiKeyboard/keyboard.desktop ~/.config/autostart/keyboard.desktop
```

And now, when you reboot the Pi, the keyboard will work automatically
