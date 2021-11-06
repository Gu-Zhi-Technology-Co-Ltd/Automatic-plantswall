# Automatic-plantswall
Automatic-plantswall\
南港高中數位科學實驗班 AIOT智慧務農植物牆
## Description
Use Raspberry Pi to detect the temperature and humidity of the plantswall, and automatically water and switch lights. You can use your mobile phone to remotely monitor the various values of the plantswall.

## Setup
```terminal
sudo python3 main.py 
```
## Environment
- Android 8+
- Python 3.7

## Features
- Detect temperature and humidity.
- Real-time remote monitoring of values using Android.



## Structure
```
.
├── .gradle
├── .idea                
├── app    
│   └── src
│       └── main
│           ├── myapplication123
│               ├── MainActivity.kt 
│               ├── MainActivity2.kt
│               └── socket.kt 
│           └── AndroidManifest.xml
├── python                      
│   ├── led_blink.py
│   ├── main.py              
│   ├── pump_switch.py  
│   └── read_sht10.py   
├── LICENSE
└── README.md                      
```

## Developers
- 姜義新 (software)
- 白秉軒 (software)
- 許崇嘉 (software)
- 賴沅承 (hardware)
- 林亮村 (hardware)
- 陳仲磊 (hardware)
- 戴子桓 (hardware)


