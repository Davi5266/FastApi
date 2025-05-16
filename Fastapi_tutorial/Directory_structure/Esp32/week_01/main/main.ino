#include <WiFi.h>
#include <HTTPClient.h>
#include "arduino_secrets.h"

const char* ssid = "Paulo";
const char* password = "15151515";
const char* serverName = "http://192.168.0.104:3000/";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  Serial.print("Conectando ao Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConectado!");

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");

    String jsonPayload = "{\"user\": \"esp32\"}";
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

void loop() {
  // Código contínuo aqui, se necessário
  fun_test();
}

void fun_test() {
  
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  Serial.print("Conectando ao Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConectado!");

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");

    String jsonPayload = "{\"user\": \"esp32\"}";
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

// void post_data(http){
//   http.begin(serverName);
//   http.addHeader("Content-Type", "application/json");

//   String jsonPayload = "{\"user\": \"esp32\"}";
//   int httpResponseCode = http.POST(jsonPayload);

  
//   if (httpResponseCode > 0) {
//     String resposta = http.getString();
//     Serial.println("Código HTTP: " + String(httpResponseCode));
//     Serial.println("Resposta: " + resposta);
//   } else {
//     Serial.println("Erro na requisição: " + String(httpResponseCode));
//   }

//   http.end();
// }