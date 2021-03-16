# Smartgarden Sensors

You will need:
- [Google Coral Environmental Sensor Board](https://coral.ai/products/environmental)
and a compatible device to host the sensor board and InfluxDB. I'm using a Raspberry 3 model B V1.2, but feel free to check out the other [compatible devices](https://coral.ai/products/environmental#compatible-with-coral-and-raspberry-pi-boards).

## Setup Coral Environmental Sensor Board

![alt Environmental Sensor Board](sensorBoard.webp)

Simply attach the Environmental Sensor Board to 40-pin header on the Raspberry Pi. 
You can now power the Raspberry Pi and it will automatically apply the device tree and configure the header pins.

Now install the needed libraries and driver - from your Raspberry Pi:

```
echo "deb https://packages.cloud.google.com/apt coral-cloud-stable main" | sudo tee /etc/apt/sources.list.d/coral-cloud.list

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt update

sudo apt upgrade

sudo apt install python3-coral-enviro
```

Reboot the Raspberry Pi with `sudo reboot now` to allow the changes to be applied.

See for more details: [Attach Sensor Board](https://coral.ai/docs/enviro-board/get-started/#1-attach-the-sensor-board)

You can use a demo script from Google Coral to check if everything works - [demo](https://coral.googlesource.com/coral-cloud/+/refs/heads/master/python/coral-enviro/coral/enviro/enviro_demo.py).

## Setup InfluxDB
