- EXPLICAÇÃO DO CÓDIGO -

Este código em Python utiliza a biblioteca PySimpleGUI para criar uma interface gráfica e a biblioteca pyautogui para automatizar algumas ações.
Ao executar o programa, uma janela é exibida com um campo de entrada de texto e dois botões. O usuário pode inserir o tempo em segundos para desligar o computador
e confirmar ou cancelar a ação.
Quando o usuário confirma o tempo, o programa aguarda o tempo especificado e, em seguida, simula as ações de pressionar a tecla "Win" (a tecla do Windows),
clicar no botão "Desligar" e, após isso, confirmar o desligamento.
Este código pode ser útil para automatizar o processo de desligamento do computador em uma tarefa específica, por exemplo, em um ambiente de teste ou em uma rotina
de backup.

- ARQUIVO .EXE -

Na pasta "dist", há o arquivo executável desse código (utilizei o Pyinstaller para criar esse arquivo .exe), para que haja uma facilidade na hora de compartilhar essa
ferramenta.

- AVISO IMPORTANTE -

Importante: a biblioteca pyautogui se baseia nos pixels da tela para executar o clique do mouse, esse código foi feito com base em uma tela Full HD (1920x1080), então
ao utilizar, certifique-se que sua tela está nessa resolução ou adapte o código para a resolução da tela que você possui.
