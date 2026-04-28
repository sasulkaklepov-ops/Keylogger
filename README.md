🖥️ Simple Keylogger

A lightweight educational keylogger written in Python using the `pynput` library.  
Captures keystrokes, handles word separation (space/enter), backspace deletion, and exits gracefully with ESC.

-------------------------------------------------------------------------------------

⚠️ DISCLAIMER

> **This tool is for educational and research purposes ONLY.**  
> Use it only on your own systems or with explicit written permission from the owner.  
> Unauthorized use violates computer fraud laws (e.g., CFAA in the US, Article 272 in Russia).  
> **You are solely responsible for any misuse.**

-----------------------------------------------------------------------------------

🚀 Features

- ✅ Real-time keystroke capture  
- ✅ Word grouping (supports space and enter separators)  
- ✅ Backspace handling (deletes last character)  
- ✅ Clean exit with ESC key  
- ✅ Error handling  
- ✅ Console output format: `>>> captured_word`

--------------------------------------------------------------------------------------------------

📦 Installation

### Prerequisites
- Python 3.6+
- pip

### Steps
bash
git clone https://github.com/yourusername/simple-keylogger.git
cd simple-keylogger
pip install -r requirements.txt

requirements.txt:

txt
pynput

------------------------------------------------------------------------------

⌨️ Usage

bash
python keylogger.py

· Type normally – words will be printed after space/enter
· Press BACKSPACE to remove the last character
· Press ESC to exit the program

Example output

Keylogger запущен
ESC - exit

>>> hello
>>> world
>>> this is a test
Выход....

-----------------------------------------------------------------------------------------

🧠 How It Works

Action Behavior
Letter/number key Appends character to current word buffer
Space key Prints accumulated word, clears buffer
Enter key Prints word and adds a blank line
Backspace key Removes last character from buffer
ESC key Exits the listener and program

The script uses pynput.keyboard.Listener to intercept global keyboard events without requiring admin privileges (on most systems).

------------------------------------------------------------------------------------

🛡️ Ethical Use Guidelines

✅ DO:

· Test on your own computers
· Use in isolated lab environments
· Learn how keyloggers work to better defend against them

❌ DON'T:

· Deploy on any device without authorization
· Use for stealing passwords or personal data
· Share with malicious intent

-------------------------------------------------------------------------------------

🐛 Troubleshooting

Issue Solution
ImportError: No module named pynput Run pip install pynput
No output on keypress Run script with normal user privileges (admin not required)
Script doesn't exit Press ESC key (not Ctrl+C)
Special keys not handled Only printable characters are collected; modifiers are ignored by design

------------------------------------------------------------------------------------------

📁 Project Structure

simple-keylogger/
├── keylogger.py         # Main script
├── requirements.txt     # Dependencies
└── README.md            # This file

-------------------------------------------------------------------------------------

🔮 Possible Improvements

· Save logged words to a file (words.txt)
· Timestamp each word
· Send logs via email/SMTP
· Hide console window (compile with pyinstaller --noconsole)
· Add auto-startup registry key (for authorized testing only)

----------------------------------------------------------------------------------

📄 License

MIT License – for educational use only.
The author assumes no liability for misuse.

-----------------------------------------------------------------------------

👨‍💻 Author

Created for learning Windows internals, input hooking, and ethical hacking concepts.

-------------------------------------------------------------------------------------------

⭐ Acknowledgments

· pynput – cross-platform keyboard/mouse control

-------------------------------------------------------

📁 Файлы для загрузки

### `requirements.txt`
txt
pynput

.gitignore

pycache/
*.pyc
*.log
*.txt
words.txt
venv/
.env
