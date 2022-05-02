# import librosa
# from pydub import AudioSegment
# import torch
# from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
# import time

# # load model and tokenizer
# tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
# model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# # The base model pretrained and fine-tuned on 960 hours of Librispeech on 16kHz sampled speech audio.
# # When using the model make sure that your speech input is also sampled at 16Khz.

# # load any audio file of your choice
# mp3_audio = AudioSegment.from_file(r"adio2.wav", format="wav")
# collection_of_text = []
# speechtiming = []
# starttime = time.time()
# for i in range(round(len(mp3_audio)/(1000*30))):

#     speech, rate = librosa.load(f"{i+1}_audi_file.wav", sr=16000)

#     input_values = tokenizer(speech, return_tensors='pt').input_values
#     # Store logits (non-normalized predictions)
#     with torch.no_grad():
#         logits = model(input_values).logits

#     # Store predicted id's
#     predicted_ids = torch.argmax(logits, dim=-1)
#     # decode the audio to generate text
#     # Passing the prediction to the tokenzer decode to get the transcription
#     transcription = tokenizer.batch_decode(predicted_ids)[0]
#     # transcriptions = tokenizer.decode(predicted_ids[0])
#     print(transcription)
#     collection_of_text.append(transcription)
#     speechtiming.append(round((time.time() - starttime), 2))

# print(collection_of_text)
# final_complete_speech = ""
# wordtime = ""

# # convert batch of text into one complete sentence
# for i in collection_of_text:  
#     final_complete_speech += i

# for i in speechtiming:
#     wordtime += str(i)

# file = open("op.txt", "w")
# file.write(final_complete_speech)
# file.close()

from summa import keywords
import yake 

file = open("op.txt")
final_text = file.read()

TR_keywords = keywords.keywords(final_text, scores=True)
print(TR_keywords[0:10])

print()

kw_extractor = yake.KeywordExtractor(top=10, stopwords=None, dedupLim=0.3, n=1)
keywords = kw_extractor.extract_keywords(final_text)

query = ""
for kw, v in keywords:
  query += kw + " "  
  print("Keyphrase: ",kw, ": score", v)

from googlesearch import search

for j in search(query, tld="com", lang = "english", num=20, stop=20, pause=2):
	print(j)