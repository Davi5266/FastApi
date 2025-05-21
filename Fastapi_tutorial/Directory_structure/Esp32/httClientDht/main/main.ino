#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h"

const char* ssid = "";
const char* password = "";
const char* serverName = "http://192.168.0.102:3000";

#define DHTPIN 4
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);

    Serial.print("Conectando ao Wi-Fi");
    while (WiFi.status() != WL_CONNECTED){
        delay(500);
        Serial.print(".");
    }
    Serial.print("\nConectado!");

    dht.begin();
}

void loop() {
    delay(2000);

        
    float h = dht.readHumidity();

    float t = dht.readTemperature();

    float f = dht.readTemperature(true);

    if(isnan(h) || isnan(t) || isnan(f)) {
        Serial.println(F("Falha na leitura do sensor DHT!"));
    }

    float hif = dht.computeHeatIndex(f, h);

    float hic = dht.computeHeatIndex(t, h, false);

    if (WiFi.status() == WL_CONNECTED){
        HTTPClient http;

        http.begin(serverName);
        http.addHeader("Content-Type", "application/json");
        /*
        humidade
        temperature_C
        temperature_F
        */

        // String jsonPayload = "{\"temperature\":\"%d\"}", hic;
        String jsonPayload = "{\"temperature\":" + String(hic,2) + ",\"temperature_C\":\"23\",\"temperature_F\":\"45\"}";

        int httpResponseCode = http.POST(jsonPayload);

        if (httpResponseCode > 0) {
            String resposta = http.getString();
            Serial.println("Código HTTP: " + String(httpResponseCode));
            Serial.println("Resposta: " + resposta);
        } else {
            Serial.println("Erro na requisição: " + String(httpResponseCode));
        }

        http.end();
    }

}
