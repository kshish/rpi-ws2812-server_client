# rpi-ws2812-server_client
client test python scripts

for server, https://github.com/tom-2015/rpi-ws2812-server
to start server from install folder:
sudo ./ws2812svr -i "setup 1,300,WS2811_STRIP_GRB;init;" -tcp 80
sudo ./ws2812svr -i "setup 1,300,WS2811_STRIP_GRB;init;random 1,0,300,GRBWL;fade 1,255,0,50,0,300;" -tcp 80

cli 
random 1,0,300,GRBWL
fade 1,255,0,50,0,300
