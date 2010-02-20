%define	major 1
%define libname	%mklibname id3_ %{major}
%define develname %mklibname -d id3_ %{major}

Summary:	ID3 Parsing Library
Name:		libid3
Version:	1.2
Release:	%mkrel 4
Group:		System/Libraries
License:	BSD-like
URL:		http://www.tangent.org/
Source0:	http://download.tangent.org/%{name}-%{version}.tar.bz2
Patch0:		libid3-1.2-soversion.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Library for parsing ID3 tags from files or sections of memory.

%package -n	%{libname}
Summary:	ID3 Parsing Library
Group:          System/Libraries
Obsoletes:	%{_lib}id3_0 < %{version}-%{release}

%description -n	%{libname}
Library for parsing ID3 tags from files or sections of memory.

%package -n	%{develname}
Summary:	Static library and header files for the ID3 Parsing Library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Conflicts:	libid3_3.8-devel
Provides:	lib%{name}_%{major}-devel = %{version}
Requires:	%{libname} = %{version}
Obsoletes:	%{_lib}id3_0-devel < %{version}-%{release}

%description -n	%{develname}
Library for parsing ID3 tags from files or sections of memory.

This package contains the static libid3 library and its header
files.

%package	tools
Summary:	Tools using the ID3 Parsing Library
Group:		Sound

%description	tools
This package contains various files using the ID3 Parsing Library.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
autoreconf -fi
%configure2_5x  --disable-static
%make

# make the man pages
pod2man Docs/libID3.pod > libID3.3
pod2man Docs/tagpuller.pod > tagpuller.1

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_mandir}/man{1,3}

%makeinstall_std

install -m0755 tests/id3test %{buildroot}%{_bindir}/

install -m0644 libID3.3 %{buildroot}%{_mandir}/man3/
install -m0644 tagpuller.1 %{buildroot}%{_mandir}/man1/

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING ChangeLog README TODO
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_mandir}/man3/*

%files tools
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
