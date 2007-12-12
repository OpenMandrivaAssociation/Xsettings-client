%define name 	Xsettings-client
%define version	0.10
%define release 1mdk

%define major 	0
%define libname %mklibname %name %major

Summary: 	Inter-toolkit configuration settings
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://www.freedesktop.org/standards/xsettings-spec/
License: 	GPL
Group: 		System/Libraries
Source: 	http://matchbox.handhelds.org/sources/optional-dependencies/%{name}-%{version}.tar.bz2

BuildRequires:	XFree86-devel
Buildroot: 	%_tmppath/%name-%version-buildroot

%description
The intent of this specification is to specify a mechanism to allow the
configuration of settings such as double click timeout, drag-and-drop
threshold, and default foreground and background colors for all applications
running within a desktop. The mechanism should:
- allow for instant updates to be propagated across all applications at runtime
- perform well, even for remote applications.

It is not intended:
- for the storage of application-specific data
- to be able to store large amounts of data
- to store complex data types (other than as strings)

%package -n	%libname
Group:		System/Libraries
Summary:	Inter-toolkit configuration settings

%description -n %libname
The intent of this specification is to specify a mechanism to allow the
configuration of settings such as double click timeout, drag-and-drop
threshold, and default foreground and background colors for all applications
running within a desktop. The mechanism should:
- allow for instant updates to be propagated across all applications at runtime
- perform well, even for remote applications.

It is not intended:
- for the storage of application-specific data
- to be able to store large amounts of data
- to store complex data types (other than as strings)

%package -n %libname-devel
Group:          Development/C
Summary:        Static libraries and header files from %name
Provides:       %name-devel = %version-%release
Provides:	lib%name-devel = %version-%release
Requires:       %libname = %version-%release

%description -n %libname-devel
Static libraries and header files from %name

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%_libdir/*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%doc README
%_libdir/*.so
%_libdir/*.la
%_libdir/*.a
%_includedir/*.h

