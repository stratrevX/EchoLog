# EchoLog - 0.1.0
A simple logging library I made for myself in Python. 
Made public just to be able to install it onto every project of mine easily.
## 💡Features

### 📋 Standard Logs
These functions return a formatted string. You need to `print()` them.
* `infoLog(message, detail)`
* `warnLog(message, detail)`
* `errorLog(message, detail)`
* `successLog(message, detail)`
	### ⌨️ Interactive Logs
These functions use `input()` and return the user's string.
* `inputLog(message)` - Standard prompt.
* `requestLog(message)` - Prompt with a `(Y/n)` hint.
* `maskedLog(message, mask)` - Hidden input (Suggested for sensitive content, such as passwords, keys, etc.).
* `holdLog()` - Pauses execution until a key is pressed.

## 📑Requirements
- At least Python 3.9 is required.
- Its dependencies will automatically be installed

## 💻Installation
`pip install git+https://github.com/stratrevX/EchoLog.git`

to specify a version, add `@version, example:v0.1.0` at the end.

## 📕Usage

```
from echolog import *
print(infoLog("This is an info log.", detail="Additional details can be provided here."))
```

### or

```
import echolog as elog
print(elog.infoLog("This is an info log.", "Additional details here."))
```
