Summary:	VideoLAN Server
Summary(pl):	Serwer VideoLAN
Name:		vls
Version:	0.5.3
Release:	0.2
License:	GPL
Group:		Applications/Multimedia
Source0:	http://www.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	63fb39e7312fdd87f27e2e4c99593143
URL:		http://www.videolan.org/
BuildRequires:	libdvbpsi-devel
BuildRequires:	libdvdread-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The VideoLAN project targets multimedia streaming of MPEG-1, MPEG-2,
MPEG-4 and DivX files, DVDs, digital satellite channels, digital
terrestial television channels and live videos on a high-bandwidth
IPv4 or IPv6 network in unicast or multicast under many OSes.

%description -l pl
Projekt VideoLAN zajmuje siê multimedialnymi strumieniami MPEG-1,
MPEG-2, MPEG-4 oraz plikami DivX, danymi DVD, cyfrowymi kana³ami
satelitarnymi, cyfrowymi kana³ami telewizji naziemnej oraz obrazem
trasmitowanym na ¿ywo po wysokoprzepustowej sieci IPv4 lub IPv6
w trybie unicast lub multicast pod kontrol± wielu systemów
operacyjnych.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# help rpm find dependencies
chmod 755 $RPM_BUILD_ROOT%{_libdir}/videolan/%{name}/*.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/videolan
%dir %{_libdir}/videolan/%{name}
%attr(755,root,root) %{_libdir}/videolan/%{name}/dvdreader.so
%dir %{_sysconfdir}/videolan
%dir %{_sysconfdir}/videolan/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/videolan/%{name}/%{name}.cfg
