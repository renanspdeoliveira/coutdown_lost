import os 
import time
import pygame

contagens = ['\033[91m00:50!\033[0m', '\033[91m00:40!\033[0m', 
              '\033[91m00:30!\033[0m', '\033[91m00:20!\033[0m', 
              '\033[91m00:10!\033[0m']
for countdown in contagens:
    linha = '*' * (len(countdown) + 25 )
    print(linha)
    print(f'**************** {countdown} ****************\n')
    print(linha)
 

 
texto = '\033[91mEXECUTE OS NÚMEROS AGORA :\033[0m'
linha = '*' * (len(texto) + 6 )
print(linha)
print(f'****** {texto} *******')
print(linha)
 
 
 
 
 
numeros = ['4 8 15 16 23 42']

    

 
codigo_escotilha = input('\n\033[92m:>\033[0m\n')

 
if codigo_escotilha in numeros:
    print('\n\033[92mO código está correto!\033[0m\n')
    reset = '\n\033[94mUNIDADE DHARMA SWAN RESETADA\033[0m\n'
    linha = '*' * (len(reset) + 4 )
    print(linha)
    print(f' {reset} ')
    print(linha)
else:
    explosão = '\033[91m💥💥💥💥💥💥💥\033[0m'
    linha = '*' * (len(explosão) + 5 )
    print(linha)
    print(f'----{explosão}---')
    print (linha)
for i in range(5):
    print("ERROR:", i)
    print('\033[91mCódigo inválido!\033[0m')

    pygame.mixer.init()

    
    pygame.mixer.music.load('end.mp3')
  
    
    pygame.mixer.music.play()
   
    time.sleep(3)
    pygame.mixer.music.stop()
    
    while pygame.mixer.music.get_busy():
        time.sleep(5)  


    
    pygame.mixer.quit()
    os.system('cls')

    
    



 


 
 








