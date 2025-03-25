# Gemini Vision Analyzer

Gemini Vision Analyzer is a Streamlit-based web application that utilizes **Google's Gemini AI** to analyze images and generate insights based on text prompts. This project enables users to upload an image, provide an optional text prompt, and receive AI-generated descriptions or analysis of the image.

## 🚀 Features

- **Image Upload**: Supports JPG, JPEG, and PNG formats.
- **Text-Based Prompting**: Users can provide additional context for image analysis.
- **Google Gemini AI Integration**: Utilizes `learnlm-1.5-pro-experimental` model for generating responses.
- **User-Friendly Interface**: Built with Streamlit for easy accessibility.

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/PulkitChatwal/Gemini-Vision-Analyzer.git
cd Gemini-Vision-Analyzer
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv vision
source vision/bin/activate  # macOS/Linux
vision\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up API Key

1. Create a `.env` file in the project directory.
2. Add your Google API key:

```bash
GOOGLE_API_KEY=your_google_api_key_here
```

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

## 📂 Project Structure

```bash
Gemini-Vision-Analyzer/
│── vision/                # Virtual environment (if created)
│── app.py                 # Main Streamlit app
│── vision.py              # Core functionality
│── .gitignore             # Ignoring .env and unnecessary files
│── requirements.txt       # Dependencies
│── pyvenv.cfg             # Python environment config
│── .env                   # API keys (ignored by Git)
```

## 📌 How It Works

1. Upload an image using the file uploader.
2. Enter an optional text prompt to guide the AI analysis.
3. Click the **"Tell me about the image"** button.
4. Receive AI-generated insights based on the image and prompt.

## 🔥 Technologies Used

- **Python**
- **Streamlit**
- **Google Gemini AI** (via `google.generativeai`)
- **PIL (Pillow)** for image processing
- **Dotenv** for managing API keys

## 🛡️ Environment Variables

Ensure your `.env` file includes:

```bash
GOOGLE_API_KEY=your_google_api_key_here
```

## 🙌 Contributing

Contributions are welcome! Feel free to fork this repo, submit issues, or create pull requests.

## 📞 Contact

For any inquiries, reach out to **Pulkit Chatwal** at [GitHub](https://github.com/PulkitChatwal).

---

🎉 **Enjoy using Gemini Vision Analyzer!** 🚀
