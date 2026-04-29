# Combo Maker

Combo Maker is a visually rich web application that allows fighting game players to easily generate, visualize, and share combo notations using in-game graphical inputs. 

Currently supports visual keyboards for:
- Street Fighter 6 (SF6)
- Tekken 8
- 2XKO
- Generic / Traditional NumPad Notation

Built with **Python**, **Flask**, and **Vanilla CSS/JS** on the frontend, featuring dynamic image scaling and exporting functionality via `html2canvas`.

---

## 🛠️ Local Development Setup

To run this project locally, you will need Python 3 and a package manager (like pip).

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd combomaker
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   
   # Windows:
   .venv\Scripts\activate
   # Mac/Linux:
   source .venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask development server:**
   ```bash
   python run.py
   ```
   The app will be accessible at `http://127.0.0.1:5000/`.

---

## 🚀 Deployment to Vercel

This project is fully configured to run on [Vercel's Serverless environment](https://vercel.com/docs/concepts/functions/serverless-functions).

### Automatic Deployment

1. Make sure all your code is pushed to your GitHub repository.
2. Go to the **Vercel Dashboard** and click **"Add New..."** > **"Project"**.
3. Import your GitHub repository.
4. Leave the Framework Preset as **Other**.
5. Vercel will automatically detect the `vercel.json` file and use the `@vercel/python` runtime via `api/index.py`.
6. Click **Deploy**. In under a minute, your website will be live!

### Manual / CLI Deployment

If you prefer using the Vercel CLI:
```bash
npx vercel
```
Vercel will detect configurations automatically and prompt you through the quick deployment steps.

---

## 📁 Project Structure

```
d: \
 `-- Programacion
      `-- combomaker
           |-- api/                # Vercel serverless entry points
           |   `-- index.py
           |-- combomaker/         # Main Flask Application module
           |   |-- static/         # Image assets and icons
           |   |-- templates/      # Jinja2 HTML templates
           |   |-- __init__.py     # Flask app factory
           |   `-- home.py         # Primary Routes and dictionaries
           |-- .gitignore
           |-- README.md
           |-- requirements.txt    # Python dependencies
           |-- run.py              # Local dev server starter
           `-- vercel.json         # Vercel Configuration
```

## 📝 Technologies Used
* **Backend Framework:** Flask (Python)
* **Frontend:** HTML5, Modern CSS Variables & Flexbox Layouts, Vanilla JavaScript.
* **Libraries:** `html2canvas` for screenshot exports.
