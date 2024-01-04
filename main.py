def on_forever():
    global lightintensity
    microIoT.microIoT_clear()
    lightintensity = pins.analog_read_pin(AnalogPin.P0)
    microIoT.microIoT_SendMessage(convert_to_text(lightintensity), microIoT.TOPIC.TOPIC_0)
    microIoT.microIoT_showUserText(0, "Send... " + convert_to_text(lightintensity))
    if lightintensity > 500:
        pins.analog_write_pin(AnalogPin.P16, 1023)
    else:
        pins.analog_write_pin(AnalogPin.P16, 0)
    pause(1000)
basic.forever(on_forever)

lightintensity = 0
wifi_name = "izowifi"
password = "izo1234@"
iot_id = "lmZB9bXGR"
iot_pwd = "liWfrxXMgz"
topic_0 = "qwPmNL37g"
microIoT.microIoT_initDisplay()
microIoT.microIoT_WIFI(wifi_name, password)
microIoT.microIoT_MQTT(iot_id, iot_pwd, topic_0, microIoT.SERVERS.ENGLISH)