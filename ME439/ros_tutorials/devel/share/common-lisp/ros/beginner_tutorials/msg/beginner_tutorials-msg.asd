
(cl:in-package :asdf)

(defsystem "beginner_tutorials-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Num" :depends-on ("_package_Num"))
    (:file "_package_Num" :depends-on ("_package"))
    (:file "WheelCommands" :depends-on ("_package_WheelCommands"))
    (:file "_package_WheelCommands" :depends-on ("_package"))
  ))