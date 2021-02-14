
# b64 Obfuscator
<a href="https://github.com/can-er/b64obfuscator/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/can-er/b64obfuscator?color=yellow&label=License&logo=Github"></a> <svg height="20" width="129.8" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><linearGradient id="smooth" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><clipPath id="round"><rect fill="#fff" height="20" rx="3" width="129.8"/></clipPath><g clip-path="url(#round)"><rect fill="#555" height="20" width="100.8"/><rect fill="#007ec6" height="20" width="29.0" x="100.8"/><rect fill="url(#smooth)" height="20" width="129.8"/></g><g fill="#fff" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="110" text-anchor="middle"><image height="14" width="14" x="5" xlink:href="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj4KICA8ZGVmcz4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0icHlZZWxsb3ciIGdyYWRpZW50VHJhbnNmb3JtPSJyb3RhdGUoNDUpIj4KICAgICAgPHN0b3Agc3RvcC1jb2xvcj0iI2ZlNSIgb2Zmc2V0PSIwLjYiLz4KICAgICAgPHN0b3Agc3RvcC1jb2xvcj0iI2RhMSIgb2Zmc2V0PSIxIi8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGxpbmVhckdyYWRpZW50IGlkPSJweUJsdWUiIGdyYWRpZW50VHJhbnNmb3JtPSJyb3RhdGUoNDUpIj4KICAgICAgPHN0b3Agc3RvcC1jb2xvcj0iIzY5ZiIgb2Zmc2V0PSIwLjQiLz4KICAgICAgPHN0b3Agc3RvcC1jb2xvcj0iIzQ2OCIgb2Zmc2V0PSIxIi8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KCiAgPHBhdGggZD0iTTI3LDE2YzAtNyw5LTEzLDI0LTEzYzE1LDAsMjMsNiwyMywxM2wwLDIyYzAsNy01LDEyLTExLDEybC0yNCwwYy04LDAtMTQsNi0xNCwxNWwwLDEwbC05LDBjLTgsMC0xMy05LTEzLTI0YzAtMTQsNS0yMywxMy0yM2wzNSwwbDAtM2wtMjQsMGwwLTlsMCwweiBNODgsNTB2MSIgZmlsbD0idXJsKCNweUJsdWUpIi8+CiAgPHBhdGggZD0iTTc0LDg3YzAsNy04LDEzLTIzLDEzYy0xNSwwLTI0LTYtMjQtMTNsMC0yMmMwLTcsNi0xMiwxMi0xMmwyNCwwYzgsMCwxNC03LDE0LTE1bDAtMTBsOSwwYzcsMCwxMyw5LDEzLDIzYzAsMTUtNiwyNC0xMywyNGwtMzUsMGwwLDNsMjMsMGwwLDlsMCwweiBNMTQwLDUwdjEiIGZpbGw9InVybCgjcHlZZWxsb3cpIi8+CgogIDxjaXJjbGUgcj0iNCIgY3g9IjY0IiBjeT0iODgiIGZpbGw9IiNGRkYiLz4KICA8Y2lyY2xlIHI9IjQiIGN4PSIzNyIgY3k9IjE1IiBmaWxsPSIjRkZGIi8+Cjwvc3ZnPgo=" y="3"/><text fill="#010101" fill-opacity=".3" lengthAdjust="spacing" textLength="738.0" transform="scale(0.1)" x="599.0" y="150">Python</text><text lengthAdjust="spacing" textLength="738.0" transform="scale(0.1)" x="599.0" y="140">Python</text><text fill="#010101" fill-opacity=".3" lengthAdjust="spacing" textLength="190.0" transform="scale(0.1)" x="1143.0" y="150">3.7</text><text lengthAdjust="spacing" textLength="190.0" transform="scale(0.1)" x="1143.0" y="140">3.7</text></g></svg>
## This tool allows you to obfuscate your program into a base64 form. It can be usefull for many reasons:

    * Hide credentials who can be in "plain-text"
    * Bypass Windows Defender or other malware recon tools
    * Learn and appear clever to your friends :D

## Usage

```
python3 b64obfuscer.py path/of/source.py path/of/destination.py
```

### Note:
Source & destination must be .py file. Destination is created by the tool itself

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

----------------------------------------------------------------

Disclaimer: Any malicious use of this tool will not hold the author responsible, this content is only for educationnal purpose.
