/**
 * Smart College Helper Portal - Main JavaScript
 * Handles animations, interactions, and dynamic features
 */

// Page Loader
document.addEventListener('DOMContentLoaded', function() {
    const loader = document.querySelector('.page-loader');
    if (loader) {
        setTimeout(() => {
            loader.classList.add('hidden');
        }, 1000);
    }

    // Initialize all features
    initAnimations();
    initFormValidation();
    initTooltips();
});

// Smooth scroll animations
function initAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.6s ease forwards';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe all cards
    document.querySelectorAll('.dashboard-card, .glass-card, .note-card').forEach(card => {
        observer.observe(card);
    });
}

// Form validation
function initFormValidation() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = 'var(--error)';
                } else {
                    field.style.borderColor = '';
                }
            });

            if (!isValid) {
                e.preventDefault();
                showNotification('Please fill all required fields', 'error');
            }
        });
    });
}

// Tooltips
function initTooltips() {
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    tooltipElements.forEach(element => {
        element.addEventListener('mouseenter', function() {
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.textContent = this.getAttribute('data-tooltip');
            document.body.appendChild(tooltip);

            const rect = this.getBoundingClientRect();
            tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
            tooltip.style.top = rect.top - tooltip.offsetHeight - 10 + 'px';

            setTimeout(() => tooltip.classList.add('show'), 10);
        });

        element.addEventListener('mouseleave', function() {
            const tooltip = document.querySelector('.tooltip');
            if (tooltip) {
                tooltip.remove();
            }
        });
    });
}

// Notification system
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `message message-${type}`;
    notification.innerHTML = `
        <i class="fas fa-${type === 'error' ? 'exclamation-circle' : type === 'success' ? 'check-circle' : 'info-circle'}"></i>
        <span>${message}</span>
        <button class="message-close" onclick="this.parentElement.remove()">&times;</button>
    `;

    const container = document.querySelector('.messages-container') || createMessagesContainer();
    container.appendChild(notification);

    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

function createMessagesContainer() {
    const container = document.createElement('div');
    container.className = 'messages-container';
    document.body.appendChild(container);
    return container;
}

// AI Chat Functions
function sendAIMessage() {
    const input = document.getElementById('chat-input');
    const query = input.value.trim();

    if (!query) return;

    // Add user message to chat
    addChatMessage(query, 'user');
    input.value = '';

    // Show AI thinking
    showAIThinking();

    // Send to backend
    fetch('/ai-assistant/api/query/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({
                query: query
            })
        })
        .then(response => response.json())
        .then(data => {
            hideAIThinking();
            if (data.success) {
                addChatMessage(data.response, 'ai');
            } else {
                addChatMessage('Sorry, I encountered an error. Please try again.', 'ai');
            }
        })
        .catch(error => {
            hideAIThinking();
            addChatMessage('Connection error. Please check your internet.', 'ai');
        });
}

function addChatMessage(message, type) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message ${type}`;

    if (type === 'ai') {
        // Format AI response with markdown-like formatting
        messageDiv.innerHTML = formatAIMessage(message);
    } else {
        messageDiv.textContent = message;
    }

    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Animate message
    messageDiv.style.animation = 'fadeInUp 0.3s ease';
}

function formatAIMessage(text) {
    // Convert markdown-like formatting to HTML
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    text = text.replace(/\*(.*?)\*/g, '<em>$1</em>');
    text = text.replace(/`(.*?)`/g, '<code>$1</code>');
    text = text.replace(/\n/g, '<br>');
    text = text.replace(/^(\d+\.\s)/gm, '<br>$1');
    return text;
}

function showAIThinking() {
    const chatMessages = document.getElementById('chat-messages');
    const thinkingDiv = document.createElement('div');
    thinkingDiv.id = 'ai-thinking';
    thinkingDiv.className = 'chat-message ai ai-thinking';
    thinkingDiv.innerHTML = `
        <div class="ai-thinking">
            <span>AI is analyzing your query...</span>
            <div class="ai-thinking-dots">
                <div class="ai-thinking-dot"></div>
                <div class="ai-thinking-dot"></div>
                <div class="ai-thinking-dot"></div>
            </div>
        </div>
    `;
    chatMessages.appendChild(thinkingDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function hideAIThinking() {
    const thinking = document.getElementById('ai-thinking');
    if (thinking) {
        thinking.remove();
    }
}

// Get CSRF token
function getCSRFToken() {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        const [name, value] = cookie.trim().split('=');
        if (name === 'csrftoken') {
            return value;
        }
    }
    return '';
}

// Enter key to send message
document.addEventListener('DOMContentLoaded', function() {
    const chatInput = document.getElementById('chat-input');
    if (chatInput) {
        chatInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendAIMessage();
            }
        });
    }

    const sendButton = document.getElementById('send-button');
    if (sendButton) {
        sendButton.addEventListener('click', sendAIMessage);
    }
});

// Study Plan Form Handler
function generateStudyPlan() {
    const form = document.getElementById('study-plan-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const examDate = new Date(document.getElementById('exam_date').value);
            const today = new Date();

            if (examDate <= today) {
                e.preventDefault();
                showNotification('Exam date must be in the future!', 'error');
                return false;
            }
        });
    }
}

// Initialize study plan handler
document.addEventListener('DOMContentLoaded', generateStudyPlan);

// Smooth scroll to top
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Add scroll to top button
window.addEventListener('scroll', function() {
    const scrollTop = document.querySelector('.scroll-to-top');
    if (window.pageYOffset > 300) {
        if (!scrollTop) {
            const button = document.createElement('button');
            button.className = 'scroll-to-top btn';
            button.innerHTML = '<i class="fas fa-arrow-up"></i>';
            button.onclick = scrollToTop;
            button.style.cssText = 'position: fixed; bottom: 20px; right: 20px; z-index: 1000; width: 50px; height: 50px; border-radius: 50%;';
            document.body.appendChild(button);
        }
    } else {
        const scrollTop = document.querySelector('.scroll-to-top');
        if (scrollTop) scrollTop.remove();
    }
});