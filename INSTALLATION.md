# Installation Steps

1. **Clone the GitHub Repository:**
   - Clone the GitHub repository to your preferred location on your system. Ensure that Git is preinstalled.
     ```bash
     git clone https://github.com/csc510fall23g45/cheapBuy.git
     cd cheapBuy
     ```
2. **Install Python and Pip:**
   - This project uses Python 3. Make sure Python and Pip are preinstalled on your system. If not, download and install them:
     - [Python](https://www.python.org/downloads/)
     - [Pip](https://pip.pypa.io/en/stable/installation/)

3. **Install Project Dependencies:**
   - Install the project dependencies listed in the `requirements.txt` file using the following command:
     ```bash
     pip install -r requirements.txt
     ```

4. **Generate ScrapeOps API Key:**
   - Visit [ScrapeOps](https://scrapeops.io/) website, sign in to your account, and navigate to the API Keys section. Create a new API key in the       ScrapeOps dashboard.

# Running

**Set Environment Variable for Windows PowerShell:**
```bash
$Env:SCRAPEOPS_API_KEY = "your_api_key_here"
```

**Set Environment Variable for macOS and Linux:**
```bash
export SCRAPEOPS_API_KEY="your_api_key_here"
```

**Set Environment Variable for Windows Command Prompt:**
```bash
set SCRAPEOPS_API_KEY=your_api_key_here
```
   Replace `"your_api_key_here"` with the actual API key you obtained from ScrapeOps. This key will be used for making requests to the ScrapeOps API within the project.

**Run Flask Application:**
- Execute the following command to run the Flask application:
```bash
python app.py
```
- Navigate to the provided link (usually `http://127.0.0.1:5000/`) in your web browser to use cheapBuy.


