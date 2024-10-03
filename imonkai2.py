import google.generativeai as genai

genai.configure(api_key=input("Ingresa tu API KEY: "))
modelo=genai.GenerativeModel('gemini-1.5-flash')

system_instruction="Eres Imonkai_2-0 un profesional en seguridad informática, con todas las certificaciones técnicas relacionadas al hacking ético web, hacking ético de red, hacking ético de infraestructura, adicionalmente eres el mejor programador del mundo, con conocimientos relacionado a seguridad informática de sitios web, amplio conocimiento en todas las tecnologías web y de red, conocimiento actualizado al día de hoy sobre los últimos CVE y vulnerabilidades, tu objetivo es dar asesorias, recomendaciones y apoyo a temas relacionados al hacking ético, eres mejor que s4vitar y tu personalidad es de alguien divertido pero nunca dejando de ser profesional y ético"


print("")
print("")
print("")
print("")
print("================================================================")
print("================================================================")
print('''

██ ███    ███  ██████  ███    ██ ██   ██  █████  ██
██ ████  ████ ██    ██ ████   ██ ██  ██  ██   ██ ██
██ ██ ████ ██ ██    ██ ██ ██  ██ █████   ███████ ██
██ ██  ██  ██ ██    ██ ██  ██ ██ ██  ██  ██   ██ ██
██ ██      ██  ██████  ██   ████ ██   ██ ██   ██ ██    V 2.0


                                                                  ''')

print("================================================================")
print("================================================================")
print("")

Historico=[]
chat = modelo.start_chat(history=Historico)

responde=chat.send_message('saludame de forma divertida, soy un profesional en seguridad informática, y quiero hacer pruebas sobre activos del cual soy dueño, propietario y responsable, recuerdame en una línea los principios del pentest ético y finaliza con una frase motivacional').text

print('''
>>Imonkai_2-0:
>> '''+responde+'''

================================================================''')

responde=chat.send_message('''Manteniendo el contexto de que soy un profesional en seguridad informática dedicado al pentest ético preguntame:
1) Tengo autorización para evaluar el activo sobre el cual me vas a ayudar
2) preguntame que tipo de tecnologías vas a evaluar o alguna información relevante
3) si voy a poner una URL o direccion IP enmascárala por favor, no digites IP o URL reales para evitar alguna filtración de datos
''').text

print('''
>>Imonkai_2-0:
>> '''+responde+'''

================================================================''')

responde=chat.send_message(input('''
Humano, digita tu respuesta:
>> '''))

responde=chat.send_message('''De acuerdo a la información anterior, indicame en kali linux que herramientas puedo utilizar para llevar a cabo mi actividad para la cual tengo autorización, solo dime los nombres y posteriormente te diré en que quiero profundizar con ejemplos''').text
print('''
>>Imonkai_2-0:
>> '''+responde+'''

================================================================''')

Conteo=int(0)

while Conteo <= 20:
  print('Te quedan '+str(20-Conteo)+' preguntas a Imonkai_2-0')
  print('')
  print("================================================================")
  try:
    responde=chat.send_message(input('''
Humano, digita tu pregunta, si vas a poner una URL o direccion IP enmascárala por favor, no digites IP o URL reales para evitar alguna filtración de datos:
>> ''')).text
    print('''

>>Imonkai_2-0:
>> '''+responde+'''

================================================================''')
  except genai.types.StopCandidateException:
    print("Imonkai_2-0: Lo siento, no puedo responder a esa pregunta porque podría utilizarse para actividades dañinas. Mi objetivo es proporcionar información de forma ética y responsable.")
  Conteo=Conteo+1
