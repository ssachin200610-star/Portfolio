// API Base URL
const API_BASE = "";

// ==================== PROFILE IMAGE ERROR HANDLER ====================
function handleProfileImageError(img) {
  img.style.display = "none";
  const container = img.parentElement;
  const fallback = document.createElement("div");
  fallback.style.cssText = `
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #667eea, #764ba2);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 60px;
    border-radius: 50%;
  `;
  fallback.textContent = "👤";
  container.appendChild(fallback);
}

// ==================== VISITOR COUNT LOADER ====================
async function loadVisitorCount() {
  try {
    const res = await fetch(`${API_BASE}/api/widgets`);
    if (!res.ok) throw new Error("Failed to load widgets");
    const data = await res.json();
    const visitorEl = document.getElementById("visitorCount");
    if (visitorEl) {
      visitorEl.textContent = data.visitors || "100";
    }
  } catch (err) {
    console.error("Error loading visitor count:", err);
    const visitorEl = document.getElementById("visitorCount");
    if (visitorEl) {
      visitorEl.textContent = "100";
    }
  }
}

// ==================== CONTACT FORM HANDLER ====================
document.addEventListener("DOMContentLoaded", () => {
  const contactForm = document.getElementById("contactForm");
  
  if (contactForm) {
    contactForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      
      const nameInput = contactForm.querySelector('input[name="name"]');
      const emailInput = contactForm.querySelector('input[name="email"]');
      const messageInput = contactForm.querySelector('textarea[name="message"]');
      const statusEl = document.getElementById("formMessage");
      
      const name = nameInput.value.trim();
      const email = emailInput.value.trim();
      const message = messageInput.value.trim();
      
      // Clear previous messages
      statusEl.className = '';
      
      if (!name || !email || !message) {
        statusEl.textContent = "❌ All fields are required!";
        statusEl.classList.add("error");
        return;
      }
      
      if (!email.includes("@")) {
        statusEl.textContent = "❌ Please enter a valid email address!";
        statusEl.classList.add("error");
        return;
      }
      
      try {
        statusEl.textContent = "⏳ Sending your message...";
        statusEl.className = '';
        
        const res = await fetch(`${API_BASE}/api/contact`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ name, email, message }),
        });
        
        if (!res.ok) {
          const errorData = await res.json().catch(() => ({}));
          throw new Error(errorData.error || "Failed to send message");
        }
        
        statusEl.textContent = "✅ MESSAGE SENT SUCCESSFULLY! Thank you for reaching out!";
        statusEl.classList.add("success");
        contactForm.reset();
        
        // Reload visitor count after successful message
        setTimeout(() => {
          loadVisitorCount();
        }, 1000);
      } catch (err) {
        console.error("Error sending message:", err);
        statusEl.textContent = `❌ FAILED: ${err.message}`;
        statusEl.classList.add("error");
      }
    });
  }
  
  // Load visitor count on page load
  loadVisitorCount();
});
