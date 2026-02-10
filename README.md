# 🥗 GreenClassify - Vegetable Image Classification App

A beautiful Flask web application that uses TensorFlow to classify vegetable images. Upload an image and let our AI model identify the vegetable instantly!

## ✨ Features

- **Beautiful Modern UI**: Responsive Bootstrap-based design with smooth animations
- **Drag & Drop Upload**: Intuitive drag-and-drop interface for easy image uploads
- **Real-time Preview**: See the image before submission
- **AI-Powered Classification**: Uses trained TensorFlow model for accurate vegetable identification
- **Confidence Score**: Displays prediction confidence percentage
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Fast Processing**: Quick image preprocessing and prediction
- **Error Handling**: Comprehensive error messages and validation

## 🚀 Supported Vegetables

The model can classify the following vegetables:
- Tomato
- Carrot
- Broccoli
- Potato
- Cabbage
- Cucumber
- Bell Pepper
- Spinach
- Pumpkin
- Lettuce

## First step:
Code files/Vegetable_Image_Classification go to this path and run this file which will create flask app folder in which the model and other congiure file is presented by the code

## project code drive link:
https://drive.google.com/drive/folders/1maBWF0ro3jl-pjLHmKPnXbkAcize1ibe?usp=drive_link


## 📋 Requirements

- Python 3.8+
- Flask 2.3.2+
- TensorFlow 2.13.0+
- NumPy 1.24.3+
- Pillow 10.0.0+

## 📦 Installation

1. **Clone or Extract the Project**
   ```bash
   cd e:\vegetable_flask_app
   ```

2. **Create a Virtual Environment (Recommended)**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Running the Application

1. **Start the Flask Server**
   ```bash
   python app.py
   ```

2. **Open in Browser**
   ```
   http://localhost:5000/
   ```

3. **Use the Application**
   - Upload an image by clicking or dragging it to the upload area
   - View the preview
   - Click "Predict Vegetable" button
   - See the classification result with confidence score

## 📁 Project Structure

```
vegetable_flask_app/
├── app.py                      # Flask application main file
├── requirements.txt            # Python dependencies
├── vegetable_classifier.h5     # Trained model (binary file)
├── class_map.pkl               # Class labels mapping
├── static/
│   ├── css/
│   │   └── main.css           # Styling with Bootstrap + custom CSS
│   └── js/
│       └── main.js            # Interactive features (drag-drop, preview)
├── templates/
│   ├── index.html             # Home page with upload form
│   ├── prediction.html        # Results page with confidence score
│   └── logout.html            # Exit confirmation page
└── uploads/                    # Temporary folder for uploaded images
```

## 🎨 Frontend Highlights

### Modern UI/UX Features
- **Gradient Backgrounds**: Eye-catching linear gradients
- **Card Design**: Clean card-based layout with hover effects
- **Smooth Animations**: Bounce animations and fade-in effects
- **Interactive Elements**: Real-time feedback and progress indicators
- **Mobile Responsive**: Adapts beautifully to all screen sizes
- **Keyboard Shortcuts**: Press 'U' to focus upload, 'Enter' to submit

## 🔧 Configuration

Edit `app.py` to customize:

```python
# Maximum file size (in bytes)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Target image size for model
target_size = (150, 150)
```

## 🐛 Troubleshooting

### Port Already in Use
If port 5000 is already in use, modify `app.py`:
```python
if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Use port 5001
```

### Model File Not Found
- Ensure `vegetable_classifier.h5` is in the project root
- The app will still run with a demo model if file is missing

### Image Upload Issues
- Check file size (max 16MB)
- Ensure file is in PNG, JPG, JPEG, or GIF format
- Check `uploads/` folder has write permissions

## 📊 Technology Stack

- **Backend**: Flask (Python)
- **ML Framework**: TensorFlow/Keras
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Scripting**: Vanilla JavaScript
- **Image Processing**: Pillow (PIL)
- **Icons**: Font Awesome 6

## 🎓 Model Details

- **Architecture**: Convolutional Neural Network (CNN)
- **Input Size**: 150×150 pixels
- **Output Classes**: 10 vegetables
- **Pre-processing**: Normalized to [0, 1] range
- **Confidence Score**: Softmax probability output

## 📝 API Endpoints

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Home page with upload form |
| `/predict` | POST | Process image and return prediction |
| `/uploads/<filename>` | GET | Serve uploaded images |
| `/logout` | GET | Exit page |

## 🔒 Security Features

- **Secure Filename Sanitization**: Prevents path traversal attacks
- **File Type Validation**: Only allows image files
- **File Size Limits**: Prevents DoS attacks
- **Error Handling**: Graceful error messages without exposing sensitive info

## 📈 Performance

- **Fast Loading**: Optimized CSS and JS
- **Efficient Image Processing**: TensorFlow GPU acceleration (if available)
- **Responsive UI**: No blocking operations
- **Caching**: Browser caching for static assets

## 🎯 Future Enhancements

- [ ] Add batch image processing
- [ ] Save prediction history
- [ ] User authentication
- [ ] Export results as PDF
- [ ] Train custom models
- [ ] Add more vegetable categories
- [ ] Implement webcam capture
- [ ] Add REST API for mobile apps

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Improve documentation
- Optimize code

## 📧 Support

For issues or questions, please check the troubleshooting section or contact the development team.

---

**Made with ❤️ by the GreenClassify Team**

Happy classifying! 🥬
