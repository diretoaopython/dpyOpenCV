# 1. Instalar o pacote dpyOpenCV-python
# 2. Criar o arquivo xxx.py
# 3. Importar o módulo cv2 em nosso código Python
import cv2

# 4. Criar um objeto a partir da classe VideoCapture do módulo cv2 (dpyOpenCV)
objImagem = cv2.VideoCapture(0)

# 5. Capturar uma imagem através do método read do objeto objImagem
# status da câmera: Se obteve a imagem com sucesso (True ou False)
# frame (Imagem)
resultado, frame = objImagem.read()

# 6. Verificar se a imagem foi capturada corretamente
if resultado:
    # 7. Salvar a imagem capturada em um arquivo
    cv2.imwrite("imagem.jpg", frame)
    print("Imagem salva com sucesso")
else:
    # 8. Informa um erro, caso haja problemas na captura da imagem
    print("Erro ao capturar ao imagem")

# 9. Liberar a câmera
objImagem.release()
