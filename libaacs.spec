Name:           libaacs
Version:        0.9.0
Release:        1%{?dist}
Summary:        Open implementation of AACS specification
License:        LGPLv2+
URL:            http://www.videolan.org/developers/libaacs.html

Source0:        ftp://ftp.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1:        README.Fedora
# http://git.videolan.org/?p=libaacs.git;a=commit;h=883d3c07b156dab21f90a00d7ae7ca5b40ef9564
Patch0:         %{name}-git.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  libgcrypt-devel

%description
Open implementation of the AACS specification.

%package utils
Summary:        Test utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
The %{name}-utils package contains test utilities for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1

%build
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete
mkdir -p /etc/xdg/aacs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING 
%doc KEYDB.cfg ChangeLog README.txt README.Fedora
%{_libdir}/*.so.*
%{_sysconfdir}/xdg/aacs

%files utils
%{_bindir}/aacs_info

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jan 25 2018 Simone Caronni <negativo17@gmail.com> - 0.9.0-1
- First build.
