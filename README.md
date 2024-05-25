# DirBlade
```DirBlade``` is a versatile directory bruteforce tool designed to uncover hidden directories and files on web servers. Whether you're conducting penetration tests, security assessments, or bug bounty hunting, ```DirBlade``` empowers you to thoroughly explore web applications for potential vulnerabilities.

![Example](https://github.com/m1dn1ghtMHR/DirBlade/blob/main/Image.png)

## Features
- **Efficient Bruteforcing:** DirBlade utilizes a brute force approach to systematically scan directories and files on target web servers.
- **Customizable Wordlists:** Users can specify their own wordlists tailored to the target application or use default wordlists included with the tool.
- **Concurrency:** DirBlade leverages concurrency to maximize speed and efficiency during directory enumeration.
- **Comprehensive Reporting:** DirBlade provides detailed reports of discovered directories and files, aiding in vulnerability assessment and analysis.
- **User-Friendly Interface:** With a simple command-line interface, DirBlade is accessible to users of all experience levels.
## Usage
To start using DirBlade, simply provide the target URL using ```-u``` or ```--url``` along with a wordlist using ```-w``` or ```--url``` containing directory and file paths to be bruteforced.
#### NOTE--> If you want to use default wordlist then don't use wordlist option simply press ```ENTER```.

## Example usage:
```
python3 dirblade.py -u http://example.com -w path/to/wordlist
```
## Installation
> Clone the DirBlade repository from GitHub:
```
git clone https://github.com/midnight-zain/DirBlade.git
```

> Navigate to the DirBlade directory:
```
cd DirBlade
```
> Ensure you have Python 3 installed on your system.

> Run DirBlade using Python:
```
python3 dirblade.py -u http://example.com -w path/to/wordlist
```
### Contributing
Contributions to DirBlade are welcome! If you encounter any bugs or have suggestions for improvements, please open an issue on the GitHub repository.

## Disclaimer
DirBlade is intended for legal security testing purposes only. Unauthorized use of this tool against targets without prior mutual consent is illegal.
