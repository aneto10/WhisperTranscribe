import os
import subprocess
from datetime import datetime

def convert_to_wav(input_file):
    # Capturando data e hora atual para usar como parte do nome do arquivo
    data_e_hora_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Definindo o nome do arquivo de saída com a data e hora atual
    output_file = os.path.join("C:\\whisper\\WhisperTranscribe\\temp", f"{data_e_hora_atual}.wav")
    
    # Comando para conversão do arquivo para WAV com redução de ruído
    command = f"C:\\ffmpeg\\bin\\ffmpeg.exe -i \"{input_file}\" -af \"highpass=f=200, lowpass=f=3000, afftdn\" -ar 16000 -ac 1 -c:a pcm_s16le \"{output_file}\""
    
    # Executando o comando
    subprocess.run(command, shell=True)

    return output_file

def transcribe_audio(input_file, result_dir):
    # Definindo o nome do arquivo de saída para a transcrição
    output_file = os.path.join(result_dir, os.path.basename(input_file).replace(".wav", ""))
    
    """
    ggml-small.bin: Este é provavelmente um modelo pequeno, destinado a tarefas simples de transcrição de áudio para texto. Pode ser útil em situações onde a precisão não é crítica e a velocidade de processamento é mais importante. Pode ser usado em dispositivos com recursos limitados ou quando a latência é uma preocupação.
    ggml-tiny.bin: Este modelo é ainda menor que o ggml-small.bin, e provavelmente é otimizado para dispositivos com recursos muito limitados ou para transcrições muito simples e rápidas. No entanto, a precisão pode ser comprometida em comparação com modelos maiores.
    ggml-base.bin: Este é um modelo base que oferece um equilíbrio entre precisão e velocidade. É adequado para uso geral em uma variedade de situações e pode ser uma escolha segura se você não estiver certo sobre qual modelo escolher.
    ggml-large-v3.bin: Este é um modelo grande que provavelmente oferece a melhor precisão, mas pode exigir mais recursos computacionais e tempo de processamento. É ideal para transcrições que exigem alta precisão, como em contextos profissionais ou acadêmicos, onde a qualidade é primordial.
    ggml-medium.bin: Este modelo provavelmente fica entre o ggml-base.bin e o ggml-large-v3.bin em termos de precisão e velocidade. Pode ser uma boa escolha se você precisar de uma precisão razoável sem comprometer muito a velocidade de processamento.
    """
    # Comando para executar a transcrição
    command = f"C:\\whisper\\main.exe -f \"{input_file}\" -l portuguese -m C:\\whisper\\ggml-medium.bin --output-txt --output-file \"{output_file}\""
    
    # Executando o comando
    subprocess.run(command, shell=True)

    return output_file

def main():
    # Solicita ao usuário que insira o caminho do arquivo de áudio
    input_file = input("Insira o caminho do arquivo de áudio: ")
    
    # Verifica se o arquivo existe
    if not os.path.exists(input_file):
        print("O arquivo especificado não existe.")
        return

    # Define o diretório de saída para os arquivos transcritos
    result_dir = "C:\\whisper\\WhisperTranscribe\\result"
    os.makedirs(result_dir, exist_ok=True)
    
    # Convertendo o arquivo de áudio para WAV
    wav_file = convert_to_wav(input_file)
    print(f"Arquivo convertido para WAV: {wav_file}")
    
    # Transcrevendo o arquivo de áudio convertido
    transcribed_file = transcribe_audio(wav_file, result_dir)
    print(f"Transcrição completa. Arquivo de saída: {transcribed_file}")

    # Exclui o arquivo WAV convertido após a transcrição
    os.remove(wav_file)

if __name__ == "__main__":
    main()
