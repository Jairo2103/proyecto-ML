// Funciones para generar información del caso
function generateCaseNumber() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    const random = Math.floor(Math.random() * 1000).toString().padStart(3, '0');
    return `PD-${year}${month}${day}-${random}`;
}

function formatTimestamp() {
    const now = new Date();
    return now.toLocaleString('es-ES', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    });
}

// Manejar selección de archivo
function handleFileSelect(event) {
    const file = event.target.files[0];
    const fileInfo = document.getElementById('fileInfo');
    const fileName = document.getElementById('fileName');
    const fileSize = document.getElementById('fileSize');
    const caseNumber = document.getElementById('caseNumber');
    const timestamp = document.getElementById('timestamp');
    const analyzeBtn = document.getElementById('analyzeBtn');

    if (file) {
        // Validar tipo de archivo
        const validTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp'];
        if (!validTypes.includes(file.type)) {
            alert('⚠️ Tipo de archivo no válido. Solo se permiten: JPG, PNG, WEBP');
            event.target.value = '';
            return;
        }

        // Validar tamaño (10MB máximo)
        const maxSize = 10 * 1024 * 1024; // 10MB en bytes
        if (file.size > maxSize) {
            alert('⚠️ El archivo es demasiado grande. Tamaño máximo: 10MB');
            event.target.value = '';
            return;
        }

        // Mostrar información del archivo
        fileName.textContent = file.name;
        fileSize.textContent = `${(file.size / 1024 / 1024).toFixed(2)} MB • ${file.type}`;
        caseNumber.textContent = generateCaseNumber();
        timestamp.textContent = formatTimestamp();
        
        // Mostrar sección de información y habilitar botón
        fileInfo.classList.add('show');
        analyzeBtn.disabled = false;
        
        console.log('✅ Archivo válido cargado:', file.name);
    }
}

// Efectos de drag & drop
function initializeDragAndDrop() {
    const uploadArea = document.querySelector('.upload-area');
    
    if (!uploadArea) return;
    
    uploadArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadArea.style.border = '2px dashed #4CAF50';
        uploadArea.style.backgroundColor = 'rgba(76, 175, 80, 0.1)';
    });

    uploadArea.addEventListener('dragleave', (e) => {
        e.preventDefault();
        uploadArea.style.border = '2px dashed #ccc';
        uploadArea.style.backgroundColor = 'transparent';
    });

    uploadArea.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadArea.style.border = '2px dashed #ccc';
        uploadArea.style.backgroundColor = 'transparent';

        const dt = e.dataTransfer;
        const files = dt.files;

        if (files.length > 0) {
            // Simular un evento de selección de archivo
            const event = {
                target: {
                    files: files
                }
            };
            handleFileSelect(event);
        }
    });
}