;; Auto-generated. Do not edit!


(when (boundp 'beginner_tutorials::WheelCommands)
  (if (not (find-package "BEGINNER_TUTORIALS"))
    (make-package "BEGINNER_TUTORIALS"))
  (shadow 'WheelCommands (find-package "BEGINNER_TUTORIALS")))
(unless (find-package "BEGINNER_TUTORIALS::WHEELCOMMANDS")
  (make-package "BEGINNER_TUTORIALS::WHEELCOMMANDS"))

(in-package "ROS")
;;//! \htmlinclude WheelCommands.msg.html


(defclass beginner_tutorials::WheelCommands
  :super ros::object
  :slots (_CommandL _CommandR ))

(defmethod beginner_tutorials::WheelCommands
  (:init
   (&key
    ((:CommandL __CommandL) 0.0)
    ((:CommandR __CommandR) 0.0)
    )
   (send-super :init)
   (setq _CommandL (float __CommandL))
   (setq _CommandR (float __CommandR))
   self)
  (:CommandL
   (&optional __CommandL)
   (if __CommandL (setq _CommandL __CommandL)) _CommandL)
  (:CommandR
   (&optional __CommandR)
   (if __CommandR (setq _CommandR __CommandR)) _CommandR)
  (:serialization-length
   ()
   (+
    ;; float32 _CommandL
    4
    ;; float32 _CommandR
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _CommandL
       (sys::poke _CommandL (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _CommandR
       (sys::poke _CommandR (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _CommandL
     (setq _CommandL (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _CommandR
     (setq _CommandR (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get beginner_tutorials::WheelCommands :md5sum-) "da8262406bdbe1e606838ce0ded8f1bb")
(setf (get beginner_tutorials::WheelCommands :datatype-) "beginner_tutorials/WheelCommands")
(setf (get beginner_tutorials::WheelCommands :definition-)
      "float32 CommandL
float32 CommandR

")



(provide :beginner_tutorials/WheelCommands "da8262406bdbe1e606838ce0ded8f1bb")


