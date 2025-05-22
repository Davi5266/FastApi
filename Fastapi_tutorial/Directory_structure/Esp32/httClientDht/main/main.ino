#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h"

// Configuração de rede
const char* ssid = ""; // Nome da rede
const char* password = ""; // Senha da rede
// Rota da API para o registro de dados
const char* serverName = "http://192.168.0.105:3000/clientesp/temperature";

// Configuração do sensor DHT
#define DHTPIN 4 // Pino que vai entregar os dados
#define DHTTYPE DHT22 // Tipo de sensor DHT

DHT dht(DHTPIN, DHTTYPE);

void setup() {
    Serial.begin(115200);
    // WiFi.begin(ssid, password);

    Serial.print("Conectando ao Wi-Fi");
    // while (WiFi.status() != WL_CONNECTED){
    //     delay(500);
    //     Serial.print(".");
    // }
    connect_wifi();
    Serial.print("\nConectado!");

    dht.begin();
}

void loop() {
    delay(2000);

    // Coletando dados do DHT
    // Humidade
    float h = dht.readHumidity();
    // Temperatura em Celsius
    float t = dht.readTemperature();
    // Temperature em Fahrenheit
    float f = dht.readTemperature(true);

    // Verificação de leitura
    if(isnan(h) || isnan(t) || isnan(f)) {
        Serial.println(F("Falha na leitura do sensor DHT!"));
    }

    // Calculando o índice de temperatura 
    //em Fahrenheit
    float hif = dht.computeHeatIndex(f, h);
    //em Celsius
    float hic = dht.computeHeatIndex(t, h, false);
    register_dht(h, hic, hif);
}

void register_dht(float h, float hic, float hif){
    connect_wifi();

    // if (WiFi.status() == WL_CONNECTED){
    HTTPClient http;

    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");
        /*
        Resposta Json para o endpoint
        {"data_hora": "string",
        "humidade": float,
	    "temperature_C": float,
	    "temperature_F": float
        }
        */
       // arquivando dados em json
    String jsonPayload = "{\"humidade\":" + String(h,2) +",\"temperature_C\":" + String(hic,2) +",\"temperature_F\":" + String(hif,2) +"}";
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


/* Função: connect to wifi network
 * Parâmetros: nenhum
 * Retorno: nenhum 
 */
void connect_wifi(void) 
{
    /* If module is already connected to a WI-FI, there is nothing to do here. 
       If there isn't WI-FI connection established, a WI-FI connection is done */
    if (WiFi.status() == WL_CONNECTED)
        return;
        
    WiFi.begin(ssid, password);
    
    while (WiFi.status() != WL_CONNECTED) 
    {
        delay(100);
        Serial.print(".");
    }
  
    Serial.println();
    Serial.print("Successfully connected to WI-FI network: ");
    Serial.println(ssid);
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
}

/* Função: verifica se há conexão wi-fi ativa (e conecta-se caso não haja)
 * Parâmetros: nenhum
 * Retorno: nenhum 
 */
void verify_wifi_connection(void)
{
    connect_wifi(); 
}

/* Função: inicaliza conexão wi-fi
 * Parâmetros: nenhum
 * Retorno: nenhum 
 */
void init_wifi(void) 
{
    delay(10);
    Serial.println("------ WI-FI -----");
    Serial.print("Tentando se conectar a seguinte rede wi-fi: ");
    Serial.println(ssid_wifi);
    Serial.println("Aguarde");    
    connect_wifi();
}