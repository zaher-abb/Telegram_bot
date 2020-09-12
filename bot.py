import requests
import json
import os

     
TOKEN = os.getenv('TOKEN')
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"
#push



def lambda_handler(event, context):
    try:
        data = json.loads(event["body"])    
        message = str(data["message"]["text"])
        first_name = data["message"]["chat"]["first_name"]
        last_name = data["message"]["chat"]["last_name"]
        chat_id = data["message"]["chat"]["id"]
        user_input=data['message']['text']
        weather_url=f'https://api.openweathermap.org/data/2.5/weather?appid=""&q=Berlin'
       # you should to write the key of the openweather API 
        user_input=data['message']['text']
        response = {"chat_id": chat_id, }
       
        # Reagiere auf die Eingabe
        # Fallunterscheidung
        if message.startswith('/start'):
            response['text'] = f"Hello {first_name} write or click /dog to get random dog photo /cat to get a cat photo or /name to get your full name\
            /myinstagram\to get my instagram profile link or /nasa to get Today's photo of nasa or /weather to get Today's weather of berlin\
            /THB to get a photo of my university /end to say goodbye to you ".encode("utf8")
            requests.post(f"{BASE_URL}/sendMessage", response)

        elif message.startswith('/dog'):
            contents = requests.get('https://random.dog/woof.json').json()
            response['photo'] = contents['url']
            requests.post(f"{BASE_URL}/sendPhoto", response)
            
        elif message.startswith('/nasa'):
          # you should to write the key of the Nasa API
            contents = requests.get('https://api.nasa.gov/planetary/apod?api_key=').json()
            response['text']="Today's Date : "+ contents['date']
            requests.post(f"{BASE_URL}/sendMessage", response)
            response['text']="Title of the Photo: "+ contents['title']
            requests.post(f"{BASE_URL}/sendMessage", response)
            response['photo'] = contents['url']
            requests.post(f"{BASE_URL}/sendPhoto", response)
            
        elif message.startswith('/weather'):
            contents=requests.get(weather_url).json()
            response['text']='the weather now in Berlin is ' +contents['weather'][0]['main']
            requests.post(f"{BASE_URL}/sendMessage", response)
            response['text']=f" and the temperature is : {contents['main']['temp']} Kelvin"
            requests.post(f"{BASE_URL}/sendMessage", response)
            
        elif message.startswith('/cat'):
            response['photo'] = f'https://cataas.com/cat/says/Hello%20{first_name}'
            requests.post(f"{BASE_URL}/sendPhoto", response)
        # Hier können jetzt noch weitere Kommandos eingetragen werden
        elif message.startswith('/end'):
            response['text'] = f"Goodbye {first_name } { last_name}".encode("utf8")
            requests.post(f"{BASE_URL}/sendMessage", response)
            
        elif message.startswith('/myinstagram'):
        # you are welcome to follow me on instagram 
              myurl="https://www.instagram.com/abboud.zaher/"
              response["text"] =f"here is my instagram Link {myurl}".encode("utf-8")
              requests.post(f"{BASE_URL}/sendMessage", response)
              
        elif message.startswith('/name'):
               response['text'] = f"{first_name } { last_name}".encode("utf8")
               requests.post(f"{BASE_URL}/sendMessage", response)
                 
        elif message.startswith('/THB'):
             response["photo"] ="https://erlebnis-brandenburg.de/assets/images/1/Fachhochschule_1_C_Ulf_Boettcher-564fdf94.jpg"
             requests.post(f"{BASE_URL}/sendPhoto", response)
      
        else:
            response['text'] = f"Please /start, {first_name}".encode("utf8")
            requests.post(f"{BASE_URL}/sendMessage", response)
    
    except Exception as e:
        print(e)

    return {"statusCode": 200}
