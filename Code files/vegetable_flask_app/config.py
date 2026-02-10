"""
GreenClassify Configuration File
Modify this file to customize the application behavior
"""

# Flask Configuration
FLASK_DEBUG = True
FLASK_ENV = 'development'
HOST = '127.0.0.1'
PORT = 5000

# File Upload Configuration
MAX_FILE_SIZE_MB = 16  # Maximum file size in MB
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
UPLOAD_FOLDER = 'uploads'

# Model Configuration
MODEL_PATH = 'vegetable_classifier.h5'
CLASS_MAP_PATH = 'class_map.pkl'
IMAGE_TARGET_SIZE = (150, 150)
IMAGE_NORMALIZATION = True

# Model Classes (Default)
DEFAULT_CLASSES = {
    0: "Tomato",
    1: "Carrot",
    2: "Broccoli",
    3: "Potato",
    4: "Cabbage",
    5: "Cucumber",
    6: "Bell Pepper",
    7: "Spinach",
    8: "Pumpkin",
    9: "Lettuce"
}

# Prediction Configuration
CONFIDENCE_THRESHOLD = 0.3  # Minimum confidence to show result
SHOW_CONFIDENCE_SCORE = True
VERBOSE_PREDICTIONS = False

# UI Configuration
SHOW_FEATURE_ICONS = True
ENABLE_DRAG_DROP = True
SHOW_FILE_PREVIEW = True
ANIMATION_ENABLED = True

# Security Configuration
ENABLE_CORS = False
SECURE_HEADERS = True
SESSION_TIMEOUT = 3600  # 1 hour in seconds
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Logging Configuration
LOG_LEVEL = 'INFO'  # DEBUG, INFO, WARNING, ERROR
ENABLE_REQUEST_LOGGING = True
LOG_FILE = 'app.log'

# Environment Specific Settings
PRODUCTION_SETTINGS = {
    'FLASK_DEBUG': False,
    'FLASK_ENV': 'production',
    'ENABLE_CORS': True,
    'SECURE_HEADERS': True,
}

DEVELOPMENT_SETTINGS = {
    'FLASK_DEBUG': True,
    'FLASK_ENV': 'development',
    'ENABLE_CORS': True,
    'SECURE_HEADERS': False,
}

# Advanced Settings
USE_GPU = True  # Use GPU if available (TensorFlow)
BATCH_PREDICTION = False
CACHE_MODEL = True
CLEANUP_UPLOADS = True  # Delete old uploads
CLEANUP_DAYS = 7  # Delete uploads older than 7 days
