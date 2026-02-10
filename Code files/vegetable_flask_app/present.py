#!/usr/bin/env python3
"""
GreenClassify - Interactive Presentation Script
Run this to present the project in the terminal
"""

import os
import time
import platform
from typing import List

class PresentationSlide:
    def __init__(self, title: str, content: str, slide_number: int = 0, total_slides: int = 0):
        self.title = title
        self.content = content
        self.slide_number = slide_number
        self.total_slides = total_slides
    
    def display(self, clear_first: bool = True):
        """Display the slide with formatting"""
        if clear_first:
            self.clear_screen()
        
        # Display header
        self.print_header()
        
        # Display slide number
        if self.total_slides > 0:
            print(f"\n{'─' * 80}")
            print(f"SLIDE {self.slide_number} of {self.total_slides}".center(80))
            print(f"{'─' * 80}\n")
        
        # Display title
        print("┌" + "─" * 78 + "┐")
        print("│" + f" {self.title}".ljust(79) + "│")
        print("└" + "─" * 78 + "┘")
        print()
        
        # Display content
        print(self.content)
        print()
    
    @staticmethod
    def clear_screen():
        """Clear terminal screen"""
        os.system('cls' if platform.system() == 'Windows' else 'clear')
    
    @staticmethod
    def print_header():
        """Print presentation header"""
        header = """
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║           🥗  GreenClassify - Vegetable Classification System  🥗          ║
║                  Complete Project Explanation & Demo                       ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
"""
        print(header)

