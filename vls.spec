Summary:	VideoLAN Server
Summary(pl.UTF-8):   Serwer VideoLAN
Name:		vls
Version:	0.5.6
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://download.videolan.org/pub/videolan/vls/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2844d8780efd69cafc0be3b398b9553d
URL:		http://www.videolan.org/
BuildRequires:	ffmpeg-devel
BuildRequires:	libdvb-devel
BuildRequires:	libdvbpsi-devel
BuildRequires:	libdvdread-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The VideoLAN project targets multimedia streaming of MPEG-1, MPEG-2,
MPEG-4 and DivX files, DVDs, digital satellite channels, digital
terrestial television channels and live videos on a high-bandwidth
IPv4 or IPv6 network in unicast or multicast under many OSes.

%description -l pl.UTF-8
Projekt VideoLAN zajmuje się multimedialnymi strumieniami MPEG-1,
MPEG-2, MPEG-4 oraz plikami DivX, danymi DVD, cyfrowymi kanałami
satelitarnymi, cyfrowymi kanałami telewizji naziemnej oraz obrazem
trasmitowanym na żywo po wysokoprzepustowej sieci IPv4 lub IPv6 w
trybie unicast lub multicast pod kontrolą wielu systemów operacyjnych.

%package dvd
Summary:	DVD input for VideoLAN Server
Summary(pl.UTF-8):   Wejście DVD dla serwera VideoLAN
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description dvd
This package includes the DVD input plugin for vls, the VideoLAN
Server. With this plugin vls is able to read MPEG data from a DVD and
send the stream to the network, together with all subtitles and audio
tracks.

%description dvd -l pl.UTF-8
Ten pakiet zawiera wtyczkę wejściową DVD dla vls - serwera VideoLAN.
Przy pomocy tej wtyczki vls może odczytywać dane MPEG z DVD i wysyłać
strumień w sieć wraz z wszystkimi napisami i ścieżkami dźwiękowymi.

%package dvb
Summary:	DVB input for VideoLAN Server
Summary(pl.UTF-8):   Wejście DVB dla serwera VideoLAN
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description dvb
This package includes the DVB input plugin for the VideoLAN Server. It
allows reception of digital unencrypted satellite channels and digital
unencrypted terrestial television channels from a DVB device using the
DVB drivers from linuxtv.org.

%description dvb -l pl.UTF-8
Ten pakiet zawiera wtyczkę wejściową DVB dla serwera VideoLAN. Pozwala
ona odbierać cyfrowe nieszyfrowane kanały satelitarne i cyfrowe
nieszyfrowane kanały telewizji naziemnej z urządzenia DVB przy użyciu
sterowników DVB z linuxtv.org.

%prep
%setup -q

%build
%configure \
	--enable-dvb \
	--enable-v4l \
	--with-libdvb=%{_libdir}
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
%dir %{_sysconfdir}/videolan
%dir %{_sysconfdir}/videolan/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/videolan/%{name}/%{name}.cfg

%files dvd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/%{name}/dvdreader.so

%files dvb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/%{name}/dvbinput.so
%attr(755,root,root) %{_libdir}/videolan/%{name}/dvbreader.so
