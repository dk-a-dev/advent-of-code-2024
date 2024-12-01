# Advent of Code Project Setup

Python local setup for advent of code ⭐️🎄

---

## Features

1. **Input Fetching**

   - Automatically fetch inputs for any day or range of days.
   - Save inputs in the `inputs/` folder, named as `day-XX.txt`.

2. **Solution File Template**

   - Automatically create solution files for any day.
   - Files follow a standard template, saved in the `solutions/` folder.

3. **Run Solutions**
   - Run solutions for any day.
   - Automatically fetch missing inputs and create solution files as needed.

---

## Getting Started

1. Clone the repository:

   ```bash
    git clone <your-repo-url>
    cd <your-repo-name>
   ```

2. Setup virtual environment(MAC):

   ```bash
    python3 -m venv venv
    source venv/bin/activate
   ```

   Setup virtual environment(WINDOWS):

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Create file 'requirements.txt' and add the following:

   ```bash
     advent-of-code-data
     rich
   ```

4. Install dependencies:

   ```bash
    pip install -r requirements.txt
   ```

5. Add your adoc session cookie:

   - Go to [adventofcode.com](https://adventofcode.com/).
   - Open the developer console.
   - Go to the Applications tab>Cookie option>copy `session` cookie.
     ```bash
     mkdir -p ~/.config/aocd && echo "<your_session_cookie>" > ~/.config/aocd/token
     ```

6. Run the main script:
- MAC
   ```bash
   python main.py
   ```
- WINDOWS
   ```bash(mac)
   python3 main.py
   ```

7. Example Folder Structure:
   ```bash
   ├── advent-of-code/
   │├── inputs/             
   │   ├── day-01.txt        
   │   ├── day-02.txt
   │   ├── ...
   │├── solutions/
   │   ├── day-01.py
   │   ├── day-02.py
   │   ├── ...
   │├── main.py
   │├── utils.py
   │├── README.md
   │├── requirements.txt
   │├── .gitignore
   ```        
---

## References

- Advent of Code Data Library:
  - [Documentation](https://pypi.org/project/advent-of-code-data/).
- Session Token Setup:
  - See this [issue](https://github.com/wimglenn/advent-of-code-wim/issues/1) for help with configuring your Advent of Code session token.