class Presentation:
    def __init__(self):
        self.slides: List[PresentationSlide] = []
        self.current_slide = 0
        self.setup_slides()
    
    def setup_slides(self):
        """Setup all presentation slides"""
        
        # Slide 1: Welcome
        self.slides.append(PresentationSlide(
            title="🎉 WELCOME TO THE PRESENTATION",
            content="""
This interactive presentation covers:
├─ Project Overview & Goals
├─ Complete Folder Structure
├─ How Each Component Works
├─ Data Flow & Architecture
├─ Technology Stack
├─ Security Features
├─ Deployment & Customization
└─ Future Enhancements

Press any key to continue...
""",
            slide_number=1,
            total_slides=20
        ))
        
        # Slide 2: Project Overview
        self.slides.append(PresentationSlide(
            title="📊 PROJECT OVERVIEW",
            content="""
GreenClassify is a web-based AI application that:

✓ Allows users to upload vegetable images
✓ Uses TensorFlow to classify vegetables
✓ Displays predictions with confidence scores
✓ Provides beautiful, responsive UI
✓ Works on desktop, tablet, and mobile

Key Features:
├─ Drag-and-drop image upload
├─ Real-time image preview
├─ AI-powered classification (10 vegetables)
├─ Confidence percentage indicator
├─ Error handling & validation
└─ Production-ready code

Technology Stack:
Backend:  Python, Flask, TensorFlow
Frontend: HTML5, CSS3, Bootstrap, JavaScript
""",
            slide_number=2,
            total_slides=20
        ))
        
        # Slide 3: Folder Structure
        self.slides.append(PresentationSlide(
            title="📁 COMPLETE FOLDER STRUCTURE",
            content="""
vegetable_flask_app/
│
├─ 📄 app.py                    ← Main Flask application
├─ 📄 config.py                 ← Configuration settings
├─ 📄 requirements.txt           ← Python dependencies
├─ 📄 setup.bat                 ← Windows setup script
├─ 📄 class_map.pkl             ← Vegetable class mapping
├─ 📄 vegetable_classifier.h5   ← Trained AI model (binary)
│
├─ 📄 PRESENTATION_SCRIPT.md    ← This presentation
├─ 📄 README.md                 ← Full documentation
├─ 📄 QUICKSTART.md             ← Quick setup guide
│
├─ 📁 templates/                ← HTML pages (frontend)
│   ├─ index.html               ← Home/upload page
│   ├─ prediction.html          ← Results page
│   └─ logout.html              ← Exit page
│
├─ 📁 static/                   ← CSS & JavaScript
│   ├─ css/
│   │   └─ main.css             ← Styling (450+ lines)
│   └─ js/
│       └─ main.js              ← Interactivity (350+ lines)
│
└─ 📁 uploads/                  ← Temporary file storage
    └─ [user uploaded images]

Total: 11 main files, ~1800 lines of code
""",
            slide_number=3,
            total_slides=20
        ))
        
        # Slide 4: Backend - app.py
        self.slides.append(PresentationSlide(
            title="⚙️  BACKEND - app.py",
            content="""
Main Flask Application (150+ lines)

Key Sections:

1️⃣  IMPORTS & SETUP
   from flask import Flask, render_template, request
   from tensorflow.keras.models import load_model
   import numpy as np, pickle, PIL

2️⃣  CONFIGURATION
   - Upload folder: uploads/
   - Max file size: 16MB
   - Allowed extensions: PNG, JPG, JPEG, GIF

3️⃣  MODEL LOADING
   - Load TensorFlow model (vegetable_classifier.h5)
   - Load class mapping (class_map.pkl)
   - Create demo mapping if files missing

4️⃣  THREE main ROUTES:
   
   Route 1: GET "/"
   └─ Display home page (index.html)
   
   Route 2: POST "/predict"
   └─ Process image upload
   └─ Resize to 150x150
   └─ Normalize pixel values
   └─ Feed to AI model
   └─ Return prediction.html with results
   
   Route 3: GET "/logout"
   └─ Display thank you page
""",
            slide_number=4,
            total_slides=20
        ))
        
        # Slide 5: Image Processing Pipeline
        self.slides.append(PresentationSlide(
            title="🔄 IMAGE PROCESSING PIPELINE",
            content="""
How images are processed in /predict route:

1. USER UPLOADS IMAGE
   ↓
2. VALIDATE FILE
   ├─ Check file exists
   ├─ Check size < 16MB
   ├─ Check extension (PNG/JPG/etc)
   └─ Error if invalid
   
3. SAVE IMAGE
   └─ Use secure_filename (prevent hacking)
   └─ Save to uploads/ folder
   
4. LOAD IMAGE
   └─ Use TensorFlow image loader
   └─ Handles any size/format
   
5. RESIZE IMAGE
   └─ Resize to 150x150 pixels
   └─ This is what the model expects
   
6. NORMALIZE
   └─ Convert pixel values from 0-255 to 0-1
   └─ Standard practice in deep learning
   
7. ADD BATCH DIMENSION
   └─ Convert to shape: (1, 150, 150, 3)
   └─ First dimension = batch size
   
8. PASS TO MODEL
   └─ Neural network processes image
   └─ Outputs 10 probability scores
   
9. GET PREDICTION
   └─ Find highest probability (argmax)
   └─ Look up in class_map.pkl
   └─ Calculate confidence percentage
   
10. RETURN RESULTS
    └─ Pass to prediction.html template
    └─ Render response to user
""",
            slide_number=5,
            total_slides=20
        ))
        
        # Slide 6: Frontend - HTML Pages
        self.slides.append(PresentationSlide(
            title="🎨 FRONTEND - HTML PAGES",
            content="""
Three Beautiful HTML Pages:

1️⃣  index.html (HOME PAGE)
   ┌──────────────────────────────┐
   │ Navigation Bar (Green Gradient)
   │ 🌿 GreenClassify
   ├──────────────────────────────┤
   │ Welcome Section
   │ ├─ Title & Description
   │ └─ Feature Grid (3 icons)
   │
   │ Upload Card
   │ ├─ Drag & Drop Zone
   │ ├─ File Input Hidden
   │ ├─ Image Preview (hidden until selected)
   │ └─ "Predict Vegetable" Button
   │
   │ Footer
   └──────────────────────────────┘

2️⃣  prediction.html (RESULTS PAGE)
   Shows TWO states:
   
   SUCCESS: ✓
   ├─ Uploaded Image Display
   ├─ Vegetable Name (Large Green Text)
   ├─ Confidence Bar (95%)
   ├─ "Try Another" Button
   └─ "Exit" Button
   
   ERROR: ✗
   ├─ Error Icon (Red)
   ├─ Error Message
   └─ "Go Back" Button

3️⃣  logout.html (EXIT PAGE)
   ├─ Thank You Message
   ├─ Goodbye Icon (Waving Hand)
   ├─ "Return to Home" Button
   └─ Footer
""",
            slide_number=6,
            total_slides=20
        ))
        
        # Slide 7: CSS Styling
        self.slides.append(PresentationSlide(
            title="🎨 CSS STYLING - main.css",
            content="""
Beautiful Modern Styling (450+ lines)

COLOR SCHEME:
├─ Primary: #27ae60 (Green - Vegetables!)
├─ Secondary: #2ecc71 (Light Green)
├─ Dark: #2c3e50 (Dark Gray)
└─ Light: #ecf0f1 (Light Gray)

KEY FEATURES:

✓ GRADIENTS
  └─ Linear gradients for backgrounds
  └─ Button hover effects
  └─ Card backgrounds

✓ ANIMATIONS
  ├─ Bounce animation (icons)
  ├─ Fade-in effect (preview)
  ├─ Scale on hover (buttons)
  └─ Smooth transitions (0.3s)

✓ RESPONSIVE DESIGN
  ├─ Desktop: Full layout (1200px+)
  ├─ Tablet: Adjusted (768px-1199px)
  └─ Mobile: Single column (< 768px)

✓ COMPONENTS
  ├─ Navigation bar
  ├─ Card designs
  ├─ Error/success messages
  ├─ Progress bars
  ├─ Buttons with hover states
  └─ Upload zones

✓ BOOTSTRAP 5 INTEGRATION
  └─ Grid system (flexbox)
  └─ Utility classes
  └─ Pre-built components
""",
            slide_number=7,
            total_slides=20
        ))
        
        # Slide 8: JavaScript
        self.slides.append(PresentationSlide(
            title="⚡ JAVASCRIPT - main.js",
            content="""
Interactive Functionality (350+ lines)

FEATURES:

1️⃣  DRAG & DROP
   uploadArea.addEventListener('dragover', ...)
   uploadArea.addEventListener('drop', ...)
   └─ Highlight zone when dragging
   └─ Accept dropped files
   └─ Show preview automatically

2️⃣  IMAGE PREVIEW
   FileReader API to read image
   └─ Display thumbnail before upload
   └─ Show selected filename
   └─ Real-time feedback

3️⃣  FILE VALIDATION
   ├─ Check file type (is it an image?)
   ├─ Check file size (< 16MB)
   ├─ Show validation errors
   └─ Only enable submit when valid

4️⃣  KEYBOARD SHORTCUTS
   ├─ Press 'U' to focus upload
   ├─ Press 'Enter' to submit (if file selected)
   └─ Standard web app shortcuts

5️⃣  FORM LOADING STATE
   ├─ Disable submit button during processing
   ├─ Show "Analyzing..." message
   ├─ Display loading spinner
   └─ Prevent double-submission

6️⃣  EVENT LOGGING
   └─ Console logging for debugging
   └─ Track user actions
   └─ Performance monitoring
""",
            slide_number=8,
            total_slides=20
        ))
        
        # Slide 9: AI Model
        self.slides.append(PresentationSlide(
            title="🤖 AI MODEL - vegetable_classifier.h5",
            content="""
Pre-trained Deep Learning Model

WHAT IS IT?
├─ Binary file containing neural network
├─ Trained on thousands of vegetable images
├─ Uses Convolutional Neural Networks (CNN)
└─ Custom trained for 10 vegetables

HOW IT WORKS:

INPUT:
  User Image → Any size/format
  ↓
  Resize to 150×150 pixels
  ↓
  Normalize pixel values (0-1)
  ↓

PROCESSING:
  Input Layer: (150, 150, 3) RGB pixels
  ↓
  Convolutional Layers: Extract features
  ├─ Detect colors
  ├─ Detect shapes
  ├─ Detect textures
  └─ Detect patterns
  ↓
  Pooling Layers: Reduce data size
  ↓
  Fully Connected Layers: Classification
  ↓

OUTPUT:
  10 Probability Scores:
  ├─ Tomato:      95.32% ███████████
  ├─ Carrot:       2.15% █
  ├─ Broccoli:     1.20%
  └─ ... (7 more vegetables)
  
  Final Prediction: TOMATO (95.32%)

SUPPORTED VEGETABLES:
├─ Tomato, Carrot, Broccoli, Potato
├─ Cabbage, Cucumber, Bell Pepper
├─ Spinach, Pumpkin, Lettuce (10 total)
└─ Easily replaceable with custom model
""",
            slide_number=9,
            total_slides=20
        ))
        
        # Slide 10: Data Flow
        self.slides.append(PresentationSlide(
            title="📊 COMPLETE DATA FLOW",
            content="""
From User Click to AI Prediction:

1. HOME PAGE LOADS
   http://localhost:5000/ → index.html
   
2. USER SELECTS IMAGE
   Click/Drag image →
   JavaScript triggers (main.js) →
   Validate file →
   Show preview →
   Enable submit button
   
3. USER SUBMITS FORM
   POST request to /predict
   Include: image file, metadata
   
4. SERVER RECEIVES REQUEST
   Flask app @ /predict route
   Check: file exists, size OK, type OK
   
5. SAVE IMAGE
   Save to: uploads/filename.jpg
   
6. IMAGE PROCESSING
   Load → Resize (150×150) →
   Normalize (0-1) → Add batch dimension
   
7. AI PREDICTION
   Feed to neural network →
   Get 10 probability scores →
   Find highest score (argmax) →
   Calculate confidence %
   
8. CLASS MAPPING
   Model output: index 0
   class_map[0] = "Tomato"
   
9. GENERATE RESPONSE
   Create HTML with:
   ├─ Vegetable name
   ├─ Confidence score
   ├─ Image URL
   └─ Error status (false = success)
   
10. RENDER RESULTS
    Browser displays prediction.html
    Show: Image + Name + Confidence Bar
    
11. USER ACTION
    [Try Again] → Back to home
    [Exit] → Goodbye page
""",
            slide_number=10,
            total_slides=20
        ))
        
        # Slide 11: Technology Stack
        self.slides.append(PresentationSlide(
            title="🛠️  TECHNOLOGY STACK",
            content="""
Frontend Technologies:
├─ HTML5: Semantic structure
├─ CSS3: Gradients, animations, flexbox
├─ Vanilla JavaScript: No dependencies
├─ Bootstrap 5: Responsive framework
└─ Font Awesome 6: Beautiful icons

Backend Technologies:
├─ Python 3.8+: Programming language
├─ Flask 2.3.2: Web framework
├─ TensorFlow 2.13.0: AI/ML
├─ NumPy 1.24.3: Numerical computing
├─ Pillow 10.0.0: Image processing
└─ Werkzeug 2.3.6: Security utilities

CDN Libraries:
├─ Bootstrap 5 CSS Framework
├─ Font Awesome Icons
└─ No backend dependencies

Browser APIs:
├─ FileReader API (image preview)
├─ Drag & Drop API
├─ Fetch API (requests)
└─ Local Storage (data persistence)

Why These Technologies?

✓ FastAPI: Fast, lightweight
✓ TensorFlow: Powerful ML framework
✓ Bootstrap: Professional UI
✓ Vanilla JS: No bloat, fast
✓ CDN: Faster loading worldwide
✓ Open Source: Free, customizable
✓ Industry Standard: Used by big companies
""",
            slide_number=11,
            total_slides=20
        ))
        
        # Slide 12: Security
        self.slides.append(PresentationSlide(
            title="🔒 SECURITY FEATURES",
            content="""
Security Measures Implemented:

FILE UPLOAD SECURITY:

✓ Filename Sanitization
  └─ werkzeug.secure_filename()
  └─ Removes dangerous characters
  └─ Prevents directory traversal (e.g., ../../../)

✓ File Type Validation
  └─ Whitelist: PNG, JPG, JPEG, GIF
  └─ Server-side checking (not just client)
  └─ Prevents executable uploads

✓ File Size Limits
  └─ Maximum: 16MB per file
  └─ Prevents server DoS attacks
  └─ Protects disk space

✓ MIME Type Checking
  └─ Validates actual file content
  └─ Not just file extension
  └─ Detects disguised files

APPLICATION SECURITY:

✓ Input Validation
  ├─ Check if file exists
  ├─ Check if filename empty
  ├─ Validate request format
  └─ Error handling

✓ Error Handling
  ├─ Try-catch blocks
  ├─ No sensitive info in errors
  ├─ User-friendly messages
  └─ Graceful failures

✓ Folder Protection
  ├─ uploads/ created safely
  ├─ Isolated storage
  ├─ Path traversal prevention
  └─ Permissions set correctly

✓ Best Practices
  ├─ Use Flask security modules
  ├─ Validate all inputs
  ├─ Sanitize all outputs
  ├─ Never trust user input
  └─ Log security events
""",
            slide_number=12,
            total_slides=20
        ))
        
        # Slide 13: Deployment
        self.slides.append(PresentationSlide(
            title="🚀 DEPLOYMENT & SETUP",
            content="""
How to Run Locally:

STEP 1: Install Python
└─ Download from python.org (3.8+)
└─ Add to PATH during installation

STEP 2: Install Dependencies
cd e:\\vegetable_flask_app
pip install -r requirements.txt

STEP 3: Verify Files
Ensure exists:
├─ vegetable_classifier.h5 (or auto-creates demo)
├─ class_map.pkl (auto-created if missing)
├─ uploads/ folder (auto-created)
└─ All template files

STEP 4: Start Application
python app.py

Log output:
  * Running on http://127.0.0.1:5000
  * Press CTRL+C to quit

STEP 5: Open Browser
http://localhost:5000/

AUTOMATIC SETUP (Windows):
Double-click: setup.bat
└─ Installs virtual environment
└─ Installs dependencies
└─ Shows next steps

CLOUD DEPLOYMENT:

Option 1: Heroku
├─ Create Procfile
├─ heroku login
├─ git push heroku main

Option 2: AWS
├─ DockerFile
├─ Push to ECR
├─ Deploy to ECS

Option 3: PythonAnywhere
├─ Upload files
├─ Set Python version
├─ Configure web app
└─ Enable HTTPS
""",
            slide_number=13,
            total_slides=20
        ))
        
        # Slide 14: Customization
        self.slides.append(PresentationSlide(
            title="🎨 CUSTOMIZATION GUIDE",
            content="""
Easy Ways to Customize:

1. CHANGE COLORS
   Edit: static/css/main.css
   
   :root {
       --primary-color: #FF6B35;
       --secondary-color: #FFB627;
   }

2. MODIFY VEGETABLES
   Option A: Train new model
   └─ Create new vegetable_classifier.h5
   └─ Create matching class_map.pkl
   └─ Place in project root
   
   Option B: Edit class mapping
   Edit: class_map.pkl (binary, or recreate)
   
   {
       0: "NewVegetable1",
       1: "NewVegetable2",
       ...
   }

3. CHANGE UI TEXT
   Edit: templates/index.html
   └─ Welcome message
   └─ Button text
   └─ Instructions
   └─ Feature descriptions

4. MODIFY LAYOUT
   Edit: templates/index.html (structure)
   Edit: static/css/main.css (positioning)
   └─ Add sections
   └─ Reorder elements
   └─ Change grid layout

5. ADD NEW ROUTES
   Edit: app.py
   
   @app.route("/new-page")
   def new_page():
       return render_template("new_page.html")

6. CHANGE PORT
   Edit: app.py (last line)
   
   if __name__ == "__main__":
       app.run(debug=True, port=5001)

7. ADJUST FILE SIZE LIMIT
   Edit: app.py
   
   app.config["MAX_CONTENT_LENGTH"] = 32 * 1024 * 1024
""",
            slide_number=14,
            total_slides=20
        ))
        
        # Slide 15: Troubleshooting
        self.slides.append(PresentationSlide(
            title="🐛 TROUBLESHOOTING",
            content="""
Common Issues & Solutions:

❌ ERROR: ModuleNotFoundError: No module 'flask'
✅ SOLUTION:
   pip install -r requirements.txt
   Or: pip install Flask==2.3.2

❌ ERROR: Port 5000 already in use
✅ SOLUTION:
   Edit app.py, change port:
   app.run(debug=True, port=5001)

❌ ERROR: Model file not found
✅ SOLUTION:
   Place vegetable_classifier.h5 in root
   Or app creates demo mapping automatically

❌ ERROR: Predictions not showing
✅ SOLUTION:
   Open browser console (F12)
   Check for JavaScript errors
   Verify main.js is loaded
   Clear browser cache

❌ ERROR: Upload button not working
✅ SOLUTION:
   Check browser console for errors
   Verify uploads/ folder exists
   Check file permissions
   Restart Flask app

❌ ERROR: Images showing but no predictions
✅ SOLUTION:
   Check TensorFlow installation
   Verify model file format
   Check Python version (3.8+)
   Try pip install --upgrade tensorflow

❌ SLOW PREDICTIONS
✅ SOLUTION:
   Use GPU (install tensorflow-gpu)
   Close other applications
   Reduce image size
   Check system resources

❌ Permission Denied on uploads/
✅ SOLUTION:
   Check folder permissions
   Run as Administrator
   Manually create uploads/ folder
""",
            slide_number=15,
            total_slides=20
        ))
        
        # Slide 16: Architecture
        self.slides.append(PresentationSlide(
            title="🏗️  APPLICATION ARCHITECTURE",
            content="""
High-Level Architecture:

┌─────────────────────────────────────────────┐
│         PRESENTATION LAYER                  │
│     (User sees this)                        │
├─────────────────────────────────────────────┤
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │   Frontend (HTML/CSS/JS)            │   │
│  │ ├─ index.html (Upload Page)        │   │
│  │ ├─ prediction.html (Results)       │   │
│  │ ├─ main.css (Styling)              │   │
│  │ └─ main.js (Interactivity)         │   │
│  └─────────────────────────────────────┘   │
│                                             │
└──────────────────┬──────────────────────────┘
                   │ HTTP Requests
                   ↓
┌─────────────────────────────────────────────┐
│      APPLICATION LOGIC LAYER                │
│     (How it works)                          │
├─────────────────────────────────────────────┤
│                                             │
│  ┌─── Flask Application (app.py) ───────┐  │
│  │  Route Manager                       │  │
│  │  ├─ GET /                           │  │
│  │  ├─ POST /predict                   │  │
│  │  └─ GET /logout                     │  │
│  │                                     │  │
│  │  File Handler                       │  │
│  │  ├─ Receive upload                  │  │
│  │  ├─ Validate                        │  │
│  │  └─ Save to disk                    │  │
│  │                                     │  │
│  │  Image Processor                    │  │
│  │  ├─ Resize                          │  │
│  │  ├─ Normalize                       │  │
│  │  └─ Prepare for ML                  │  │
│  └─────────────────────────────────────┘  │
│                                             │
└──────────────────┬──────────────────────────┘
                   │
                   ↓
┌─────────────────────────────────────────────┐
│      DATA & AI LAYER                        │
│     (The brain)                             │
├─────────────────────────────────────────────┤
│                                             │
│  TensorFlow Model                          │
│  └─ Neural Network                         │
│     ├─ Convolutional Layers                │
│     ├─ Pooling Layers                      │
│     └─ Classification Layers               │
│                                             │
│  Class Mapping                             │
│  └─ { 0: "Tomato", 1: "Carrot", ...}     │
│                                             │
│  Storage                                   │
│  ├─ uploads/ (temp images)                 │
│  ├─ vegetable_classifier.h5 (model)       │
│  └─ class_map.pkl (classes)                │
│                                             │
└─────────────────────────────────────────────┘

Three-Tier Architecture Pattern:
1. Presentation: What user sees
2. Application: How it works
3. Data: What powers it
""",
            slide_number=16,
            total_slides=20
        ))
        
        # Slide 17: Project Stats
        self.slides.append(PresentationSlide(
            title="📈 PROJECT STATISTICS",
            content="""
Code Metrics:

TOTAL PROJECT:
├─ 11 main files
├─ ~1800 lines of code
└─ ~550 lines of documentation

BACKEND (Python):
├─ app.py: 150+ lines
├─ config.py: 70+ lines
└─ Total: ~220 lines

FRONTEND (HTML/CSS/JS):
├─ index.html: 120+ lines
├─ prediction.html: 110+ lines
├─ logout.html: 70+ lines
├─ main.css: 450+ lines
├─ main.js: 350+ lines
└─ Total: ~1100 lines

DOCUMENTATION:
├─ README.md: 300+ lines
├─ QUICKSTART.md: 250+ lines
└─ PRESENTATION: 350+ lines

DEPENDENCIES:
├─ Python packages: 5 core
├─ Frontend CDNs: 2 libraries
└─ Browser APIs: 4+ APIs

FEATURES IMPLEMENTED:
├─ Routes: 3 main
├─ HTML Pages: 3
├─ CSS Animations: 5+
├─ JavaScript Functions: 10+
├─ Security: 5+ measures
├─ Responsive Breakpoints: 3+
└─ Error Handlers: Multiple

SUPPORTED:
├─ Vegetables: 10 types
├─ File Formats: 4 types (PNG, JPG, JPEG, GIF)
├─ Maximum File Size: 16MB
├─ Target Image Size: 150×150 px
├─ Confidence Precision: 2 decimal places
└─ Browser Support: Modern browsers

PERFORMANCE:
├─ Prediction Time: < 1 second
├─ Page Load: < 500ms
├─ Model Size: ~50-100MB
├─ Upload Limit: 16MB
└─ Concurrent Users: 5+ (scalable)
""",
            slide_number=17,
            total_slides=20
        ))
        
        # Slide 18: Future Improvements
        self.slides.append(PresentationSlide(
            title="🚀 FUTURE ENHANCEMENTS",
            content="""
Phase 2 & Beyond - Enhancement Ideas:

USER FEATURES:
├─ User Accounts & Authentication
├─ Prediction History
├─ Save Favorite Results
├─ User Preferences
└─ Persistent Storage

FUNCTIONALITY:
├─ Batch Upload (multiple images)
├─ Webcam Integration
├─ Image Comparison
├─ Confidence Threshold Setting
├─ Vegetable Details (nutrition, recipes)
└─ Real-time Suggestions

MOBILE:
├─ Native iOS App
├─ Native Android App
├─ Progressive Web App (PWA)
└─ Offline Mode

ADVANCED ML:
├─ More Vegetables (50+)
├─ Better Accuracy (99%+)
├─ Multiple Crop Detection
├─ Disease/Quality Assessment
└─ Edge Device Support

ANALYTICS:
├─ User Statistics
├─ Prediction Logs
├─ Model Accuracy Tracking
├─ Usage Analytics
└─ API Metrics

MONETIZATION:
├─ API for Third-Party Apps
├─ Premium Features
├─ Cloud Storage Plans
├─ Subscription Model
└─ White Label Version

INTEGRATION:
├─ Database Backend
├─ API Marketplace
├─ Social Sharing
├─ Email Notifications
└─ Webhook Support

INFRASTRUCTURE:
├─ Docker Containerization
├─ Kubernetes Orchestration
├─ CDN Distribution
├─ Load Balancing
└─ Auto-scaling
""",
            slide_number=18,
            total_slides=20
        ))
        
        # Slide 19: Key Takeaways
        self.slides.append(PresentationSlide(
            title="🎓 KEY TAKEAWAYS",
            content="""
What We've Built:

✓ COMPLETE WEB APPLICATION
  └─ Production-ready Python Flask app
  └─ AI-powered vegetable classification
  └─ Beautiful responsive UI
  └─ Secure file handling
  └─ Comprehensive error handling

✓ THREE-TIER ARCHITECTURE
  ├─ Presentation: Frontend UI
  ├─ Application: Business Logic
  └─ Data: AI & Storage

✓ MODERN DEVELOPMENT PRACTICES
  ├─ MVC Pattern (Model-View-Controller)
  ├─ Responsive Design (Mobile-First)
  ├─ Security Best Practices
  ├─ Error Handling & Validation
  ├─ Code Organization & Comments
  └─ Comprehensive Documentation

✓ COMPLETE TECHNOLOGY STACK
  ├─ Backend: Python/Flask
  ├─ Frontend: HTML/CSS/JavaScript
  ├─ AI: TensorFlow/Keras
  ├─ Framework: Bootstrap
  └─ All modern & maintained

LEARNING OUTCOMES:

✓ Full Stack Development
✓ Web Application Architecture
✓ Machine Learning Integration
✓ Image Processing Techniques
✓ Frontend Design Best Practices
✓ Security & Validation
✓ Responsive Web Design
✓ API Design Patterns
✓ Deployment Strategies
✓ Production-Ready Code

SUCCESS METRICS:

✓ Fully Functional Application
✓ Beautiful User Interface
✓ Fast & Accurate Predictions
✓ Secure File Handling
✓ Well-Documented Code
✓ Easy to Customize
✓ Ready to Deploy
✓ Scalable Architecture
""",
            slide_number=19,
            total_slides=20
        ))
        
        # Slide 20: Thank You / Conclusion
        self.slides.append(PresentationSlide(
            title="🎉 THANK YOU!",
            content="""
╔════════════════════════════════════════════════════════════════════════════╗
║                       PROJECT COMPLETE & READY!                           ║
╚════════════════════════════════════════════════════════════════════════════╝

GreenClassify v1.0
├─ Status: ✅ Production Ready
├─ Version: 1.0
├─ Date: February 2026
└─ Ready to Deploy & Customize

GET STARTED NOW:

1. Install Dependencies:
   pip install -r requirements.txt

2. Run Application:
   python app.py

3. Open Browser:
   http://localhost:5000/

4. Start Classifying:
   Upload vegetable images

5. Customize:
   Edit colors, classes, features

6. Deploy:
   Heroku, AWS, PythonAnywhere

WHAT YOU LEARNED:

✓ Building complete web applications
✓ Integrating AI/ML models
✓ Creating beautiful UIs
✓ Handling security
✓ Production deployment

NEXT STEPS:

→ Review the code
→ Customize for your needs
→ Deploy to cloud
→ Add new features
→ Build your own version

RESOURCES:

├─ README.md: Full documentation
├─ QUICKSTART.md: 5-minute setup
├─ This Script: Presentation slides
└─ Code Comments: Line-by-line explanation

═════════════════════════════════════════════════════════════════════════════

             "From Concept to Production: Complete AI Web App"

═════════════════════════════════════════════════════════════════════════════

Thank you for exploring GreenClassify! 🥗✨

Questions? Check documentation or review the code.
Ready to deploy? Run 'python app.py' now!

═════════════════════════════════════════════════════════════════════════════
""",
            slide_number=20,
            total_slides=20
        ))
    
    def run(self):
        """Run the presentation"""
        PresentationSlide.clear_screen()
        
        while self.current_slide < len(self.slides):
            slide = self.slides[self.current_slide]
            slide.display()
            
            # Get user input
            print("\n" + "─" * 80)
            print("Navigation: [N]ext | [P]revious | [Q]uit | [J]ump to slide")
            print("─" * 80)
            
            choice = input("\nYour choice: ").strip().lower()
            
            if choice == 'n':
                if self.current_slide < len(self.slides) - 1:
                    self.current_slide += 1
                else:
                    print("\n✓ Reached the end of presentation!")
                    break
            elif choice == 'p':
                if self.current_slide > 0:
                    self.current_slide -= 1
                else:
                    print("\n✗ Already at the beginning!")
            elif choice == 'q':
                print("\n👋 Thank you for viewing the presentation!")
                break
            elif choice == 'j':
                try:
                    slide_num = int(input("Jump to slide (1-20): "))
                    if 1 <= slide_num <= len(self.slides):
                        self.current_slide = slide_num - 1
                    else:
                        print(f"✗ Please enter a number between 1 and {len(self.slides)}")
                except ValueError:
                    print("✗ Invalid input. Please enter a number.")
            else:
                print("✗ Invalid choice. Please try again.")
            
            time.sleep(0.5)
    
    def generate_pdf_outline(self):
        """Generate a text outline for PDF conversion"""
        outline = []
        for slide in self.slides:
            outline.append(f"{'=' * 80}")
            outline.append(f"SLIDE {slide.slide_number}")
            outline.append(f"{'=' * 80}")
            outline.append(f"{slide.title}")
            outline.append("")
            outline.append(slide.content)
            outline.append("\n")
        
        return "\n".join(outline)


def main():
    """Main entry point"""
    print("\n🥗 GreenClassify - Interactive Presentation\n")
    print("Starting in 3 seconds...\n")
    
    for i in range(3, 0, -1):
        print(f"{i}...", end=" ", flush=True)
        time.sleep(1)
    print("GO!\n")
    
    time.sleep(0.5)
    
    # Run presentation
    presentation = Presentation()
    presentation.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Presentation interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please make sure you're running this from the vegetable_flask_app directory.")
