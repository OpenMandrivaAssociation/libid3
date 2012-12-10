%define	major 1
%define libname	%mklibname id3_ %{major}
%define develname %mklibname -d id3_ %{major}

Summary:	ID3 Parsing Library
Name:		libid3
Version:	1.2
Release:	6
Group:		System/Libraries
License:	BSD-like
URL:		http://www.tangent.org/
Source0:	http://download.tangent.org/%{name}-%{version}.tar.bz2
Patch0:		libid3-1.2-soversion.patch

%description
Library for parsing ID3 tags from files or sections of memory.

%package -n	%{libname}
Summary:	ID3 Parsing Library
Group:		System/Libraries
Obsoletes:	%{_lib}id3_0 < %{version}-%{release}

%description -n	%{libname}
Library for parsing ID3 tags from files or sections of memory.

%package -n	%{develname}
Summary:	Static library and header files for the ID3 Parsing Library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	libid3_3.8-devel
Provides:	lib%{name}_%{major}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
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
%setup -q
%patch0 -p1

%build
autoreconf -fi
%configure2_5x  --disable-static
%make

# make the man pages
pod2man Docs/libID3.pod > libID3.3
pod2man Docs/tagpuller.pod > tagpuller.1

%install
install -d %{buildroot}%{_mandir}/man{1,3}

%makeinstall_std

install -m0755 tests/id3test %{buildroot}%{_bindir}/

install -m0644 libID3.3 %{buildroot}%{_mandir}/man3/
install -m0644 tagpuller.1 %{buildroot}%{_mandir}/man1/

%files -n %{libname}
%doc COPYING ChangeLog README TODO
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*

%files tools
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2-5mdv2011.0
+ Revision: 609754
- rebuild

* Sat Feb 20 2010 Funda Wang <fwang@mandriva.org> 1.2-4mdv2010.1
+ Revision: 508657
- add upstream patch to fix soversion

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2-2mdv2009.0
+ Revision: 239062
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 08 2007 Funda Wang <fwang@mandriva.org> 1.2-1mdv2008.0
+ Revision: 60340
- use versioned devel package to avoid confusion
- automake at first
- Disable static build
- New version 1.2

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1-1mdv2008.0
+ Revision: 25437
- Import libid3



* Fri Apr 28 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1-1mdk

* Sat Mar 19 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0-2mdk
- use the %%mkrel macro
- added a conflict for the devel sub package conflicts with 
  libid3_3.8-devel

* Mon Feb 07 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0-1mdk
- initial Mandrakelinux package
