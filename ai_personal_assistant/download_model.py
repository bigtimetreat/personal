import os
import urllib.request
import zipfile

# Define the URL of the Vosk model
model_url = "https://alphacephei.com/vosk/models/vosk-model-cn-0.22.zip"
model_dir = "ai_personal_assistant/models"
model_path = os.path.join(model_dir, "vosk-model-cn-0.22")

# Create the models directory if it doesn't exist
os.makedirs(model_dir, exist_ok=True)

# Download the model
print("Downloading Vosk model...")
model_zip_path = os.path.join(model_dir, "vosk-model-cn-0.22.zip")
urllib.request.urlretrieve(model_url, model_zip_path)
print("Download complete.")

# Extract the model
print("Extracting Vosk model...")
with zipfile.ZipFile(model_zip_path, 'r') as zip_ref:
    zip_ref.extractall(model_dir)
print("Extraction complete.")

# Clean up the zip file
os.remove(model_zip_path)
print("Cleanup complete.")

print(f"Model is ready at {model_path}")
