import tempfile, shutil
import os
# 1️⃣ NamedTemporaryFile → simulate user uploaded file
with tempfile.NamedTemporaryFile(mode="w+t", delete=False, suffix=".txt") as uploaded_file:
    uploaded_file.write("User uploaded content\n")
    uploaded_file.write("More data... check\n")
    uploaded_file.flush()
    print("Uploaded file path (NamedTemporaryFile):", uploaded_file.name)

# 2️⃣ SpooledTemporaryFile → process data in memory first
with tempfile.SpooledTemporaryFile(max_size=50, mode="w+t") as processing_file:
    # Read from uploaded_file
    with open(uploaded_file.name, "r") as f:
        for line in f:
            # Add some processing
            processing_file.write(line.upper())

    processing_file.seek(0)
    print("Processed content (SpooledTemporaryFile):")
    print(processing_file.read())


print("current directory",os.getcwd())
# 3️⃣ shutil → move original uploaded file to permanent storage
permanent_path = "uploads/final_upload.txt"
os.makedirs(os.path.dirname(permanent_path),exist_ok=True)
shutil.copy(uploaded_file.name, permanent_path)
print(f"Uploaded file moved to permanent storage: {permanent_path}")
