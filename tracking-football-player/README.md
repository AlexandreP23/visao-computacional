##FIA
##Aluno: Alexandre Godoy Peres

# Rastreamento de Jogadores de Futebol com OpenCV
Este projeto utiliza a biblioteca OpenCV para rastrear jogadores de futebol em um vídeo. Nele são implementados dois algoritmos de rastreamento CSRT (Channel and Spatial Reliability Tracker) e o KFC (Kernel Correlation Filters) para monitorar a posição dos jogadores ao longo do tempo. 
A principal ideia do projeto é poder extrair uma infinidade de insights e métricas dos jogadores, fazer previsões, medições de performance e etc.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Pré-requisitos
Python 3.6 ou superior
OpenCV 4.5 ou superior

## Uso
1 - Certifique-se de que o caminho para o seu vídeo está correto no script. O caminho atual é:
video_path = r'C:\Senac\I.A\visao-computacional\tracking-football-player\video_football.mp4'

2 - Execute o script:
'''python main.py'''

3 - Selecione a região de interesse (ROI) no primeiro frame do vídeo e pressione SPACE ou ENTER para iniciar o rastreamento. Pressione 'c' para cancelar a seleção.

4 - O vídeo será exibido com a caixa delimitadora (bounding box) rastreando o objeto selecionado. Pressione ESC para encerrar o rastreamento.

## [Me contate pelo Linkedin](https://www.linkedin.com/in/alexandre-peres-a085b9a6/)
