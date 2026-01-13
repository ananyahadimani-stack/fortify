# Fortify — OS Monitoring Agent (Windows)

## Overview
This module implements the OS-level monitoring agent for the Fortify project.  
It is a Windows Host-Based Intrusion Detection & Response Agent designed to protect a device when the user is away.

The agent runs silently in the background, detects unauthorized usage based on system activity, captures evidence using the webcam, securely logs events offline using encryption, and enforces immediate OS-level security actions.

---

## Responsibilities of the OS Agent

- Automatic execution at system startup  
- Background monitoring without user interaction  
- Detection of unauthorized access using keyboard and mouse activity  
- Webcam-based evidence capture  
- Encrypted offline event logging  
- Immediate system lock on intrusion  
- Offline-first operation  

---

## Features Implemented

### Boot-Time Execution
- Configured using Windows Task Scheduler  
- Starts automatically on system boot  

### Unauthorized Access Detection
- Monitors keyboard and mouse input using OS-level listeners  
- Any activity detected while the system is armed is treated as unauthorized access  

### Evidence Capture
- Captures webcam images during intrusion events  
- Stores evidence locally for later review  

### Encrypted Offline Logging
- Intrusion events are encrypted using Fernet symmetric encryption  
- Logs are stored securely on the local device  

### OS-Level Response
- Locks the system immediately using native Windows APIs  

### Network Context Logging
- Captures basic network information (IP address) during intrusion events  

---

## Technologies Used

- Python  
- Windows Task Scheduler  
- OpenCV  
- pynput  
- cryptography (Fernet)  

---

## File Structure

