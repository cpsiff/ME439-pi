; Auto-generated. Do not edit!


(cl:in-package beginner_tutorials-msg)


;//! \htmlinclude WheelCommands.msg.html

(cl:defclass <WheelCommands> (roslisp-msg-protocol:ros-message)
  ((CommandL
    :reader CommandL
    :initarg :CommandL
    :type cl:float
    :initform 0.0)
   (CommandR
    :reader CommandR
    :initarg :CommandR
    :type cl:float
    :initform 0.0))
)

(cl:defclass WheelCommands (<WheelCommands>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WheelCommands>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WheelCommands)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name beginner_tutorials-msg:<WheelCommands> is deprecated: use beginner_tutorials-msg:WheelCommands instead.")))

(cl:ensure-generic-function 'CommandL-val :lambda-list '(m))
(cl:defmethod CommandL-val ((m <WheelCommands>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:CommandL-val is deprecated.  Use beginner_tutorials-msg:CommandL instead.")
  (CommandL m))

(cl:ensure-generic-function 'CommandR-val :lambda-list '(m))
(cl:defmethod CommandR-val ((m <WheelCommands>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:CommandR-val is deprecated.  Use beginner_tutorials-msg:CommandR instead.")
  (CommandR m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WheelCommands>) ostream)
  "Serializes a message object of type '<WheelCommands>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'CommandL))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'CommandR))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WheelCommands>) istream)
  "Deserializes a message object of type '<WheelCommands>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'CommandL) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'CommandR) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WheelCommands>)))
  "Returns string type for a message object of type '<WheelCommands>"
  "beginner_tutorials/WheelCommands")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WheelCommands)))
  "Returns string type for a message object of type 'WheelCommands"
  "beginner_tutorials/WheelCommands")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WheelCommands>)))
  "Returns md5sum for a message object of type '<WheelCommands>"
  "da8262406bdbe1e606838ce0ded8f1bb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WheelCommands)))
  "Returns md5sum for a message object of type 'WheelCommands"
  "da8262406bdbe1e606838ce0ded8f1bb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WheelCommands>)))
  "Returns full string definition for message of type '<WheelCommands>"
  (cl:format cl:nil "float32 CommandL~%float32 CommandR~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WheelCommands)))
  "Returns full string definition for message of type 'WheelCommands"
  (cl:format cl:nil "float32 CommandL~%float32 CommandR~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WheelCommands>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WheelCommands>))
  "Converts a ROS message object to a list"
  (cl:list 'WheelCommands
    (cl:cons ':CommandL (CommandL msg))
    (cl:cons ':CommandR (CommandR msg))
))
