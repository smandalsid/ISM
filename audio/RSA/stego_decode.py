# Use wave package (native to Python) for reading the received audio file
import wave

def Decode():
    # song = wave.open("audio/song_embedded.wav", mode='rb')
    file=input("Enter name of embedded audio file: ")
    # file='audio/RSA/song_embedded.wav'
    song = wave.open(file, mode='rb')
    # Convert audio to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    # Extract the LSB of each byte
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]

    # print(extracted[:5])

    # Convert byte array back to string
    # string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
    # message=""

    string=bytearray(b'')
    count=3
    for i in range(0, len(extracted), 8):
        # print(''.join(map(str, extracted[i:i+8])))
        if int(''.join(map(str, extracted[i:i+8])), 2).to_bytes(1, "big")==b'#' and int(''.join(map(str, extracted[i+8:i+16])), 2).to_bytes(1, "big")==b'#' and int(''.join(map(str, extracted[i+16:i+24])), 2).to_bytes(1, "big")==b'#':
            break
        string+=int(''.join(map(str, extracted[i:i+8])), 2).to_bytes(1, "big")
    # Cut off at the filler characters
    # decoded = string.split("###")[0]
    decoded=string

    # Print the extracted text
    print("\nSucessfully decoded: ")
    song.close()
    return decoded