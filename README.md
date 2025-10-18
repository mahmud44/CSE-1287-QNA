
---

## ⚙️ Functionality Summary

1. **Sidebar Toggle:**  
   - Mobile-friendly slide-in/out menu using Tailwind’s transform utilities.  
2. **Active Highlight:**  
   - The currently viewed subtopic is visually highlighted.  
3. **Accordion Q&A:**  
   - Clicking a question expands or collapses its answer.  
   - Uses pure JS for smooth transitions.  

---

## 🧠 How It Works

- The website loads all content (either directly from `index.html` or dynamically from `content.md`).
- JavaScript binds click events to:
  - Sidebar links → Scroll or display the selected section.  
  - Question headers → Toggle the corresponding answer.  
- TailwindCSS ensures responsive behavior and consistent design.

---

## 🛠️ Setup Instructions

1. **Download or clone** this repository.
2. Open `index.html` in your browser — it runs locally without a server.
3. (Optional) Edit `content.md` and regenerate the HTML if you want to update questions or topics.

---

## 📜 License

This project is open for educational and personal use.  
Attribution is appreciated if reused or modified.

---

**Author:** [Your Name]  
**Course Reference:** CSE 1287 – Computer Fundamentals & C Programming  
**Built with:** ❤️ HTML + Tailwind + JS
