// Auto-generated. Do not edit!

// (in-package beginner_tutorials.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class WheelCommands {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.CommandL = null;
      this.CommandR = null;
    }
    else {
      if (initObj.hasOwnProperty('CommandL')) {
        this.CommandL = initObj.CommandL
      }
      else {
        this.CommandL = 0.0;
      }
      if (initObj.hasOwnProperty('CommandR')) {
        this.CommandR = initObj.CommandR
      }
      else {
        this.CommandR = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type WheelCommands
    // Serialize message field [CommandL]
    bufferOffset = _serializer.float32(obj.CommandL, buffer, bufferOffset);
    // Serialize message field [CommandR]
    bufferOffset = _serializer.float32(obj.CommandR, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type WheelCommands
    let len;
    let data = new WheelCommands(null);
    // Deserialize message field [CommandL]
    data.CommandL = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [CommandR]
    data.CommandR = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'beginner_tutorials/WheelCommands';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'da8262406bdbe1e606838ce0ded8f1bb';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 CommandL
    float32 CommandR
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new WheelCommands(null);
    if (msg.CommandL !== undefined) {
      resolved.CommandL = msg.CommandL;
    }
    else {
      resolved.CommandL = 0.0
    }

    if (msg.CommandR !== undefined) {
      resolved.CommandR = msg.CommandR;
    }
    else {
      resolved.CommandR = 0.0
    }

    return resolved;
    }
};

module.exports = WheelCommands;
