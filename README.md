# P2P Chat Application 

A decentralized peer-to-peer chat application that enables real-time messaging between peers on a local network without requiring a centralized server. Built with Python (FastAPI backend) and vanilla JavaScript frontend.

## Features

- **Decentralized Architecture**: No central server required - all peers communicate directly with each other
- **Automatic Peer Discovery**: Uses UDP broadcasting to discover active peers on the network
- **Real-time Messaging**: TCP-based messaging for reliable message delivery
- **Live Peer Detection**: Automatic peer list updates with live network monitoring
- **Simple Web UI**: Clean, intuitive interface for easy chatting
- **Async Operations**: Non-blocking async I/O for handling multiple concurrent connections

## Architecture

### Backend Stack
- **FastAPI**: Modern Python web framework for building the REST API
- **Async/Await**: Asynchronous programming for handling concurrent tasks
- **UDP**: Peer discovery mechanism via broadcast messages
- **TCP**: Reliable message delivery between peers

### Frontend Stack
- **HTML5**: Semantic markup
- **CSS3**: Responsive styling
- **Vanilla JavaScript**: No dependencies, lightweight client-side logic

## Project Structure

```
P2P Chat/
├── main.py                    # FastAPI application entry point
├── frontend/
│   ├── index.html            # Main UI template
│   └── script.js             # Client-side logic
└── app/
    ├── api/
    │   └── routes.py         # REST API endpoints
    ├── chat/
    │   ├── TCP_Client.py     # TCP client for sending messages
    │   └── TCP_Server.py     # TCP server for receiving messages
    ├── config/
    │   └── config.py         # Configuration constants
    ├── core/
    │   ├── state.py          # Application state management
    │   └── tasks.py          # Background task initialization
    └── discovery/
        ├── UDP_broadcaster.py # UDP broadcast for peer announcement
        └── UDP_Listener.py    # UDP listener for peer discovery
```

## Configuration

Configure your application in `app/config/config.py`:

```python
UDP_PORT = 5000              # Port for peer discovery broadcasts
TCP_PORT = 6000              # Port for TCP messaging
DISCOVERY_MESSAGE = "HEY THERE.."  # Broadcast discovery message
BROADCAST_INTERVAL = 2       # Seconds between discovery broadcasts
```

## Getting Started

### Prerequisites
- Python 3.7+
- FastAPI
- Uvicorn

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/daaman3110/Peer_2_Peer_chatapp.git
   cd Peer_2_Peer_chatapp
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi uvicorn
   ```

3. **Run the application**
   ```bash
   python main.py
   ```
   Or with Uvicorn directly:
   ```bash
   uvicorn main:app --reload
   ```

4. **Open in browser**
   - Navigate to `http://localhost:8000`
   - The application will automatically discover peers on your network

## How It Works

### Peer Discovery (UDP)
1. Each peer broadcasts a discovery message via UDP every 2 seconds
2. Listening peers receive the broadcast and store the sender's IP address
3. The peer list is maintained in application state and exposed via REST API

### Message Exchange (TCP)
1. User selects a peer from the sidebar
2. User types and sends a message
3. Frontend sends the message to the backend via POST request
4. Backend connects to the peer's TCP server and sends the message
5. Receiving peer's TCP server handles the message and stores it
6. Frontend polls `/messages` endpoint and displays new messages

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/peers` | GET | Returns list of discovered peers with timestamps |
| `/messages` | GET | Returns list of received messages |
| `/send` | POST | Sends a message to a specific peer |

**POST `/send` Request Body:**
```json
{
  "ip": "192.168.1.100",
  "msg": "Hello!"
}
```

## Frontend Features

- **Peer Sidebar**: Lists all discovered peers on the network
- **Chat Area**: Displays messages and message input field
- **Auto-refresh**: 
  - Peers list updates every 2 seconds
  - Messages refresh every 1 second
- **Peer Selection**: Click any peer to select for chatting

## Core Components

### `state.py`
Manages application state including discovered peers and message history with thread-safe access using asyncio locks.

### `tasks.py`
Initializes and schedules background tasks:
- UDP peer discovery broadcasting
- UDP peer discovery listening
- TCP server for receiving messages

### `TCP_Client.py` & `TCP_Server.py`
- **Client**: Handles outgoing TCP connections to send messages to peers
- **Server**: Listens for incoming TCP connections and receives messages

### `UDP_Broadcaster.py` & `UDP_Listener.py`
- **Broadcaster**: Sends periodic discovery broadcasts to notify network presence
- **Listener**: Receives discovery broadcasts and registers new peers
