import torch
import torchaudio
from zonos.model import Zonos
from zonos.conditioning import make_cond_dict
from zonos.utils import DEFAULT_DEVICE as device
import helper_functions as hfs

# Load and process the speaker embedding
def get_speaker_embedding(audio_path):
  wav, sampling_rate = torchaudio.load(audio_path)
  return model.make_speaker_embedding(wav, sampling_rate)

# Function to generate speech
def generate_speech(text, speaker_embedding, language="en-us", output_filename="output.wav", seed=421):
  torch.manual_seed(seed)  # Set seed for reproducibility
  
  # Prepare the conditioning dictionary
  cond_dict = make_cond_dict(text=text, speaker=speaker_embedding, language=language)
  conditioning = model.prepare_conditioning(cond_dict)
  
  # Generate speech
  codes = model.generate(conditioning)
  
  # Decode to waveform
  wavs = model.autoencoder.decode(codes).cpu()
  
  # Save output
  torchaudio.save(output_filename, wavs[0], model.autoencoder.sampling_rate)
  print(f"Generated speech saved as {output_filename}")

# Load the model once
model = Zonos.from_pretrained("Zyphra/Zonos-v0.1-transformer", device=device)
print("computing speaker embedding")
speaker = get_speaker_embedding("assets/exampleaudio.mp3")

# Example usage:
def main():
  # Define default sentences
  default_sentences = [
    "Hello, world!",
    "This is a second test sentence.",
    "How are you doing today?",
    "The quick brown fox jumps over the lazy dog.",
  ]

  # Set up argument parser
  parser = argparse.ArgumentParser(description="Generate voice audio from a list of sentences")
  parser.add_argument(
    "--txt_file_path",  # Optional argument with "--"
    #nargs="+",  # Accepts multiple space-separated values
    type=str,
    help="List of sentences for text-to-speech conversion.",
    default=None,  # Use default if not provided
  )

  args = parser.parse_args()

  # Get sentences based on file path or default
  #sentences = args.txt_file_path  # Always a file path or None object
  sentences = get_sentences(file_path=args.txt_file_path, default_sentences=default_sentences)

  # Example: speaker embedding (assuming function exists)
  # speaker = get_speaker_embedding("assets/exampleaudio.mp3")

  # Process each sentence
  for i, text in enumerate(sentences):
    generate_speech(text, speaker, output_filename=f"output_{i}.wav")

if __name__ == "__main__":
  main()
