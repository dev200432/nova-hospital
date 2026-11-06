document.addEventListener("DOMContentLoaded", function () {
    
    
    const slides = document.querySelectorAll('.slide');
    if (slides.length > 0) {
        let currentSlide = 0;
        function nextSlide() {
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
        }
        setInterval(nextSlide, 4000);
    }

    
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('status') === 'success') {
        showToast('✅ Appointment Booked Successfully! We will contact you shortly.');
    }
});

// Global Toast Function
function showToast(message) {
    let container = document.getElementById('toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toast-container';
        container.style.cssText = 'position: fixed; top: 20px; right: 20px; z-index: 9999;';
        document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.style.cssText = `
        background: #064e3b;
        color: #ffffff;
        padding: 16px 24px;
        border-radius: 8px;
        border-left: 6px solid #10b981;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        font-size: 15px;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 10px;
        animation: slideIn 0.4s ease, fadeOut 0.5s ease 4s forwards;
        margin-bottom: 10px;
    `;
    toast.innerText = message;
    container.appendChild(toast);

    setTimeout(() => {
        toast.remove();
    }, 4500);
}