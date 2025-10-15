# quantum-dev-portfolio
# 🌀 Bloch Sphere Simulator (MVP)

A minimal Python project that generates **one random qubit** and displays it as a point on the **Bloch sphere**.  
Part of my *Quantum Dev Portfolio*.

---

## 🧭 Project Goal
To learn how a qubit can be represented on the Bloch sphere using the angles **θ (theta)** and **φ (phi)**,  
and to visualise that quantum state in 3D with Matplotlib.

---

## 🧱 Step-by-Step Setup Guide (Windows + Git Bash)

### 1️⃣ Install Python
1. Go to [python.org/downloads](https://www.python.org/downloads/).
2. Download the latest version (Python 3.x).
3. During installation **tick** ✅ *“Add Python to PATH”*.

To confirm:
bash
python --version

Get Git Bash
Download from git-scm.com
During setup, select “Use Git from Windows Command Prompt”.
Open Git Bash after installation.

3️⃣ Clone this repository
In Git Bash:

cd /c/Users/<you>/Documents
git clone https://github.com/<your-username>/quantum-dev-portfolio.git
cd quantum-dev-portfolio/bloch-sphere-simulator

4️⃣ Create a virtual environment
python -m venv venv-bloch
source venv-bloch/Scripts/activate


Your prompt should now show (venv-bloch).

5️⃣ Install dependencies
python -m pip install --upgrade pip
python -m pip install numpy matplotlib

6️⃣ Save the installed packages (optional but good practice)
python -m pip freeze > requirements.txt

7️⃣ Run the simulator
python bloch_one_qubit.py


A 3D plot window will open showing a Bloch sphere with one red dot —
that dot is a randomly generated qubit.

8️⃣ Deactivate the environment when done
deactivate
