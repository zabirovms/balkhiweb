// Main JavaScript for the Rumi Poetry Application

document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
    }
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', function(event) {
        if (mobileMenu && !mobileMenu.contains(event.target) && 
            mobileMenuButton && !mobileMenuButton.contains(event.target) && 
            !mobileMenu.classList.contains('hidden')) {
            mobileMenu.classList.add('hidden');
        }
    });
    
    // Poem filtering functionality
    initializeFilterDependencies();
});

// Function to initialize the dependencies between filters
function initializeFilterDependencies() {
    // This is handled in the poems.html template with inline JavaScript
    // But could be moved here for organization if desired
}

// Function to format poem text for display
function formatPoemText(text) {
    if (!text) return '';
    
    // Replace newlines with HTML line breaks
    return text.replace(/\n/g, '<br>');
}

// Function to copy text to clipboard
function copyToClipboard(text) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    document.body.appendChild(textArea);
    textArea.select();
    
    try {
        const successful = document.execCommand('copy');
        const message = successful ? 'Матн нусхабардорӣ шуд!' : 'Нусхабардорӣ бо хато анҷом ёфт.';
        showNotification(message);
    } catch (err) {
        console.error('Нусхабардорӣ бо хато анҷом ёфт:', err);
        showNotification('Нусхабардорӣ бо хато анҷом ёфт.');
    }
    
    document.body.removeChild(textArea);
}

// Function to show notification
function showNotification(message, type = 'success') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `fixed bottom-4 right-4 px-6 py-3 rounded-md text-white ${
        type === 'success' ? 'bg-green-600' : 'bg-red-600'
    } shadow-lg transition-opacity duration-300 opacity-0`;
    notification.textContent = message;
    
    // Add to DOM
    document.body.appendChild(notification);
    
    // Trigger animation
    setTimeout(() => notification.classList.replace('opacity-0', 'opacity-100'), 10);
    
    // Remove after timeout
    setTimeout(() => {
        notification.classList.replace('opacity-100', 'opacity-0');
        setTimeout(() => document.body.removeChild(notification), 300);
    }, 3000);
}
