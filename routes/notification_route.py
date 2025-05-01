from flask import Blueprint, request, jsonify
from ..collection.notification_collection import notification_collection

notification_route = Blueprint('notification_route', __name__)

@notification_route.route('/notifications', methods=['POST'])
def create_notification():
    """Create a new notification rule"""
    data = request.json
    notification_collection.insert_one(data)
    return jsonify({'success': True, 'message': 'Notification rule created'}), 201

@notification_route.route('/notifications', methods=['GET'])
def get_notifications():
    """Get all notification rules"""
    notifications = list(notification_collection.find({}, {'_id': 0}))
    return jsonify({'success': True, 'data': notifications}), 200

@notification_route.route('/notifications/<event_type>', methods=['PUT'])
def update_notification(event_type):
    """Update a notification rule"""
    data = request.json
    notification_collection.update_one({'event_type': event_type}, {'$set': data})
    return jsonify({'success': True, 'message': 'Notification rule updated'}), 200

@notification_route.route('/notifications/<event_type>', methods=['DELETE'])
def delete_notification(event_type):
    """Delete a notification rule"""
    notification_collection.delete_one({'event_type': event_type})
    return jsonify({'success': True, 'message': 'Notification rule deleted'}), 200