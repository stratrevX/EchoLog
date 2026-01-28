''' Imports '''

import os, datetime
from colorama import Fore, Style
from platform import system as userSystem
from pwinput import pwinput as maskedInput

''' Objects '''
user = os.getlogin()

''' Functions '''

def missingLog() -> str:
    return f"{Fore.LIGHTRED_EX}⨉ MISSING LOG ⨉{Style.RESET_ALL}"

def infoLog(message: str=None, detail: str=None) -> str:
    """ 
    —— [xx:xx:xx] ▸ Information ◂ {message: str} 
                    ⌞… Detail: {detail: str}
    """
    return f"{Fore.LIGHTRED_EX}——{Style.RESET_ALL} [{datetime.datetime.now().strftime('%H:%M:%S')}] {Fore.LIGHTRED_EX}▸{Style.RESET_ALL} Information {Fore.LIGHTRED_EX}◂{Style.RESET_ALL} {message if message else f'{missingLog()}'}\n{Fore.LIGHTRED_EX}  ⌞… {Style.RESET_ALL} Detail: {detail if detail else f'{missingLog()}'}"

def warnLog(message: str=None, detail: str=None) -> str:
    """ 
    —— [xx:xx:xx] ▸ Warn ◂ {message: str}
                    ⌞… Detail: {detail: str}
    """
    return f"{Fore.LIGHTRED_EX}——{Style.RESET_ALL} [{datetime.datetime.now().strftime('%H:%M:%S')}] {Fore.LIGHTRED_EX}▸{Style.RESET_ALL} Warn {Fore.LIGHTRED_EX}◂{Style.RESET_ALL} {message if message else f'{missingLog()}'}\n{Fore.LIGHTRED_EX}  ⌞… {Style.RESET_ALL} Detail: {detail if detail else f'{missingLog()}'}"

def errorLog(message: str=None, detail: str=None) -> str:
    """ 
    —— [xx:xx:xx] ▸ Error ◂ {message: str}
                    ⌞… Detail: {detail: str}
    """
    return f"{Fore.LIGHTRED_EX}——{Style.RESET_ALL} [{datetime.datetime.now().strftime('%H:%M:%S')}] {Fore.LIGHTRED_EX}▸{Style.RESET_ALL} Error {Fore.LIGHTRED_EX}◂{Style.RESET_ALL} {message if message else f'{missingLog()}'}\n{Fore.LIGHTRED_EX}  ⌞… {Style.RESET_ALL} Detail: {detail if detail else f'{missingLog()}'}"

def successLog(message: str=None, detail: str=None) -> str:
    """ 
    —— [xx:xx:xx] ▸ Success ◂ {message: str}
                    ⌞… Detail: {detail: str}
    """
    return f"{Fore.LIGHTRED_EX}——{Style.RESET_ALL} [{datetime.datetime.now().strftime('%H:%M:%S')}] {Fore.LIGHTRED_EX}▸{Style.RESET_ALL} Success {Fore.LIGHTRED_EX}◂{Style.RESET_ALL} {message if message else f'{missingLog()}'}\n{Fore.LIGHTRED_EX}  ⌞… {Style.RESET_ALL} Detail: {detail if detail else f'{missingLog()}'}"

def requestLog(message: str=None) -> str:
    """
    —— [xx:xx:xx] ▸ Request ◂ {message: str} (Y/n)
    """
    return input(f"{Fore.LIGHTRED_EX}——{Style.RESET_ALL} [{datetime.datetime.now().strftime('%H:%M:%S')}] {Fore.LIGHTRED_EX}▸{Style.RESET_ALL} Request {Fore.LIGHTRED_EX}◂{Style.RESET_ALL} {message if message else f'{missingLog()}'}" + f"? (Y/n)\n{user}{Fore.LIGHTMAGENTA_EX}${Style.RESET_ALL} ")

def inputLog(message: str=None) -> str:
    """
    —— [xx:xx:xx] ▸ Input ◂ {message: str}
    """    
    return input(f"{Fore.LIGHTRED_EX}——{Style.RESET_ALL} [{datetime.datetime.now().strftime('%H:%M:%S')}] {Fore.LIGHTRED_EX}▸{Style.RESET_ALL} Input {Fore.LIGHTRED_EX}◂{Style.RESET_ALL} {message if message else f'{missingLog()}'}\n{user}{Fore.LIGHTMAGENTA_EX}${Style.RESET_ALL} ")

def holdLog() -> str:
    """
    —— [xx:xx:xx] ▸ Hold ◂ Press Enter to proceed...
    """
    return input(f"{Fore.LIGHTRED_EX}——{Style.RESET_ALL} [{datetime.datetime.now().strftime('%H:%M:%S')}] {Fore.LIGHTRED_EX}▸{Style.RESET_ALL} Hold {Fore.LIGHTRED_EX}◂{Style.RESET_ALL} Press Enter to proceed...")

def maskedLog(message: str=None, mask: str='$') -> str:
    """
    —— [xx:xx:xx] ▸ Masked Input ◂ {message: str}
    """
    return maskedInput(f"{Fore.LIGHTRED_EX}——{Style.RESET_ALL} [{datetime.datetime.now().strftime('%H:%M:%S')}] {Fore.LIGHTRED_EX}▸{Style.RESET_ALL} Masked Input {Fore.LIGHTRED_EX}◂{Style.RESET_ALL} {message if message else f'{missingLog()}'}\n{user}{Fore.LIGHTMAGENTA_EX}${Style.RESET_ALL} ", mask=mask)

def testLogs():
    os.system('cls' if userSystem().lower() == 'windows' else 'clear')
    for name, logFunction in logs.items():
        if name in ['info','warn','error','success']:
            print(logFunction(message=f"This is a test {name} log.", detail="This is additional detail for the log."))
        elif name in ['request','input']:
            logFunction(message=f"This is a test {name} log")
        elif name == 'hold':
            logFunction()
        elif name == 'masked':
            logFunction(message=f"This is a test {name} log")

''' POST FUNCTION OBJECTS '''
logs = {
    "info"   : infoLog,
    "warn"   : warnLog,
    "error"  : errorLog,
    "success": successLog,  
    "request": requestLog,
    "input"  : inputLog,
    "hold"   : holdLog,
    "masked" : maskedLog
}
