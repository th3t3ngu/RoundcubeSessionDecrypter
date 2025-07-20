# RoundcubeSessionDecrypter
Decrypting a password from auth_secret, request_token, DES-EDE3-key and an encrypted password.

## Overview
A Python3-script to decrypt an encrypted session-password, using the Roundcube DES-EDE3-key (commonly found in `config.inc.php`) and a users  `auth_secret, request_token` and `password`, all in base64. I wrote this script to solve a Box on HTB, I don't know if it will also work in different scenarios.

## Usage
Needs `pycryptodome` to operate.  

Open `roundcube_session_decrypter.py` and fill in KEY, PASSWORD, AUTH_TOKEN and REQUEST_TOKEN. 

Save and run via `./roundcube_session_decrypter.py`. 