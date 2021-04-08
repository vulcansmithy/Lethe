# Lethe

[logo]: https://i.ibb.co/pxt0SCx/requirements-txt-lethe-Visual-Studio-Code-08-04-2021-18-07-23-2.png "Logo Lethe"
![logo]
## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Modules](#Modules)

## General info
Lethe is a lightweight pentest framework. It uncludes modules for Information Gathering, Vulnerability analysis, Explotation and more.

## Setup

Lethe runs on any platform that has python3 and setting it up is very easy.

```
$ git clone https://github.com/hades921/Lethe.git
$ cd Lethe
$ pip3 install -r requirements.txt
$ python lethe.py
```
	
## Modules

### 1.Information Gathering: 
  *  WhoIS scan 
  *  Port scanner 
  *  Subdomain Scanner 
  *  Spider/Crawler
### 2.Vulnerability Analysis: 
  * SQLI scan 
  * SSL scan 

### 3.Exploiting: 
  * SQL Injection
  * DOS
      * Slowloris
      * SYN flood 

### 4.Password: 
  * Hashes 
	* Hash Identifier 
	* Hash cracker (supported hashes: md5, sha1, sha256, sha3 256)
		* Online Hash database lookup 
		* Hash dictionary attack 
  * Brute Force 
	* SSH cracker 
	* FTP cracker 

### 5.GeoIP 
	

