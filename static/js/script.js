// PPE Detection Frontend Script

document.addEventListener('DOMContentLoaded', function() {
    const uploadArea = document.getElementById('uploadArea');
    const fileInput = document.getElementById('imageInput');
    const uploadBtn = document.getElementById('uploadBtn');
    const loading = document.getElementById('loading');
    const resultDiv = document.getElementById('result');

    // Initialize drag and drop functionality
    initializeDragAndDrop();

    function initializeDragAndDrop() {
        // Click to open file dialog
        uploadArea.addEventListener('click', () => fileInput.click());

        // Drag over effect
        uploadArea.addEventListener('dragover', handleDragOver);

        // Drag leave effect
        uploadArea.addEventListener('dragleave', handleDragLeave);

        // Drop file
        uploadArea.addEventListener('drop', handleDrop);

        // File input change
        fileInput.addEventListener('change', handleFileSelect);
    }

    function handleDragOver(e) {
        e.preventDefault();
        uploadArea.classList.add('dragover');
    }

    function handleDragLeave() {
        uploadArea.classList.remove('dragover');
    }

    function handleDrop(e) {
        e.preventDefault();
        uploadArea.classList.remove('dragover');

        const files = e.dataTransfer.files;
        if (files.length > 0) {
            fileInput.files = files;
            updateUploadText(files[0].name);
        }
    }

    function handleFileSelect(e) {
        if (e.target.files.length > 0) {
            updateUploadText(e.target.files[0].name);
        }
    }

    function updateUploadText(filename) {
        const uploadText = uploadArea.querySelector('.upload-text');
        uploadText.textContent = `Selected: ${filename}`;
    }

    // Main upload function
    window.uploadImage = async function() {
        const file = fileInput.files[0];
        if (!file) {
            showAlert('Please select an image file.', 'error');
            return;
        }

        // Validate file type
        if (!file.type.startsWith('image/')) {
            showAlert('Please select a valid image file.', 'error');
            return;
        }

        // Show loading state
        setLoadingState(true);

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('/predict/', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                const blob = await response.blob();
                const imageUrl = URL.createObjectURL(blob);
                showResult(imageUrl);
            } else {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }
        } catch (error) {
            console.error('Error:', error);
            showError('Error processing image. Please try again.');
        } finally {
            setLoadingState(false);
        }
    };

    function setLoadingState(isLoading) {
        uploadBtn.disabled = isLoading;
        uploadBtn.textContent = isLoading ? 'Processing...' : 'Detect PPE';
        loading.style.display = isLoading ? 'block' : 'none';
    }

    function showResult(imageUrl) {
        resultDiv.innerHTML = `
            <img src="${imageUrl}" alt="Detection Result" class="result-image">
            <p style="text-align: center; margin-top: 15px; color: #4a5568; font-weight: 500;">
                ✅ Detection completed successfully
            </p>
        `;
    }

    function showError(message) {
        resultDiv.innerHTML = `
            <div class="no-result">
                <div style="font-size: 3rem; margin-bottom: 15px;">❌</div>
                <p>${message}</p>
            </div>
        `;
    }

    function showAlert(message, type = 'info') {
        // Simple alert for now - could be enhanced with a proper notification system
        alert(message);
    }

    // Add keyboard support
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && e.target === uploadBtn && !uploadBtn.disabled) {
            uploadImage();
        }
    });
});
