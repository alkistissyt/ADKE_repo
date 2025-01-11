# ADKE_repo

## Network File Transfer Experiment
### Overview
This repository contains three Python scripts (server_a.py, server_b.py, client.py) designed to simulate a file transfer experiment between two servers (Server A and Server B) and a client. The experiment measures the time required to download files under various configurations, helping analyze network performance and resource sharing.

### Scripts
**1. server_a.py**
Purpose: Simulates Server A, which serves files to the client via a wired or wireless connection.  
***Key Features:***   
Listens on port 8080.  
Serves files from a specified directory.  
Responds to client requests by sending the requested files.  
Usage: ```python server_a.py```

**2. server_b.py**
Purpose: Simulates Server B, which serves files to the client, typically using a wireless connection.  
***Key Features:***  
Similar functionality to Server A, but listens on port 9090.  
Usage: ```python server_b.py```  

**3. client.py**
Purpose: Acts as a client to download files from both servers, balancing the workload based on parameters n_A and n_B.  
***Key Features:***   
Connects to Server A and Server B to request files.  
Measures the total time to download all files.  
Outputs download progress and results.  
Usage:
```python client.py <n_A> <n_B> <IP_A> <IP_B>```  
n_A: Number of files to request from Server A per cycle.  
n_B: Number of files to request from Server B per cycle.  
IP_A: IP address of Server A.  
IP_B: IP address of Server B.  

### Experiment Workflow
***Start Servers:***  
Run server_a.py on a device connected via Ethernet or Wi-Fi.  
Run server_b.py on a mobile device or another computer.  
***Run Client:***  
Execute client.py on a third device, specifying the servers' IPs and file request parameters (n_A and n_B).  
.
### Example Usage
Start Server A: ```python server_a.py```  
Start Server B: ```python server_b.py```  
Run Client to request files:  
```python client.py 5 1 192.168.1.10 192.168.1.11```  

### Results
The total time required to download all files will be displayed by the client. The results can help determine the optimal balance between Server A (n_A) and Server B (n_B) for minimal transfer time.  
