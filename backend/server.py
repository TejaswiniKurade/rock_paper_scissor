from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_socketio import emit, join_room

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend/static') 
app.config['SECRET_KEY'] = 'my_key' 
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')










# Placeholder game logic will go here

# if __name__ == '__main__':
#     socketio.run(app, debug=True)
# game_rooms = {}  # Our main dictionary to store rooms

# @socketio.on('join-room')
# def handle_join_room(data):
#     room_id = data['roomId']
#     username = data.get('username')  # Assuming you get a username too

#     # Create the room if it doesn't exist
#     if room_id not in game_rooms:
#         game_rooms[room_id] = {
#             'players': [], 
#             'moves': {}
#         }

#     # Add the player to the room  
#     game_rooms[room_id]['players'].append({'id': socketio.sid, 'username': username})

#     join_room(room_id)  # Associate the player's SocketIO session with the room

#     # Check if room is full (limit of 2 players)
#     if len(game_rooms[room_id]['players']) == 2:
#         emit('room_full', room=room_id)  
#     else:
#         emit('player-joined', {'username': username}, room=room_id)  
