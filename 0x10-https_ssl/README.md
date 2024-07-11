* HTTPS SSL

** What is HTTPS?
HTTPS (HyperText Transfer Protocol Secure) is the secure version of HTTP, the protocol over which data is sent between your browser and the website you're connected to. The 'S' at the end of HTTPS stands for 'Secure'. It means all communications between your browser and the website are encrypted.

** What are the 2 Main Elements that SSL is Providing?
Encryption: Encrypts the data transferred between the user and the website, ensuring that any third party cannot access the data.
Authentication: Provides verification that the website is who it claims to be, protecting against phishing attacks.

** HAProxy SSL Termination on Ubuntu 16.04
SSL termination refers to the process of decrypting SSL-encrypted traffic, which typically occurs at the server level where the traffic is received. In HAProxy, SSL termination can be configured to handle the encryption and decryption of data.

** SSL Termination
This is the process of decrypting encrypted traffic before it is passed on to a web server.
Bash Function
A Bash function is a block of reusable code that can be called within a Bash script to perform specific tasks.

** Man or Help:
awk: A powerful programming language for working on files.
dig: A network administration command-line tool for querying DNS name servers.

SSL (Secure Sockets Layer) is a standard security technology for establishing an encrypted link between a server and a client—typically a web server (website) and a browser, or a mail server and a mail client (e.g., Outlook).

Key Points about SSL:
Encryption:

SSL encrypts data transferred between the server and the client, ensuring that any data exchanged is private and integral. This prevents eavesdroppers from intercepting and reading the data.
Authentication:

SSL provides authentication, ensuring that the server you're communicating with is actually the server you intend to connect to. This prevents man-in-the-middle attacks.
Data Integrity:

SSL ensures that the data transferred between the server and the client is not tampered with or altered during transit.
How SSL Works:
Handshake Process:

When a browser connects to an SSL-secured website, an SSL handshake occurs. This process involves the following steps:
The browser requests the server to identify itself.
The server sends a copy of its SSL certificate to the browser.
The browser checks whether it trusts the SSL certificate. If so, it sends a message to the server.
The server responds with a digitally signed acknowledgment to start an SSL-encrypted session.
Encrypted data is shared between the browser and the server.
SSL Certificate:

An SSL certificate is a digital certificate that authenticates the identity of a website and enables an encrypted connection. It contains the website's public key and the identity of the certificate owner, verified by a trusted Certificate Authority (CA).
Public and Private Keys:

SSL relies on a pair of keys: a public key, which is known to everyone, and a private key, which is known only to the recipient of the message. Data encrypted with the public key can only be decrypted with the private key and vice versa.
