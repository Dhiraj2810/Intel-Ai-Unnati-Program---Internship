# Workshop Day 2 - RAG (Retrieval-Augmented Generation) & Vibe Coding with Vercel

This guide covers Day 2 of the workshop, where you'll learn about RAG systems using Hugging Face models and create a modern web application using Vercel's AI-powered development.

---

## Part 1: RAG with Hugging Face

### Overview
Today you'll work with Retrieval-Augmented Generation (RAG), a technique that combines document retrieval with AI text generation to create intelligent chatbots that can answer questions based on specific documents.

---

### Step 1: Install UV (If Not Already Installed)

**Reminder:** This was covered in Day 1. If you've already installed UV, skip this step.

Verify UV is installed:
```bash
uv --version
```

If not installed, refer to Day 1 instructions.

---

### Step 2: Navigate to Curriculum Directory

```bash
cd ~/intel-training/curriculum/
```

---

### Step 3: Pull Latest Changes

Always pull the latest updates from the repository before starting:

```bash
git pull
```

This ensures you have the most recent code and fixes.

---

### Step 4: Deactivate Existing Virtual Environment

If you have an active virtual environment from Day 1 (you'll see the environment name in parentheses in your terminal prompt), deactivate it:

```bash
deactivate
```

**Why:** Each project should have its own isolated environment to avoid package conflicts.

---

### Step 5: Navigate to Today's Working Directory

```bash
cd text-generation/rag/rag00-simple-flow
```

Today's working directory: `~/intel-training/curriculum/text-generation/rag/`

We'll start with the first chapter: `rag00-simple-flow`

---

### Step 6: Install PDF Extension (If Not Already Installed)

**Reminder:** This was covered in Day 1.

In VS Code, install the **vscode-pdf** extension if you haven't already. This allows you to view PDF files directly in VS Code.

---

### Step 7: Set Up Virtual Environment

Follow the instructions in the `rag00-simple-flow` README to:

1. Create a new virtual environment
2. Activate it
3. Install requirements

**Important:** Create a new virtual environment for each RAG chapter to keep dependencies isolated.

---

### Step 8: Obtain Hugging Face API Token

#### Understanding Gated vs Non-Gated Models

**Gated Models:**
- Require explicit access approval from the model creator
- Often used for newer, more powerful models
- Require you to accept terms of use or request access
- Example: Meta's Llama models (like Llama 3.2 1B Instruct)

**Non-Gated Models:**
- Freely accessible to anyone with a Hugging Face account
- Can be used immediately without approval
- Example: Many BERT, GPT-2, and smaller open-source models

#### Steps to Get API Token:

1. **Create a Hugging Face Account** (if not already done):
   - Visit [https://huggingface.co/join](https://huggingface.co/join)

2. **Request Access to Llama 3.2 1B Instruct**:
   - Visit the model page: [https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)
   - Click "Request Access" and accept META's terms
   - **Note:** Approval may take from a few minutes to several hours

3. **Create API Token**:
   - Go to [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
   - Click "New token"
   - Give it a name (e.g., "workshop-token")
   - Select "Write" permissions
   - Copy the token (it starts with `hf_`)

---

### Step 9: Configure Environment Variables

Export your Hugging Face token in the WSL terminal:

```bash
export HF_TOKEN=hf_your_actual_token_here
```

**Important:** Replace `hf_your_actual_token_here` with your actual token from Hugging Face.

**Note:** This export is temporary and will be lost when you close the terminal. For permanent setup, add it to your `~/.bashrc` file.

#### Improve Download Speed

```bash
export HF_HUB_DISABLE_XET=1
```

This disables XET protocol and uses standard downloads, which can be faster in some network conditions.

---

### Step 10: Run the Embedding Script

```bash
python read-file-adapt-create-embeddings-and-write.py
```

#### What to Expect:

- The script will start downloading the **embedding model**
- You'll see download progress in the terminal
- The model will be cached at: `~/.cache/huggingface/hub`
- This may take several minutes depending on your internet speed

#### What This Script Does:
- Reads a document (PDF or text file)
- Splits it into chunks
- Creates embeddings (numerical representations) of the text
- Stores these embeddings for later retrieval

---

### Step 11: Run the Chatbot

```bash
python ask_chatbot.py
```

#### What to Expect:

- The script will download the **Llama 3.2 1B Instruct text generation model**
- Models are cached at: `~/.cache/huggingface/hub`
- Once loaded, you can ask questions about the document

#### Try Sample Questions:
- Ask questions related to the content of the document you processed
- The chatbot uses RAG to retrieve relevant information and generate answers

---

### Understanding the RAG Pipeline

1. **Document Processing**: Your document was split into chunks and embedded
2. **Retrieval**: When you ask a question, the system finds relevant chunks
3. **Generation**: The LLM uses those chunks as context to generate an answer

This is the foundation of document-based AI assistants!

---

## Part 2: Vibe Coding with Vercel

### Overview

"Vibe coding" is a modern approach where you describe what you want to build using natural language, and AI generates the code for you. We'll use Vercel's v0.dev platform to create a professional web application.

---

### Step 1: Create a Vercel Account

1. Visit [https://v0.dev](https://v0.dev)
2. Sign up for a free account (use your GitHub account for easy integration)
3. **Free Tier:** You get **3 free AI generation credits per day**

---

### Step 2: Generate Your Application

#### Initial Prompt

Copy and paste this prompt into v0.dev:

```
Build a multi-page ONGC-themed web application with a professional, modern design. The application should reflect ONGC's identity as a leading Indian energy company involved in oil and natural gas exploration, production, and energy innovation.

🔹 Design & Branding
• Use ONGC's brand color palette, primarily the deep maroon/red background from the ONGC logo (#800000 or similar).
• Maintain a clean, corporate, and trustworthy visual style consistent with an energy-sector enterprise.
• Include the ONGC logo in the navbar and favicon area.
• Typography should be simple and professional (e.g., Inter, Roboto, or Open Sans).

🔹 Application Structure
The app should have multiple pages, all connected through smooth navigation:

1. Landing Page
   ○ Brief introduction to ONGC: its mission, vision, and global energy initiatives.
   ○ Include sections such as About ONGC, Sustainability Efforts, and Latest Projects.
   ○ Add a prominent "Explore Dashboard" button leading to the dashboards page.

2. Dashboard Page (Seismology & Energy Data)
   ○ A collapsible sidebar for navigation between dashboard sections (e.g., Seismic Activity, Production Data, Drilling Insights).
   ○ Display charts and graphs visualizing seismology-related data (e.g., earthquake monitoring, field activity, and exploration sites).
   ○ Include dropdown filters (region, date range, seismic magnitude, production zone).
   ○ Use mock data or sample datasets for visualization.
   ○ Present data using interactive visual components (line charts, bar charts, and pie charts).

3. Projects or Operations Page
   ○ Showcase major ONGC operations, offshore rigs, renewable energy initiatives, and research projects.
   ○ Include a card/grid layout with images, short descriptions, and links.

4. About or Contact Page
   ○ Provide information about ONGC's legacy, sustainability commitments, and leadership.
   ○ Include a contact form and social media links.

🔹 Layout & Components
• Navbar: Fixed at the top, containing ONGC logo, navigation links, and possibly a dark/light theme toggle.
• Sidebar: Collapsible, with icons and labels for different dashboard views.
• Main Content Area: Dynamic — updates based on the active route.
• Footer: Containing ONGC's tagline and copyright notice.

🔹 Technical Requirements
• Build using React + Tailwind CSS (or equivalent modern stack).
• Use Recharts or Chart.js for data visualization.
• Ensure full responsiveness and accessibility.
• Include smooth transitions when collapsing or expanding the sidebar.
```

#### Wait for Generation

- v0.dev will generate your application
- You'll see a live preview of the application
- You can iterate and refine by providing additional prompts

---

### Step 3: Download Your Application

Once you're satisfied with the generated application:

1. Click the **"Download"** or **"Export"** button
2. Download as a **ZIP file**
3. Save it to your Downloads folder

---

### Step 4: (Optional) Publish to GitHub

If you want to version control your project:

1. In v0.dev, click **"Publish to GitHub"**
2. Authenticate with your GitHub account
3. Create a new repository or select an existing one
4. The code will be pushed to GitHub automatically

You can then clone this repository to your local machine:
```bash
git clone https://github.com/your-username/your-repo-name.git
```

---

### Step 5: Install Node.js

#### Why Node.js is Required

Node.js is a JavaScript runtime that allows you to run JavaScript code outside the browser. Since the Vercel-generated application is built with React (a JavaScript framework) and uses TypeScript, you need Node.js to:
- Install project dependencies
- Run the development server
- Build the application for production

#### Installation Using NVM (Recommended)

**Why Use NVM?**
NVM (Node Version Manager) allows you to:
- Install and manage multiple Node.js versions on the same machine
- Easily switch between different Node.js versions for different projects
- Avoid permission issues when installing global packages
- Stay up-to-date with the latest Node.js releases without conflicts

**Installation Instructions:**

1. Visit the official Node.js website: [https://nodejs.org/en/download](https://nodejs.org/en/download)
2. Select your operating system (Linux/WSL for Windows users, macOS for Mac users)
3. Follow the instructions to install Node.js using **NVM** (Node Version Manager)
4. After installation, verify:
   ```bash
   node --version
   npm --version
   ```

**Note:** Since you're working in WSL Ubuntu, make sure to install Node.js inside WSL, not on Windows.

---

### Step 6: Extract and Set Up Your Project

1. **Extract the ZIP file** you downloaded from Vercel
   - Right-click the ZIP file → Extract All
   - You'll get a folder with your project name

2. **Open VS Code in WSL** (if not already open)
   - Press `Ctrl+Shift+P`
   - Type "WSL: Connect to WSL"

3. **Drag and Drop the Extracted Folder**
   - In Windows File Explorer, locate your extracted project folder
   - **Drag and drop** the folder into the VS Code window (in the Explorer sidebar)
   - VS Code will copy the folder into your WSL file system

4. **Navigate to Your Project**
   ```bash
   cd <your_project_folder_name>
   ```

---

### Step 7: Install Dependencies

First, try a standard installation:

```bash
npm install
```

**If you encounter errors**, use the force flag:

```bash
npm install --force
```

**Why `--force`?**
- Some packages may have peer dependency conflicts
- `--force` bypasses these warnings and installs anyway
- Only use this if the regular `npm install` fails

**What's Happening:**
- npm is downloading all the JavaScript libraries and dependencies your project needs
- These are defined in `package.json`
- They'll be installed in a `node_modules` folder

---

### Step 8: Run the Development Server

```bash
npm run dev
```

**What to Expect:**
- The development server will start
- You'll see output like:
  ```
  > your-app@0.1.0 dev
  > next dev
  
  - ready started server on 0.0.0.0:3000, url: http://localhost:3000
  ```

---

### Step 9: View Your Application

1. **Open your browser**
2. **Navigate to:** [http://localhost:3000](http://localhost:3000)
3. **Explore your application!**

---

### Step 10: Making Changes

- Any changes you make to the code will automatically reload in the browser
- This is called "hot reloading"
- Try editing files in the `src` or `app` directory to see live updates

---

### Step 11: Stopping the Server

When you're done:

1. Go back to the terminal where the dev server is running
2. Press **`Ctrl+C`**
3. Confirm if prompted (usually by pressing `Y` or just `Ctrl+C` again)

---

## Summary

### Day 2 Achievements:

**Part 1 - RAG System:**
- Understood gated vs non-gated models
- Set up Hugging Face API access
- Downloaded and cached AI models locally
- Built a document-based chatbot using RAG
- Learned about embeddings and retrieval systems

**Part 2 - Vibe Coding:**
- Created a Vercel account
- Generated a full-stack web application using AI
- Set up Node.js development environment
- Ran a modern React/TypeScript application locally
- Understood the basics of npm and JavaScript tooling

---

## Troubleshooting

### RAG Issues

**Models not downloading:**
- Check your Hugging Face token is valid
- Ensure you have internet connection
- Verify you have access to gated models

**Out of disk space:**
- Models can be large (1-5GB each)
- Check available space: `df -h`
- Clear cache if needed: `rm -rf ~/.cache/huggingface/hub`

### Vercel/Node.js Issues

**npm install fails:**
- Try `npm install --force`
- Clear npm cache: `npm cache clean --force`
- Delete `node_modules` and `package-lock.json`, then try again

**Port 3000 already in use:**
- Kill the existing process: `lsof -ti:3000 | xargs kill -9`
- Or use a different port: `npm run dev -- -p 3001`

**Can't access localhost:3000:**
- Ensure the dev server is running
- Check if your firewall is blocking the port
- Try `http://127.0.0.1:3000` instead

---

## Next Steps

**Explore More RAG Chapters:**
- Navigate to other RAG examples in `text-generation/rag/`
- Each chapter builds on the previous one
- Remember to create a new virtual environment for each chapter

**Enhance Your Vercel App:**
- Customize the design and content
- Add real data instead of mock data
- Deploy to production using Vercel hosting
- Connect to APIs or databases

**Advanced Learning:**
- Study the generated code to understand React and TypeScript
- Experiment with different prompts in v0.dev
- Learn about component-based architecture
- Explore Tailwind CSS for styling

---

## Additional Resources

- [Hugging Face Documentation](https://huggingface.co/docs)
- [RAG Explained](https://huggingface.co/learn/cookbook/rag)
- [Vercel v0.dev](https://v0.dev)
- [React Documentation](https://react.dev)
- [Node.js Documentation](https://nodejs.org/docs)
- [npm Documentation](https://docs.npmjs.com)

---

*Last Updated: October 2025*