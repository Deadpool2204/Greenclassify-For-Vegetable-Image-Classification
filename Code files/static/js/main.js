// ==================== Vegetable Classification App ==================== //
console.log("🥗 GreenClassify App Loaded - Ready to classify vegetables!");

// ==================== DOM Elements ==================== //
const uploadArea = document.getElementById('uploadArea');
const imageInput = document.getElementById('imageInput');
const previewSection = document.getElementById('previewSection');
const preview = document.getElementById('preview');
const fileName = document.getElementById('fileName');
const uploadForm = document.getElementById('uploadForm');

// ==================== Drag and Drop Functionality ==================== //
if (uploadArea) {
    // Click to upload
    uploadArea.addEventListener('click', () => imageInput.click());

    // Drag over
    uploadArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadArea.style.borderColor = '#2ecc71';
        uploadArea.style.background = 'linear-gradient(135deg, #e8ffe8 0%, #d4f8e1 100%)';
    });

    // Drag leave
    uploadArea.addEventListener('dragleave', () => {
        uploadArea.style.borderColor = '#27ae60';
        uploadArea.style.background = 'linear-gradient(135deg, #f5fff8 0%, #eef9f5 100%)';
    });

    // Drop
    uploadArea.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadArea.style.borderColor = '#27ae60';
        uploadArea.style.background = 'linear-gradient(135deg, #f5fff8 0%, #eef9f5 100%)';
        
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            imageInput.files = files;
            handleImageSelect();
        }
    });

    // Regular file input change
    imageInput.addEventListener('change', handleImageSelect);
}

// ==================== Image Preview Handler ==================== //
function handleImageSelect() {
    const file = imageInput.files[0];
    
    if (file) {
        // Validate file type
        const validTypes = ['image/png', 'image/jpeg', 'image/gif', 'image/jpg', 'image/webp'];
        if (!validTypes.includes(file.type)) {
            showAlert('Please select a valid image file (PNG, JPG, JPEG, GIF)', 'danger');
            imageInput.value = '';
            return;
        }

        // Validate file size (max 16MB)
        const maxSize = 16 * 1024 * 1024;
        if (file.size > maxSize) {
            showAlert('File size must be less than 16MB', 'danger');
            imageInput.value = '';
            return;
        }

        // Show preview
        const reader = new FileReader();
        reader.onload = (e) => {
            preview.src = e.target.result;
            fileName.textContent = `Selected: ${file.name}`;
            previewSection.style.display = 'block';
            uploadArea.style.opacity = '0.5';
        };
        reader.readAsDataURL(file);
    }
}

// ==================== Form Submission Handler ==================== //
if (uploadForm) {
    uploadForm.addEventListener('submit', (e) => {
        if (!imageInput.files[0]) {
            e.preventDefault();
            showAlert('Please select an image first', 'warning');
        }
    });
}

// ==================== Alert Helper Function ==================== //
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.setAttribute('role', 'alert');
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    const container = document.querySelector('main .container');
    if (container) {
        container.insertBefore(alertDiv, container.firstChild);
        setTimeout(() => alertDiv.remove(), 5000);
    }
}

// ==================== Add Event Listeners for Action Buttons ==================== //
document.addEventListener('DOMContentLoaded', () => {
    // Log page info
    console.log('📱 Page loaded: ' + document.title);

    // Add smooth scroll behavior
    document.documentElement.style.scrollBehavior = 'smooth';

    // Add loading state for form submission
    if (uploadForm) {
        uploadForm.addEventListener('submit', () => {
            const submitBtn = uploadForm.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Analyzing...';
            }
        });
    }

    // Log user actions
    const actionButtons = document.querySelectorAll('.btn');
    actionButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            console.log('User clicked: ' + btn.textContent.trim());
        });
    });
});

// ==================== Keyboard Shortcuts ==================== //
document.addEventListener('keydown', (e) => {
    // Press 'U' to focus on file input
    if (e.key === 'u' || e.key === 'U') {
        if (imageInput) imageInput.focus();
    }
    // Press 'Enter' to submit form when file is selected
    if (e.key === 'Enter' && imageInput && imageInput.files[0]) {
        if (uploadForm) uploadForm.submit();
    }
});

// ==================== Performance Monitoring ==================== //
window.addEventListener('load', () => {
    const perfData = window.performance.timing;
    const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
    console.log(`⚡ Page loaded in ${pageLoadTime}ms`);
});

console.log('✅ All event listeners initialized successfully!');
