Summary:	VideoLAN Server
Summary(pl):	VideoLAN Serwer
Name:		vls
Version:	0.5.3
Release:	0.1
License:	GPL
Group:		Multimedia
######		Unknown group!
Source0:	http://www.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	63fb39e7312fdd87f27e2e4c99593143
URL:		http://www.videolan.org/
#BuildRequires:	-
#Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The VideoLAN project targets multimedia streaming of MPEG-1, MPEG-2,
MPEG-4 and DivX files, DVDs, digital satellite channels, digital
terrestial television channels and live videos on a high-bandwidth
IPv4 or IPv6 network in unicast or multicast under many OSes.

%description -l pl
Projekt VideoLAN zajmuje siê multimedialnymi strumieniami MPEG-1,
MPEG-2, MPEG-4, DivX, DVDs, TV

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/videolan/%{name}/dvdreader.so
%{_sysconfdir}/videolan/%{name}/%{name}.cfg
