# 🚀 Quick Start Guide - GreenClassify

## Get Started in 5 Minutes!

### Step 1: Install Python Dependencies

Open PowerShell/Command Prompt in the `vegetable_flask_app` folder and run:

```bash
pip install -r requirements.txt
```

If you encounter issues, try:
```bash
python -m pip install --upgrade pip
pip install Flask==2.3.2 tensorflow==2.13.0 numpy==1.24.3 Pillow==10.0.0 Werkzeug==2.3.6
```

### Step 2: Run the Application

```bash
python app.py
```

You should see output like:
```
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000
```

### Step 3: Open in Browser

Open your web browser and go to:
```
http://localhost:5000/
```

### Step 4: Test the App

1. **Click on the upload area** or **drag an image** onto it
2. A vegetable image preview will appear
3. Click **"Predict Vegetable"** button
4. See the AI classification result!

## 🎯 What to Try

### Test Images
You can test with images of:
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

### Features to Explore
- ✨ Try dragging images instead of clicking
- 🎨 Notice the beautiful gradient UI
- ⚡ Check how fast predictions are
- 📱 Try on mobile/tablet (it's responsive!)
- ⌨️ Press 'U' to focus upload input

## ❓ Troubleshooting

### Error: "ModuleNotFoundError: No module named 'flask'"
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Port 5000 Already in Use
**Solution**: Edit `app.py`, change the last line to:
```python
if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Use a different port
```

### TensorFlow Installation Issues
**For slow downloads**, try:
```bash
pip install --no-cache-dir tensorflow
```

**For Apple Silicon Mac**, use:
```bash
pip install tensorflow-macos
```

### Model File Not Found
The app creates a demo model mapping automatically. To use your trained model:
1. Place `vegetable_classifier.h5` in the project root
2. Restart the Flask app

## 📊 Understanding the Results

When you predict an image:

- **Result**: The identified vegetable type
- **Confidence Score**: Percentage certainty (0-100%)
- **Green Progress Bar**: Visual representation of confidence

Example:
```
Result: Tomato
Confidence: 95.32%
━━━━━━━━━━━━━━━━━━ 95%
```

## 🔄 Workflow

```
1. Home Page (index.html)
   ├─ Upload Image
   │  ├─ Drag & Drop
   │  └─ Click to Browse
   │
   2. Prediction Processing
   │  ├─ Image Resize (150x150)
   │  ├─ Normalize (0-1 range)
   │  ├─ Model Inference
   │  └─ Calculate Confidence
   │
   3. Results Page (prediction.html)
   │  ├─ Display Image
   │  ├─ Show Prediction
   │  ├─ Show Confidence
   │  └─ Action Buttons
   │
   4. Options
   │  ├─ Try Again → Back to Home
   │  └─ Exit → Thank You Page
```

## 💡 Tips & Tricks

1. **Better Results**: Use clear, well-lit images
2. **Faster Upload**: Compress images before uploading
3. **Batch Testing**: Open multiple tabs for different images
4. **Development Mode**: Flask auto-reloads on code changes
5. **Debug Mode**: Check browser console (F12) for JavaScript logs

## 🎮 Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `U` | Focus upload input |
| `Enter` | Submit prediction (if image selected) |

## 📱 Mobile Access

To access from another device on your network:

1. Find your IP address:
   ```bash
   # Windows
   ipconfig
   
   # Mac/Linux
   ifconfig
   ```

2. Open in browser on another device:
   ```
   http://YOUR_IP:5000/
   ```
   (Replace `YOUR_IP` with your actual IP)

## 🛑 Stop the Application

Press `Ctrl+C` in the terminal to stop the Flask server.

## 📚 Learn More

- Check `README.md` for detailed documentation
- Review `app.py` for backend code
- Check `templates/` for HTML structure
- Review `static/css/main.css` for styling
- Check `static/js/main.js` for frontend logic

## ✅ Checklist

- [ ] Python installed (3.8+)
- [ ] Dependencies installed
- [ ] requirements.txt available
- [ ] Flask app running without errors
- [ ] Browser showing the home page
- [ ] Upload works (drag & drop)
- [ ] Predictions working
- [ ] Results displaying correctly

## 🎉 You're Ready!

Your GreenClassify app is now running. Start predicting vegetables! 🥗

Have fun and happy classifying! 🚀
