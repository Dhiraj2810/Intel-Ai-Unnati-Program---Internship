# Workshop Day 1 - Development Environment Setup

This guide will walk you through setting up your development environment for development, including WSL (for Windows users), VS Code, Git, UV package manager, and running your first AI text generation example using the Groq API.

---

## Prerequisites
- Windows 10/11 (for WSL setup) or macOS
- Administrator/sudo access on your machine
- Stable internet connection

---

## Step 1: Install WSL (Windows Subsystem for Linux)

**For Windows Users:**

1. Open Command Prompt (CMD) as Administrator
2. Run the following command:
   ```bash
   wsl --install
   ```

3. **Restart your computer** (this is required for WSL installation to complete)

4. After restart, WSL will launch automatically. You'll be prompted to:
   - Create a **username** (use lowercase, no spaces)
   - Create a **password** (you won't see characters as you type - this is normal)
   - Confirm your password

5. Verify WSL installation:
   ```bash
   wsl --version
   ```
   or
   ```bash
   wsl -l -v
   ```

**For macOS Users:**
- Skip this step (you'll use the native Terminal)

---

## Step 2: Install Visual Studio Code

1. Download VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/) or from the **Microsoft Store**
2. Install and open VS Code

---

## Step 3: Install Required VS Code Extensions

Click on the **Extensions** icon in the left sidebar (or press `Ctrl+Shift+X`) and search for the following extensions:

### 1. **WSL** (Windows Subsystem for Linux)
- **Why:** Allows VS Code to connect directly to your WSL environment, enabling seamless development within the Linux subsystem
- **For:** Windows users only

### 2. **vscode-pdf**
- **Why:** Enables you to view PDF documentation and reference materials directly within VS Code without switching applications

### 3. **Rainbow CSV**
- **Why:** Provides color-coded columns when viewing CSV files, making data easier to read and analyze

---

## Step 4: Connect VS Code to WSL

**For Windows Users:**

1. Press `Ctrl+Shift+P` to open the Command Palette
2. Type and select: **"WSL: Connect to WSL"**
3. A new VS Code window will open connected to WSL

> **Note:** You'll need to do this every time you want to develop in the WSL environment

**For macOS Users:**
- Simply open VS Code and use the integrated terminal (`Ctrl+``)

---

## Step 5: Create Project Directory

Open the terminal in VS Code (`` Ctrl+` ``) and run:

```bash
mkdir intel-training
cd intel-training
```

---

## Step 6: Install Git

### For WSL/Linux Users:

```bash
sudo apt-get update
sudo apt-get install git
```

### For macOS Users:

1. Install Homebrew (if not already installed):
   - Visit [https://brew.sh](https://brew.sh) and copy the installation command
   - Paste and run it in your terminal

2. Install Git:
   ```bash
   brew install git
   ```

**Why Git is Required:**
Git is a version control system that allows you to track changes in your code, collaborate with others, and access open-source projects. It's essential for modern software development.

**Verify Git Installation:**
```bash
git --version
```

---

## Step 7: Configure Git

Set up your identity for Git commits:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## Step 8: Install UV Package Manager

**Why UV is Required:**
UV is a modern, blazingly fast Python package and project manager. It's significantly faster than pip and conda, provides better dependency resolution, and simplifies virtual environment management. It's written in Rust, making it highly performant for installing packages and managing Python projects.

**Why Choose UV Over Alternatives:**
- **Speed:** 10-100x faster than pip
- **Reliability:** Better dependency resolution than pip
- **Simplicity:** Combines the functionality of pip, pip-tools, pipx, poetry, and pyenv
- **Modern:** Built with modern Python best practices in mind

1. Visit the UV installation page: Google "install uv" or go to [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

2. Copy and run the installation command in your terminal:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. Restart your terminal or run:
   ```bash
   source ~/.bashrc  # or source ~/.zshrc for macOS
   ```

4. **Verify UV Installation:**
   ```bash
   uv --version
   ```

---

## Step 9: Create a GitHub Account

**Why GitHub is Required:**
GitHub is the world's largest platform for hosting and collaborating on code. It allows you to access open-source projects, contribute to repositories, showcase your work, and collaborate with developers worldwide. You'll use it to clone the workshop curriculum repository.

1. Visit [https://github.com](https://github.com)
2. Click "Sign up" and create an account
3. Verify your email address

---

## Step 10: Clone the Curriculum Repository

1. Visit the curriculum repository: [https://github.com/navchetna/curriculum](https://github.com/navchetna/curriculum)

2. Click the green **"Code"** button

3. Copy the URL (should be: `https://github.com/navchetna/curriculum.git`)

4. In VS Code terminal, run:
   ```bash
   git clone https://github.com/navchetna/curriculum.git
   cd curriculum/
   ```

5. Verify your location:
   ```bash
   pwd
   ```
   Expected output: `/home/<your_username>/intel-training/curriculum` (or as per your dev environment)

---

## Step 11: Working with Groq API (Text Generation)

### Navigate to the Groq Example

```bash
cd text-generation/api/groq
```

### Create and Activate Virtual Environment

```bash
uv venv
source .venv/bin/activate
```

### Install Dependencies

```bash
uv pip install -r requirements.txt
```

### Set Up Groq API Key

1. **Obtain API Key:**
   - Read the README.md file in the current directory for detailed instructions
   - Visit [https://console.groq.com](https://console.groq.com)
   - Create an account and generate an API key

2. **Configure API Key:**
   
   **Option 1 - Create .env file (Recommended):**
   ```bash
   # Create a .env file in the current directory
   echo "GROQ_API_KEY=your_actual_api_key_here" > .env
   ```
   
   **Option 2 - Export in terminal:**
   ```bash
   export GROQ_API_KEY=your_actual_api_key_here
   ```

### Understanding the Script

The `inference.py` script accepts command-line flags:
- `--prompt` (required): The text prompt for the AI model
- Additional optional flags are available (check the script for details)

### Run Your First Inference

```bash
python inference.py --prompt="Describe Generative AI with examples"
```

---

## Troubleshooting

### WSL Issues
- If WSL doesn't start after installation, run `wsl --update` in CMD
- Check WSL status: `wsl --status`

### Git Clone Fails
- Ensure you have internet connection
- Try using SSH instead of HTTPS (requires SSH key setup)

### UV Installation Issues
- Make sure curl is installed: `sudo apt-get install curl`
- Check if UV is in PATH: `echo $PATH`

### API Key Not Working
- Ensure no extra spaces in the .env file
- Check that the .env file is in the same directory as inference.py
- Verify API key is valid on Groq console

---

## Exploring Other API Providers

Now that you've successfully worked with the Groq API, you can explore other popular AI providers that follow similar steps:

### Available Providers in the Curriculum

Navigate back to the API directory to see all available providers:
```bash
cd ..  # Go back to text-generation/api/
ls
```

### Try These Providers:

1. **Google Gemini**
   ```bash
   cd gemini
   ```
   - Similar setup process (create venv, install requirements, configure API key)
   - Obtain API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

2. **Hugging Face**
   ```bash
   cd huggingface
   ```
   - Similar setup process
   - Obtain API token from [Hugging Face Settings](https://huggingface.co/settings/tokens)

**Exercise:** Try running the same prompt with different providers and compare the responses!

---

## Next Steps

You've completed Day 1 setup. You now have:
- A fully functional development environment
- Git configured for version control
- UV package manager installed
- Successfully run an AI text generation example
- Knowledge of how to work with multiple API providers

**Challenge:** Experiment with Gemini and Hugging Face APIs using the same workflow you learned with Groq!

**Day 2 content will be provided separately.**

---

## Additional Resources

- [VS Code Documentation](https://code.visualstudio.com/docs)
- [Git Documentation](https://git-scm.com/doc)
- [UV Documentation](https://docs.astral.sh/uv/)
- [Groq Documentation](https://console.groq.com/docs)

---

*Last Updated: October 2025*