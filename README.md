# 🔒 Secure Data Hiding in Images Using Steganography

A simple Python project that hides and extracts secret messages in images using the Least Significant Bit (LSB) technique.

## 📌 Features
- Hide secret text messages inside .png images
- Extract hidden messages without altering the original image appearance
- Uses lossless image steganography (works best with .png)
- Simple CLI-based interaction using Python

## 📁 Project Structure

project-folder/
│── steganography.py        # Core logic
│── main.py                 # Run & interact with project
│── requirements.txt        # Dependencies
│── README.md               # Project documentation
│── test.png                # Sample image to test (user provided)


## 🛠 How to Use

### Step 1: Clone the Repository
bash
git clone (https://github.com/preethi-siv/image-steganography)
cd image-steganography


### Step 2: Install Dependencies
bash
pip install -r requirements.txt


### Step 3: Run the Program
bash
python main.py


### Step 4: Choose an Option
- Enter 1 to hide a message in an image
- Enter 2 to extract a hidden message

> ⚠ Works best with .png images. Avoid .jpeg or .jpg to prevent corruption.

## 🧪 Example
*Hide a Message*

Enter the input file name: test.png
Enter the output file name: stego.png
Enter the secret message to hide: Hello


*Extract a Message*

Enter the input file name: stego.png
Extracted Message: Hello


## 📦 Dependencies
- Python 3.x
- Pillow (PIL)

## 🔮 Future Scope
- AES encryption for message security
- Support for hiding entire files (PDF, TXT)
- Web or desktop GUI

## 🧑‍💻 Author
Preethi | [GitHub](https://github.com/preethi-siv)

## 📜 License
This project is licensed under the MIT License.
