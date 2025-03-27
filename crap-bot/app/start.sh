#!/bin/bash -x

# Start Xvfb
Xvfb :1 -screen 0 1920x1080x24 +extension RANDR &> /tmp/xvfb.log &
export DISPLAY=:1.0

# Start Fluxbox (lightweight window manager)
fluxbox &> /tmp/fluxbox.log &

# Start x11vnc
x11vnc -display :1 -nopw -shared -forever -xkb -bg -rfbport 5900 &> /tmp/x11vnc.log &

# Start noVNC
/usr/share/novnc/utils/novnc_proxy --listen 6900 --vnc localhost:5900 & #&> /tmp/novnc.log &

# Run your Python script
sleep 10
python bot.py