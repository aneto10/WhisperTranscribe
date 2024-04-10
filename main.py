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

def transcribe_audio(input_file, result_dir, model_choice):
    model_mapping = {
        1: "ggml-small.bin",
        2: "ggml-tiny.bin",
        3: "ggml-base.bin",
        4: "ggml-large-v3.bin",
        5: "ggml-medium.bin"
    }
    modelo = model_mapping.get(model_choice, "ggml-small.bin")
    print("#####################################################################################################################\n")
    print(f"Modelo selecionado: {modelo}\n")
    print("#####################################################################################################################\n")
    output_file = os.path.join(result_dir, os.path.basename(input_file).replace(".wav", ""))
    command = f"C:\\whisper\\main.exe -f \"{input_file}\" -l portuguese -m C:\\whisper\\{modelo} --output-txt --output-file \"{output_file}\""
    subprocess.run(command, shell=True)

    return output_file

def main():
    print("#####################################################################################################################")
    print("################################## Modelos para transcrição #########################################################\n")
    print("1. ggml-small.bin: Ideal para tarefas simples e rápidas, onde a precisão não é crucial. Perfeito para dispositivos com recursos limitados.\n")
    print("2. ggml-tiny.bin: O menor modelo disponível, ideal para dispositivos com recursos muito limitados. A precisão pode ser menor que outros modelos.\n")
    print("3. ggml-base.bin: Equilíbrio entre precisão e velocidade. Adequado para uso geral em diversas situações. Uma boa escolha se você não tem certeza qual modelo usar.\n")
    print("4. ggml-large-v3.bin: Maior modelo, com a melhor precisão. Exige mais recursos computacionais e tempo de processamento. Ideal para transcrições que exigem alta qualidade, como em contextos profissionais ou acadêmicos.\n")
    print("5. ggml-medium.bin: Intermediário entre o ggml-base.bin e o ggml-large-v3.bin em termos de precisão e velocidade. Uma boa escolha quando você precisa de boa precisão sem comprometer muito a velocidade.\n")
    print("#####################################################################################################################\n")
    model_choice = int(input("Digite o número correspondente ao modelo desejado: "))
    print("#####################################################################################################################\n")
    print("################################## Informe o caminho do arquivo de áudio ############################################\n")
    input_file = input("Insira o caminho do arquivo de áudio: ")
    print("#####################################################################################################################\n")
    if not os.path.exists(input_file):
        print("O arquivo especificado não existe.")
        return

    result_dir = "C:\\whisper\\WhisperTranscribe\\result"
    os.makedirs(result_dir, exist_ok=True)
    
    wav_file = convert_to_wav(input_file)
    print("################################## Conversão de áudio ################################################################\n")
    print(f"Arquivo convertido para WAV: {wav_file}\n")
    print("#####################################################################################################################\n")

    transcribed_file = transcribe_audio(wav_file, result_dir, model_choice)
    print("################################## Transcrição de áudio #############################################################\n")
    print(f"Transcrição completa. Arquivo de saída: {transcribed_file}\n")
    print("#####################################################################################################################\n")
    os.remove(wav_file)

if __name__ == "__main__":
    main()