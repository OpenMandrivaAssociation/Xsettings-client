%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define debug_package %{nil}

Summary: 	Inter-toolkit configuration settings
Name: 		Xsettings-client
Version: 	0.10
Release: 	14
URL: 		http://www.freedesktop.org/standards/xsettings-spec/
# Tarball includes a copy of the GPL but the source headers clearly
# specify an MIT license - AdamW 2008/12
License: 	MIT
Group: 		System/Libraries
Source0:	http://matchbox-project.org/sources/optional-dependencies/%{name}-%{version}.tar.bz2
# Fix underlinking - AdamW 2008/12
Patch0:		Xsettings-client-0.10-underlink.patch
Patch1:		xsettings-automake-1.13.patch
BuildRequires:	pkgconfig(x11)

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

%package -n	%{libname}
Group:		System/Libraries
Summary:	Inter-toolkit configuration settings

%description -n %{libname}
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

%package -n %{develname}
Group:          Development/C
Summary:        Static libraries and header files from %{name}
Provides:       %{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname Xsettings-client 0 -d}
Requires:       %{libname} = %{version}-%{release}

%description -n %{develname}
Static libraries and header files from %{name}.

%prep
%setup -q
%apply_patches

%build
autoreconf -fi
%configure
%make

%install
%makeinstall_std


%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc README
%{_libdir}/*.so
%{_includedir}/*.h
