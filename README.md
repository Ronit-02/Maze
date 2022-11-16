# Maze - ransomware

A ransomware is a type of malware that prevents legitimate users from accessing
their device or data and asks for a payment in exchange for the stolen functionality.
They have been used for mass extortion in various forms, but the
most successful one seems to be encrypting ransomware: most of the user data are
encrypted and the key can be obtained paying the attacker.
To be widely successful a ransomware must fulfill three properties:

**Property 1**: The hostile binary code must not contain any secret (e.g. deciphering
keys). At least not in an easily retrievable form, indeed white box cryptography
can be applied to ransomware.

**Property 2**: Only the author of the attack should be able to decrypt the
infected device.

**Property 3**: Decrypting one device can not provide any useful information
for other infected devices, in particular the key must not be shared among them.


**Ransomware Impact on industry**

https://medium.com/@tarcisioma/how-can-a-malware-encrypt-a-company-existence-c7ed584f66b3

**How this ransomware encryption scheme works:**

https://medium.com/@tarcisioma/ransomware-encryption-techniques-696531d07bb9
