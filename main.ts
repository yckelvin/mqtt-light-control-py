basic.forever(function on_forever() {
    
    microIoT.microIoT_clear()
    lightintensity = pins.analogReadPin(AnalogPin.P0)
    microIoT.microIoT_SendMessage(convertToText(lightintensity), microIoT.TOPIC.topic_0)
    microIoT.microIoT_showUserText(0, "Send... " + convertToText(lightintensity))
    if (lightintensity < 500) {
        pins.analogWritePin(AnalogPin.P16, 1023)
    } else {
        pins.analogWritePin(AnalogPin.P16, 0)
    }
    
    pause(1000)
})
let lightintensity = 0
let wifi_name = "izowifi"
let password = "izo1234@"
let iot_id = "lmZB9bXGR"
let iot_pwd = "liWfrxXMgz"
let topic_0 = "qwPmNL37g"
microIoT.microIoT_initDisplay()
microIoT.microIoT_WIFI(wifi_name, password)
microIoT.microIoT_MQTT(iot_id, iot_pwd, topic_0, microIoT.SERVERS.English)
