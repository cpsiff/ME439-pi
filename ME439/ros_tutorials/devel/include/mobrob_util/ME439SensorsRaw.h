// Generated by gencpp from file mobrob_util/ME439SensorsRaw.msg
// DO NOT EDIT!


#ifndef MOBROB_UTIL_MESSAGE_ME439SENSORSRAW_H
#define MOBROB_UTIL_MESSAGE_ME439SENSORSRAW_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace mobrob_util
{
template <class ContainerAllocator>
struct ME439SensorsRaw_
{
  typedef ME439SensorsRaw_<ContainerAllocator> Type;

  ME439SensorsRaw_()
    : e0(0)
    , e1(0)
    , a0(0)
    , a1(0)
    , a2(0)
    , a3(0)
    , a4(0)
    , a5(0)
    , u0(0)
    , u1(0)
    , u2(0)
    , t()  {
    }
  ME439SensorsRaw_(const ContainerAllocator& _alloc)
    : e0(0)
    , e1(0)
    , a0(0)
    , a1(0)
    , a2(0)
    , a3(0)
    , a4(0)
    , a5(0)
    , u0(0)
    , u1(0)
    , u2(0)
    , t()  {
  (void)_alloc;
    }



   typedef int64_t _e0_type;
  _e0_type e0;

   typedef int64_t _e1_type;
  _e1_type e1;

   typedef int16_t _a0_type;
  _a0_type a0;

   typedef int16_t _a1_type;
  _a1_type a1;

   typedef int16_t _a2_type;
  _a2_type a2;

   typedef int16_t _a3_type;
  _a3_type a3;

   typedef int16_t _a4_type;
  _a4_type a4;

   typedef int16_t _a5_type;
  _a5_type a5;

   typedef int32_t _u0_type;
  _u0_type u0;

   typedef int32_t _u1_type;
  _u1_type u1;

   typedef int32_t _u2_type;
  _u2_type u2;

   typedef ros::Time _t_type;
  _t_type t;





  typedef boost::shared_ptr< ::mobrob_util::ME439SensorsRaw_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mobrob_util::ME439SensorsRaw_<ContainerAllocator> const> ConstPtr;

}; // struct ME439SensorsRaw_

typedef ::mobrob_util::ME439SensorsRaw_<std::allocator<void> > ME439SensorsRaw;

typedef boost::shared_ptr< ::mobrob_util::ME439SensorsRaw > ME439SensorsRawPtr;
typedef boost::shared_ptr< ::mobrob_util::ME439SensorsRaw const> ME439SensorsRawConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mobrob_util::ME439SensorsRaw_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mobrob_util::ME439SensorsRaw_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::mobrob_util::ME439SensorsRaw_<ContainerAllocator1> & lhs, const ::mobrob_util::ME439SensorsRaw_<ContainerAllocator2> & rhs)
{
  return lhs.e0 == rhs.e0 &&
    lhs.e1 == rhs.e1 &&
    lhs.a0 == rhs.a0 &&
    lhs.a1 == rhs.a1 &&
    lhs.a2 == rhs.a2 &&
    lhs.a3 == rhs.a3 &&
    lhs.a4 == rhs.a4 &&
    lhs.a5 == rhs.a5 &&
    lhs.u0 == rhs.u0 &&
    lhs.u1 == rhs.u1 &&
    lhs.u2 == rhs.u2 &&
    lhs.t == rhs.t;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::mobrob_util::ME439SensorsRaw_<ContainerAllocator1> & lhs, const ::mobrob_util::ME439SensorsRaw_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace mobrob_util

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::mobrob_util::ME439SensorsRaw_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mobrob_util::ME439SensorsRaw_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mobrob_util::ME439SensorsRaw_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mobrob_util::ME439SensorsRaw_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mobrob_util::ME439SensorsRaw_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mobrob_util::ME439SensorsRaw_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mobrob_util::ME439SensorsRaw_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e832476c98d8752e8bb419b8adb5fe2a";
  }

  static const char* value(const ::mobrob_util::ME439SensorsRaw_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe832476c98d8752eULL;
  static const uint64_t static_value2 = 0x8bb419b8adb5fe2aULL;
};

template<class ContainerAllocator>
struct DataType< ::mobrob_util::ME439SensorsRaw_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mobrob_util/ME439SensorsRaw";
  }

  static const char* value(const ::mobrob_util::ME439SensorsRaw_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mobrob_util::ME439SensorsRaw_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 e0\n"
"int64 e1\n"
"int16 a0\n"
"int16 a1\n"
"int16 a2\n"
"int16 a3\n"
"int16 a4\n"
"int16 a5\n"
"int32 u0\n"
"int32 u1\n"
"int32 u2\n"
"time t\n"
;
  }

  static const char* value(const ::mobrob_util::ME439SensorsRaw_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mobrob_util::ME439SensorsRaw_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.e0);
      stream.next(m.e1);
      stream.next(m.a0);
      stream.next(m.a1);
      stream.next(m.a2);
      stream.next(m.a3);
      stream.next(m.a4);
      stream.next(m.a5);
      stream.next(m.u0);
      stream.next(m.u1);
      stream.next(m.u2);
      stream.next(m.t);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ME439SensorsRaw_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mobrob_util::ME439SensorsRaw_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mobrob_util::ME439SensorsRaw_<ContainerAllocator>& v)
  {
    s << indent << "e0: ";
    Printer<int64_t>::stream(s, indent + "  ", v.e0);
    s << indent << "e1: ";
    Printer<int64_t>::stream(s, indent + "  ", v.e1);
    s << indent << "a0: ";
    Printer<int16_t>::stream(s, indent + "  ", v.a0);
    s << indent << "a1: ";
    Printer<int16_t>::stream(s, indent + "  ", v.a1);
    s << indent << "a2: ";
    Printer<int16_t>::stream(s, indent + "  ", v.a2);
    s << indent << "a3: ";
    Printer<int16_t>::stream(s, indent + "  ", v.a3);
    s << indent << "a4: ";
    Printer<int16_t>::stream(s, indent + "  ", v.a4);
    s << indent << "a5: ";
    Printer<int16_t>::stream(s, indent + "  ", v.a5);
    s << indent << "u0: ";
    Printer<int32_t>::stream(s, indent + "  ", v.u0);
    s << indent << "u1: ";
    Printer<int32_t>::stream(s, indent + "  ", v.u1);
    s << indent << "u2: ";
    Printer<int32_t>::stream(s, indent + "  ", v.u2);
    s << indent << "t: ";
    Printer<ros::Time>::stream(s, indent + "  ", v.t);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOBROB_UTIL_MESSAGE_ME439SENSORSRAW_H
